"""prepass_compare and occlusion_compare (renderer-example captures, pt-lab included) on the four
configurations, from the transparency worktree, into out/transparency/{prepass,occlusion}-compare-review/."""
import json
import subprocess
import sys

WT = '<local-path>/.claude/worktrees/transparency'
OUT = '<local-path>/out/transparency'
CASES = 'cubes-sphere,cubes-dense,cubes-shadows,splats,gi-room-static,pt-lab-static'
tool = sys.argv[1]  # prepass or occlusion
for adapter in ['5060', '780m']:
    for backend in ['dx12', 'vulkan']:
        name = f'{adapter}-{backend}'
        out = f'{OUT}/{tool}-compare-review/{name}'
        p = subprocess.run([sys.executable, f'{WT}/tools/{tool}_compare.py', '--backend', backend, '--adapter',
                            adapter, '--cases', CASES, '--scenes', '', '--out', out, '--summary', out + '.json'],
                           cwd=WT, capture_output=True, text=True)
        print(name, 'exit', p.returncode)
        print(p.stdout[-1500:])
        if p.returncode:
            print(p.stderr[-1500:])
