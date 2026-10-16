"""Prints the markdown tables of docs/bench/dynamic-scenes.md section 5 from out/dynscene/*.json."""
import json
import statistics
import sys
from collections import defaultdict

O = "<local-path>/out/dynscene/"


def load(name):
    try:
        return json.load(open(O + name, encoding="utf-8"))["runs"]
    except FileNotFoundError:
        return []


def med(values):
    v = [x for x in values if x is not None]
    return statistics.median(v) if v else None


def f(x, digits=None):
    if x is None:
        return "-"
    if digits is None:
        digits = 2 if x < 10 else 1 if x < 100 else 0
    return f"{x:,.{digits}f}"


def mhz(run):
    c = run.get("clocks") or {}
    return (c.get("frames") or c).get("graphics_mhz_median")


def group(runs):
    g = defaultdict(list)
    for r in runs:
        if r.get("headline"):
            g[(r["case"], r["backend"], r.get("adapter"), r["build"])].append(r)
    return g


def cell(rs, key):
    return med([r["headline"].get(key) for r in rs])


CASES = ["static", "moving-1k", "moving-10k", "moving-100k", "sparse-1k", "sparse-10k",
         "sparse-100k", "moving-1.6m"]


def before_after(runs, builds, backends, adapter=None, clocks=True):
    g = group(runs)
    b0, b1 = builds
    head = "| Case | Backend | Apply, ms | Scene sync, ms | Frame, ms | GPU, ms" + (
        " (RTX MHz)" if clocks else "") + " |"
    print(head)
    print("| --- | --- | ---: | ---: | ---: | ---: |")
    for case in CASES:
        for be in backends:
            a, b = g.get((case, be, adapter, b0)), g.get((case, be, adapter, b1))
            if not a or not b:
                continue
            def pair(key):
                return f"{f(cell(a, key))} → {f(cell(b, key))}"
            gpu = f"{f(cell(a, 'gpu'))} → {f(cell(b, 'gpu'))}"
            if clocks:
                gpu += f" ({f(med([mhz(r) for r in a]), 0)} → {f(med([mhz(r) for r in b]), 0)})"
            name = {"dx12": "D3D12", "vulkan": "Vulkan"}[be]
            print(f"| {case} | {name} | {pair('apply')} | {pair('scene sync')} | {pair('frame')} | {gpu} |")


def steps(sessions, key, cases, backend):
    print(f"| Case | " + " | ".join(n for n, _, _ in sessions) + " |")
    print("| --- |" + " ---: |" * len(sessions))
    for case in cases:
        cells = []
        for _, runs, build in sessions:
            rs = group(runs).get((case, backend, None, build))
            cells.append(f(cell(rs, key)) if rs else "")
        print(f"| {case} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    what = sys.argv[1]
    if what == "final":
        before_after(load("final-rtx.json"), ("before", "after"), ["dx12", "vulkan"])
    elif what == "780m":
        before_after(load("bd-780m.json"), ("before", "d"), ["dx12", "vulkan"], "780m", False)
    elif what == "780m-g":
        before_after(load("bd-780m.json") + load("g-780m.json"), ("before", "g"), ["dx12", "vulkan"],
                     "780m", False)
    elif what == "steps":
        for be in ("dx12", "vulkan"):
            print(be)
            abc = load("abc-dx12.json") if be == "dx12" else load("bcd-vulkan.json")
            sessions = [("before", abc, "before")]
            if be == "dx12":
                sessions += [("(a)", abc, "a"), ("(a, c)", abc, "c"), ("(c) again", load("ce-dx12.json"), "c"),
                             ("+(e)", load("ce-dx12.json"), "e")]
            else:
                sessions += [("(a, c)", abc, "c"), ("+(e), (d)", abc, "d")]
            sessions += [("(e), (d) again", load("df.json"), "d"), ("+(f)", load("df.json"), "f"),
                         ("(f) again", load("fg.json"), "f"), ("+(g)", load("fg.json"), "g")]
            for key in ("apply", "scene sync"):
                print(key)
                steps(sessions, key, CASES, be)
