# Amoris benchmark results

Measured outputs, quality comparisons, and validation logs for [Amoris](https://github.com/qiulinfan/amoris).
Engine code, benchmark programs, and specifications remain in the engine repository. Historical
results keep their original workload, platform, and date; a source snapshot is not a new rerun.

| Directory | Origin |
| --- | --- |
| `sources/pioneer-20261010/docs/evidence/` | Amoris Pioneer snapshot `9a3e4b0814959629202629845b85205c42086505`, including earlier inherited Amoris results. |
| `sources/amoris-local-backup-20261010/` | Local artifacts archived from Amoris on 2026-10-10: physics, showcase, lighting, and agent evaluations. Identical Pioneer artifacts are stored once. |
| `sources/amoris-20261010/` | macOS integration and source-output cleanup validation runs. |
| `sources/pioneer-prepass-20261010/` | Amoris Pioneer `explore/prepass` at `8cde3bdf501696ccd50173ba750d4aafa5d8f952` (Pioneer's `out/prepass/`): depth prepass benchmarks on the RTX 5060 and Radeon 780M, headless and windowed, with Direct3D 12 and Vulkan; the auto mode's probe A/B; image comparisons with the prepass off and on, difference strips and heat maps; run logs. Full frame pairs stay local. |
| `sources/pioneer-profiler-20261010/` | Amoris Pioneer `explore/profiler` at `53ad87d587dd083d7902bbe290377c03d0005fbe` (Pioneer's `out/profiler/`): per-frame Chrome Trace Event JSON of the dense many_cubes grid with Direct3D 12 and Vulkan, review re-measurements, nvidia-smi samples, and RenderDoc analyses with the forward shader's DXIL and SPIR-V disassembly. RenderDoc captures (`.rdc`) and shader binaries stay local. |
| `sources/pioneer-dynscene-20261015/` | Amoris Pioneer `explore/dynscene` at `71d13929f551ecc48d41070b35c83248a67fda14` (Pioneer's `out/dynscene/`): dynamic scenes (linear scene apply, one-write instance upload, one skinning dispatch) on the RTX 5060 and Radeon 780M with Direct3D 12 and Vulkan: build-by-build step comparisons, the quiet re-measurement rounds, crowd, ray-traced-shadow and 1.6M-instance cases, image-comparison results, GPU test logs per build and adapter, review runs, job scripts, and eight sample frame traces (moving 100k, before and after). The other 600 frame traces (96 MB), frame captures and test and bench binaries stay local. |
| `sources/pioneer-liveprof-20261015/` | Amoris Pioneer `explore/liveprof` at `d58d1b57a2093bf41e25567f6869651719d166db` (Pioneer's `out/liveprof/`): the editor's live profiler on the real host: profile benches (paced and unpaced) of the smoke run, three runs and the quiet re-measurement, captured profile frames, console and viewport statistics, and profiler-panel screenshots. Full editor and viewport screenshots and the bench binary stay local. |
| `sources/pioneer-webauto-20261015/` | Amoris Pioneer `explore/webauto` at `e231afea0bf45003e656f24a9cf02018f5b41d6e` (Pioneer's `out/webauto/`): the prepass and occlusion auto modes in Chrome's WebGPU on both GPUs: per-run summaries of every round (before, after, r2, truth, occlusion and quiet), the quiet round's raw poll samples, native references, tables, run scripts and logs. Raw poll samples of the earlier rounds (42 MB), off/on frame pairs, copies of the web harness and binaries stay local. |
| `sources/pioneer-physx-20261015/` | Amoris Pioneer `explore/physx` at `23d862b3bde831cc2314a2af8132ed6a58afe827`, merged into `master` by `f6beb090368cd5a52cc1316acc2fb1424800b12c` (the branch has since been fast-forwarded to a later `master`; Pioneer's `out/physx/`): the R1 physics bench, Rapier only, on the Ryzen 9 270: smoke, instruction-set, wave and quiet rounds (JSONL runs, summaries, check records, machine records) and the sampling profiler's per-scene summaries. The profiler's raw samples (`profile.json`, 38 MB) stay local; everything from the untested Unity PhysX harness is omitted. |
| `sources/pioneer-rules-20261015/` | Amoris Pioneer `explore/rules` at `bf7ea8ca3ffbf9ffc90d2c9473d77264b7c682d7` (Pioneer's `out/rules/`): the in-engine script cost baseline (rules workload): native, Node and Chrome WebAssembly rounds of the smoke, wave, quiet and quiet-repeat runs, the fixed input sets and the web harness the runs used. The WebAssembly builds stay local. |
| `sources/pioneer-taau-20261015/` | Amoris Pioneer `explore/taau` at `8fb39dc077ae70c111bbec7979dda33c676908be` (Pioneer's `out/taau/`): TAA upscaling at render scales below 1: cost rounds on both GPUs and backends, build and prepass comparison summaries, quality metrics with their comparison panels, the fix investigation's crops, mutation checks, web runs, tables and scripts. Full frame pairs (1.6 GB), earlier quality panels and binaries stay local. |
| `sources/pioneer-shadowcull-20261015/` | Amoris Pioneer `explore/shadowcull` at `0bdb251dd642df3a0844a1dab00aad2e1497a39f` (Pioneer's `out/shadowcull/`): shadow casters culled by each cascade's slice: bench rounds including 1.6M instances, off/on comparisons on six configurations with occlusion and minimal-feature variants, game-sample checks, GPU mutation runs, web runs and frame traces, with every difference image. Full frame pairs (628 MB) and binaries stay local. |
| `sources/pioneer-writes-20261015/` | Amoris Pioneer `explore/writes` at `5499c22ec43924a2d706fc86bc7733f0b269d37d` (Pioneer's `out/writes/`): the write-trace bench (`debug.writes`) rounds and the quiet re-measurement, the course-helm project it ran, smoke and test logs. |
| `sources/pioneer-gizmo-20261015/` | Amoris Pioneer `explore/gizmo` at `e688d7dbd1877101e181e9191463247b73d49727` (Pioneer's `out/gizmo/`): live gizmo drags on the real host: drag latency records of the provisional, review and quiet runs, Chrome CPU profiles, serve and console logs, and a history-panel crop. Full editor screenshots stay local. |
| `sources/pioneer-qjs-20261015/` | Amoris Pioneer `explore/qjs` at `7e4f2b6f9bf23d7cf0b127b52bfc32dfa5ca51e4` (Pioneer's `out/qjs/`): QuickJS-ng with P12 computed goto and C Math natives: rules-workload rounds of the base, P12, natives and flag builds, native and web, the quiet, repeat and flags5 re-measurements, the fixed input sets, build and test logs and the build-script diffs. Copied source trees, build trees and binaries stay local. |
| `sources/pioneer-gpu780m-20261015/` | Amoris Pioneer `explore/gpu780m` at `76f2e5cd15c87da3c26bf5bbaa05a77c7e191ad8` (Pioneer's `out/gpu780m/`): render tests on both GPUs and both backends: GPU-matrix runs before and after the fixes, debug and repeat runs, timestamp, TAA and parallel probes, splat and TAA reruns, the quiet re-measurement, neural-material diagnostic images and the run scripts. |
| `sources/pioneer-transparency-20261016/` | Amoris Pioneer `explore/transparency` at `261eb475dcb19efd539f60e098081aff2b2750a5` (Pioneer's `out/transparency/`): the sorted transparent stage: bench and A/B rounds of the draw strategies, the quiet and review re-measurements, hitch, ghosting and path-traced reference checks with their small images, build, occlusion and prepass comparison summaries, browser draw-path checks and a GPU-matrix run. Full frame pairs (1.2 GB), raw float readbacks, copied source trees and binaries stay local. |
| `sources/pioneer-lookahead-20261016/` | Amoris Pioneer `explore/lookahead` at `29aba17a7b72459003b21baf6717f9b81ea3495d` (Pioneer's `out/lookahead/`): fork lookahead for the skipper: the three tuning runs, the exploration course, the four runs of 2026-10-15 and the quiet re-measurement (course and fork results, tables, logs). |
| `sources/pioneer-physcache-20261016/` | Amoris Pioneer `explore/physcache` at `d70abdc1695c0bbdbd50d307f158865dc37a3997` (Pioneer's `out/physcache/`): fixed shapes by reference in the physics cache: four runs of 2026-10-15 and the quiet re-measurement, trajectory and test notes, the A/B script and probe. Benchmark binaries and WebAssembly builds stay local. |
| `sources/pioneer-serveloop-20261016/` | Amoris Pioneer `explore/serveloop` at `ceb7e6de94573b7e51cdeef48cf1093b12669bbe` (Pioneer's `out/serveloop/`): the serve loop: idle-cycle diagnostics, publish benches, live runs and gizmo drags against the base, host and new builds in two waves and the quiet re-measurement. Editor screenshots, the base editor build and binaries stay local. |
| `sources/pioneer-scriptprof-20261016/` | Amoris Pioneer `explore/scriptprof` at `ec93b98fe1101e58e9123cad9bce81b6e370ab39` (Pioneer's `out/scriptprof/`): `scripts.profile` and the split of script time: split runs of the wave and the quiet re-measurement, the end-to-end rules project and harness, and depth-test notes. |
| `sources/pioneer-robust-20261016/` | Amoris Pioneer `explore/robust` at `495703d3e67dd613fe52fcaed476e973e87cbb11` (Pioneer's `out/robust/`): dev-viewport loads (first, fix, probe, master and production builds), clock calibration idle and under load, play-order and library test runs, several of them repeated with a game running, the sailing projects used, probes and GPU-matrix logs. Viewport screenshots, viewport builds and binaries stay local. |
| `sources/pioneer-merge-checks-20261016/` | Amoris Pioneer `master` after the wave merges (Pioneer's `out/wave4/`, `out/wave5/`, `out/wave6/` and `out/gpu-matrix/`): full `cargo xtask check` logs at `b7be59a24da8a53f957685d7163fa2843fb11c5a` (wave 4), `3fdc5b832b75b665996d3f49c5ff8b454b0cfd5f` (wave 5) and `6af291dbafaaef8b99614225825fa29ab0fe34eb` (wave 6), and the GPU-matrix results of the last two with per-test logs of the wave-6 run. A test binary kept for a driver-cache investigation stays local. |

Source references: Amoris base `04c43b61c7263f8eb378fb664d389ea00a9ec039`, local pre-rewrite
snapshot `7bb578df551901812ef10bb73a61a59842f2b489`, and reconstructed engine reference
`10f6d4f9989ba3140e7674ff89c78cda081d4bb9`. Per-run records retain the build references actually
recorded when they ran. The final reference adds a same-pipeline TAA test control; earlier
failed comparisons, reruns, and the deliberately failing negative control remain in the archive.

The records cover Apple M5/Metal, Windows Direct3D 12 and Vulkan on RTX 5060 and Radeon 780M,
and browser WebGPU. Consult each record for its actual adapter, settings, limitations, and run status.
Failures and repeats are retained alongside successful runs; skipped checks are not passes.

Methods and interpretation: [rendering](https://github.com/qiulinfan/amoris/tree/main/docs/bench),
[physics](https://github.com/qiulinfan/amoris/blob/main/docs/bench/physics.md),
[agent development](https://github.com/qiulinfan/amoris/blob/main/bench/agent-dev/protocol.md),
and [agent debugging](https://github.com/qiulinfan/amoris/blob/main/docs/bench/agent-debug.md).

Public copies omit local paths, connection addresses, process inventories, credentials, private
setup context, and file-checksum audit records. Public game tasks and model responses are retained.
Unsafe UI screenshots are omitted rather than altering their pixels. Metrics and scores are not
recalculated during publication. Historical shell wrappers contain anonymized paths and are not
ready-to-run commands. World-state, coverage, and cache identities retain their diagnostic meaning.

Unsafe UI originals are retained locally under ignored `.private-originals/`; the public image
set contains only the reviewed safe subset. Original source records remain available locally.
Privacy reviews, exclusion inventories, and secret scan reports are kept outside this repository.

Engine-authored material follows the Amoris MIT license in `LICENSES/amoris-engine-MIT.txt`.
Render previews may depict third-party assets; their authors and licenses are preserved under
`LICENSES/`. These records do not grant additional rights to depicted assets or third-party model
responses. See [asset credits](LICENSES/showcase-credits.md) and [town credits](LICENSES/town-walk-CREDITS.txt).
