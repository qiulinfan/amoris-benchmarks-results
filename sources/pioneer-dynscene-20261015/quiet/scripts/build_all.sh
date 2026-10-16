#!/bin/sh
# Quiet re-measurement builds (docs/bench/dynamic-scenes.md 7): each commit from git archive,
# extracted with tar -m into the worktree's ignored target/src-NAME, built in the shared
# target/archive, its six examples copied to out/dynscene/quiet/NAME/target/release/examples.
set -e
WT=<local-path>/.claude/worktrees/dynscene
DEST=<local-path>/out/dynscene/quiet
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
unset CARGO_TARGET_DIR
EX="many_cubes rt_shadows lod_field splats showcase_bench image_diff"
build() {
  name=$1; commit=$2
  echo "=== build $name $commit start $(date +%T)"
  cd $WT
  rm -rf target/src-$name && mkdir -p target/src-$name
  git archive $commit | tar -x -m -C target/src-$name
  args=""; for e in $EX; do args="$args --example $e"; done
  (cd target/src-$name && CARGO_TARGET_DIR=$WT/target/archive \
      cargo build --release --offline --locked -p pocket-render $args 2>&1 | grep -E "Compiling pocket|Finished|error|warning: unused" || true)
  mkdir -p $DEST/$name/target/release/examples
  for e in $EX; do cp target/archive/release/examples/$e.exe $DEST/$name/target/release/examples/; done
  echo "$name = $commit ($(git rev-parse $commit)) via git archive (tar -m), built $(date)" > $DEST/$name/BUILD.txt
  md5sum $DEST/$name/target/release/examples/*.exe
  echo "=== build $name end $(date +%T)"
}
for pair in "$@"; do build ${pair%%=*} ${pair#*=}; done
