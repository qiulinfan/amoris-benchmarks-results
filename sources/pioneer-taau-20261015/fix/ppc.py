"""prepass_compare below scale 1 (local driver): pocket-render capture cases, per adapter/API."""
import json
import os
import subprocess
import sys
W = "<local-path>/.claude/worktrees/taau"
O = "<local-path>/out/taau/fix/prepass/"
CASES = "cubes-sphere,cubes-dense,cubes-shadows,splats,gi-room-static,pt-lab-static"
os.makedirs(O, exist_ok=True)
for combo in sys.argv[1].split(","):
    ad, be = combo.split(":")
    for aa in ["msaa+taa", "taa"]:
        for scale in ["0.5", "0.67"]:
            name = f"{ad}-{be}-{aa}-{scale}"
            env = dict(os.environ, POCKET_AA=aa, POCKET_RENDER_SCALE=scale)
            p = subprocess.run(["python", W + "/tools/prepass_compare.py", "--backend", be, "--adapter", ad,
                                "--cases", CASES, "--scenes", "", "--out", f"../../../out/taau/fix/prepass/{name}",
                                "--summary", f"../../../out/taau/fix/prepass/{name}.json"],
                               cwd=W, env=env, capture_output=True, text=True)
            try:
                j = json.loads(open(O + name + ".json").read())
                res = {c: (v["on_vs_off"]["max_diff_8bit"], v["on_vs_off"]["rmse_8bit"])
                       if "on_vs_off" in v else "error" for c, v in j["cases"].items()}
            except Exception as e:
                res = f"error {e} {p.stderr[-300:]}"
            print(name, res, flush=True)
