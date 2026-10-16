"""Synthetic CPU load: N busy-loop processes (default: every logical CPU) for SECONDS.

    python burn.py SECONDS [N]
"""
import multiprocessing
import os
import sys
import time


def spin(until):
    parent = multiprocessing.parent_process()
    x = 0
    while time.time() < until:
        x += 1
        if x % 5_000_000 == 0 and not parent.is_alive():
            return


if __name__ == "__main__":
    seconds = float(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else os.cpu_count()
    until = time.time() + seconds
    procs = [multiprocessing.Process(target=spin, args=(until,)) for _ in range(n)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
