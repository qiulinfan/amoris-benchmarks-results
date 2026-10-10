#!/bin/sh
# Review follow-up, part 2: the mixed scene on the RTX 5060 as session 1 ran it (no settling, the
# cascaded path first) on the final build, to tell the settling from the build.
WT=<local-path>
cd $WT || exit 1
step() { echo "=== $(date '+%H:%M:%S') $*"; }
step "ray-traced shadows, mixed, RTX 5060, no settling"
python tools/rt_shadows_bench.py --adapters 5060 --configs mixed --rounds 5 --all-rounds \
  --cool 70 --out out/rts-followup-nosettle \
  --summary docs/evidence/quiet/rt/shadows-mixed-nosettle-final.json
python tools/machine_conditions.py docs/evidence/quiet/conditions-29-end-followup.json --label end-followup
step "done"
