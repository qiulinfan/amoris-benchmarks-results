"""pt-lab's forward image (transparency_pt.py's showcase_bench call) drawn several times by each build:
does a build reproduce its own image to the bit? Run inside the bench lock."""
import os
import subprocess
import sys
from array import array

WT = '<local-path>/.claude/worktrees/transparency'
T = '<local-path>/out/transparency'
OUT = f'{T}/quiet/determinism'
BUILDS = [('after', f'{WT}/target/release/examples/showcase_bench.exe', 6),
          ('before', f'{T}/before/target/release/examples/showcase_bench.exe', 3)]
REFS = {'after-2a59b3d7': f'{T}/pt-lab/after-2a59b3d7.f32', 'after-440dd7f8': f'{T}/pt-lab/after-440dd7f8.f32',
        'before': f'{T}/pt-lab/before.f32', 'after-review-0018': f'{T}/pt-lab/after.f32'}
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, POCKET_BACKEND='dx12', POCKET_AA='msaa', POCKET_GTAO='off', POCKET_OCCLUSION='off',
           POCKET_ADAPTER='5060')


def load(p):
    a = array('f')
    with open(p, 'rb') as f:
        a.frombytes(f.read())
    return a


def diff(a, b):
    px = {i // 3 for i in range(len(a)) if a[i] != b[i]}
    return len(px), max((abs(x - y) for x, y in zip(a, b)), default=0.0)


images = {}
for label, exe, n in BUILDS:
    for k in range(n):
        hdr, ids = f'{OUT}/{label}-{k}.f32', f'{OUT}/{label}-{k}.ids.u32'
        p = subprocess.run([exe, 'samples/pt-lab', '--width', '320', '--height', '240', '--frames', '5', '--warm', '5',
                            '--hdr', hdr, '--ids', ids], cwd=WT, env=env, capture_output=True, text=True, timeout=600)
        if p.returncode:
            print(label, k, 'failed', p.stderr[-800:])
            sys.exit(1)
        images[f'{label}-{k}'] = load(hdr)
refs = {k: load(v) for k, v in REFS.items()}
for name, img in images.items():
    row = [f'{r}: {diff(img, ref)[0]} px' for r, ref in refs.items()]
    first = images[name.rsplit('-', 1)[0] + '-0']
    print(f'{name:12} vs its run 0: {diff(img, first)[0]:3} px (max {diff(img, first)[1]:.2e}); ' + ', '.join(row))

# Which pixels: the runs' differences against the stored images' differences.
def pixels(a, b):
    return {i // 3 for i in range(len(a)) if a[i] != b[i]}
base = refs['after-2a59b3d7']
sets = {'440dd7f8 vs 2a59b3d7 (stored)': pixels(refs['after-440dd7f8'], base),
        'review 00:18 vs 2a59b3d7 (stored)': pixels(refs['after-review-0018'], base)}
for name, img in images.items():
    if name.startswith('after'):
        sets[f'{name} vs 2a59b3d7'] = pixels(img, base)
union = set().union(*[v for k, v in sets.items() if not k.startswith('440')])
for k, v in sets.items():
    print(f'{k:36} {len(v):3} px')
print('440dd7f8 pixels also varying between runs of one build:', len(sets['440dd7f8 vs 2a59b3d7 (stored)'] & union),
      'of', len(sets['440dd7f8 vs 2a59b3d7 (stored)']), '; union of run-to-run pixels', len(union))
