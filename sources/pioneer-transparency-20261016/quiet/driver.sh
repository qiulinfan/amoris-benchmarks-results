#!/usr/bin/env bash
# The transparency track's quiet re-measurement (docs/bench/transparency.md 5), in order.
set -u
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
WT=<local-path>/.claude/worktrees/transparency
L=<local-path>/out/locks/bench_lock.py
T=<local-path>/out/transparency
Q=$T/quiet
OLD=$T/build-05716664/target/release/examples/transparency.exe
LOG=$Q/driver.log
log() { echo "$(date '+%F %T') $*" >>"$LOG"; }
temp() { nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | tr -d ' \r'; }
cool() { local n=0; while [ "$(temp)" -ge 70 ] && [ $n -lt 40 ]; do sleep 15; n=$((n+1)); done; log "rtx $(temp) C"; }
run() { cool; log "start: $*"; python "$L" run --label quiet-transparency -- "$@" >>"$LOG" 2>&1; log "exit $?: $*"; }
cd "$WT"
log "settling after the builds"
sleep 90
python tools/machine_conditions.py "$Q/conditions-start.json" --label "transparency quiet start" >>"$LOG" 2>&1
# Section 2 (both tables), with section 2.3's A/B right after each RTX configuration's run.
for a in 5060 780m; do for b in dx12 vulkan; do
  run python tools/transparency_bench.py --adapter $a --backend $b --out $Q/bench
  if [ $a = 5060 ]; then
    run python tools/transparency_bench.py --adapter $a --backend $b --kinds hidden,blend,glass,double --exe $OLD --out $Q/ab-05716664
  fi
  run python tools/transparency_bench.py --adapter $a --backend $b --kinds hidden,blend,double --extra=--orbit --out $Q/bench
done; done
# Section 2.2.
export HITCH_OUT=$Q/hitch
run python -I $T/scripts/hitch.py
unset HITCH_OUT
# Section 2.1: lists (the worktree), one draw (b9eea658), two draws (440dd7f8); then the lists
# before the review (05716664, which still casts and draws before GTAO), like the two older builds.
for a in 5060 780m; do for b in dx12 vulkan; do
  run python tools/transparency_bench.py --adapter $a --backend $b --kinds hidden,double --out $Q/ab3-lists
  run python $T/src-b9eea658/tools/transparency_bench.py --adapter $a --backend $b --kinds hidden,double --out $Q/ab3-one-draw
  run python $T/src-440dd7f8/tools/transparency_bench.py --adapter $a --backend $b --kinds hidden,double --out $Q/ab3-two-draws
  run python tools/transparency_bench.py --adapter $a --backend $b --kinds hidden,double --exe $OLD --out $Q/ab3-lists-05716664
done; done
# Deterministic checks on the idle machine.
run python tools/transparency_bench.py --adapter 5060 --backend dx12 --ghost --out $Q/ghost
mkdir -p $Q/pt-lab && cp $T/pt-lab/reference-320x240-* $Q/pt-lab/
run python tools/transparency_pt.py --build before=$T/before --build after=. --out $Q/pt-lab --backend dx12 --adapter 5060
run python tools/transparency_pt.py --build before=$T/before --build after=. --out $Q/pt-lab --backend dx12 --adapter 5060 "--pt-args=--emission-scale 0"
run python tools/transparency_pt.py --build before=$T/before --build prefix=$T/build-05716664 --build after=. --out $Q/pt-lab --backend dx12 --adapter 5060 --gtao depth
run python tools/transparency_pt.py --build before=$T/before --build prefix=$T/build-05716664 --build after=. --out $Q/pt-lab --backend dx12 --adapter 5060 --gtao depth "--pt-args=--emission-scale 0"
run python -I $Q/compares_quiet.py prepass
run python -I $Q/compares_quiet.py occlusion
python tools/machine_conditions.py "$Q/conditions-end.json" --label "transparency quiet end" >>"$LOG" 2>&1
log "done"
