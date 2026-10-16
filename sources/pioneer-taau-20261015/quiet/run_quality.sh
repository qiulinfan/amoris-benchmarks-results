#!/bin/sh
# Quiet re-run of taau's quality (docs/bench/taau.md 5, step 3), 2026-10-15.
WT=<local-path>/.claude/worktrees/taau
Q=<local-path>/out/taau/quiet
LOCK=<local-path>/out/locks/bench_lock.py
cd "$WT"
echo "$(date +%T) start quality nvidia vulkan" >> $Q/run_quality.progress
POCKET_BACKEND=vulkan POCKET_ADAPTER=nvidia python $LOCK run --label quiet-taau -- $WT/target/release/examples/aa_eval.exe $Q/quality --only upscale-tune --scale 0.5,0.67,0.77,1.0 > $Q/quality.log 2>&1
echo "$(date +%T) end quality nvidia vulkan exit $?" >> $Q/run_quality.progress
echo "$(date +%T) start quality 780m dx12" >> $Q/run_quality.progress
POCKET_BACKEND=dx12 POCKET_ADAPTER=780m python $LOCK run --label quiet-taau -- $WT/target/release/examples/aa_eval.exe $Q/quality780 --only upscale --scale 0.5,0.67,0.77,1.0 > $Q/quality780.log 2>&1
echo "$(date +%T) end quality 780m dx12 exit $?" >> $Q/run_quality.progress
echo "$(date +%T) done" >> $Q/run_quality.progress
