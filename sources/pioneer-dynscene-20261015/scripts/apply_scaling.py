"""Apply cost of 100k moving cubes against the total entity count (exploration)."""
import json
import os
import subprocess
import sys

exe = sys.argv[1]
moving = sys.argv[2] if len(sys.argv) > 2 else "100000"
extra = sys.argv[3:]
for count in ("100000", "400000", "1600000"):
    p = subprocess.run([exe, "--count", count, "--moving", moving, "--headless-bench", "60", "--warm", "30",
                        *extra],
                       capture_output=True, text=True, env=dict(os.environ, POCKET_BACKEND="dx12"))
    r = json.loads(p.stdout.strip().splitlines()[-1])
    print(count, "apply", r["moving"]["apply_ms"], "feed p50", r["moving"]["feed_ms"]["p50"], flush=True)
