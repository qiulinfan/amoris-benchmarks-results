"""One bench-lock hold: the release matrix (7 configurations), the WGPU_DEBUG=1 780M path-tracer
check, and the reruns of the two one-off 780M failures. Run from the worktree after
`python tools/gpu_matrix.py --build-only`."""
import glob
import os
import subprocess
import sys

OUT = "<local-path>/out/gpu780m"
WT = "<local-path>/.claude/worktrees/gpu780m"
DEPS = WT + "/target/release/deps/"


def exe(name):
    # The newest test binary of that name (lib: pocket_render-*.exe).
    files = [f for f in glob.glob(DEPS + name + "-*.exe")]
    return max(files, key=os.path.getmtime)


def run(cmd, env=None):
    print("$", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=WT, env=env)


py = sys.executable
run([py, OUT + "/run_matrix.py", "final",
     "5060-dx12,5060-vulkan,780m-dx12,780m-vulkan,5060-dx12-minimal,5060-auto,780m-auto"])
run([py, OUT + "/run_matrix.py", "od", "780m-dx12", "--bins", "lib", "--filter", "ray_query_pt"],
    env=dict(os.environ, WGPU_DEBUG="1"))
run([py, OUT + "/reruns/rerun.py", "splat-780m-vulkan", "10", "780m-vulkan", exe("pocket_render"),
     "splat::tile"])
run([py, OUT + "/reruns/rerun.py", "taa-780m-dx12", "5", "780m-dx12", exe("taa")])
# The debug build for the next hold, inside this one so it lands in nobody's timing run.
run([py, WT + "/tools/gpu_matrix.py", "--debug", "--build-only"],
    env=dict(os.environ, CARGO_BUILD_JOBS="5",
             PATH=os.path.expanduser("~/.cargo/bin") + os.pathsep + os.environ["PATH"]))
