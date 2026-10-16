"""The viewport-loads check against several servers in one bench-lock hold (explore/robust, review).
Each RUN is NAME=URL[,touch]; the servers must already run (see the track's report). From the
worktree's editor/ directory:

    python viewport_runs.py OUTROOT --loads-dev 10 --loads-prod 5 NAME=URL[,touch] ...
"""
import subprocess
import sys
from pathlib import Path

BUN = "<local-path>"
REPO = Path("<local-path>")
root = Path(sys.argv[1])
runs = sys.argv[2:]
root.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, str(REPO / ".claude/worktrees/robust/tools/machine_conditions.py"),
                str(root / "conditions-start.json"), "--label", "viewport-loads"], check=False)
for run in runs:
    name, spec = run.split("=", 1)
    url, *flags = spec.split(",")
    loads = next((f.split(":")[1] for f in flags if f.startswith("loads:")), "5")
    cmd = [BUN, "tools/viewport-loads.ts", "--url", url, "--loads", loads, "--seconds", "12",
           "--out", str(root / name)]
    if "touch" in flags:
        cmd += ["--touch", "src/panels/viewport/ViewportPanel.tsx"]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    (root / f"{name}.txt").write_text(p.stdout + p.stderr, encoding="utf-8")
    last = (p.stdout.strip().splitlines() or ["(no output)"])[-1]
    print(f"{name}: exit {p.returncode}: {last}", flush=True)
subprocess.run([sys.executable, str(REPO / ".claude/worktrees/robust/tools/machine_conditions.py"),
                str(root / "conditions-end.json"), "--label", "viewport-loads"], check=False)
