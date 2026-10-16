"""Draw the README's charts as standalone SVG files in charts/.

Standard library only. Every number below is copied from a recorded table or
sentence in the engine's benchmark documents (docs/bench/*.md and
docs/charter.md); the comment above each chart names the file and section.
Nothing is recomputed here except pixel positions.

    python tools/make_charts.py            # writes charts/*.svg
"""

from __future__ import annotations

import math
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "charts"

WIDTH = 800
FONT = 'system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'

# Light values first; the dark block re-steps the same roles for a dark page.
STYLE = """
.bg{fill:#fcfcfb;stroke:rgba(11,11,11,0.10)}
.t1{fill:#0b0b0b}.t2{fill:#52514e}.t3{fill:#77756f}
.grid{stroke:#e1e0d9}.base{stroke:#c3c2b7}.link{stroke:#c3c2b7}
.amoris{fill:#2a78d6}.other{fill:#eb6834}.muted{fill:#a3a19a}
.ring{stroke:#fcfcfb}
@media (prefers-color-scheme: dark){
.bg{fill:#1a1a19;stroke:rgba(255,255,255,0.10)}
.t1{fill:#ffffff}.t2{fill:#c3c2b7}.t3{fill:#9a988f}
.grid{stroke:#2c2c2a}.base{stroke:#4a4a46}.link{stroke:#4a4a46}
.amoris{fill:#3987e5}.other{fill:#d95926}.muted{fill:#6e6d68}
.ring{stroke:#1a1a19}
}
text{font-family:%s}
""" % FONT


def fmt(value: float) -> str:
    """Thousands-comma'd, as many decimals as the source gives (passed as text)."""
    return f"{value:,}"


class Svg:
    def __init__(self, title: str, desc: str):
        self.title, self.desc = title, desc
        self.parts: list[str] = []

    def text(self, x, y, s, cls="t1", size=13, anchor="start", weight=None):
        w = f' font-weight="{weight}"' if weight else ""
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" '
            f'text-anchor="{anchor}"{w}>{escape(s)}</text>'
        )

    def line(self, x1, y1, x2, y2, cls="grid", width=1):
        self.parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'class="{cls}" stroke-width="{width}"/>'
        )

    def bar(self, x0, y, x1, h, cls):
        """A bar from the baseline x0 to x1, rounded only at its data end."""
        r = min(4, h / 2, abs(x1 - x0) / 2)
        if x1 >= x0:
            d = (f"M{x0:.1f},{y:.1f} H{x1 - r:.1f} A{r},{r} 0 0 1 {x1:.1f},{y + r:.1f} "
                 f"V{y + h - r:.1f} A{r},{r} 0 0 1 {x1 - r:.1f},{y + h:.1f} H{x0:.1f} Z")
        else:
            d = (f"M{x0:.1f},{y:.1f} H{x1 + r:.1f} A{r},{r} 0 0 0 {x1:.1f},{y + r:.1f} "
                 f"V{y + h - r:.1f} A{r},{r} 0 0 0 {x1 + r:.1f},{y + h:.1f} H{x0:.1f} Z")
        self.parts.append(f'<path d="{d}" class="{cls}"/>')

    def dot(self, x, y, cls, r=5):
        self.parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls} ring" stroke-width="2"/>'
        )

    def legend(self, x, y, items):
        for label, cls in items:
            self.parts.append(
                f'<rect x="{x:.1f}" y="{y - 9:.1f}" width="10" height="10" rx="2" class="{cls}"/>'
            )
            self.text(x + 15, y, label, "t2", 12)
            x += 15 + 6.6 * len(label) + 22

    def save(self, name: str, height: float):
        body = "\n".join(self.parts)
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height:.0f}" '
            f'viewBox="0 0 {WIDTH} {height:.0f}" role="img" aria-labelledby="title desc">\n'
            f"<title id=\"title\">{escape(self.title)}</title>\n"
            f"<desc id=\"desc\">{escape(self.desc)}</desc>\n"
            f"<style>{STYLE}</style>\n"
            f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1:.0f}" rx="10" class="bg"/>\n'
            f"{body}\n</svg>\n"
        )
        OUT.mkdir(exist_ok=True)
        (OUT / name).write_text(svg, encoding="utf-8", newline="\n")


