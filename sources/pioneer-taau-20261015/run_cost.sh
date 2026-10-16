#!/bin/sh
# The taau cost protocol (docs/bench/taau.md 3): one aa_bench.py invocation per adapter and backend
# per round, each under the machine-wide bench lock. Run from the worktree root.
O=<local-path>/out/taau/cost
LOCK=<local-path>/out/locks/bench_lock.py
mkdir -p $O
for r in ${ROUNDS:-0 1}; do
  for combo in nvidia:dx12 nvidia:vulkan 780m:dx12 780m:vulkan; do
    ad=${combo%%:*}; be=${combo##*:}
    python $LOCK run --label taau --max-hold-min 25 -- python tools/aa_bench.py \
      --adapters $ad --backends $be --rounds 1 --first-round $r --workloads check,dense \
      --scales 1,0.77,0.67,0.5 --sizes 1600x900,2560x1440 --occlusion off,auto --prepass on --frames 150 \
      --configs msaa:off,taa:off,taa:off:0.77,taa:off:0.67,taa:off:0.5,taa:depth,taa:depth:0.67 \
      --conditions $O/r$r-$ad-$be --out $O/r$r-$ad-$be.json > $O/r$r-$ad-$be.log 2>&1
    echo "round $r $ad $be: exit $?"
  done
done
