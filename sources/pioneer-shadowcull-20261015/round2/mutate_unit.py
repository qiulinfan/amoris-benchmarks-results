"""Applies known bugs to shadows.rs one at a time and runs its unit tests; restores the file."""
import subprocess, sys
from pathlib import Path
F = Path("crates/pocket-render/src/shadows.rs")
import os
os.environ["CARGO_BUILD_JOBS"] = "5"
orig = F.read_text(encoding="utf-8")
M = [
    ("no normal offset", "let margin = 1.5 * far / 1024.0 + 4.0", "let margin = 4.0"),
    ("2 texels of kernel", "+ 4.0 * casc.texel[c] +", "+ 2.0 * casc.texel[c] +"),
    ("no jitter widening", "let kx = 1.0 + jitter_ndc.x.abs() +", "let kx = 1.0 +"),
    ("far plane at the nearest corner", ".fold(f32::NEG_INFINITY, f32::max);\n        planes[n] = (-light)", ".fold(f32::INFINITY, f32::min);\n        planes[n] = (-light)"),
    ("first cascade from the split's near", "let mut prev = 0.0f32;", "let mut prev = cam.near.max(0.05);"),
    ("first cascade from the camera's near plane", "let mut prev = 0.0f32;", "let mut prev = cam.near;"),
]
results = []
try:
    for name, a, b in M:
        assert orig.count(a) == 1, name
        F.write_text(orig.replace(a, b), encoding="utf-8", newline="\n")
        p = subprocess.run(["cargo", "test", "-q", "--release", "-p", "pocket-render", "--lib", "shadows::tests"],
                           capture_output=True, text=True)
        failed = [l for l in p.stdout.splitlines() if "FAILED" in l or "panicked" in l]
        results.append((name, "caught" if p.returncode else "SURVIVED", failed[:2]))
        print(results[-1], flush=True)
finally:
    F.write_text(orig, encoding="utf-8", newline="\n")
