#!/bin/sh
# docs/bench/dynamic-scenes.md 7, the section 6 steps: this checkout's build, images, tests.
WT=<local-path>/.claude/worktrees/dynscene
Q=<local-path>/out/dynscene/quiet
LOCK="python <local-path>/out/locks/bench_lock.py run --label quiet-dynscene --max-hold-min 60 --"
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
unset CARGO_TARGET_DIR
cd $WT
echo "=== build $(date +%T)"
cargo build --release -p pocket-render --example many_cubes --example lod_field --example splats \
    --example showcase_bench --example image_diff > $Q/s6-build.log 2>&1; echo "build exit $?"
echo "=== compare rtx $(date +%T)"
$LOCK python tools/build_compare.py --before $Q/before --backends dx12,vulkan --out target/build-compare \
    --summary $Q/compare-rtx.json > $Q/compare-rtx.log 2>&1; echo "compare rtx exit $?"; tail -1 $Q/compare-rtx.log
echo "=== compare 780m $(date +%T)"
$LOCK python tools/build_compare.py --before $Q/before --backends dx12,vulkan --adapters 780m --modes msaa,taa \
    --out target/build-compare --summary $Q/compare-780m.json > $Q/compare-780m.log 2>&1; echo "compare 780m exit $?"; tail -1 $Q/compare-780m.log
echo "=== scene tests $(date +%T)"
cargo test -p pocket-render --lib scene:: > $Q/tests-scene.log 2>&1; echo "scene tests exit $?"; grep "test result" $Q/tests-scene.log
for cfg in dx12-rtx vulkan-rtx dx12-780m vulkan-780m; do
  be=${cfg%-*}; ad=${cfg#*-}
  echo "=== tests $cfg $(date +%T)"
  if [ $ad = 780m ]; then export POCKET_ADAPTER=780m; else unset POCKET_ADAPTER; fi
  POCKET_BACKEND=$be $LOCK cargo test -p pocket-render --no-fail-fast > $Q/tests-$cfg.log 2>&1
  echo "tests $cfg exit $?"; grep -E "test result|FAILED|^failures:|panicked" $Q/tests-$cfg.log | grep -v "^test .* ok$" | head -40
done
echo "=== done $(date +%T)"
