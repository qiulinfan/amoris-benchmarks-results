"""Summarizes calibration probe JSONL files (probe_test.rs.txt): per file, how many calibrations
failed to intersect, and for each failure the conflicting pair of rounds and its direction.

    python analyze.py FILE.jsonl [...]
"""
import json
import statistics
import sys


def offsets(cal):
    p = cal["period_s"]
    return [(b - g * p, a - g * p, b, a, g * p, e * p) for b, a, g, e in cal["samples"]]


def intersect_drift(cal, max_drift):
    """trace.rs `intersect` with the drift allowance: (offset, half-width) or None."""
    p = cal["period_s"]
    br = [(b, a, g * p) for b, a, g, e in cal["samples"]]
    n = min(br, key=lambda x: x[1] - x[0])
    at = (n[0] + n[1]) / 2
    lo, hi = float("-inf"), float("inf")
    for b, a, g in br:
        d = max_drift * max(abs(b - at), abs(a - at))
        lo, hi = max(lo, b - g - d), min(hi, a - g + d)
    return ((lo + hi) / 2, (hi - lo) / 2) if lo <= hi else None


def by_time(cals):
    """Per process (k restarts at 0): (time of the narrowest round, the intersection's offset) of
    each calibration whose rounds intersect."""
    out = []
    for c in cals:
        if c["k"] == 0 or not out:
            out.append([])
        o = offsets(c)
        lo, hi = max(x[0] for x in o), min(x[1] for x in o)
        if lo <= hi:
            t = min(o, key=lambda x: x[1] - x[0])
            out[-1].append(((t[2] + t[3]) / 2, (lo + hi) / 2))
    return out


def analyze(path):
    cals = [json.loads(l) for l in open(path) if l.strip()]
    errs = [c for c in cals if "err" in c]
    good = [c for c in cals if "err" not in c]
    # Judged again from the raw rounds, so files from before and after the fix compare alike.
    failed = [c for c in good if intersect_drift(c, 0.0) is None]
    widths, gaps, offs, first_widths = [], [], [], []
    rows = []
    for c in good:
        o = offsets(c)
        widths += [(hi - lo) * 1e6 for lo, hi, *_ in o]
        first_widths.append((o[0][1] - o[0][0]) * 1e6)
        gaps += [(o[i][2] - o[i - 1][3]) * 1e6 for i in range(1, len(o))]
        lo = max(x[0] for x in o)
        hi = min(x[1] for x in o)
        if lo <= hi:
            offs.append(((lo + hi) / 2, c.get("t0"), c["k"]))
        if intersect_drift(c, 0.0) is None:
            i = max(range(len(o)), key=lambda k: o[k][0])
            j = min(range(len(o)), key=lambda k: o[k][1])
            v = (o[i][0] - o[j][1]) * 1e6
            # i after j: the GPU clock advanced less than the CPU's between them (by v us at least).
            direction = "GPU behind (later round's GPU time too early)" if i > j else "GPU ahead"
            cpu_between = (o[i][2] - o[j][3]) * 1e6 if i > j else (o[j][2] - o[i][3]) * 1e6
            rows.append(f"  k={c['k']}: rounds {j}->{i}: {direction}, by {v:.1f} us; CPU between "
                        f"the brackets {cpu_between:.0f} us; widths "
                        + ", ".join(f"{(x[1] - x[0]) * 1e6:.0f}" for x in o))
    # The fix's rule (trace.rs MAX_CLOCK_DRIFT) applied to the same rounds.
    drift_failed = [c for c in good if intersect_drift(c, 0.005) is None]
    print(f"{path}: {len(cals)} calibrations, {len(failed)} disagree, {len(errs)} refused samples; "
          f"{len(drift_failed)} disagree with the 0.5% drift allowance")
    both = [(a[1], b[1]) for a, b in ((intersect_drift(c, 0.0), intersect_drift(c, 0.005))
                                      for c in good) if a and b]
    if both:
        print(f"  median half-width us: {statistics.median(x[0] for x in both) * 1e6:.1f} exact, "
              f"{statistics.median(x[1] for x in both) * 1e6:.1f} with the allowance")
    for e in errs:
        print(f"  k={e['k']}: {e['err']}")
    for r in rows:
        print(r)
    if widths:
        q = statistics.quantiles(widths, n=20)
        print(f"  bracket width us: median {statistics.median(widths):.0f}, p5 {q[0]:.0f}, "
              f"p95 {q[-1]:.0f}, max {max(widths):.0f}; first round median "
              f"{statistics.median(first_widths):.0f}")
        print(f"  CPU gap between rounds us: median {statistics.median(gaps):.0f}, max {max(gaps):.0f}")
    # Offsets of the calibrations of one process (same t0), relative to the first.
    by, proc = {}, -1
    for off, t0, k in offs:
        if k == 0 or not by:
            proc += 1
        by.setdefault(proc, []).append((k, off))
    spreads = []
    for t0, v in by.items():
        v.sort()
        spreads.append((max(x[1] for x in v) - min(x[1] for x in v)) * 1e6)
    if spreads:
        print(f"  offset spread within a process us: median {statistics.median(spreads):.1f}, "
              f"max {max(spreads):.1f} ({len(spreads)} processes)")
    # The offset's drift within each process: a least-squares line through the calibrations'
    # offsets at their narrowest round's time (ppm: microseconds of offset per second).
    slopes = []
    for proc in by_time(good):
        if len(proc) < 5:
            continue
        ts, os_ = [x[0] for x in proc], [x[1] for x in proc]
        mt, mo = statistics.mean(ts), statistics.mean(os_)
        sxx = sum((t - mt) ** 2 for t in ts)
        if sxx > 0:
            slope = sum((t - mt) * (o - mo) for t, o in zip(ts, os_)) / sxx
            res = max(abs(o - (mo + slope * (t - mt))) for t, o in zip(ts, os_))
            slopes.append((slope * 1e6, res * 1e6))
    if slopes:
        sl = [x[0] for x in slopes]
        print(f"  offset drift ppm (CPU minus GPU clock rate): median {statistics.median(sl):.0f}, "
              f"min {min(sl):.0f}, max {max(sl):.0f}; median max residual "
              f"{statistics.median(x[1] for x in slopes):.1f} us ({len(slopes)} processes)")
    return len(cals), len(failed), len(errs)


if __name__ == "__main__":
    tot = [0, 0, 0]
    for f in sys.argv[1:]:
        for i, n in enumerate(analyze(f)):
            tot[i] += n
    print(f"total: {tot[0]} calibrations, {tot[1]} disagree, {tot[2]} refused")
