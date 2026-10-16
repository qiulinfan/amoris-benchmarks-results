"""Markdown tables from the taau cost runs (DIR/r*-*.json, default out/taau/cost): medians over
rounds. Per workload and size: the GPU frame with its opaque, TAA (and GTAO) passes, then the
fixed passes (culling: cull, Hi-Z, late cull; the check scene's shadows) and the wall time.
Usage: python tables2.py [all|check|auto|off] [DIR]"""
import glob
import json
import statistics
import sys

DIR = sys.argv[2] if len(sys.argv) > 2 else "<local-path>/out/taau/cost"
runs = []
for f in sorted(glob.glob(DIR + "/r*-*.json")):
    if f.endswith(("-start.json", "-end.json")):
        continue
    runs += [r for r in json.load(open(f))["runs"] if "error" not in r]


def passes(r):
    return r.get("passes_p10") or r.get("passes_mean") or {}


def opaque(p):
    return p.get("opaque+sky", 0) + p.get("opaque early", 0) + p.get("depth prepass", 0)


FIXED = ("cull", "hi-z", "cull late", "shadows")
by = {}
for r in runs:
    k = (r["workload"], r["adapter"], r["backend"], r["size"], r["aa"], r["gtao"], round(r["scale"], 2))
    by.setdefault(k, []).append(r)


def med(rows, f):
    return statistics.median(f(r) for r in rows)


def cell(rows):
    return {
        "gpu": med(rows, lambda r: r["gpu_p50"]),
        "wall": med(rows, lambda r: r["wall_p50"]),
        "opaque": med(rows, lambda r: opaque(passes(r))),
        "fixed": med(rows, lambda r: sum(passes(r).get(k, 0) for k in FIXED)),
        "gtao": med(rows, lambda r: passes(r).get("gtao", 0)),
        "taa": med(rows, lambda r: passes(r).get("taa", 0)),
        "spread": (max(r["gpu_p50"] for r in rows) - min(r["gpu_p50"] for r in rows))
        / max(med(rows, lambda r: r["gpu_p50"]), 1e-9),
        "rounds": [r["gpu_p50"] for r in rows],
    }


order = [("msaa", "off", 1.0), ("taa", "off", 1.0), ("taa", "off", 0.77), ("taa", "off", 0.67),
         ("taa", "off", 0.5), ("taa", "depth", 1.0), ("taa", "depth", 0.67)]
combos = [("nvidia", "dx12", "RTX 5060, D3D12"), ("nvidia", "vulkan", "RTX 5060, Vulkan"),
          ("780m", "dx12", "780M, D3D12"), ("780m", "vulkan", "780M, Vulkan")]
what = sys.argv[1] if len(sys.argv) > 1 else "all"


def table(workload, size, fmt):
    print("| Mode, scale | " + " | ".join(c[2] for c in combos) + " |")
    print("|---|" + "---:|" * len(combos))
    for aa, g, s in order:
        if workload != "check scene" and g != "off":
            continue
        row = []
        for ad, be, _ in combos:
            rows = by.get((workload, ad, be, size, aa, g, s))
            row.append(fmt(cell(rows), g) if rows else "—")
        label = f"{aa}{'+gtao' if g == 'depth' else ''} x{s:g}"
        print(f"| {label} | " + " | ".join(row) + " |")


def main_cell(c, g):
    extra = f" / {c['gtao']:.2f}" if g == "depth" else ""
    flag = "*" if c["spread"] > 0.1 else ""
    return f"{c['gpu']:.2f}{flag} ({c['opaque']:.2f} / {c['taa']:.2f}{extra})"



def combined(workload):
    print("| Mode, scale | " + " | ".join(c[2] for c in combos) + " |")
    print("|---|" + "---:|" * len(combos))
    for size in ["1600x900", "2560x1440"]:
        for aa, g, s in order:
            if workload != "check scene" and g != "off":
                continue
            row = []
            for ad, be, _ in combos:
                rows = by.get((workload, ad, be, size, aa, g, s))
                c = cell(rows) if rows else None
                row.append(f"{c['fixed']:.2f} / {c['wall']:.2f}" if c else "-")
            label = f"{size}, {aa}{'+gtao' if g == 'depth' else ''} x{s:g}"
            print(f"| {label} | " + " | ".join(row) + " |")


for workload in ["check scene", "dense occlusion auto", "dense occlusion off"]:
    print(f"\n### {workload}\n")
    for size in ["1600x900", "2560x1440"]:
        print(f"\n{size}:\n")
        table(workload, size, main_cell)
for workload in ["check scene", "dense occlusion auto", "dense occlusion off"]:
    print(f"\n### fixed / wall: {workload}\n")
    combined(workload)
