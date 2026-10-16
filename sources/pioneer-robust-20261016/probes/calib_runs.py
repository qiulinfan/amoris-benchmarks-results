"""Clock-calibration reproduction (explore/robust): runs the trace calibration test and the probe
(probe_test.rs.txt, PROBE_N calibrations per process) many times on one adapter and backend, idle
or under a synthetic all-core CPU load (burn.py), and records the conditions. Run inside the bench
lock; the test binary is `cargo test -p pocket-render --release --lib --no-run`'s.

    python calib_runs.py BIN OUTDIR --label L [--load] [--adapter 780m] [--backend vulkan]
        [--procs 30] [--tests 30] [--n 20]
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path("<local-path>")
TEST = "trace::tests::gpu_clock_samples_are_current_and_bound_by_the_cpu_brackets"
PROBE = "trace::tests::calibration_probe"

ap = argparse.ArgumentParser()
ap.add_argument("bin")
ap.add_argument("out")
ap.add_argument("--label", required=True)
ap.add_argument("--load", action="store_true")
ap.add_argument("--adapter", default="780m")
ap.add_argument("--backend", default="vulkan")
ap.add_argument("--procs", type=int, default=30)
ap.add_argument("--tests", type=int, default=30)
ap.add_argument("--n", type=int, default=20)
ap.add_argument("--gap-ms", type=int, default=0)
a = ap.parse_args()
out = Path(a.out)
out.mkdir(parents=True, exist_ok=True)
env = {k: v for k, v in os.environ.items() if not k.startswith(("POCKET_", "WGPU_"))}
env.update(POCKET_ADAPTER=a.adapter, POCKET_BACKEND=a.backend)
cond = REPO / ".claude/worktrees/robust/tools/machine_conditions.py"
subprocess.run([sys.executable, str(cond), str(out / f"{a.label}-conditions-start.json"),
                "--label", a.label], check=False)
burn = None
if a.load:
    burn = subprocess.Popen([sys.executable, str(HERE / "burn.py"), "1200"])
    time.sleep(2)
t0 = time.time()
try:
    jsonl = out / f"{a.label}-probe.jsonl"
    for i in range(a.procs):
        r = subprocess.run([a.bin, "--ignored", "--exact", PROBE, "--test-threads", "1"],
                           env={**env, "PROBE_N": str(a.n), "PROBE_GAP_MS": str(a.gap_ms),
                                "PROBE_OUT": str(jsonl)},
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            print(f"probe {i}: exit {r.returncode}\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}")
    fails = []
    for i in range(a.tests):
        r = subprocess.run([a.bin, "--exact", TEST, "--test-threads", "1", "--nocapture"], env=env,
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            fails.append({"run": i, "out": (r.stdout + r.stderr)[-3000:]})
    summary = {"label": a.label, "load": a.load, "adapter": a.adapter, "backend": a.backend,
               "probe_processes": a.procs, "probe_calibrations_per_process": a.n,
               "test_runs": a.tests, "test_failures": len(fails), "seconds": round(time.time() - t0, 1)}
    (out / f"{a.label}-tests.json").write_text(json.dumps({**summary, "failures": fails}, indent=1))
    print(json.dumps(summary))
finally:
    if burn:
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(burn.pid)], capture_output=True)
        burn.kill()
subprocess.run([sys.executable, str(cond), str(out / f"{a.label}-conditions-end.json"),
                "--label", a.label], check=False)
