"""Mutation checks of the taau tests (local driver, not committed): applies one mutation, builds
the taa test, runs the named test under the bench lock on the given adapters, saves the log to
out/taau/mutations/NAME-BACKEND-ADAPTER.txt and restores the sources."""
import os
import subprocess
import sys

W = "<local-path>/.claude/worktrees/taau"
O = "<local-path>/out/taau/mutations/"
LOCK = "<local-path>/out/locks/bench_lock.py"
CARGO = os.path.expanduser("~/.cargo/bin/cargo.exe")

MUTATIONS = {
    # The reconstruction reads the jitter with the wrong sign (the projection keeps the right one).
    "jitter-sign": ("upscaling_converges_on_a_still_scene", [
        ("crates/pocket-render/src/taa.rs",
         "            jitter: [\n                jitter.pixels.x,\n                jitter.pixels.y,",
         "            jitter: [\n                -jitter.pixels.x,\n                -jitter.pixels.y,")]),
    # The current frame's share is the usual alpha everywhere.
    "share-unweighted": ("upscaling_converges_on_a_still_scene", [
        ("crates/pocket-render/src/taa.rs",
         "            upscale_weight: true,", "            upscale_weight: false,")]),
    # The splats' depth drawn with the jittered frame group (the defect the test guards).
    "splat-jittered-depth": ("splats_behind_meshes_are_stable_under_taa", [
        ("crates/pocket-render/src/renderer.rs",
         "        pass.set_bind_group(0, &self.binds.frame_stable, &[]);\n        pass.set_bind_group(1, self.empty, &[]);\n        pass.set_bind_group(2, &self.binds.textures, &[]);\n        pass.set_vertex_buffer(0, self.meshes.vertices.slice(..));\n        pass.set_index_buffer(self.meshes.indices.slice(..), wgpu::IndexFormat::Uint32);\n        let mut calls = 0;\n        for variant in 0..VARIANTS {\n            // A neural variant (NEURAL_VARIANT + v) has variant v's culling and alpha test.\n            pass.set_pipeline(&self.pipelines[(variant % NEURAL_VARIANT) as usize]);",
         "        pass.set_bind_group(0, &self.binds.frame, &[]);\n        pass.set_bind_group(1, self.empty, &[]);\n        pass.set_bind_group(2, &self.binds.textures, &[]);\n        pass.set_vertex_buffer(0, self.meshes.vertices.slice(..));\n        pass.set_index_buffer(self.meshes.indices.slice(..), wgpu::IndexFormat::Uint32);\n        let mut calls = 0;\n        for variant in 0..VARIANTS {\n            // A neural variant (NEURAL_VARIANT + v) has variant v's culling and alpha test.\n            pass.set_pipeline(&self.pipelines[(variant % NEURAL_VARIANT) as usize]);")]),
}
# The same defect, the test limited to its upscaled case (the first failing case stops the test).
MUTATIONS["splat-jittered-depth-x0.5"] = (MUTATIONS["splat-jittered-depth"][0],
    MUTATIONS["splat-jittered-depth"][1] + [
        ("crates/pocket-render/tests/taa.rs",
         "        for (aa, scale) in [\n            (Antialiasing::Msaa, 1.0),\n            (Antialiasing::Taa, 1.0),\n            (Antialiasing::MsaaTaa, 1.0),\n            (Antialiasing::Taa, 0.5),\n        ] {",
         "        for (aa, scale) in [(Antialiasing::Taa, 0.5)] {")])

name = sys.argv[1]
combos = sys.argv[2].split(",")
test, edits = MUTATIONS[name]
saved = {}
try:
    for path, old, new in edits:
        p = os.path.join(W, path)
        s = saved.get(p) or open(p, encoding="utf-8").read()
        saved.setdefault(p, s)
        cur = open(p, encoding="utf-8").read()
        assert cur.count(old) == 1, (path, old[:60])
        open(p, "w", encoding="utf-8", newline="\n").write(cur.replace(old, new))
    env = dict(os.environ, CARGO_BUILD_JOBS="5")
    b = subprocess.run([CARGO, "test", "--release", "-p", "pocket-render", "--test", "taa", "--no-run"],
                       cwd=W, env=env, capture_output=True, text=True)
    assert b.returncode == 0, b.stderr[-2000:]
    for combo in combos:
        be, ad = combo.split(":")
        e = dict(env, POCKET_BACKEND=be, POCKET_ADAPTER=ad)
        p = subprocess.run(["python", LOCK, "run", "--label", "taau", "--", CARGO, "test", "--release",
                            "-p", "pocket-render", "--test", "taa", "--", test, "--exact",
                            "--nocapture", "--test-threads", "1"], cwd=W, env=e, capture_output=True,
                           text=True)
        out = p.stdout + p.stderr
        open(O + f"{name}-{be}-{ad}.txt", "w", encoding="utf-8").write(
            f"mutation {name}: {edits}\nexit {p.returncode}\n" + out)
        keep = [l for l in out.splitlines() if "dB" in l or "flicker" in l or "panicked" in l
                or l.startswith("test result")]
        print(name, combo, p.returncode, *keep, sep="\n  ", flush=True)
finally:
    for p, s in saved.items():
        open(p, "w", encoding="utf-8", newline="\n").write(s)
