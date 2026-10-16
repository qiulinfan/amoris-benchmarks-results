"""Runs the given test executables under each backend/adapter config; prints pass/fail."""
import os, subprocess, sys, json, time
root = sys.argv[1]
configs = sys.argv[2].split(",")
exes = sys.argv[3:]
results = []
for cfg in configs:
    backend, _, adapter = cfg.partition(":")
    env = dict(os.environ, POCKET_BACKEND=backend)
    if adapter:
        env["POCKET_ADAPTER"] = adapter
    for exe in exes:
        t = time.time()
        p = subprocess.run([exe, "--test-threads=1"], cwd=root, env=env, capture_output=True, text=True)
        summary = [l for l in p.stdout.splitlines() if l.startswith("test result")]
        failed = [l for l in p.stdout.splitlines() if "FAILED" in l or "panicked" in l]
        r = {"config": cfg, "exe": os.path.basename(exe), "code": p.returncode,
             "summary": summary, "failed": failed[:6], "seconds": round(time.time() - t)}
        if p.returncode:
            r["stderr"] = p.stderr[-1500:]
        results.append(r)
        print(json.dumps(r), flush=True)
sys.exit(1 if any(r["code"] for r in results) else 0)
