"""Builds master's tests that failed on the 780M on this branch (the exported before tree) and runs
them and this branch's snapshot on the 780M, both backends, twice each."""
import os
import re
import subprocess

BEFORE = "<local-path>/.claude/worktrees/dynscene/target/before-src"
WT = "<local-path>/.claude/worktrees/dynscene"
SNAP = "<local-path>/out/dynscene/testbins/g"
env = dict(os.environ)
env["PATH"] = os.path.expanduser("~/.cargo/bin") + os.pathsep + env["PATH"]
env.pop("CARGO_TARGET_DIR", None)
env["CARGO_BUILD_JOBS"] = "6"
p = subprocess.run([os.path.expanduser("~/.cargo/bin/cargo.exe"), "test", "--offline", "-p", "pocket-render", "--lib", "--test", "frame_trace",
                    "--test", "gpu_profiler", "--no-run"], cwd=BEFORE, env=env, capture_output=True,
                   text=True)
exes = {}
for m in re.finditer(r"Executable (?:tests\\(\w+)\.rs|unittests src\\lib\.rs) \(([^)]+)\)", p.stderr):
    exes[m.group(1) or "pocket_render"] = os.path.join(BEFORE, m.group(2))
print("built", exes, p.returncode, p.stderr[-300:] if p.returncode else "", flush=True)
CHECKS = [
    ("frame_trace", []),
    ("gpu_profiler", []),
    ("pocket_render", ["gi::pt::tests::ray_query_pt_transport_training_and_accumulation",
                       "trace::tests::gpu_clock_samples_are_current_and_bound_by_the_cpu_brackets"]),
]
for attempt in range(2):
    for backend in ("dx12", "vulkan"):
        run_env = dict(os.environ, POCKET_BACKEND=backend, POCKET_ADAPTER="780m")
        for name, filters in CHECKS:
            for build, exe, cwd in (("master", exes.get(name), BEFORE),
                                    ("dynscene", f"{SNAP}/{name}.exe", WT)):
                if not exe:
                    print(build, name, "missing", flush=True)
                    continue
                for flt in filters or [None]:
                    argv = [exe] + ([flt, "--exact"] if flt else [])
                    r = subprocess.run(argv, cwd=cwd + "/crates/pocket-render", env=run_env,
                                       capture_output=True, text=True)
                    lines = [l for l in (r.stdout + r.stderr).splitlines()
                             if l.startswith("test result") or "panicked" in l]
                    print(attempt, backend, build, name, flt or "", r.returncode,
                          " | ".join(lines)[:300], flush=True)
