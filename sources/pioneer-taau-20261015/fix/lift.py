import os, subprocess, sys
from PIL import Image
F = '<local-path>/out/taau/fix'
W = '<local-path>/.claude/worktrees/taau'
os.chdir(W)
exe = W + '/target/release/examples/showcase_bench.exe'
for backend in ('vulkan', 'dx12'):
    for scene in ('samples/pt-lab', F + '/pt-lab-lift'):
        imgs = []
        for pre in ('off', 'on'):
            out = f'{F}/lift-{backend}-{os.path.basename(scene)}-{pre}.png'
            env = dict(os.environ, POCKET_BACKEND=backend, POCKET_ADAPTER='nvidia', POCKET_PREPASS=pre,
                       POCKET_AA='msaa+taa', POCKET_RENDER_SCALE='0.5')
            subprocess.run([exe, scene, '--width', '1280', '--height', '720', '--frames', '5', '--warm', '5',
                            '--capture', out], env=env, check=True, capture_output=True)
            imgs.append(Image.open(out).convert('RGB'))
        a, b = imgs[0].load(), imgs[1].load()
        w, h = imgs[0].size
        diff = [(x, y, a[x, y], b[x, y]) for y in range(h) for x in range(w) if a[x, y] != b[x, y]]
        print(backend, scene, 'differing pixels:', len(diff), diff[:4], flush=True)
