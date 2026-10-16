#!/bin/sh
# Runs each job file under its own hold of the bench lock; logs to review/<job>.log.
cd <local-path>/.claude/worktrees/dynscene
for j in "$@"; do
  echo "=== $j start $(date +%T)"
  python <local-path>/out/locks/bench_lock.py run --label dynscene --max-hold-min 25 -- python <local-path>/out/dynscene/scripts/run_seq.py <local-path>/out/dynscene/review/job_$j.json > <local-path>/out/dynscene/review/$j.log 2>&1
  echo "=== $j exit $? $(date +%T)"
done
