"""The calibration test in its original condition (explore/robust, review): the whole pocket-render
lib test binary, its tests in parallel (libtest's default threads; the gi ray-query tests share
the adapter), N times on one adapter and backend, optionally under burn.py's all-core load. With
two binaries (before and after a change) the runs alternate, so both see the same conditions.
Run inside the bench lock.

    python lib_runs.py OUTDIR --label L [--load] [--adapter 780m] [--backend vulkan] [--runs 30]
        NAME=BIN [NAME=BIN ...]

Writes OUTDIR/L-lib.json: per binary, runs, failures of the calibration test, and every other
failing test's name; the failing runs' output tails.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path("<local-path>")
CRATE = REPO / ".claude/worktrees/robust/crates/pocket-render"
TEST = "trace::tests::gpu_clock_samples_are_current_and_bound_by_the_cpu_brackets"

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("bins", nargs="+", help="NAME=PATH")
ap.add_argument("--label", required=True)
ap.add_argument("--load", action="store_true")
ap.add_argument("--adapter", default="780m")
ap.add_argument("--backend", default="vulkan")
ap.add_argument("--runs", type=int, default=30)
a = ap.parse_args()
bins = dict(b.split("=", 1) for b in a.bins)
out = Path(a.out)
out.mkdir(parents=True, exist_ok=True)
env = {k: v for k, v in os.environ.items() if not k.startswith(("POCKET_", "WGPU_"))}
env.update(POCKET_ADAPTER=a.adapter, POCKET_BACKEND=a.backend)
cond = REPO / ".claude/worktrees/robust/tools/machine_conditions.py"
subprocess.run([sys.executable, str(cond), str(out / f"{a.label}-conditions-start.json"),
                "--label", a.label], check=False)
burn = None
if a.load:
    burn = subprocess.Popen([sys.executable, str(HERE / "burn.py"), "1800"])
    time.sleep(2)
t0 = time.time()
result = {name: {"runs": 0, "calibration_failures": 0, "other_failures": {}, "seconds": [],
                 "failing_runs": []} for name in bins}
try:
    for i in range(a.runs):
        for name, path in bins.items():
            s = time.time()
            r = subprocess.run([path], cwd=CRATE, env=env, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=600)
            res = result[name]
            res["runs"] += 1
            res["seconds"].append(round(time.time() - s, 1))
            failed = re.findall(r"^test (\S+) \.\.\. FAILED", r.stdout, re.M)
            if TEST in failed:
                res["calibration_failures"] += 1
            for t in failed:
                if t != TEST:
                    res["other_failures"][t] = res["other_failures"].get(t, 0) + 1
            if r.returncode != 0:
                res["failing_runs"].append({"run": i, "failed": failed,
                                            "tail": (r.stdout + r.stderr)[-4000:]})
            print(f"run {i} {name}: exit {r.returncode}, failed {failed}", flush=True)
finally:
    if burn:
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(burn.pid)], capture_output=True)
        burn.kill()
summary = {"label": a.label, "load": a.load, "adapter": a.adapter, "backend": a.backend,
           "bins": bins, "seconds": round(time.time() - t0, 1), "result": result}
(out / f"{a.label}-lib.json").write_text(json.dumps(summary, indent=1))
print(json.dumps({n: {k: v for k, v in r.items() if k not in ("failing_runs", "seconds")}
                  for n, r in result.items()}))
subprocess.run([sys.executable, str(cond), str(out / f"{a.label}-conditions-end.json"),
                "--label", a.label], check=False)
