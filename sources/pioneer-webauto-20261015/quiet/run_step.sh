#!/bin/sh
# Usage: run_step.sh NAME -- web_auto args...   (runs from the webauto worktree under the bench lock)
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
WT=<local-path>/.claude/worktrees/webauto
Q=<local-path>/out/webauto/quiet
LOCK=<local-path>/out/locks/bench_lock.py
name=$1; shift; shift
cd "$WT" || exit 1
for i in $(seq 1 60); do
  t=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | tr -d '\r ')
  [ "$t" -lt 70 ] && break
  echo "cooling: RTX at $t C" >> "$Q/$name.log"; sleep 10
done
echo "$(date '+%F %T') start $name, RTX $(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | tr -d '\r ') C" >> "$Q/$name.log"
python "$LOCK" run --label quiet-webauto --max-hold-min 25 -- python tools/web_auto.py "$@" >> "$Q/$name.log" 2>&1
rc=$?
echo "$(date '+%F %T') end $name rc=$rc, RTX $(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | tr -d '\r ') C" >> "$Q/$name.log"
exit $rc
