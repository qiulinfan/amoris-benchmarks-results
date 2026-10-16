#!/usr/bin/env bash
# The serveloop track's quiet re-measurement (2026-10-16), each step under the bench lock.
set -u
W=<local-path>/.claude/worktrees/serveloop
O=<local-path>/out/serveloop
PY=<local-path>
LOCK="$PY <local-path>/out/locks/bench_lock.py run --label quiet-serveloop --max-hold-min 25 --"
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
cd "$W"

cool() {
  # Let the RTX 5060 drop below 70 C before the next step.
  for i in $(seq 1 60); do
    t=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | head -1 | tr -d ' \r')
    [ "${t:-0}" -lt 70 ] && break
    sleep 10
  done
  echo "$(date '+%F %T') before $1: RTX ${t:-?} C"
}

step() {
  local name=$1; shift
  cool "$name"
  echo "$(date '+%F %T') start $name"
  $LOCK "$@"
  echo "$(date '+%F %T') end $name: exit $?"
}

step publish $PY $W/tools/publish_bench.py --out $O/quiet/publish --runs 5 \
  --also base=$O/base-build/publish_bench-3fdc5b83.exe
step live $PY $W/tools/serve_loop_bench.py --out $O/quiet/live --rounds 5 --idle 30 --idle-rounds 3 \
  --clients none sockets editor --pocket base=$O/bin/pocket-base.exe --pocket new=$O/bin/pocket-new.exe
step diag $PY $W/tools/serve_loop_bench.py --out $O/quiet/diag --rounds 5 --idle 0 \
  --clients none sockets-reads editor editor-dgpu busy1 busy3 --pocket base=$O/bin/pocket-base.exe
step speed8 $PY $W/tools/serve_loop_bench.py --out $O/quiet/speed8 --rounds 5 --idle 0 --speed 8 \
  --clients none editor editor-dgpu busy1 --pocket base=$O/bin/pocket-base.exe
step pinned $PY $W/tools/serve_loop_bench.py --out $O/quiet/pinned --rounds 3 --idle 0 --host-cpus 2-5 \
  --client-cpus 0-1,6-15 --clients none sockets editor editor-dgpu --pocket base=$O/bin/pocket-base.exe
step gizmo-base $PY $W/tools/gizmo_bench.py --runs 5 --out $O/quiet/gizmo-base --pocket $O/bin/pocket-base.exe \
  --dist $O/editor-base/dist
step gizmo-host $PY $W/tools/gizmo_bench.py --runs 5 --out $O/quiet/gizmo-host --pocket $O/bin/pocket-new.exe \
  --dist $O/editor-base/dist
step gizmo-new $PY $W/tools/gizmo_bench.py --runs 5 --out $O/quiet/gizmo-new --pocket $O/bin/pocket-new.exe \
  --dist $W/editor/dist
for X in base host new; do
  $PY $W/tools/gizmo_bench.py --table $O/quiet/gizmo-$X
done
echo QUIET-DONE
