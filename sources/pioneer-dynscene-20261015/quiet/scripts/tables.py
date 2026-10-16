"""Tables for docs/bench/dynamic-scenes.md from the quiet sessions (out/dynscene/quiet/NAME-rN.json):
medians across rounds of each run's medians, with the rounds' range."""
import glob
import json
import statistics
import sys
from collections import defaultdict

Q = "<local-path>/out/dynscene/quiet/"
BE = {"dx12": "D3D12", "vulkan": "Vulkan"}


def runs(name):
    out = []
    for f in sorted(glob.glob(Q + name + "-r[0-9].json")):
        r = int(f[-6])
        for x in json.load(open(f, encoding="utf-8"))["runs"]:
            x["round"] = r
            out.append(x)
    return out


def fmt(x):
    if x is None:
        return "-"
    d = 3 if x < 1 else 2 if x < 10 else 1 if x < 100 else 0
    return f"{x:,.{d}f}"


def med(v):
    v = [x for x in v if x is not None]
    return statistics.median(v) if v else None


def rng(v):
    v = sorted(x for x in v if x is not None)
    return f"{fmt(v[0])}–{fmt(v[-1])}" if v else "-"


def frames_clock(r, key="graphics_mhz_median"):
    return ((r.get("clocks") or {}).get("frames") or {}).get(key)


def pstates(rs):
    s = set()
    for r in rs:
        s |= set(((r.get("clocks") or {}).get("frames") or {}).get("pstates") or [])
    return ",".join(sorted(s))


def group(name):
    g = defaultdict(list)
    errors = []
    for r in runs(name):
        if r.get("headline"):
            g[(r["case"], r["backend"], r.get("adapter"), r["build"])].append(r)
        else:
            errors.append((r["case"], r["backend"], r["build"], r["round"], r.get("error")))
    for e in errors:
        print("ERROR", e)
    return g


def cubes(name, b0, b1, keys=("apply", "scene sync", "render cpu", "frame", "gpu"), ranges=False):
    g = group(name)
    cases = []
    for (c, be, ad, b) in g:
        if c not in cases:
            cases.append(c)
    print(f"## {name}: {b0} → {b1}; " + ", ".join(keys) + ", GPU MHz (frames)")
    for c in cases:
        for be in ("dx12", "vulkan"):
            for ad in sorted({k[2] for k in g if k[0] == c and k[1] == be}, key=str):
                a, b = g.get((c, be, ad, b0)), g.get((c, be, ad, b1))
                if not a and not b:
                    continue
                cells = []
                for k in keys:
                    x = med(h["headline"].get(k) for h in a or [])
                    y = med(h["headline"].get(k) for h in b or [])
                    cell = f"{fmt(x)} → {fmt(y)}"
                    if ranges:
                        cell += f" [{rng(h['headline'].get(k) for h in a or [])} / " \
                                f"{rng(h['headline'].get(k) for h in b or [])}]"
                    cells.append(cell)
                cells.append(f"{fmt(med(frames_clock(h) for h in a or []))} → "
                             f"{fmt(med(frames_clock(h) for h in b or []))}")
                n = (len(a or []), len(b or []))
                print(f"| {c} | {BE[be]}{'/' + ad if ad else ''} | " + " | ".join(cells) +
                      f" | n={n}")


def single(name, keys=("apply", "feed", "scene sync", "render cpu", "frame", "gpu")):
    g = group(name)
    print(f"## {name}: " + ", ".join(keys) + ", MHz, mem MHz, P-states (frames)")
    for (c, be, ad, b), rs in sorted(g.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][3])):
        cells = [f"{fmt(med(h['headline'].get(k) for h in rs))} [{rng(h['headline'].get(k) for h in rs)}]"
                 for k in keys]
        print(f"| {c} | {BE[be]} | {b} | " + " | ".join(cells) +
              f" | {fmt(med(frames_clock(h) for h in rs))} [{rng(frames_clock(h) for h in rs)}]"
              f" | {fmt(med(frames_clock(h, 'memory_mhz_median') for h in rs))} | {pstates(rs)} | n={len(rs)}")


def rt(name):
    g = group(name)
    print(f"## {name}: frame, cpu, gpu per path; clock over the last path's frames")
    for (c, be, ad, b), rs in sorted(g.items(), key=lambda kv: (kv[0][1], kv[0][3])):
        for path in ("cascaded", "ray_traced"):
            cells = [f"{fmt(med(h['headline'][path][k] for h in rs))} [{rng(h['headline'][path][k] for h in rs)}]"
                     for k in ("frame", "cpu", "gpu")]
            clock = ""
            if rs[0].get("clocks_path") == path:
                clock = (f" | {fmt(med(frames_clock(h) for h in rs))} [{rng(frames_clock(h) for h in rs)}] MHz,"
                         f" mem {fmt(med(frames_clock(h, 'memory_mhz_median') for h in rs))}"
                         f" [{rng(frames_clock(h, 'memory_mhz_median') for h in rs)}], {pstates(rs)}")
            print(f"| {path} | {BE[be]} | {b} | " + " | ".join(cells) + clock + f" | n={len(rs)}")
        ratio = [h["headline"]["ray_traced"]["gpu"] / h["headline"]["cascaded"]["gpu"] - 1 for h in rs]
        print(f"   rt/cascaded GPU: {fmt(med(ratio) * 100)}% [{rng([x * 100 for x in ratio])}]")


def crowd(name):
    g = group(name)
    print(f"## {name}: render CPU, frame, GPU (p50), median [range]")
    for (c, be, ad, b), rs in sorted(g.items(), key=lambda kv: (kv[0][1], kv[0][3])):
        hs = [h["headline"]["crowd"] for h in rs]
        print(f"| {BE[be]} | {b} | " + " | ".join(
            f"{med(h[k] for h in hs):.3f} ({min(h[k] for h in hs):.3f}–{max(h[k] for h in hs):.3f})"
            for k in ("cpu", "frame", "gpu")) + f" | n={len(rs)}")


def passes(name, keys=("scatter instances", "opaque", "opaque early")):
    print(f"## {name}: passes")
    for r in runs(name):
        p = (r.get("result") or {}).get("passes_ms", {})
        print(r["case"], r["backend"], r.get("adapter"), r["build"], r["round"],
              {k: p.get(k) for k in keys}, "frame", (r.get("headline") or {}).get("frame"))


if __name__ == "__main__":
    w = sys.argv[1]
    if w == "cubes":
        cubes(sys.argv[2], sys.argv[3], sys.argv[4], ranges="--ranges" in sys.argv)
    elif w == "single":
        single(sys.argv[2])
    elif w == "rt":
        rt(sys.argv[2])
    elif w == "crowd":
        crowd(sys.argv[2])
    elif w == "passes":
        passes(sys.argv[2])
