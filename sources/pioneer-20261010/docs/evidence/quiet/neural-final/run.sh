#!/bin/sh
# As run on 2026-10-10 (log: run.log). Its condition records were renumbered afterwards:
# conditions-22-before-neural.json is conditions-23-before-neural.json, 23-after-neural is 24.
# Neural texture decode cost on the final build: three rounds, both GPUs and APIs, both views.
cd <local-path> || exit 1
echo "=== $(date '+%H:%M:%S') encode"
mkdir -p out/neural docs/evidence/quiet/neural-final
target/release/examples/neural_encode.exe --out out/neural procedural:bricks
ls -la out/neural
python tools/machine_conditions.py docs/evidence/quiet/conditions-22-before-neural.json --label before-neural
for r in 0 1 2; do
  t0=$(date +%s); while [ "$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)" -gt 70 ]; do sleep 5; done
  echo "=== $(date '+%H:%M:%S') round $r (cooled $(( $(date +%s) - t0 )) s)"
  for a in nvidia 780m; do
    for b in vulkan dx12; do
      for v in 0 1; do
        POCKET_ADAPTER=$a POCKET_BACKEND=$b target/release/examples/neural_bench.exe out/neural/bricks.ntex \
          procedural:bricks --view $v --frames 150 > docs/evidence/quiet/neural-final/r$r-$a-$b-view$v.json 2> /dev/null
        echo "r$r $a $b view$v: $(head -c 120 docs/evidence/quiet/neural-final/r$r-$a-$b-view$v.json)"
      done
    done
  done
done
python tools/machine_conditions.py docs/evidence/quiet/conditions-23-after-neural.json --label after-neural
echo "=== $(date '+%H:%M:%S') done"
