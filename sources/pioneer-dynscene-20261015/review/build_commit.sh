#!/bin/sh
# build_commit.sh DEST NAME COMMIT EXAMPLE...: builds the commit's examples from `git archive`
# (extracted with tar -m: the extraction's mtimes, so the shared target dir rebuilds them; cargo
# hashes a workspace member by its path inside the workspace, so every tree shares its units) and
# copies them to DEST/NAME/target/release/examples.
set -e
WT=<local-path>/.claude/worktrees/dynscene
dest=$1; name=$2; commit=$3; shift 3
export PATH="$HOME/.cargo/bin:$HOME/scoop/shims:$PATH"
unset CARGO_TARGET_DIR
cd $WT
rm -rf target/src-$name && mkdir -p target/src-$name
git archive $commit | tar -x -m -C target/src-$name
args=""; for e in "$@"; do args="$args --example $e"; done
(cd target/src-$name && CARGO_TARGET_DIR=$WT/target/archive CARGO_BUILD_JOBS=6 \
    cargo build --release --offline --locked -p pocket-render $args 2>&1 | grep -E "Compiling pocket-render|Finished|error")
mkdir -p $dest/$name/target/release/examples
for e in "$@"; do cp target/archive/release/examples/$e.exe $dest/$name/target/release/examples/; done
echo "$name = $commit via git archive (tar -m), built $(date)" > $dest/$name/BUILD.txt
md5sum $dest/$name/target/release/examples/*.exe
