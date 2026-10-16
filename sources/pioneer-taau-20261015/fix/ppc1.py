"""prepass_compare controls at scale 1 (local driver)."""
import json
import os
import subprocess
import sys
W = "<local-path>/.claude/worktrees/taau"
O = "<local-path>/out/taau/fix/prepass/"
cases = sys.argv[2]
for combo in sys.argv[1].split(","):
    ad, be = combo.split(":")
    for aa in ["msaa+taa", "taa", "msaa"]:
        for rep in range(int(sys.argv[3]) if len(sys.argv) > 3 else 1):
            name = f"{ad}-{be}-{aa}-1-r{rep}"
            env = dict(os.environ, POCKET_AA=aa, POCKET_RENDER_SCALE="1")
            p = subprocess.run(["python", W + "/tools/prepass_compare.py", "--backend", be, "--adapter", ad,
                                "--cases", cases, "--scenes", "", "--out", f"../../../out/taau/fix/prepass/{name}",
                                "--summary", f"../../../out/taau/fix/prepass/{name}.json"],
                               cwd=W, env=env, capture_output=True, text=True)
            j = json.loads(open(O + name + ".json").read())
            print(name, {c: (v["on_vs_off"]["max_diff_8bit"], v["on_vs_off"]["rmse_8bit"]) for c, v in j["cases"].items()}, flush=True)
