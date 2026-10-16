"""Fills docs/bench/taau.md's cost section from out/taau/tables.md (local helper)."""
import re

doc_path = "<local-path>/.claude/worktrees/taau/docs/bench/taau.md"
tables = open("<local-path>/out/taau/tables.md", encoding="utf-8").read()

def section(name):
    m = re.search(r"### " + re.escape(name) + r"\n(.*?)(?=\n### |\Z)", tables, re.S)
    body = m.group(1)
    out = []
    for block in re.split(r"\n(?=\d+x\d+: )", body.strip()):
        lines = [l for l in block.strip().splitlines() if l.strip()]
        size = lines[0].split(":")[0]
        out.append(f"{size}:\n\n" + "\n".join(lines[1:]))
    return "\n\n".join(out)

cost = f"""Cells: the frame's median timestamped GPU time in ms (opaque passes, that is the depth prepass
and the one or two opaque passes / the TAA pass, and for the check scene with GTAO / GTAO); `*`
marks a cell whose two rounds differ by more than 10%. The check scene's pass times are 10th
percentiles, the dense grid's means.

**The check scene** (light geometry, shading-bound):

{section("check scene")}

**The dense grid, occlusion culling on** (`auto`, the default; 443 cubes visible):

{section("dense occlusion auto")}

**The dense grid, occlusion culling off** (482,000 cubes in the frustum, geometry-bound):

{section("dense occlusion off")}

**Chrome** (155, WebGPU through Direct3D 12, the RTX 5060 with `--force_high_performance_gpu`; the
viewport's check scene, canvas 1574x744; medians of three rounds of 600 timestamped frames; a
viewport built locally from this branch before the clip box's change to 1.5 sigmas, which costs
nothing):

| Mode, scale | GPU frame | Opaque passes | TAA pass |
|---|---:|---:|---:|
| msaa x1 | 0.234 | 0.174 | — |
| taa x1 | 0.392 | 0.158 | 0.148 |
| taa x0.67 | 0.322 | 0.080 | 0.166 |
| taa x0.5 | 0.294 | 0.052 | 0.164 |

What it buys:

- The opaque passes scale with the pixels drawn: at 2560x1440, 0.67 draws them in 44 to 49% of
  their time at the output's size on the RTX 5060 and 47 to 55% on the Radeon 780M; GTAO at 0.67
  takes 42 to 47% of its time. The TAA pass stays the output's size: on the RTX 5060 with
  Direct3D 12 it costs what TAA at the output's size does (0.49 to 0.50 ms at 2560x1440), with
  Vulkan 0.51 to 0.54 ms against 0.38 to 0.40, on the 780M 1.94 to 2.17 ms against 1.56 to 1.88
  with Direct3D 12 and 1.42 to 1.72 against 1.28 to 1.55 with Vulkan; in Chrome 0.16 against 0.15.
- A light frame therefore saves little: the check scene at 2560x1440 with TAA at 0.67 is 25% (RTX
  5060, Direct3D 12) to 9% (Vulkan) cheaper than TAA at the output's size and still dearer than
  MSAA there (0.82 against 0.67 ms with Direct3D 12). On the 780M, where MSAA is dear, 0.67 saves 19
  to 39% against MSAA. With GTAO the saving grows (1.52 to 0.98 ms, RTX 5060 with Direct3D 12).
- The dense grid with occlusion culling is mostly fixed costs at this size (culling, Hi-Z, the TAA
  pass): 0.67 saves 7 to 11% against TAA at the output's size, 0.5 17 to 27%, on both GPUs.
- Without occlusion culling the dense grid is bound by its 5.8M triangles and their overdraw: on
  the RTX 5060 the opaque passes shrink by only 14 to 22% from 1 to 0.5 at 2560x1440, while on the
  780M, whose frame is fill-bound, the frame falls from 31.5 to 19.7 ms at 0.67 and 15.5 ms at 0.5
  with Direct3D 12 (MSAA at the output's size: 89.8 ms).

Wall time per frame (submitted and waited for, including encoding) follows the GPU time on the
780M and moves less on the RTX 5060, whose light frames are bound by submission (for example the
check scene at 2560x1440 with Direct3D 12: 2.63 ms at 1, 2.12 at 0.67, MSAA 1.94)."""

doc = open(doc_path, encoding="utf-8").read()
assert "COST TABLES" in doc
doc = doc.replace("COST TABLES", cost)
open(doc_path, "w", encoding="utf-8", newline="\n").write(doc)
print("ok")
