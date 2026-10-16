"""Markdown rows for docs/bench/dynamic-scenes.md from the review sessions (out/dynscene/review)."""
import json
import statistics
import sys
from collections import defaultdict

R = "<local-path>/out/dynscene/review/"


def runs(name):
    return json.load(open(R + name, encoding="utf-8"))["runs"]


def fmt(x):
    if x is None:
        return "-"
    d = 2 if x < 10 else 1 if x < 100 else 0
    return f"{x:,.{d}f}"


def mhz(r):
    return ((r.get("clocks") or {}).get("frames") or {}).get("graphics_mhz_median")


def before_after(name, b0, b1, cases, clocks):
    g = defaultdict(list)
    for r in runs(name):
        if r.get("headline"):
            g[(r["case"], r["backend"], r["build"])].append(r)
    be_name = {"dx12": "D3D12", "vulkan": "Vulkan"}
    for case in cases:
        for be in ("dx12", "vulkan"):
            a, b = g.get((case, be, b0)), g.get((case, be, b1))
            if not a or not b:
                continue
            m = lambda rs, k: statistics.median(  # noqa: E731
                [x["headline"][k] for x in rs if x["headline"].get(k) is not None] or [None]) \
                if any(x["headline"].get(k) is not None for x in rs) else None
            cells = []
            for k in ("apply", "scene sync", "frame", "gpu"):
                x, y = m(a, k), m(b, k)
                cells.append("-" if x is None and y is None else f"{fmt(x)} → {fmt(y)}")
            if clocks:
                cells.append(f"{fmt(mhz(a[0]))} → {fmt(mhz(b[0]))}")
            print(f"| {case} | {be_name[be]} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    which = sys.argv[1]
    if which == "rtx":
        before_after("head-rtx.json", "before", "head", ["static", "moving-1k", "moving-10k",
                     "moving-100k", "sparse-1k", "sparse-10k", "sparse-100k"], True)
    elif which == "780m":
        before_after("head-780m.json", "before", "head", ["static", "moving-10k", "moving-100k",
                     "sparse-10k", "sparse-100k"], False)
    elif which == "passes":
        for r in runs(sys.argv[2]):
            p = (r.get("result") or {}).get("passes_ms", {})
            print(r["case"], r["backend"], r["build"], r.get("round"),
                  {k: p.get(k) for k in ("opaque", "opaque early", "scatter instances")},
                  "frame", (r.get("headline") or {}).get("frame"), "gpu",
                  (r.get("headline") or {}).get("gpu"))
    elif which == "crowd":
        g = defaultdict(list)
        for r in runs("ed-crowd.json"):
            h = (r.get("headline") or {}).get("crowd")
            if h:
                g[(r["backend"], r["build"])].append(h)
        for (be, b), hs in sorted(g.items()):
            for k in ("cpu", "frame", "gpu"):
                v = sorted(h[k] for h in hs)
                print(be, b, k, "median", statistics.median(v), "range", v[0], v[-1], v)
