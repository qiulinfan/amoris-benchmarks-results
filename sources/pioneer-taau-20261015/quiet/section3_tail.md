**Chrome** (155, WebGPU through Direct3D 12, the RTX 5060 with `--force_high_performance_gpu`; the
viewport's check scene, canvas 1574x744; medians of three rounds of 600 timestamped frames; a
viewport built locally from c8128f1c and not committed; quiet, 14:44 to 14:46). The opaque pass is
the one every frame draws (`opaque+sky`): the passes the auto modes' probes draw on a few frames
(the depth prepass, the early opaque pass, Hi-Z) report medians over those frames only, so they
are left out.

| Mode, scale | GPU frame | Opaque pass | TAA pass |
|---|---:|---:|---:|
| msaa x1 | 0.287 | 0.194 | — |
| taa x1 | 0.441 | 0.178 | 0.166 |
| taa x0.67 | 0.413 | 0.099 | 0.216 |
| taa x0.5 | 0.381 | 0.067 | 0.216 |

Every pass took 10 to 42% longer than in the provisional run on the shared machine (0.234, 0.392,
0.322 and 0.294 ms frames), the passes this branch does not touch too (culling 23 to 42%, the
shadows 10 to 21%), so the difference between the two runs is not the code; its cause was not
measured (the GPU's clocks were not recorded). Within the quiet run the shadow pass takes the same
time in every configuration (0.073 to 0.080 ms), and the upscaling TAA pass costs 30% more than
TAA at the output's size, where the provisional run showed 12% (0.166 against 0.148 ms).

What it buys:

- Where shading bounds them (the check scene, the dense grid with occlusion culling) the opaque
  passes scale with the pixels drawn (45% of them at 0.67): at 2560x1440, 0.67 draws them in 47 to
  49% of their time at the output's size on the RTX 5060 and 50 to 58% on the Radeon 780M; GTAO at
  0.67 takes 43 to 46% of its time. The culling passes do not depend on the scale.
- The TAA pass stays the output's size and costs at least what TAA there does: the same with
  Direct3D 12 on the RTX 5060 (-0.01 to +0.00 ms), 0.05 to 0.06 ms more at 1600x900 and 0.12 to
  0.14 ms more at 2560x1440 with Vulkan (34 to 38%), 0.08 to 0.52 ms more on the 780M with
  Direct3D 12 (14 to 33%) and 0.07 to 0.27 ms more with Vulkan (12 to 28%), over every workload and
  scale here; in Chrome 0.216 against 0.166 ms (30%). On the 780M with Direct3D 12 at 2560x1440 it
  is dearest at 0.67 (the dense grid: 2.09 ms against 1.57 at 1, 1.87 at 0.77 and 1.94 at 0.5; the
  check scene: 1.69 against 1.35, 1.57 and 1.56).
- A light frame therefore saves little: the check scene at 2560x1440 with TAA at 0.67 is 23% (RTX
  5060, Direct3D 12) to 8% (Vulkan) cheaper than TAA at the output's size, and still dearer than
  MSAA there (0.79 against 0.66 ms with Direct3D 12). On the 780M with Vulkan, where MSAA is dear,
  0.67 costs 42% (2560x1440) to 52% (1600x900) of MSAA's frame and 83 to 88% of TAA's at the
  output's size; with Direct3D 12 83% of TAA's at both sizes (81 to 84% within each round). With
  GTAO the saving grows (1.40 to 0.94 ms on the RTX 5060 with Direct3D 12).
- The dense grid with occlusion culling is mostly fixed costs at these sizes (culling and Hi-Z,
  0.5 to 0.8 ms on the RTX 5060 and 2.1 to 3.5 ms on the 780M, and the TAA pass): at 2560x1440, 0.67
  saves 7 to 16% against TAA at the output's size and 0.5 13 to 22%, on both GPUs; at 1600x900
  0.67 saves 3 to 9%.
- Without occlusion culling the dense grid is bound by its 5.8M triangles and their overdraw: on
  the RTX 5060 the opaque passes shrink by only 21% from 1 to 0.5 at 2560x1440 with Direct3D 12
  (the Vulkan row jumps between two levels, section 6), while on the 780M, whose frame is
  fill-bound, the frame falls from 30.5 to 18.9 ms at 0.67 and 14.9 ms at 0.5 with Direct3D 12
  (MSAA at the output's size: 86.0 ms).
- Wall time per frame follows the GPU time on the 780M and moves less on the RTX 5060, whose light
  frames are bound by submission (the check scene at 2560x1440 with Direct3D 12: 2.24 ms at 1,
  1.98 at 0.67, MSAA 1.66).

## 4. Context: UE 5.7 on the same scene

Branch `explore/ue5` measured Unreal Engine 5.7.4 on the dense grid at 2560x1440 on this RTX 5060
(2026-10-10, quiet, `docs/bench/ue5-dense.md` there; a different engine and frame, so context, not
a match). A new project's defaults render 1552x873 (61%) and reconstruct with TSR: TSR alone took
3.55 ms with Direct3D 12 and 3.95 ms with Vulkan of a 16.40 and 21.23 ms frame (Lumen, virtual
shadow maps, the ray-tracing scene). With Nanite at 100% TSR took 5.17 and 6.58 ms of 9.21 and
12.09 ms; with UE's TAA instead the Nanite frame was 4.23 and 5.88 ms. The matched forward
configuration with MSAA and per-instance HZB occlusion drew it in 3.49 and 4.59 ms against our
2.98 and 3.08 ms then (in the window, with the post chain timed; the numbers below are headless,
without it, on a later master).

Here the same grid at 2560x1440 with occlusion culling, TAA upscaling from 0.67 (the measured
scale nearest 61%) costs 1.32 ms with Direct3D 12 and 1.29 ms with Vulkan on the RTX 5060 (from 0.5,
1.27 and 1.20), of which the upscaling resolve is 0.50 to 0.54 ms; UE's TSR pass from 61% alone took
3.55 to 3.95 ms. TSR reconstructs far more carefully (its own history rejection and thin-feature
handling among others), and section 2 shows what the cheaper resolve loses under motion; our
timestamped total also leaves out bloom and the display transform, which UE's includes.

On the RTX 5060, whose default is MSAA at the output's size (1.39 ms with Direct3D 12, 1.35 with
Vulkan), upscaling barely pays on this scene: 0.67 saves 5 and 4%, 0.5 9 and 11%, for 3.5 and 5.5
dB under the panning camera (section 2); the provisional runs had 0.67 level with MSAA with
Direct3D 12 (1.37 against 1.36 ms). On the Radeon 780M the default is TAA at the output's size
(5.66 ms with Direct3D 12, 5.34 with Vulkan here). Against it 0.77 saves 9% with Direct3D 12 and
10% with Vulkan (6 and 11%, and 10 and 10%, within each round), 0.67 7% with Direct3D 12 (5.29 ms;
0 and 13% within the two rounds) and 16% with Vulkan (4.49 ms; 16% in both rounds), 0.5 18 and
22%; for 2.3, 3.8 and 6.6 dB of the still image, 2.0, 2.7 and 4.5 dB under the panning camera, and
at 0.67 2.1 to 4.2 dB in the regions (section 2). With Direct3D 12, whose resolve is dearest at
0.67, 0.67 is no cheaper than 0.77 there (5.29 against 5.17 ms). MSAA at the output's size (7.30
and 10.08 ms on the 780M) is not the mode upscaling would replace there.

