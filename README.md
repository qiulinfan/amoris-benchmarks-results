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
