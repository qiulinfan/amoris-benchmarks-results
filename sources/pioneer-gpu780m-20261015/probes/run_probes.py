"""Runs the zz_probe test binary's probes on several configurations and keeps every log.

    python run_probes.py LABEL EXE CONFIG[,CONFIG] TEST[,TEST] [--repeat N] [--env K=V ...]

CONFIG is ADAPTER-BACKEND as in tools/gpu_matrix.py (`default` adapter: none). Machine conditions
are recorded first (tools/machine_conditions.py). Logs: out/gpu780m/probes/LABEL/CONFIG-TEST-I.log;
the summary lines are printed and appended to out/gpu780m/probes/LABEL/summary.txt.
"""
import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

WT = Path("<local-path>/.claude/worktrees/gpu780m")
OUT = Path("<local-path>/out/gpu780m/probes")
KEEP = ("probe on", "timestamps ", "calibration ", "parallel opens", "taa edge", "neural vs",
        "test result", "panicked", "FAILED")

ap = argparse.ArgumentParser()
ap.add_argument("label")
ap.add_argument("exe")
ap.add_argument("configs")
ap.add_argument("tests")
ap.add_argument("--repeat", type=int, default=1)
ap.add_argument("--env", nargs="*", default=[])
args = ap.parse_args()
out = OUT / args.label
out.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, str(WT / "tools/machine_conditions.py"),
                str(out / f"conditions-{time.strftime('%H%M%S')}.json"), "--label", args.label],
               cwd=WT)
summary = open(out / "summary.txt", "a", encoding="utf-8")
commit = subprocess.run(["git", "describe", "--always", "--dirty", "--abbrev=12"], cwd=WT,
                        capture_output=True, text=True).stdout.strip()
summary.write(f"== {time.strftime('%Y-%m-%d %H:%M:%S')} {commit} {args.exe} {args.env}\n")
for config in args.configs.split(","):
    adapter, backend = config.split("-")
    env = {k: v for k, v in os.environ.items()
           if k not in ("POCKET_BACKEND", "POCKET_ADAPTER", "POCKET_GPU_MINIMAL")}
    if backend != "auto":
        env["POCKET_BACKEND"] = backend
    if adapter != "default":
        env["POCKET_ADAPTER"] = adapter
    for kv in args.env:
        k, v = kv.split("=", 1)
        env[k] = v
    for test in args.tests.split(","):
        for i in range(args.repeat):
            t = time.time()
            try:
                p = subprocess.run([args.exe, test, "--exact", "--nocapture", "--test-threads=1"],
                                   cwd=WT / "crates/pocket-render", env=env, capture_output=True,
                                   text=True, encoding="utf-8", errors="replace", timeout=600)
                text, code = p.stdout + p.stderr, p.returncode
            except subprocess.TimeoutExpired as e:
                text, code = str(e.stdout or "") + str(e.stderr or ""), "timeout"
            log = out / f"{config}-{test}-{i}.log"
            log.write_text(text, encoding="utf-8")
            head = f"{config} {test} #{i}: exit {code} in {time.time() - t:.0f}s"
            print(head, flush=True)
            summary.write(head + "\n")
            for l in text.splitlines():
                if l.strip().startswith(KEEP):
                    print("   " + l.strip(), flush=True)
                    summary.write("   " + l.strip() + "\n")
summary.close()
