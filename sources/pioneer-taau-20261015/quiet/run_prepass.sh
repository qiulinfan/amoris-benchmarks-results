#!/bin/sh
# Quiet re-run of taau's prepass check below scale 1 (step 5), 2026-10-15.
WT=<local-path>/.claude/worktrees/taau
Q=<local-path>/out/taau/quiet
LOCK=<local-path>/out/locks/bench_lock.py
cd "$WT"
for ad in nvidia 780m; do for be in dx12 vulkan; do
  echo "$(date +%T) start $ad $be" >> $Q/run_prepass.progress
  POCKET_AA=msaa+taa POCKET_RENDER_SCALE=0.5 python $LOCK run --label quiet-taau -- python tools/prepass_compare.py \
    --backend $be --adapter $ad --cases cubes-sphere,cubes-dense,cubes-shadows,splats,gi-room-static,pt-lab-static \
    --scenes "" --out $Q/prepass/$ad-$be --summary $Q/prepass/$ad-$be.json > $Q/prepass-$ad-$be.log 2>&1
  echo "$(date +%T) end $ad $be exit $?" >> $Q/run_prepass.progress
done; done
echo "$(date +%T) done" >> $Q/run_prepass.progress