def header(svg: Svg, title: str, subtitle: str) -> float:
    svg.text(24, 34, title, "t1", 17, weight="600")
    svg.text(24, 56, subtitle, "t2", 12.5)
    return 64


def footer(svg: Svg, y: float, lines: list[str]) -> float:
    y += 8
    for line in lines:
        y += 17
        svg.text(24, y, line, "t3", 11.5)
    return y + 18


def nice_ticks(top: float) -> list[float]:
    """Round tick values from 0 that cover top."""
    raw = top / 5
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    ticks, t = [], 0.0
    while t < top + step * 0.01:
        ticks.append(round(t, 6))
        t += step
    if ticks[-1] < top:
        ticks.append(round(t, 6))
    return ticks


def tick_label(t: float) -> str:
    return f"{t:,.0f}" if t == int(t) else f"{t:g}"


def bar_chart(name, title, subtitle, legend, groups, notes, label_w=250, desc=""):
    """Horizontal bars on one linear axis.

    groups: [(label, sublabel, [(value, shown_text, css_class), ...]), ...]
    """
    svg = Svg(title, desc or subtitle)
    y = header(svg, title, subtitle)
    if legend:
        y += 22
        svg.legend(24, y, legend)
    y += 18
    x0, x1 = 24 + label_w, WIDTH - 96
    top = max(v for _, _, bars in groups for v, _, _ in bars)
    ticks = nice_ticks(top)
    scale = (x1 - x0) / ticks[-1]
    bar_h, bar_gap, group_gap = 14, 2, 16
    plot_top = y
    rows = []
    for label, sub, bars in groups:
        bars_h = len(bars) * bar_h + (len(bars) - 1) * bar_gap
        h = max(bars_h, 30 if sub else 0)
        rows.append((y, h, bars_h, label, sub, bars))
        y += h + group_gap
    plot_bottom = y - group_gap + 8
    for t in ticks:
        x = x0 + t * scale
        svg.line(x, plot_top - 6, x, plot_bottom, "grid")
        svg.text(x, plot_bottom + 15, tick_label(t), "t3", 11, "middle")
    for top_y, h, bars_h, label, sub, bars in rows:
        mid = top_y + h / 2
        if sub:
            svg.text(24, mid - 2, label, "t1", 13)
            svg.text(24, mid + 13, sub, "t3", 11.5)
        else:
            svg.text(24, mid + 4.5, label, "t1", 13)
        by = top_y + (h - bars_h) / 2
        for value, shown, cls in bars:
            end = x0 + max(value * scale, 2)
            svg.bar(x0, by, end, bar_h, cls)
            svg.text(end + 6, by + bar_h - 2.5, shown, "t1", 12)
            by += bar_h + bar_gap
    svg.line(x0, plot_top - 6, x0, plot_bottom, "base")
    height = footer(svg, plot_bottom + 18, notes)
    svg.save(name, height)


def log_ticks(lo: float, hi: float) -> list[float]:
    ticks = []
    for k in range(math.floor(math.log10(lo)) - 1, math.ceil(math.log10(hi)) + 1):
        for m in (1, 2, 5):
            t = m * 10 ** k
            if lo <= t * 1.0001 and t <= hi * 1.0001:
                ticks.append(t)
    return ticks


