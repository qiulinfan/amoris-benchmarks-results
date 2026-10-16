"""build_compare at scale 1 against master b7be59a2's binaries, one adapter/API per call (local)."""
import subprocess
import sys
W = "<local-path>/.claude/worktrees/taau"
O = "<local-path>/out/taau/fix/"
for combo in sys.argv[1].split(","):
    ad, be = combo.split(":")
    p = subprocess.run(["python", W + "/tools/build_compare.py", "--before",
                        "<local-path>/out/taau/before", "--adapters", ad,
                        "--backends", be, "--out", "../../../out/taau/fix/build-compare/" + f"{ad}-{be}",
                        "--summary", "../../../out/taau/fix/build-compare/" + f"summary-{ad}-{be}.json"],
                       cwd=W, capture_output=True, text=True)
    open(O + f"build-compare-{ad}-{be}.log", "w").write(p.stdout + p.stderr)
    print(combo, p.returncode, (p.stdout + p.stderr).strip().splitlines()[-1:], flush=True)
