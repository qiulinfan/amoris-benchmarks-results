#!/bin/sh
# Quiet re-measurement of taau's cost (docs/bench/taau.md 5, step 1), 2026-10-15.
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
WT=<local-path>/.claude/worktrees/taau
Q=<local-path>/out/taau/quiet
LOCK=<local-path>/out/locks/bench_lock.py
cd "$WT"
cool() {
  while :; do
    t=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | tr -d '\r ')
    [ "$t" -lt 70 ] && break
    echo "$(date +%T) RTX at $t C, waiting" >> $Q/run_cost.progress
    sleep 15
  done
  echo "$(date +%T) RTX at $t C" >> $Q/run_cost.progress
}
sleep 60   # settle after the builds
for r in 0 1; do
  for c in nvidia:dx12 nvidia:vulkan 780m:dx12 780m:vulkan; do
    cool
    a=${c%%:*}; b=${c##*:}
    echo "$(date +%T) start r$r $a $b" >> $Q/run_cost.progress
    python $LOCK run --label quiet-taau -- python tools/aa_bench.py --adapters $a --backends $b \
      --rounds 1 --first-round $r --workloads check,dense --scales 1,0.77,0.67,0.5 \
      --sizes 1600x900,2560x1440 --occlusion off,auto --prepass on --frames 150 \
      --configs msaa:off,taa:off,taa:off:0.77,taa:off:0.67,taa:off:0.5,taa:depth,taa:depth:0.67 \
      --conditions $Q/r$r-$a-$b --out $Q/r$r-$a-$b.json > $Q/r$r-$a-$b.log 2>&1
    echo "$(date +%T) end r$r $a $b exit $?" >> $Q/run_cost.progress
  done
done
echo "$(date +%T) done" >> $Q/run_cost.progress
