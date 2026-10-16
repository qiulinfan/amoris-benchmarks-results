"""Reruns one test binary N times on one configuration and keeps every log (gpu-matrix.md 3 e, 3 f).

    python rerun.py LABEL N CONFIG EXE [libtest args...]

CONFIG is ADAPTER-BACKEND. Machine conditions first; logs in out/gpu780m/reruns/LABEL/I.log, the
result lines in out/gpu780m/reruns/LABEL/summary.txt.
"""
import os
import subprocess
import sys
import time
from pathlib import Path

WT = Path("<local-path>/.claude/worktrees/gpu780m")
label, n, config, exe, rest = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5:]
out = Path("<local-path>/out/gpu780m/reruns") / label
out.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, str(WT / "tools/machine_conditions.py"),
                str(out / f"conditions-{time.strftime('%H%M%S')}.json"), "--label", label], cwd=WT)
adapter, backend = config.split("-")
env = {k: v for k, v in os.environ.items()
       if k not in ("POCKET_BACKEND", "POCKET_ADAPTER", "POCKET_GPU_MINIMAL")}
env["POCKET_BACKEND"] = backend
if adapter != "default":
    env["POCKET_ADAPTER"] = adapter
commit = subprocess.run(["git", "describe", "--always", "--dirty", "--abbrev=12"], cwd=WT,
                        capture_output=True, text=True).stdout.strip()
summary = open(out / "summary.txt", "a", encoding="utf-8")
summary.write(f"== {time.strftime('%Y-%m-%d %H:%M:%S')} {commit} {config} {exe} {rest}\n")
for i in range(n):
    t = time.time()
    try:
        p = subprocess.run([exe, *rest], cwd=WT / "crates/pocket-render", env=env,
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=300)
        text, code = p.stdout + "\n" + p.stderr, p.returncode
    except subprocess.TimeoutExpired as e:
        text = "\n".join(x if isinstance(x, str) else (x or b"").decode("utf-8", "replace")
                         for x in (e.stdout, e.stderr))
        code = "timeout"
    (out / f"{i}.log").write_text(text, encoding="utf-8")
    result = [l for l in text.splitlines() if l.startswith("test result") or "FAILED" in l
              or "has been running" in l]
    line = f"run {i}: exit {code} in {time.time() - t:.0f}s; " + " | ".join(result[:4])
    print(line, flush=True)
    summary.write(line + "\n")
summary.close()
