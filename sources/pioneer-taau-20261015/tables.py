"""Markdown tables from the taau cost runs (out/taau/cost/r*-*.json): medians over rounds."""
import glob
import json
import statistics
import sys

runs = []
for f in sorted(glob.glob("<local-path>/out/taau/cost/r*-*.json")):
    if f.endswith(("-start.json", "-end.json")):
        continue
    runs += [r for r in json.load(open(f))["runs"] if "error" not in r]

def passes(r):
    return r.get("passes_p10") or r.get("passes_mean") or {}

def opaque(p):
    return p.get("opaque+sky", 0) + p.get("opaque early", 0) + p.get("depth prepass", 0)

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
        "hiz": med(rows, lambda r: passes(r).get("hi-z", 0)),
        "gtao": med(rows, lambda r: passes(r).get("gtao", 0)),
        "taa": med(rows, lambda r: passes(r).get("taa", 0)),
        "n": len(rows),
        "spread": (max(r["gpu_p50"] for r in rows) - min(r["gpu_p50"] for r in rows))
        / max(med(rows, lambda r: r["gpu_p50"]), 1e-9),
    }

order = [("msaa", "off", 1.0), ("taa", "off", 1.0), ("taa", "off", 0.77), ("taa", "off", 0.67),
         ("taa", "off", 0.5), ("taa", "depth", 1.0), ("taa", "depth", 0.67)]
combos = [("nvidia", "dx12", "RTX 5060, D3D12"), ("nvidia", "vulkan", "RTX 5060, Vulkan"),
          ("780m", "dx12", "780M, D3D12"), ("780m", "vulkan", "780M, Vulkan")]
what = sys.argv[1] if len(sys.argv) > 1 else "all"
for workload in ["check scene", "dense occlusion auto", "dense occlusion off"]:
    if what != "all" and what not in workload:
        continue
    print(f"\n### {workload}\n")
    for size in ["1600x900", "2560x1440"]:
        print(f"\n{size}: GPU frame ms (opaque passes + prepass / TAA" + (" / GTAO" if workload == "check scene" else "") + "), wall p50\n")
        head = "| Mode, scale | " + " | ".join(c[2] for c in combos) + " |"
        print(head)
        print("|---|" + "---:|" * len(combos))
        for aa, g, s in order:
            if workload != "check scene" and g != "off":
                continue
            row = []
            for ad, be, _ in combos:
                rows = by.get((workload, ad, be, size, aa, g, s))
                if not rows:
                    row.append("—")
                    continue
                c = cell(rows)
                extra = f" / {c['gtao']:.2f}" if g == "depth" else ""
                flag = "*" if c["spread"] > 0.1 else ""
                row.append(f"{c['gpu']:.2f}{flag} ({c['opaque']:.2f} / {c['taa']:.2f}{extra})")
            label = f"{aa}{'+gtao' if g == 'depth' else ''} x{s:g}"
            print(f"| {label} | " + " | ".join(row) + " |")
