#!/bin/sh
cd <local-path>/.claude/worktrees/dynscene
for cfg in "dx12 " "vulkan " "dx12 780m" "vulkan 780m"; do
  set -- $cfg
  echo "== $1 ${2:-rtx}"
  POCKET_BACKEND=$1 POCKET_ADAPTER=${2:-} <local-path>/out/dynscene/review/lib-test.exe upload:: --nocapture 2>&1 | grep -E "test |result|no GPU|panicked"
done
