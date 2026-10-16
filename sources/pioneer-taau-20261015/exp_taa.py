"""Times the TAA pass of the check scene for one shader variant (local experiment driver)."""
import json
import os
import subprocess
import sys

W = "<local-path>/.claude/worktrees/taau"
label = sys.argv[1]
combos = sys.argv[2].split(",") if len(sys.argv) > 2 else ["780m:dx12"]
for combo in combos:
    ad, be = combo.split(":")
    env = dict(os.environ, POCKET_BACKEND=be, POCKET_ADAPTER=ad)
    for rep in range(2):
        p = subprocess.run([W + "/target/release/examples/aa_eval.exe",
                            "<local-path>/out/taau/quick", "--only", "bench",
                            "--bench-sizes", "1600x900,2560x1440", "--scale", "0.67,0.5",
                            "--bench-configs", "taa:off,taa:off:0.67,taa:off:0.5", "--frames", "300"],
                           env=env, capture_output=True, text=True)
        for line in p.stderr.splitlines():
            if line.startswith("bench "):
                j = json.loads(line[6:])
                print(label, combo, rep, j["size"], round(j["render_scale"], 2), "gpu",
                      j["profiled_gpu_p50_ms"], "taa p10", j["passes_p10_ms"].get("taa"),
                      "p50", j["passes_p50_ms"].get("taa"), flush=True)
