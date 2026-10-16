"""Throwaway (explore/robust): how often Play's world.changed reset reaches /ws before the
play.start answer. Starts `pocket serve` on a copy of samples/sailing, subscribes, then N times
play.start / play.stop, recording the frames in arrival order.

    python play_order.py REPO POCKET [N]
"""
import importlib.util
import json
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

repo, pocket = Path(sys.argv[1]), sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 40
spec = importlib.util.spec_from_file_location("smoke_server", repo / "tools/smoke_server.py")
smoke = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smoke)

tmp = Path(tempfile.mkdtemp(prefix="pocket-order-"))
proj = tmp / "sailing"
shutil.copytree(repo / "samples/sailing", proj)
server = subprocess.Popen([pocket, "serve", str(proj), "--port", "0"], stdout=subprocess.PIPE,
                          stderr=subprocess.DEVNULL, text=True,
                          creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
counts = {"reset_before_answer": 0, "reset_after_answer": 0, "no_reset": 0}
try:
    info = json.loads(server.stdout.readline())
    ws = smoke.WS(info["port"])
    ws.recv()
    ws.request(1, "subscribe", {"topics": ["world.changed", "events", "history", "profile"]})
    rid = 10
    for i in range(n):
        rid += 1
        ws.send({"id": rid, "method": "play.start", "params": {"speed": 2}})
        before = False
        answer, _ = ws.until(lambda f, r=rid: f.get("id") == r, 10)
        # until() consumed the frames before the answer; look at them through the backlog-less path
        seen = _
        before = any(f.get("event") == "world.changed" and f["data"].get("reset") for f in seen)
        if before:
            counts["reset_before_answer"] += 1
        else:
            r, _ = ws.until(lambda f: f.get("event") == "world.changed" and f["data"].get("reset"), 3)
            counts["reset_after_answer" if r else "no_reset"] += 1
        rid += 1
        ws.request(rid, "play.stop")
        time.sleep(0.05)
finally:
    server.send_signal(signal.CTRL_BREAK_EVENT)
    try:
        server.wait(10)
    except subprocess.TimeoutExpired:
        server.kill()
    shutil.rmtree(tmp, ignore_errors=True)
print(json.dumps({"play_starts": n, **counts}))
