#!/bin/sh
# The second round's remaining runs (webauto review): before at the fixed canvas, the fixed-mode
# truths for the prepass and occlusion culling, the native reference. Run from the worktree.
set -e
O=<local-path>/out/webauto
LOCK="python <local-path>/out/locks/bench_lock.py run --label webauto --max-hold-min 20 --"
# Before: master's viewport package (the rules before this branch), default Chrome, fixed canvas.
$LOCK python tools/web_auto.py run --out $O/r2-before.jsonl --web $O/web-before/web --chrome default --label r2before > $O/r2-before.log 2>&1
# Which way is cheaper: the prepass fixed on and off (unsafe Chrome).
$LOCK python tools/web_auto.py run --out $O/r2-truth.jsonl --chrome unsafe --modes on,off --seconds 20 --label r2truth > $O/r2-truth.log 2>&1
# Occlusion culling fixed on and off, the prepass fixed as the auto mode decides each page.
$LOCK sh -c "python tools/web_auto.py run --out $O/r2-occ.jsonl --pages dense --chrome unsafe --modes 'occlusion=on&prepass=on,occlusion=off&prepass=on' --seconds 20 --label r2occ && python tools/web_auto.py run --out $O/r2-occ.jsonl --pages sphere,occluders --chrome unsafe --modes 'occlusion=on&prepass=off,occlusion=off&prepass=off' --seconds 20 --label r2occ" > $O/r2-occ.log 2>&1
# Native reference.
$LOCK python tools/web_auto.py native --out $O/r2-native.jsonl --label r2native > $O/r2-native.log 2>&1
echo "r2-rest done"
