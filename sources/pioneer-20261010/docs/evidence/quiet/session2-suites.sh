#!/bin/sh
# As run on 2026-10-10 (log: session2-suites.log). Its last condition record, written as
# conditions-21-end.json, was renamed conditions-21-after-cpu.json.
# The quiet re-measurement's remaining suites on the final build, one after another (no builds).
WT=<local-path>
S=<local-path>
cd $WT || exit 1
export POCKET_TSC=<local-path>
NOTE="quiet machine 2026-10-10 (no other agent; conditions in docs/evidence/quiet/conditions-1*.json), build 0871920d + explore/quiet2"
step() { echo "=== $(date '+%H:%M:%S') $*"; }
cond() { python tools/machine_conditions.py docs/evidence/quiet/conditions-$1.json --label $2; }
cool() { t0=$(date +%s); while [ "$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)" -gt 70 ]; do sleep 5; done; echo "cooled in $(( $(date +%s) - t0 )) s"; }

if [ -z "$SKIP_IMAGES" ]; then
step "splat images"
cond 15-before-splat-images before-splat-images
cool
python tools/splats/compare_matrix.py --adapters nvidia,780m --backends dx12,vulkan \
  --scene "1M 1600x900=--count 1000000" \
  --scene "3M 2560x1440=--count 3000000 --size 2560x1440" \
  --scene "orb close-up=--count 1000000 --look 0,1.4,3 --distance 0.12" \
  --scene "1M anti-aliased=--count 1000000 --antialias" \
  --scene "1M 2.5x distance AA=--count 1000000 --distance 2.5 --antialias" \
  --images $S/splat-compare --out docs/evidence/quiet/splats/compare-fixed.json
fi

step "Direct3D 12 against Vulkan, headless"
cond 16-before-dx12 before-dx12
cool
POCKET_AA=msaa POCKET_GTAO=off POCKET_OCCLUSION=off python tools/backend_bench.py \
  --adapters nvidia,780m --rounds 5 --settle 5 --cool 70 \
  --cases cubes-sphere-headless,cubes-dense-headless,splats-headless,crowd-headless \
  --summary docs/evidence/quiet/dx12/bench-headless-final.json \
  --note "$NOTE; POCKET_AA=msaa POCKET_GTAO=off POCKET_OCCLUSION=off; --settle 5"
step "Direct3D 12 against Vulkan, windowed"
cool
POCKET_AA=msaa POCKET_GTAO=off POCKET_OCCLUSION=off python tools/backend_bench.py \
  --adapters nvidia,780m --rounds 3 --cool 70 --variants vulkan,dx12 \
  --cases cubes-sphere-window,cubes-dense-window,splats-window \
  --summary docs/evidence/quiet/dx12/bench-window-final.json \
  --note "$NOTE; POCKET_AA=msaa POCKET_GTAO=off POCKET_OCCLUSION=off"

step "Hi-Z spot-check"
cond 17-before-hiz before-hiz
cool
POCKET_AA=msaa POCKET_GTAO=off python tools/occlusion_bench.py \
  --configs dx12:nvidia,vulkan:nvidia,dx12:780m,vulkan:780m --layouts sphere --frames 200 \
  --repeats 3 --out docs/evidence/quiet/hiz/spot-final-sphere.json --note "$NOTE"
cool
POCKET_AA=msaa POCKET_GTAO=off python tools/occlusion_bench.py \
  --configs dx12:nvidia,vulkan:nvidia,dx12:780m,vulkan:780m --layouts dense \
  --counts 27000,64000 --frames 200 --repeats 3 \
  --out docs/evidence/quiet/hiz/spot-final-counts.json --note "$NOTE"

step "TAA and GTAO"
cond 18-before-aa before-aa
cool
python tools/aa_bench.py --adapters nvidia,780m --backends dx12,vulkan --rounds 3 \
  --out docs/evidence/quiet/aa/bench-native-final.json

step "browser"
cond 19-before-web before-web
python -m http.server -d web 8090 --bind <local-host> > $S/http.log 2>&1 &
SERVER=$!
sleep 2
python tools/web_paths_bench.py --base <local-endpoint> \
  --pages "cubes-100k=demo=cubes&count=100000&occlusion=off,cubes-400k=demo=cubes&count=400000&occlusion=off,cubes-1.6m=demo=cubes&count=1600000&occlusion=off" \
  --gpus nvidia,default --rounds 5 --seconds 10 \
  --out docs/evidence/quiet/web/cubes.json --note "$NOTE"
kill $SERVER

step "CPU: player bench"
cond 20-before-cpu before-cpu
mkdir -p docs/evidence/quiet/player docs/evidence/quiet/agentdebug docs/evidence/quiet/typecheck
for i in 1 2 3; do
  target/release/examples/player_bench.exe docs/evidence/quiet/player/bench-r$i.json > docs/evidence/quiet/player/bench-r$i.txt 2>&1
  target/release/examples/perception_bench.exe > docs/evidence/quiet/player/perception-r$i.txt 2>&1
done
step "CPU: held host"
for i in 1 2 3; do
  python tools/held_host_bench.py --out docs/evidence/quiet/agentdebug/held-host-r$i.json
done
step "CPU: type checking"
cargo test --release -p pocket-runtime --features thread,transpile --test host script_types_cost \
  -- --ignored --nocapture > docs/evidence/quiet/typecheck/script-types-cost.txt 2>&1
rm -rf $S/tc && mkdir -p $S/tc && cp -r samples/sailing $S/tc/sailing
target/release/pocket.exe check $S/tc/sailing --only types > $S/tc/first.txt 2>&1
python - <<EOF
import json, statistics, subprocess, time
proj = r"$S/tc/sailing"
tsc = r"$POCKET_TSC"
def timed(cmd):
    t = time.perf_counter(); p = subprocess.run(cmd, capture_output=True, text=True); return (time.perf_counter() - t) * 1000, p.returncode
rows = {"tsc_noemit": [], "pocket_check_types": []}
for _ in range(15):
    rows["tsc_noemit"].append(timed([tsc, "--noEmit", "-p", proj]))
    rows["pocket_check_types"].append(timed([r"target/release/pocket.exe", "check", proj, "--only", "types"]))
out = {k: {"median_ms": round(statistics.median(x for x, _ in v), 1), "min_ms": round(min(x for x, _ in v), 1),
           "max_ms": round(max(x for x, _ in v), 1), "exit_codes": sorted({c for _, c in v}),
           "all_ms": [round(x, 1) for x, _ in v]} for k, v in rows.items()}
open("docs/evidence/quiet/typecheck/cli.json", "w").write(json.dumps(out, indent=1) + "\n")
print(json.dumps({k: (v["median_ms"], v["min_ms"], v["max_ms"], v["exit_codes"]) for k, v in out.items()}))
EOF
cond 21-end end
step "done"
