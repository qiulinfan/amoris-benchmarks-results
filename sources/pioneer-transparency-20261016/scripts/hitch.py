"""The first frame with transparent instances, before and after the review (the stage's pipeline
built on first use, against built with the others): per configuration, build and kind, three
processes of `transparency bench --frames 3 --warm 0`; their largest encoding time (the first
frame's), the process's wall time, and (after) Renderer::new's time. Run inside the bench lock."""
import json
import os
import statistics
import subprocess
import sys
import time

WT = '<local-path>/.claude/worktrees/transparency'
OUT = os.environ.get('HITCH_OUT', '<local-path>/out/transparency/review/hitch')
BUILDS = {
    'before': '<local-path>/out/transparency/build-05716664/target/release/examples/transparency.exe',
    'after': f'{WT}/target/release/examples/transparency.exe',
}
os.makedirs(OUT, exist_ok=True)
configs = [c.split('-') for c in sys.argv[1:]] or [['5060', 'dx12'], ['5060', 'vulkan'], ['780m', 'dx12'],
                                                  ['780m', 'vulkan']]
rows = []
for adapter, backend in configs:
    name = f'{adapter}-{backend}'
    subprocess.run([sys.executable, f'{WT}/tools/machine_conditions.py', f'{OUT}/conditions-{name}.json',
                    '--label', f'transparency hitch {name}'], check=False)
    env = dict(os.environ, POCKET_ADAPTER=adapter, POCKET_BACKEND=backend)
    for rep in range(3):
        for build, exe in BUILDS.items():
            for kind in ['hidden', 'blend']:
                t = time.perf_counter()
                p = subprocess.run([exe, 'bench', '--kind', kind, '--frames', '3', '--warm', '0'], cwd=WT, env=env,
                                   capture_output=True, text=True, timeout=300)
                wall = (time.perf_counter() - t) * 1000.0
                j = json.loads(p.stdout[p.stdout.index('{'):])
                rows.append({'config': name, 'build': build, 'kind': kind, 'rep': rep, 'wall_ms': round(wall, 1),
                             'first_encode_ms': j['cpu_encode_ms']['max'], 'init_ms': j.get('init_ms'),
                             'antialiasing': j['antialiasing'], 'gtao': j['gtao']})
                print(rows[-1], flush=True)
open(f'{OUT}/hitch-{"_".join("-".join(c) for c in configs)}.json', 'w', newline='\n').write(
    json.dumps(rows, indent=1) + '\n')
print('median per config, build, kind: first-frame encode ms, wall ms, init ms')
for c in sorted({r['config'] for r in rows}):
    for b in BUILDS:
        for k in ['hidden', 'blend']:
            rs = [r for r in rows if (r['config'], r['build'], r['kind']) == (c, b, k)]
            med = lambda key: statistics.median(r[key] for r in rs) if rs[0][key] is not None else None  # noqa
            print(c, b, k, med('first_encode_ms'), med('wall_ms'), med('init_ms'))
