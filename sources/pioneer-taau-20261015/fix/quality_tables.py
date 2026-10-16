"""Prints the taau quality tables (docs/bench/taau.md 2) from an aa_eval upscale(-tune) JSON."""
import json
import sys

j = json.load(open(sys.argv[1]))['upscale']
st = j['still']
main = ['msaa', 'taa x1', 'taa x0.77', 'taa x0.67', 'taa x0.5', 'msaa+taa x0.67']
print('| Mode | Opaque pass | 1 | 4 | 16 | 64 | 128 | last cycle |')
for n in main:
    if n not in st:
        continue
    v = st[n]
    c = dict((a, b) for a, b in v['psnr_by_frame'])
    print(f"| {n} | {v['scene_size']} | " + ' | '.join(f"{c[k]:.2f}" for k in [1, 4, 16, 64, 128])
          + f" | {v['psnr_last_cycle']:.2f} ({v['jitter_cycle']}) |")
print()
print('| Region | ' + ' | '.join(main[:5]) + ' |')
for reg, rv in j['regions'].items():
    cyc = rv['psnr_last_cycle']
    print(f"| {reg} | " + ' | '.join(f"{cyc[n]:.2f}" for n in main[:5]) + ' |')
print()


def mot(key, n, frame=60):
    for r in j[key]['variants'][n]:
        if r['frame'] == frame:
            return f"{r['psnr']:.2f} / {r['psnr_moving_cube']:.2f} / {r['temporal_psnr']:.2f}"


print('| Mode | Panning camera | Still camera, moving cube |')
for n in main[:5]:
    print(f"| {n} | {mot('motion_pan', n)} | {mot('motion_still', n)} |")
print()
# ranges over frames 30..90 of the loss against msaa and taa x1 (pan)
for ref in ['msaa', 'taa x1']:
    for key in ['motion_pan', 'motion_still']:
        losses = []
        tl = []
        for n in ['taa x0.77', 'taa x0.67', 'taa x0.5']:
            for a, b in zip(j[key]['variants'][ref], j[key]['variants'][n]):
                losses.append(a['psnr'] - b['psnr'])
                tl.append(a['temporal_psnr'] - b['temporal_psnr'])
        print(f"{key} vs {ref}: image loss {min(losses):.1f}..{max(losses):.1f}, temporal {min(tl):.1f}..{max(tl):.1f}")
for key in ['motion_pan']:
    for n in ['taa x0.77', 'taa x0.67', 'taa x0.5']:
        r = [x for x in j[key]['variants'][n] if x['frame'] == 60][0]
        a = [x for x in j[key]['variants']['taa x1'] if x['frame'] == 60][0]
        print(n, 'f60 drop image', round(a['psnr'] - r['psnr'], 2), 'cube', round(a['psnr_moving_cube'] - r['psnr_moving_cube'], 2))
tune = [k for k in st if '(' in k]
if tune:
    print()
    print('| Variant (scale) | Still, last cycle | Panning camera | Still camera, moving cube |')
    for scale in ['0.67', '0.5', '0.77']:
        base = f'taa x{scale}'
        print(f"| {base} default | {st[base]['psnr_last_cycle']:.2f} | {mot('motion_pan', base)} | {mot('motion_still', base)} |")
        for k in tune:
            if k.startswith(base + ' ('):
                d = st[k]['psnr_last_cycle'] - st[base]['psnr_last_cycle']
                print(f"| {k} | {st[k]['psnr_last_cycle']:.2f} ({d:+.2f}) | {mot('motion_pan', k)} | {mot('motion_still', k)} |")
