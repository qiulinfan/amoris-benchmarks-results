#!/bin/sh
Q=<local-path>/out/webauto/quiet
S="sh $Q/run_step.sh"
$S step2 -- run --out $Q/quiet.jsonl --gpus 780m --loops vsync --label quiet
$S step3 -- run --out $Q/quiet.jsonl --gpus 780m --loops uncapped --seconds 90 --label quiet
$S step4 -- run --out $Q/quiet-truth.jsonl --chrome unsafe --modes on,off --seconds 20 --label truth
$S step5 -- run --out $Q/quiet-truth.jsonl --pages dense --chrome unsafe --modes "occlusion=on&prepass=on,occlusion=off&prepass=on" --seconds 20 --label truth
$S step6 -- run --out $Q/quiet-truth.jsonl --pages sphere,occluders --chrome unsafe --modes "occlusion=on&prepass=off,occlusion=off&prepass=off" --seconds 20 --label truth
$S step7 -- native --out $Q/quiet-native.jsonl
$S step8 -- run --web $Q/web-before/web --chrome default --out $Q/quiet-before.jsonl --label before
echo "ALL DONE" > $Q/all_done
