import subprocess, sys
O = "<local-path>/out/physcache"
with open(O + "/sailing-2026-10-15.txt", "w") as out:
    for r in range(3):
        for b in ("layout1", "layout2"):
            res = subprocess.run([f"{O}/bin/{b}/physics_bench.exe"], capture_output=True, text=True, check=True)
            line = f"round {r} {b}: " + res.stdout.strip().replace("\n", " | ")
            print(line, flush=True)
            out.write(line + "\n")
