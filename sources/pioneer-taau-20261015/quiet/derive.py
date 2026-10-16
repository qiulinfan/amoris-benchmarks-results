"""Derived numbers for docs/bench/taau.md 3 and 4 from aa_bench runs in DIR (r*-*.json)."""
import glob, json, statistics, sys
DIR = sys.argv[1]
runs = []
for f in sorted(glob.glob(DIR + "/r*-*.json")):
    if f.endswith(("-start.json", "-end.json")):
        continue
    runs += [r for r in json.load(open(f))["runs"] if "error" not in r]
def P(r): return r.get("passes_p10") or r.get("passes_mean") or {}
def opq(r): p = P(r); return p.get("opaque+sky", 0) + p.get("opaque early", 0) + p.get("depth prepass", 0)
by = {}
for r in runs:
    by.setdefault((r["workload"], r["adapter"], r["backend"], r["size"], r["aa"], r["gtao"], round(r["scale"], 2)), []).append(r)
def get(w, ad, be, sz, aa, g, s, f=lambda r: r["gpu_p50"]):
    rows = by.get((w, ad, be, sz, aa, g, s), [])
    return statistics.median(f(r) for r in rows) if rows else None
def per_round(w, ad, be, sz, aa, g, s, f=lambda r: r["gpu_p50"]):
    return {r["round"]: f(r) for r in by.get((w, ad, be, sz, aa, g, s), [])}
AD = [("nvidia", "dx12"), ("nvidia", "vulkan"), ("780m", "dx12"), ("780m", "vulkan")]
CS, DA, DO = "check scene", "dense occlusion auto", "dense occlusion off"
print("== opaque at 0.67 / at 1, 2560x1440 (check, dense auto)")
for ad, be in AD:
    v = [get(w, ad, be, "2560x1440", "taa", "off", 0.67, opq) / get(w, ad, be, "2560x1440", "taa", "off", 1.0, opq) for w in (CS, DA)]
    g = get(CS, ad, be, "2560x1440", "taa", "depth", 0.67, lambda r: P(r)["gtao"]) / get(CS, ad, be, "2560x1440", "taa", "depth", 1.0, lambda r: P(r)["gtao"])
    print(ad, be, "opaque", [f"{x*100:.0f}%" for x in v], "gtao", f"{g*100:.0f}%")
print("== GTAO at 0.67 / 1 at 1600x900 too")
for ad, be in AD:
    g = get(CS, ad, be, "1600x900", "taa", "depth", 0.67, lambda r: P(r)["gtao"]) / get(CS, ad, be, "1600x900", "taa", "depth", 1.0, lambda r: P(r)["gtao"])
    print(ad, be, f"{g*100:.0f}%")
print("== check scene: taa x0.67 vs taa x1 and msaa, frame")
for sz in ("1600x900", "2560x1440"):
    for ad, be in AD:
        t1 = get(CS, ad, be, sz, "taa", "off", 1.0); t67 = get(CS, ad, be, sz, "taa", "off", 0.67); m = get(CS, ad, be, sz, "msaa", "off", 1.0)
        g1 = get(CS, ad, be, sz, "taa", "depth", 1.0); g67 = get(CS, ad, be, sz, "taa", "depth", 0.67)
        pr1 = per_round(CS, ad, be, sz, "taa", "off", 1.0); pr67 = per_round(CS, ad, be, sz, "taa", "off", 0.67)
        rr = [f"{pr67[k]/pr1[k]*100:.0f}%" for k in sorted(pr1) if k in pr67]
        print(sz, ad, be, f"taa1 {t1:.2f} taa.67 {t67:.2f} ({(1-t67/t1)*100:.0f}% saved, {t67/t1*100:.0f}% of taa1; per round {rr}) msaa {m:.2f} ({t67/m*100:.0f}% of msaa) gtao {g1:.2f}->{g67:.2f}")
print("== dense auto: savings vs taa x1 (median-based; per round)")
for sz in ("1600x900", "2560x1440"):
    for ad, be in AD:
        t1 = get(DA, ad, be, sz, "taa", "off", 1.0); pr1 = per_round(DA, ad, be, sz, "taa", "off", 1.0)
        out = []
        for s in (0.77, 0.67, 0.5):
            t = get(DA, ad, be, sz, "taa", "off", s); pr = per_round(DA, ad, be, sz, "taa", "off", s)
            out.append(f"x{s}: {t:.2f} {(1-t/t1)*100:.0f}% [" + ", ".join(f"{(1-pr[k]/pr1[k])*100:.0f}%" for k in sorted(pr1) if k in pr) + "]")
        m = get(DA, ad, be, sz, "msaa", "off", 1.0)
        print(sz, ad, be, f"msaa {m:.2f} taa1 {t1:.2f} rounds {[round(pr1[k],2) for k in sorted(pr1)]}", "; ".join(out))
print("== dense auto resolve (taa pass) at 2560, RTX")
for ad, be in AD:
    print(ad, be, [round(get(DA, ad, be, "2560x1440", "taa", "off", s, lambda r: P(r)["taa"]), 3) for s in (1.0, 0.77, 0.67, 0.5)])
print("== dense off: opaque 1 -> 0.5 at 2560")
for ad, be in AD:
    o1 = get(DO, ad, be, "2560x1440", "taa", "off", 1.0, opq); o5 = get(DO, ad, be, "2560x1440", "taa", "off", 0.5, opq)
    fr = [get(DO, ad, be, "2560x1440", aa, "off", s) for aa, s in (("msaa", 1.0), ("taa", 1.0), ("taa", 0.67), ("taa", 0.5))]
    print(ad, be, f"opaque {o1:.2f}->{o5:.2f} ({(1-o5/o1)*100:.0f}% less); frames msaa/taa1/.67/.5 {[round(x,2) for x in fr]}")
print("== fixed passes ranges")
FIX = ("cull", "hi-z", "cull late", "shadows")
for w in (CS, DA, DO):
    for ad in ("nvidia", "780m"):
        v = [get(w, ad, be, sz, aa, g, s, lambda r: sum(P(r).get(k, 0) for k in FIX)) for (a2, be) in AD if a2 == ad for sz in ("1600x900", "2560x1440") for (aa, g, s) in [("msaa","off",1.0),("taa","off",1.0),("taa","off",0.77),("taa","off",0.67),("taa","off",0.5)]]
        v = [x for x in v if x is not None]
        print(w, ad, f"{min(v):.2f}..{max(v):.2f}")
print("== wall, check 2560 RTX dx12: taa1, taa.67, msaa")
for ad, be in AD:
    print(ad, be, [round(get(CS, ad, be, "2560x1440", aa, "off", s, lambda r: r["wall_p50"]), 2) for aa, s in (("taa", 1.0), ("taa", 0.67), ("msaa", 1.0))])
