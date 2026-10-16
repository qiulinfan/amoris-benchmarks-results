#!/bin/sh
# Quiet re-measurement of taau in Chrome (docs/bench/taau.md 5, step 2), 2026-10-15.
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
WT=<local-path>/.claude/worktrees/taau
Q=<local-path>/out/taau/quiet
LOCK=<local-path>/out/locks/bench_lock.py
cd "$WT"
python -m http.server 8231 -d web > $Q/http.log 2>&1 &
SRV=$!
sleep 3
python tools/machine_conditions.py $Q/web-start.json --label web-start
python $LOCK run --label quiet-taau -- python tools/aa_web_bench.py --url http://<local-endpoint> \
  --gpu nvidia --rounds 3 --seconds 8 --size 1600x900 --scales 1,0.67,0.5 \
  --configs msaa:off,taa:off,taa:off:0.67,taa:off:0.5 --out $Q/web-nvidia.json > $Q/web-nvidia.log 2>&1
echo "exit $?" >> $Q/web-nvidia.log
python tools/machine_conditions.py $Q/web-end.json --label web-end
kill $SRV
