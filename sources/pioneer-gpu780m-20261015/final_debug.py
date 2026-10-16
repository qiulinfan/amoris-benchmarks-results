"""Second bench-lock hold: the debug-profile matrix on both Direct3D 12 adapters, the splat reruns
with the ignored 4.1M-splat growth test included (as in the matrix run that failed), and a check
that a mistyped adapter makes the tool fail. Run from the worktree after the debug build."""
import glob
import os
import subprocess
import sys

OUT = "<local-path>/out/gpu780m"
WT = "<local-path>/.claude/worktrees/gpu780m"
os.environ["PATH"] = os.path.expanduser("~/.cargo/bin") + os.pathsep + os.environ["PATH"]


def newest(pattern):
    return max(glob.glob(pattern), key=os.path.getmtime)


def run(cmd, env=None):
    print("$", " ".join(cmd), flush=True)
    p = subprocess.run(cmd, cwd=WT, env=env)
    print(f"exit {p.returncode}", flush=True)


py = sys.executable
run([py, OUT + "/run_matrix.py", "debug-final", "5060-dx12,780m-dx12", "--debug"])
run([py, OUT + "/reruns/rerun.py", "splat-780m-vulkan-growth", "10", "780m-vulkan",
     newest(WT + "/target/release/deps/pocket_render-*.exe"), "splat::tile", "--include-ignored"])
run([py, WT + "/tools/gpu_matrix.py", "--configs", "780n-dx12", "--bins", "gpu_profiler",
     "--out", OUT + "/matrix/typo", "--json", OUT + "/matrix/typo-780n-dx12.json"])
