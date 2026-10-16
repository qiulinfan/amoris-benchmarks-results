"""Chrome checks of ?shadow_cull=off|on (run from the worktree root, under the bench lock)."""
import json, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parent
srv = subprocess.Popen([sys.executable, "-m", "http.server", "-d", str(R / "webroot"), "8093", "--bind", "<local-endpoint>"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.5)
pages = [("mixed", "demo=mixed"), ("lod-0", "demo=lod&t=0"), ("lod-off-0", "demo=lod&t=0&lod=off")]
gpus = [("rtx", "--force_high_performance_gpu"), ("780m", "")]
code = 0
try:
    for gname, flags in gpus:
        for name, q in pages:
            cmd = [sys.executable, "tools/web_draw_paths.py", f"http://<local-endpoint>/viewport/?{q}",
                   "--name", name, "--out", str(R / "web" / gname), "--compare", "shadow_cull",
                   "--seconds", "8", "--size", "1280x720"]
            if flags:
                cmd.append(f"--chrome-flags={flags}")
            p = subprocess.run(cmd, capture_output=True, text=True)
            print(gname, name, p.returncode, p.stdout.strip()[-1500:], p.stderr[-800:], flush=True)
            code |= p.returncode
finally:
    srv.terminate()
sys.exit(code)
