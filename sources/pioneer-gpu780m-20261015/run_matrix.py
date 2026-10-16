"""Records machine conditions, then runs tools/gpu_matrix.py for one or more configurations.

    python run_matrix.py LABEL CONFIG[,CONFIG] [extra gpu_matrix args...]

Results: out/gpu780m/matrix/LABEL-CONFIG.json, logs under out/gpu780m/matrix/LABEL/.
"""
import os
import subprocess
import sys
from pathlib import Path

# cargo (gpu_matrix.py's build step) is not on the default PATH on this machine.
os.environ["PATH"] = os.path.expanduser("~/.cargo/bin") + os.pathsep + os.environ["PATH"]

WT = Path("<local-path>/.claude/worktrees/gpu780m")
OUT = Path("<local-path>/out/gpu780m/matrix")
label, configs, extra = sys.argv[1], sys.argv[2], sys.argv[3:]
OUT.mkdir(parents=True, exist_ok=True)
tag = f"{label}-{configs.replace(',', '+')}"
subprocess.run([sys.executable, str(WT / "tools/machine_conditions.py"),
                str(OUT / f"{tag}-conditions.json"), "--label", tag], cwd=WT)
p = subprocess.run([sys.executable, str(WT / "tools/gpu_matrix.py"), "--configs", configs,
                    "--out", str(OUT / label), "--json", str(OUT / f"{tag}.json"), *extra], cwd=WT)
sys.exit(p.returncode)
