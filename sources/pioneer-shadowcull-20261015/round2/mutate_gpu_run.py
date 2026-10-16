"""One planted bug's runs (under the bench lock): shadow_cull compare over every scene, then the GPU
test. Prints one JSON line."""
import json, os, subprocess, sys
exe, out, backend, adapter = sys.argv[1:5]
env = dict(os.environ, POCKET_BACKEND=backend)
if adapter:
    env["POCKET_ADAPTER"] = adapter
example = os.path.join("target", "release", "examples", "shadow_cull.exe")
c = subprocess.run([example, "compare", "--out", out], env=env, capture_output=True, text=True)
rows = [json.loads(l) for l in c.stdout.splitlines() if l.startswith("{")]
scenes = {r["scene"]: [r["identical_frames"], r["frames"], r["max_abs_diff"]] for r in rows}
t = subprocess.run([exe, "--test-threads=1"], cwd="crates/pocket-render", env=env, capture_output=True,
                   text=True)
failed = [l for l in t.stdout.splitlines() + t.stderr.splitlines() if "panicked" in l or "FAILED" in l]
print(json.dumps({
    "compare_code": c.returncode,
    "compare_frames_differing": sum(f - i for i, f, _ in scenes.values()),
    "compare_scenes": scenes,
    "test_code": t.returncode,
    "test_failures": failed[:4],
}))
