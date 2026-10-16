"""Runs the commands of a JSON file (a list of argv lists) one after another, from the dynscene
worktree, printing each one's output; exits with the first failure's code."""
import json
import subprocess
import sys

WT = "<local-path>/.claude/worktrees/dynscene"
for argv in json.load(open(sys.argv[1], encoding="utf-8")):
    print("$", " ".join(argv), flush=True)
    p = subprocess.run(argv, cwd=WT)
    if p.returncode:
        sys.exit(p.returncode)
