#!/bin/sh
# neural_material on the 780M: master's tree (4d1703d4) against head, both backends, two runs each.
for run in 1 2; do for be in dx12 vulkan; do
  (cd <local-path>/.claude/worktrees/dynscene/target/src-before/crates/pocket-render && POCKET_BACKEND=$be POCKET_ADAPTER=780m <local-path>/out/dynscene/review/neural/before-neural_material.exe > <local-path>/out/dynscene/review/neural/before-$be-$run.log 2>&1); echo "before $be run $run: exit $? $(grep 'test result' <local-path>/out/dynscene/review/neural/before-$be-$run.log)"
  (cd <local-path>/.claude/worktrees/dynscene/crates/pocket-render && POCKET_BACKEND=$be POCKET_ADAPTER=780m <local-path>/out/dynscene/testbins/head/neural_material.exe > <local-path>/out/dynscene/review/neural/head-$be-$run.log 2>&1); echo "head $be run $run: exit $? $(grep 'test result' <local-path>/out/dynscene/review/neural/head-$be-$run.log)"
done; done
