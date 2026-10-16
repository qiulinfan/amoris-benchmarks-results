"""The exact checks of docs/bench/shadows.md 2 and 3 (run from the worktree root, under the lock)."""
import subprocess, sys
O = "../../../out/shadowcull/round2"
T = [sys.executable, "tools/shadow_cull_bench.py"]
steps = [
    T + ["compare", "--configs", "dx12:nvidia,vulkan:nvidia,dx12:780m,vulkan:780m,dx12:nvidia+minimal,vulkan:780m+minimal",
         "--out", f"{O}/compare"],
    T + ["compare", "--configs", "dx12:nvidia,vulkan:nvidia", "--occlusion", "on", "--out", f"{O}/compare-occlusion"],
    T + ["games", "--configs", "dx12:nvidia,vulkan:nvidia,dx12:780m", "--out", f"{O}/games"],
]
code = 0
for s in steps:
    print("::", " ".join(s[1:3]), flush=True)
    code |= subprocess.run(s).returncode
sys.exit(code)
