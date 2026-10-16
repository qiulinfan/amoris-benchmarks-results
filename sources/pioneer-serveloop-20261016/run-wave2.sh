#!/usr/bin/env bash
# The serveloop track's re-measurement after review (2026-10-15), each step under the bench lock.
set -u
W=<local-path>/.claude/worktrees/serveloop
O=<local-path>/out/serveloop
PY=<local-path>
LOCK="$PY <local-path>/out/locks/bench_lock.py run --label serveloop --max-hold-min 20 --"
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
$LOCK $PY $W/tools/publish_bench.py --out $O/wave2/publish --runs 3 --also base=$O/base-build/publish_bench-3fdc5b83.exe
$LOCK $PY $W/tools/serve_loop_bench.py --out $O/wave2/live --rounds 3 --idle 30 --idle-rounds 2 --clients none sockets editor \
  --pocket base=$O/bin/pocket-base.exe --pocket new=$O/bin/pocket-new.exe
$LOCK $PY $W/tools/gizmo_bench.py --runs 5 --out $O/wave2/gizmo-base --pocket $O/bin/pocket-base.exe --dist $O/editor-base/dist
$LOCK $PY $W/tools/gizmo_bench.py --runs 5 --out $O/wave2/gizmo-host --pocket $O/bin/pocket-new.exe --dist $O/editor-base/dist
$LOCK $PY $W/tools/gizmo_bench.py --runs 5 --out $O/wave2/gizmo-new --pocket $O/bin/pocket-new.exe --dist $W/editor/dist
$LOCK $PY $W/tools/serve_loop_bench.py --out $O/wave2/diag --rounds 4 --idle 0 --clients none editor editor-dgpu busy1 \
  --pocket base=$O/bin/pocket-base.exe
$LOCK $PY $W/tools/serve_loop_bench.py --out $O/wave2/speed8 --rounds 4 --idle 0 --speed 8 --clients none busy1 editor \
  --pocket base=$O/bin/pocket-base.exe
echo WAVE2-DONE
