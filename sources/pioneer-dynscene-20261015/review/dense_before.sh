#!/bin/sh
# The before build's cubes-dense-moving capture (build_compare.py's case, MSAA) with its whole
# stderr kept, on the RTX and the 780M under Direct3D 12, and HEAD's for comparison.
R=<local-path>/out/dynscene/review
for b in before head; do for a in "" 780m; do
  out=$R/dense-$b-dx12-${a:-rtx}
  POCKET_BACKEND=dx12 POCKET_ADAPTER=$a POCKET_OCCLUSION=off POCKET_AA=msaa POCKET_GTAO=off RUST_LOG=warn \
    $R/$b/target/release/examples/many_cubes.exe --dense --moving 320000 --sparse 5 --capture $out.png \
    > $out.log 2>&1
  echo "$b ${a:-rtx}: exit $? png $(stat -c %s $out.png 2>/dev/null || echo none)"
done; done