def dumbbell_chart(name, title, subtitle, legend, rows, domain, notes, label_w=250,
                   ratio_head=None, desc=""):
    """Before and after on a log axis, joined by a line.

    rows: [("header", text)] or [(label, sublabel, before, before_text, after, after_text, ratio)]
    """
    svg = Svg(title, desc or subtitle)
    y = header(svg, title, subtitle)
    y += 22
    svg.legend(24, y, legend)
    y += 22
    x0 = 24 + label_w
    x1 = WIDTH - (110 if ratio_head else 60)
    lo, hi = domain
    span = math.log10(hi) - math.log10(lo)

    def px(v):
        return x0 + (math.log10(v) - math.log10(lo)) / span * (x1 - x0)

    plot_top = y
    placed = []
    for row in rows:
        if row[0] == "header":
            y += 8
            placed.append(("header", y + 10, row[1]))
            y += 22
        else:
            placed.append(("row", y + 14, row))
            y += 32
    plot_bottom = y + 2
    for t in log_ticks(lo, hi):
        x = px(t)
        svg.line(x, plot_top - 6, x, plot_bottom, "grid")
        svg.text(x, plot_bottom + 15, tick_label(t), "t3", 11, "middle")
    if ratio_head:
        svg.text(WIDTH - 24, plot_top - 10, ratio_head, "t3", 11, "end")
    for kind, cy, row in placed:
        if kind == "header":
            svg.text(24, cy, row, "t2", 12, weight="600")
            continue
        label, sub, before, before_s, after, after_s, ratio = row
        if sub:
            svg.text(24, cy - 1, label, "t1", 13)
            svg.text(24, cy + 13, sub, "t3", 11)
        else:
            svg.text(24, cy + 4.5, label, "t1", 13)
        xb, xa = px(before), px(after)
        svg.line(xa, cy, xb, cy, "link", 2)
        svg.dot(xb, cy, "other")
        svg.dot(xa, cy, "amoris")
        svg.text(xb + 10, cy + 4.5, before_s, "t2", 12)
        svg.text(xa - 10, cy + 4.5, after_s, "t1", 12, "end", weight="600")
        if ratio:
            svg.text(WIDTH - 24, cy + 4.5, ratio, "t1", 12.5, "end", weight="600")
    height = footer(svg, plot_bottom + 18, notes)
    svg.save(name, height)


def ratio_chart(name, title, subtitle, rows, notes, label_w=270, desc=""):
    """Paired ratios around 1 on a log2 axis: left of 1 blue, right orange."""
    svg = Svg(title, desc or subtitle)
    y = header(svg, title, subtitle)
    y += 30
    x0, x1 = 24 + label_w, WIDTH - 40
    lo, hi = 0.25, 4.0

    def px(v):
        return x0 + (math.log2(v) - math.log2(lo)) / (math.log2(hi) - math.log2(lo)) * (x1 - x0)

    one = px(1)
    svg.text(one - 10, y, "← Rapier faster", "t2", 12, "end", weight="600")
    svg.text(one + 10, y, "Jolt faster →", "t2", 12, "start", weight="600")
    y += 16
    plot_top = y
    bar_h = 14
    placed = []
    for row in rows:
        placed.append((y, row))
        y += 34
    plot_bottom = y - 12
    for t in (0.25, 0.5, 1, 2, 4):
        x = px(t)
        svg.line(x, plot_top - 4, x, plot_bottom, "grid")
        svg.text(x, plot_bottom + 15, f"{t:g}×", "t3", 11, "middle")
    for top_y, (label, sub, ratio, shown) in placed:
        mid = top_y + bar_h / 2
        svg.text(24, mid - 1, label, "t1", 13)
        if sub:
            svg.text(24, mid + 13, sub, "t3", 11)
        end = px(ratio)
        svg.bar(one, top_y, end, bar_h, "amoris" if ratio < 1 else "other")
        if ratio < 1:
            svg.text(end - 6, top_y + bar_h - 2.5, shown, "t1", 12, "end")
        else:
            svg.text(end + 6, top_y + bar_h - 2.5, shown, "t1", 12)
    svg.line(one, plot_top - 4, one, plot_bottom, "base", 1.5)
    height = footer(svg, plot_bottom + 18, notes)
    svg.save(name, height)


AMORIS = ("Amoris", "amoris")


