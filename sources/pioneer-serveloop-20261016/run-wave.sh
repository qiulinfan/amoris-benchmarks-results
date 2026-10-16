#!/usr/bin/env bash
# The serveloop track's provisional measurements (2026-10-16), each step under the bench lock.
set -u
W=<local-path>/.claude/worktrees/serveloop
O=<local-path>/out/serveloop
LOCK="python <local-path>/out/locks/bench_lock.py run --label serveloop --max-hold-min 20 --"
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
$LOCK python $W/tools/publish_bench.py --out $O/wave/publish --runs 3 --also base=$O/bin/publish_bench-base.exe
$LOCK python $W/tools/serve_loop_bench.py --out $O/wave/live --rounds 3 --idle 20 --clients none sockets editor \
  --pocket base=$O/bin/pocket-base.exe --pocket new=$O/bin/pocket-new.exe
$LOCK python $W/tools/gizmo_bench.py --runs 5 --out $O/wave/gizmo-base --pocket $O/bin/pocket-base.exe --dist $O/editor-base/dist
$LOCK python $W/tools/gizmo_bench.py --runs 5 --out $O/wave/gizmo-host --pocket $O/bin/pocket-new.exe --dist $O/editor-base/dist
$LOCK python $W/tools/gizmo_bench.py --runs 5 --out $O/wave/gizmo-new --pocket $O/bin/pocket-new.exe --dist $W/editor/dist
echo WAVE-DONE
