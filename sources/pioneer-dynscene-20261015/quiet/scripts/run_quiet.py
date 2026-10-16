"""Runs the quiet re-measurement jobs (docs/bench/dynamic-scenes.md 7), one bench invocation per
round, each under the shared bench lock, waiting before each until the RTX 5060 is below 70 C.
Usage: run_quiet.py JOBS.json [NAME...]   (a job whose NAME.done exists is skipped)"""
import json
import subprocess
import sys
import time

Q = "<local-path>/out/dynscene/quiet"
WT = "<local-path>/.claude/worktrees/dynscene"
LOCK = "<local-path>/out/locks/bench_lock.py"


def temp():
    p = subprocess.run(["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"],
                       capture_output=True, text=True)
    try:
        return int(p.stdout.strip())
    except ValueError:
        return None


def log(msg):
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    with open(f"{Q}/jobs.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


jobs = json.load(open(sys.argv[1], encoding="utf-8"))
only = set(sys.argv[2:])
for job in jobs:
    name = job["name"]
    if only and name not in only:
        continue
    try:
        open(f"{Q}/{name}.done").close()
        log(f"skip {name} (done)")
        continue
    except OSError:
        pass
    t0 = time.time()
    while True:
        t = temp()
        if t is None or t < 70 or time.time() - t0 > 900:
            break
        time.sleep(10)
    log(f"start {name}: RTX {t} C after {time.time() - t0:.0f}s cooling")
    with open(f"{Q}/{name}.log", "w", encoding="utf-8") as out:
        rc = subprocess.call(["python", LOCK, "run", "--label", "quiet-dynscene", "--max-hold-min",
                              "40", "--", *job["argv"]], cwd=WT, stdout=out,
                             stderr=subprocess.STDOUT)
    log(f"end {name}: exit {rc}, {time.time() - t0:.0f}s, RTX {temp()} C")
    if rc == 0:
        open(f"{Q}/{name}.done", "w").close()
