"""Plants culling bugs one at a time, rebuilds the shadow_cull example and GPU test, runs both under
the bench lock on one config, records whether each catches the bug, and restores the sources.
Run from the worktree root."""
import glob, json, os, subprocess, sys, time
from pathlib import Path

OUT = Path(sys.argv[1])
CONFIG = sys.argv[2] if len(sys.argv) > 2 else "dx12:nvidia"
LOCK = "<local-path>/out/locks/bench_lock.py"
SH = Path("crates/pocket-render/src/shadows.rs")
CULL = Path("crates/pocket-render/shaders/cull.wgsl")
MARGIN = "let margin = 1.5 * far / 1024.0 + 4.0 * casc.texel[c] + 1e-5 * scale;"
M = [
    ("zero margin", SH, MARGIN, "let margin = 0.0;"),
    ("no normal offset in the margin", SH, MARGIN, "let margin = 4.0 * casc.texel[c] + 1e-5 * scale;"),
    ("planes 1 m inward", SH, MARGIN, "let margin = 1.5 * far / 1024.0 + 4.0 * casc.texel[c] + 1e-5 * scale - 1.0;"),
    ("WGSL keeps only spheres wholly inside", CULL,
     "let pl = cull.slices[cascade].p[i];" + chr(10) + "        if (dot(pl.xyz, c) + pl.w < -r) {",
     "let pl = cull.slices[cascade].p[i];" + chr(10) + "        if (dot(pl.xyz, c) + pl.w < r) {"),
]
only = sys.argv[3].split(",") if len(sys.argv) > 3 else None
OUT.mkdir(parents=True, exist_ok=True)
originals = {SH: SH.read_text(encoding="utf-8"), CULL: CULL.read_text(encoding="utf-8")}
env = dict(os.environ, CARGO_BUILD_JOBS="5")
results = []
try:
    for i, (name, f, a, b) in enumerate(M):
        if only and str(i) not in only:
            continue
        src = originals[f]
        assert src.count(a) == 1, name
        f.write_text(src.replace(a, b), encoding="utf-8", newline="\n")
        subprocess.run([sys.executable, LOCK, "idle", "--wait-min", "10"])
        t = time.time()
        b1 = subprocess.run(["cargo", "build", "--release", "-p", "pocket-render", "--example", "shadow_cull"],
                            env=env, capture_output=True, text=True)
        b2 = subprocess.run(["cargo", "test", "--release", "-p", "pocket-render", "--test", "shadow_cull",
                             "--no-run", "--message-format=json"], env=env, capture_output=True, text=True)
        exe = None
        for line in b2.stdout.splitlines():
            try:
                m = json.loads(line)
            except ValueError:
                continue
            if m.get("reason") == "compiler-artifact" and m.get("target", {}).get("name") == "shadow_cull" \
                    and m.get("executable"):
                exe = m["executable"]
        if b1.returncode or b2.returncode or not exe:
            results.append({"mutation": name, "error": "build failed", "stderr": (b1.stderr + b2.stderr)[-1500:]})
            print(json.dumps(results[-1]), flush=True)
            continue
        build_s = round(time.time() - t)
        d = OUT / f"m{i}"
        backend, _, adapter = CONFIG.partition(":")
        run = subprocess.run([sys.executable, LOCK, "run", "--label", "shadowcull", "--max-hold-min", "15", "--",
                              sys.executable, str(Path(__file__).with_name("mutate_gpu_run.py")), exe, str(d),
                              backend, adapter], capture_output=True, text=True)
        try:
            r = json.loads([l for l in run.stdout.splitlines() if l.startswith("{")][-1])
        except (IndexError, ValueError):
            r = {"error": "run failed", "stdout": run.stdout[-1500:], "stderr": run.stderr[-1500:]}
        r.update(mutation=name, build_s=build_s, config=CONFIG)
        results.append(r)
        print(json.dumps(r), flush=True)
finally:
    for f, s in originals.items():
        f.write_text(s, encoding="utf-8", newline="\n")
(OUT / "mutations-gpu.json").write_text(json.dumps(results, indent=1) + "\n")
