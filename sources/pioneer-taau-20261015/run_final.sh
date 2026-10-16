#!/bin/sh
# The final quality evaluations and the cost protocol, each step its own lock acquisition.
W=<local-path>/.claude/worktrees/taau
O=<local-path>/out/taau
LOCK=<local-path>/out/locks/bench_lock.py
mkdir -p $O/eval5 $O/eval6
POCKET_BACKEND=vulkan POCKET_ADAPTER=nvidia python $LOCK run --label taau --max-hold-min 25 -- \
  $W/target/release/examples/aa_eval.exe $O/eval5 --only upscale-tune --scale 0.5,0.67,0.77,1.0 \
  > $O/eval5/log.txt 2>&1
echo "eval5 $?"
POCKET_BACKEND=dx12 POCKET_ADAPTER=780m python $LOCK run --label taau --max-hold-min 25 -- \
  $W/target/release/examples/aa_eval.exe $O/eval6 --only upscale --scale 0.5,0.67,0.77,1.0 \
  > $O/eval6/log.txt 2>&1
echo "eval6 $?"
sh $O/run_cost.sh
