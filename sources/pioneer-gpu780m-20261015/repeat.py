"""Runs one test binary N times with an environment and filter, printing the result lines.

    python repeat.py N BACKEND ADAPTER EXE [libtest args...]
"""
import os
import subprocess
import sys

n, backend, adapter, exe, rest = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]
env = dict(os.environ, POCKET_BACKEND=backend)
if adapter != "default":
    env["POCKET_ADAPTER"] = adapter
cwd = "<local-path>/.claude/worktrees/gpu780m/crates/pocket-render"
for i in range(n):
    try:
        p = subprocess.run([exe, *rest], cwd=cwd, env=env, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=600)
        out = p.stdout + p.stderr
        code = p.returncode
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        code = "timeout"
    keep = [l for l in out.splitlines()
            if "FAILED" in l or l.startswith("test result") or "panicked" in l
            or "has been running" in l or "image change" in l or "skipped" in l]
    print(f"run {i}: exit {code}")
    for l in keep[:12]:
        print("   ", l)
    sys.stdout.flush()
