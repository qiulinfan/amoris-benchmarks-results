"""Runs snapshot test executables (out/dynscene/testbins/<label>) per backend and adapter, from
the crate's directory as cargo would; logs to out/dynscene/tests-*.log.

    python gpu_tests.py c dx12-rtx,vulkan-rtx all
    python gpu_tests.py c dx12-780m scene_changes,taa
"""
import os
import subprocess
import sys
import time

WT = "<local-path>/.claude/worktrees/dynscene/crates/pocket-render"
OUT = "<local-path>/out/dynscene"
label = sys.argv[1]
configs = {
    "dx12-rtx": {"POCKET_BACKEND": "dx12"},
    "vulkan-rtx": {"POCKET_BACKEND": "vulkan"},
    "dx12-780m": {"POCKET_BACKEND": "dx12", "POCKET_ADAPTER": "780m"},
    "vulkan-780m": {"POCKET_BACKEND": "vulkan", "POCKET_ADAPTER": "780m"},
}
which = sys.argv[2].split(",")
bins = f"{OUT}/testbins/{label}"
names = sorted(f[:-4] for f in os.listdir(bins) if f.endswith(".exe"))
if sys.argv[3] != "all":
    names = sys.argv[3].split(",")
for config in which:
    env = dict(os.environ, **configs[config])
    for name in names:
        t = time.time()
        p = subprocess.run([f"{bins}/{name}.exe"], cwd=WT, env=env, capture_output=True, text=True)
        log = f"{OUT}/tests-{label}-{config}-{name}.log"
        with open(log, "w", encoding="utf-8") as f:
            f.write(p.stdout + "\n" + p.stderr)
        lines = [l.strip() for l in (p.stdout + p.stderr).splitlines()
                 if l.startswith("test result") or "FAILED" in l or "panicked" in l
                 or "skipped" in l.lower() or "no GPU" in l]
        print(f"{config} {name}: exit {p.returncode} in {time.time() - t:.0f}s; "
              + " | ".join(lines)[:400], flush=True)