def main():
    # docs/bench/bevy-baseline.md, "Amoris on the same machine and scenes" (Amoris frame
    # 8.35 and 11.7 ms; Bevy 10.3-10.5 and 13.0-13.1 ms; Amoris sphere GPU 2.3-3.4 ms).
    # Bar lengths for Bevy use the charter's single figures (docs/charter.md section 6, the
    # baseline line under the table: sphere about 10.4 ms, dense about 13.0 ms); the labels
    # keep the measured ranges.
    bar_chart(
        "bevy-many-cubes.svg",
        "1.6 million cubes: Amoris and Bevy 0.19, same machine",
        "many_cubes benchmark, frame time in ms (lower is better)",
        [("Bevy 0.19", "other"), AMORIS],
        [
            ("Sphere layout", "cubes around the camera",
             [(10.4, "10.3–10.5 ms", "other"), (8.35, "8.35 ms (display's 120 Hz cap)", "amoris")]),
            ("Dense layout", "camera inside a solid grid",
             [(13.0, "13.0–13.1 ms", "other"), (11.7, "11.7 ms", "amoris")]),
        ],
        ["Apple M5 · Metal · 2026-10-04 · one mesh, one material, 1,600,000 cubes, release builds.",
         "Amoris's sphere frame is held at the display rate; its GPU time was 2.3–3.4 ms."],
        label_w=210,
    )

    # docs/bench/web.md, "Apple M5 against three.js (2026-10-04)", table of 100,000,
    # 400,000 and 1,600,000 cubes (three.js frame / GPU, Amoris frame / GPU).
    bar_chart(
        "threejs-webgpu.svg",
        "Same scene in the browser: Amoris and three.js r186",
        "Chrome WebGPU, GPU time per frame in ms (lower is better)",
        [("three.js r186", "other"), AMORIS],
        [
            ("100,000 cubes", None, [(2.45, "2.45 ms", "other"), (0.71, "0.71 ms", "amoris")]),
            ("400,000 cubes", None, [(2.36, "2.36 ms", "other"), (1.81, "1.81 ms", "amoris")]),
            ("1,600,000 cubes", None, [(21.9, "21.9 ms", "other"), (14.7, "14.7 ms", "amoris")]),
        ],
        ["Apple M5 · Chrome 152 headless, WebGPU · 1280x577 canvas, 4x MSAA · 2026-10-04.",
         "Frame times (requestAnimationFrame, uncapped): three.js 1.00 / 4.17 / 24.8 ms, Amoris 0.95 / 2.36 / 15.0 ms."],
        label_w=170,
    )

    # docs/bench/physics.md, "Paired ratios of step time", column "Rapier det. / Jolt det.,
    # 1 thread" (median over repetitions): Pyramid 0.67, Pyramid30 0.42, ConvexVsMesh 1.62,
    # "Raycast: the 10,000 rays" 1.16, RagdollNoSleep 2.44. Body counts: "Outcome check"
    # (1,240 and 9,455 active boxes) and "Verdict" (160 ragdolls).
    ratio_chart(
        "physics-rapier-jolt.svg",
        "Physics: Rapier (Amoris's engine) against Jolt 5.6",
        "Rapier's step time divided by Jolt's: deterministic builds, one thread, paired median",
        [
            ("Box pyramid", "1,240 boxes", 0.67, "0.67×"),
            ("Large box pyramid", "9,455 boxes", 0.42, "0.42×"),
            ("10,000 ray casts", "closest hit, per step", 1.16, "1.16×"),
            ("Convex bodies on a mesh terrain", None, 1.62, "1.62×"),
            ("Ragdolls, no sleeping", "160 motor-driven ragdolls", 2.44, "2.44×"),
        ],
        ["Apple M5 · native, single thread · 2026-10-04 · 5 to 8 interleaved repetitions on a shared machine;",
         "ratios paired within each repetition. Deterministic builds of both gave the same bits natively and in WebAssembly."],
    )

    # docs/bench/occlusion.md, "Last reliable large-layout measurements" (2026-10-09 quiet
    # build, median of three repeats, GPU ms): columns Off and Auto.
    dumbbell_chart(
        "occlusion.svg",
        "Two-phase occlusion culling",
        "GPU time per frame in ms, log scale: culling off against the default auto mode",
        [("Off", "other"), ("Auto (default)", "amoris")],
        [
            ("header", "Dense grid: camera inside, 443 of 481,933 cubes in view visible"),
            ("RTX 5060 Laptop", "Direct3D 12", 18.15, "18.15", 0.98, "0.98", None),
            ("RTX 5060 Laptop", "Vulkan", 14.77, "14.77", 0.88, "0.88", None),
            ("Radeon 780M", "Direct3D 12", 75.47, "75.47", 4.24, "4.24", None),
            ("Radeon 780M", "Vulkan", 86.64, "86.64", 5.11, "5.11", None),
            ("header", "Orbit: camera outside the grid, about 102,000 visible"),
            ("RTX 5060 Laptop", "Direct3D 12", 21.09, "21.09", 2.62, "2.62", None),
            ("RTX 5060 Laptop", "Vulkan", 20.05, "20.05", 2.56, "2.56", None),
            ("Radeon 780M", "Direct3D 12", 41.02, "41.02", 8.03, "8.03", None),
            ("Radeon 780M", "Vulkan", 47.27, "47.27", 8.26, "8.26", None),
        ],
        (0.5, 100),
        ["Windows laptop (Ryzen 9 270, RTX 5060 Laptop, Radeon 780M) · 1280x720, 4x MSAA · 2026-10-09,",
         "quiet machine, median of three interleaved repeats. Synthetic, visibility-heavy scenes."],
        label_w=190,
    )

    # docs/bench/lod.md, section 9 "Quiet re-measurement (2026-10-09)", rows t = 0:
    # levels off / on GPU ms and the ratio column.
    dumbbell_chart(
        "lod.svg",
        "Mesh levels of detail",
        "GPU time per frame in ms, log scale: 2,304 detailed rocks and knots, levels off and on",
        [("Levels off", "other"), ("Levels on", "amoris")],
        [
            ("RTX 5060 Laptop", "Vulkan", 67.79, "67.79", 0.78, "0.78", "87×"),
            ("RTX 5060 Laptop", "Direct3D 12", 69.17, "69.17", 0.86, "0.86", "80×"),
            ("Radeon 780M", "Vulkan", 125.75, "125.75", 4.94, "4.94", "25×"),
            ("Radeon 780M", "Direct3D 12", 112.73, "112.73", 4.56, "4.56", "25×"),
        ],
        (0.5, 200),
        ["Windows laptop (Ryzen 9 270, RTX 5060 Laptop, Radeon 780M) · 1280x720 with four shadow cascades ·",
         "2026-10-09, quiet machine, median of three rounds. Full meshes are 170 million triangles in view."],
        label_w=190,
        ratio_head="off ÷ on",
    )

    # docs/bench/dynamic-scenes.md, 5.1 "Before against after, RTX 5060", D3D12 rows,
    # column Frame (before -> after, ms): moving-10k, moving-100k, sparse-10k, sparse-100k.
    dumbbell_chart(
        "dynamic-scenes.svg",
        "Many moving objects",
        "Frame time in ms, log scale: 1.6 million cubes with N of them moved every frame",
        [("Before", "other"), ("After", "amoris")],
        [
            ("10,000 moving", "side by side in memory", 11.0, "11.0", 4.68, "4.68", None),
            ("100,000 moving", "side by side in memory", 284, "284", 14.5, "14.5", None),
            ("10,000 moving", "scattered among still cubes", 305, "305", 5.21, "5.21", None),
            ("100,000 moving", "scattered among still cubes", 2403, "2,403", 18.1, "18.1", None),
        ],
        (2, 5000),
        ["Windows laptop, RTX 5060 Laptop · Direct3D 12 · 1280x720 offscreen · 2026-10-15, quiet machine,",
         "median of three rounds. A still scene's frame is unchanged (3.32 → 3.29 ms)."],
        label_w=230,
    )

    # docs/bench/shadows.md, section 4 "Cost" (quiet re-measurement 2026-10-15): the
    # "Shadows off / Shadows on" columns for Direct3D 12 lod-off-0 and lod-off-0.5, and
    # the full-size dense layout paragraph ("27.1 to 15.4 ms on Direct3D 12").
    bar_chart(
        "shadow-slice-culling.svg",
        "Shadow cascades culled by the camera slice they shade",
        "GPU time of the four shadow cascades in ms (lower is better)",
        [("Slice culling off", "other"), ("On (default)", "amoris")],
        [
            ("Rock field, from its corner", "RTX 5060 Laptop", [(33.86, "33.86 ms", "other"), (18.72, "18.72 ms", "amoris")]),
            ("Rock field, halfway in", "RTX 5060 Laptop", [(39.27, "39.27 ms", "other"), (20.20, "20.20 ms", "amoris")]),
            ("Dense grid, 1.6M cubes", "RTX 5060 Laptop", [(27.1, "27.1 ms", "other"), (15.4, "15.4 ms", "amoris")]),
            ("Rock field, from its corner", "Radeon 780M", [(35.75, "35.75 ms", "other"), (20.56, "20.56 ms", "amoris")]),
            ("Rock field, halfway in", "Radeon 780M", [(45.45, "45.45 ms", "other"), (24.76, "24.76 ms", "amoris")]),
        ],
        ["Windows laptop · Direct3D 12 · 1280x720 · 2026-10-15, quiet machine, median of four rounds.",
         "Rock field with levels of detail off. Every frame is identical, bit for bit, with culling off and on."],
        label_w=200,
    )

    # docs/bench/gizmo.md, section 6 table (quiet re-measurement 2026-10-16): Input to
    # frame, median (p95): base 60.5 (92.4), host 48.0 (75.8), new 14.6 (26.1).
    bar_chart(
        "editor-drag-latency.svg",
        "Editor: dragging an object on the live host",
        "From a pointer move to the frame that shows it, median ms (lower is better)",
        None,
        [
            ("Before", None, [(60.5, "60.5 ms (p95 92.4)", "muted")]),
            ("Host sends a frame on each update", None, [(48.0, "48.0 ms (p95 75.8)", "muted")]),
            ("Editor also sends each move at once", None, [(14.6, "14.6 ms (p95 26.1)", "amoris")]),
        ],
        ["Windows laptop · Chrome 155 headless, WebGPU on the Radeon 780M · editor production build",
         "on the real host · 2026-10-16, quiet machine, median of five runs of a 1.5 s drag."],
        label_w=250,
    )

    # docs/bench/neural-textures.md, "Size and fidelity", first table, row "bricks"
    # (9 channels, 1024): Neural 5.37, BC high 37.33, BC low 26.67, 8-bit tight 96.0,
    # 8-bit GPU formats 117.3 bits per mip-0 texel.
    bar_chart(
        "neural-textures.svg",
        "Neural texture compression: storage",
        "Bits per texel for a 9-channel 1024x1024 PBR material, whole mip chain (lower is smaller)",
        None,
        [
            ("8-bit, GPU formats", None, [(117.3, "117.3", "muted")]),
            ("8-bit, tightly packed", None, [(96.0, "96.0", "muted")]),
            ("Block compression, high", "BC7, BC5, BC4", [(37.33, "37.33", "muted")]),
            ("Block compression, low", "BC1, BC5, BC4", [(26.67, "26.67", "muted")]),
            ("Neural (.ntex)", None, [(5.37, "5.37", "amoris")]),
        ],
        ["Sizes are exact for each format and do not depend on the GPU (neural: network and latents).",
         "Quality depends on the content; see the table below the chart."],
        label_w=210,
    )


if __name__ == "__main__":
    main()
