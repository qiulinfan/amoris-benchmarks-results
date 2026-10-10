#!/bin/sh
# The quiet re-measurement's review follow-up (2026-10-10): Hi-Z check 1 with settling, the tile
# walk's before/after and investigation runs, the ray-traced shadows in rounds. No builds.
WT=<local-path>
S=<local-path>
W=<local-path>
EXP=$W/splats-exp.exe
cd $WT || exit 1
NOTE="quiet machine 2026-10-10, review follow-up (no other agent; conditions in docs/evidence/quiet/conditions-2[5-9].json), build 0871920d + explore/quiet2"
step() { echo "=== $(date '+%H:%M:%S') $*"; }
cond() { python tools/machine_conditions.py docs/evidence/quiet/conditions-$1.json --label $2; }
cool() { t0=$(date +%s); while [ "$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)" -gt 70 ]; do sleep 5; done; echo "cooled in $(( $(date +%s) - t0 )) s to $(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader) C"; }
mkdir -p docs/evidence/quiet/hiz docs/evidence/quiet/splats/walk docs/evidence/quiet/rt

step "Hi-Z check 1 with settling"
cond 25-before-hiz-settle before-hiz-settle
cool
POCKET_AA=msaa POCKET_GTAO=off python tools/occlusion_bench.py \
  --configs vulkan:nvidia,dx12:nvidia,vulkan:780m,dx12:780m --layouts sphere --frames 200 \
  --repeats 6 --alternate --settle 5 --cool 70 \
  --out docs/evidence/quiet/hiz/spot-final-sphere-settled.json --note "$NOTE; --settle 5"

step "tile walk: timings"
cond 26-before-walk before-walk
cool
python tools/splats/matrix.py --rasters tile --adapters nvidia,780m --backends dx12,vulkan \
  --rounds 5 --frames 60 --cool 70 --settle 5 \
  --build final=$EXP --env final=POCKET_EXP_SPLAT_TILE=$W/orig.wgsl \
  --build fixed=$EXP --env fixed=POCKET_EXP_SPLAT_TILE=$W/fixed.wgsl \
  --build no-walk=$EXP --env no-walk=POCKET_EXP_SPLAT_TILE=$W/skip.wgsl \
  --build plain-lists=$EXP --env plain-lists=POCKET_EXP_SPLAT_TILE=$W/copy.wgsl \
  --build no-loop-bounding=$EXP --env no-loop-bounding=POCKET_EXP_SPLAT_TILE=$W/orig.wgsl \
  --env no-loop-bounding=POCKET_EXP_LEAN=1 \
  --scene "1M 1600x900=--count 1000000" \
  --note "$NOTE; one experiment build (POCKET_EXP_SPLAT_TILE, POCKET_EXP_LEAN: docs/evidence/quiet/splats/walk/)" \
  --out docs/evidence/quiet/splats/walk/timings.json

step "tile walk: captures, final against fixed"
cool
python tools/splats/compare_matrix.py --adapters nvidia,780m --backends dx12,vulkan \
  --build final=$EXP --env final=POCKET_EXP_SPLAT_TILE=$W/orig.wgsl \
  --build fixed=$EXP --env fixed=POCKET_EXP_SPLAT_TILE=$W/fixed.wgsl \
  --scene "1M 1600x900=--count 1000000" \
  --scene "3M 2560x1440=--count 3000000 --size 2560x1440" \
  --scene "orb close-up=--count 1000000 --look 0,1.4,3 --distance 0.12" \
  --scene "1M 2.5x distance AA=--count 1000000 --distance 2.5 --antialias" \
  --images $S/walk/captures --out docs/evidence/quiet/splats/walk/captures.json
step "tile walk: the override against the committed build"
python tools/splats/compare_matrix.py --adapters nvidia --backends dx12,vulkan \
  --build override=$EXP --env override=POCKET_EXP_SPLAT_TILE=$W/fixed.wgsl \
  --build committed=$WT/target/release/examples/splats.exe \
  --scene "1M 1600x900=--count 1000000" \
  --images $S/walk/captures-check --out docs/evidence/quiet/splats/walk/override-check.json

step "ray-traced shadows in rounds"
cond 27-before-rt-shadows before-rt-shadows
cool
python tools/rt_shadows_bench.py --adapters 5060,780m --rounds 5 --all-rounds --alternate \
  --settle 5 --cool 70 --out out/rts-followup \
  --summary docs/evidence/quiet/rt/shadows-rounds-final.json
cond 28-after-followup after-followup
step "done"
