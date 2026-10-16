import json, glob, statistics
runs = []
for f in sorted(glob.glob("cost/r*-*.json")):
    if f.endswith(("-start.json", "-end.json")):
        continue
    runs += [r for r in json.load(open(f))["runs"] if "error" not in r]
by = {}
for r in runs:
    if r["gtao"] != "off" or r["aa"] != "taa":
        continue
    p = r.get("passes_p10") or r.get("passes_mean")
    by.setdefault((r["adapter"], r["backend"], r["size"], r["workload"], round(r["scale"], 2)), []).append(p["taa"])
out = {}
for (ad, be, size, w, s), v in by.items():
    if s == 1.0:
        continue
    full = statistics.median(by[(ad, be, size, w, 1.0)])
    up = statistics.median(v)
    out.setdefault((ad, be, size), []).append((up - full, up / full - 1, w, s))
for k, v in sorted(out.items()):
    d = [x[0] for x in v]; rr = [x[1] for x in v]
    print(k, f"{min(d):+.2f}..{max(d):+.2f} ms, {min(rr)*100:+.0f}..{max(rr)*100:+.0f}%")
