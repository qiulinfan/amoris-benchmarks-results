# Amoris Metal profiling, 2026-10-10

Source: `qiulinfan/amoris`, based on `9b908177`; the measured engine changes were subsequently
published as `3204f24281d0c1bcb6ae9df7df1e9126d50b8f8f`. Recorded on Apple M5, macOS 27.0.1 (26A434), wgpu 30.0.1, native Metal.
These are new local runs, separate from the Windows Pioneer data.

Each run draws 200,000 cubes at 1280x720, 4x MSAA, GTAO off and occlusion off. After two seconds
settling and 60 warm-up frames, 300 frames are measured and traced. The three cases are dense
with prepass off, dense with prepass auto and sphere with prepass auto. Round two reverses their
order; rounds one and three use that listed order. Trace export occurs after the measured loop.

All nine traces contain 300 GPU frames, without missing or dropped records. Every GPU frame
span fits within its own CPU submit/wait bracket plus the reported clock uncertainty and 20 us.
Clock uncertainty ranges from 53.5 to 79.9 us. The JSON files retain the original measurements;
stdout/stderr retain the executable's startup and trace-export messages. No private paths or
credentials were present in these selected files.

`measurements.json` summarizes validation and GPU frame spans directly from the trace events;
`*.bench.json` preserves the executable's wall-time and sampled-pass summaries. The desktop was
active and GPU clocks were not locked. Dense-off run medians range from 6.278 to 29.601 ms and
sphere-auto from 0.849 to 13.877 ms, so these runs demonstrate working frame attribution rather
than a stable performance comparison. No rounds were removed from the three-round set.

`prepass-scenes.json` and `occlusion-scenes.json` compare six scenes at fixed moments. Prepass
images and entity coverage are identical. Occlusion preserves all entity coverage; pt-lab has
one channel differing by one 8-bit level, and the other images are identical.

Reproduce a traced run from the engine checkout:

```sh
cargo build --release -p pocket-render --example many_cubes -p pocket-app --example draw_paths
POCKET_BACKEND=metal POCKET_AA=msaa POCKET_GTAO=off \
  target/release/examples/many_cubes --dense --count 200000 --size 1280x720 \
  --headless-bench 300 --occlusion off --prepass auto --settle 2 \
  --trace frames=300,skip=60,out=out/profiler/metal-dense.json
python3 tools/frame_trace.py stats out/profiler/metal-dense.json
```

Full method and correctness regressions:
[Metal profiling](https://github.com/qiulinfan/amoris/blob/main/docs/bench/metal-profiling.md).

The `controls/` directory preserves deliberately failing alpha-mask, jittered-depth and ocean
motion-write tests, plus two passing TAA suite runs. Checkout paths and native test-thread IDs
are anonymized; assertions and measured pixel counts are unchanged. The preliminary dense-off
trace and stderr are also retained: capture succeeded, but the initial orchestration script
failed to parse the executable's startup banner as JSON. Its stdout was not saved, and this
preliminary capture is outside the specified three-round measurement set.
