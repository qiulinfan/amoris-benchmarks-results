"""Runs the taau track's GPU tests on both adapters and backends (local driver, not committed)."""
import os
import subprocess
import sys

D = "<local-path>/.claude/worktrees/taau/target/release/deps/"
O = "<local-path>/out/taau/fix/"
jobs = [a.split("=", 1) for a in sys.argv[1:]]  # name=exe args...
for name, spec in jobs:
    exe, *args = spec.split(" ")
    for be in ["vulkan", "dx12"]:
        for ad in ["nvidia", "780m"]:
            env = dict(os.environ, POCKET_BACKEND=be, POCKET_ADAPTER=ad)
            p = subprocess.run([D + exe, *args, "--test-threads", "1", "--nocapture"], env=env,
                               capture_output=True, text=True)
            log = O + f"test-{name}-{be}-{ad}.txt"
            open(log, "w", encoding="utf-8").write(p.stdout + p.stderr)
            tail = [l for l in (p.stdout + p.stderr).splitlines()
                    if l.startswith("test result") or "panicked" in l or "FAILED" in l]
            print(name, be, ad, p.returncode, tail[-1:] if p.returncode == 0 else tail, flush=True)
