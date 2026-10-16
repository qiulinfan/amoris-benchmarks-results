Rounds 1–7 (7), 196 runs; whole-machine CPU use during the runs: median 11.7%, range 9.3–92.4%.

### Step time

Mean ms per step over 500 steps: median over rounds (fastest–slowest round); p95 of the steps, median over rounds, in brackets.

| Configuration | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. (shipped), 1 thr. | 7.55 (6.06–9.31) [8.75] | 93.48 (92.50–93.97) [109.86] | 5.88 (5.67–6.15) [9.62] | 6.21 (6.03–6.50) [9.83] |
| Rapier default, 1 thr. | 8.29 (6.14–9.86) [9.40] | 95.64 (92.48–98.39) [110.06] | 5.82 (5.50–6.33) [9.51] | 6.07 (5.91–6.52) [9.79] |
| Rapier det.+parallel, 16 thr. | 1.89 (1.51–2.37) [2.86] | 31.64 (30.34–32.25) [34.76] | 1.89 (1.81–2.83) [2.86] | 2.32 (2.27–2.54) [3.29] |
| Rapier det., x86-64-v2, 1 thr. | 6.68 (5.97–8.81) [7.68] | 93.06 (90.73–95.62) [106.29] | 5.71 (5.61–6.00) [9.32] | 6.00 (5.96–6.15) [9.48] |
| Rapier det.+parallel, 8 thr. | 1.82 (1.54–2.50) [2.38] | 33.76 (33.55–34.12) [37.97] | 1.86 (1.81–2.63) [2.86] | 2.26 (2.19–2.61) [3.14] |
| Rapier det., x86-64-v3, 1 thr. | 6.47 (5.93–7.79) [7.14] | 89.85 (88.75–91.39) [103.18] | 5.74 (5.53–5.93) [9.52] | 6.13 (5.86–7.36) [9.46] |
| Rapier det.+parallel, 1 thr. | 7.52 (6.73–9.83) [9.25] | 96.53 (92.66–98.06) [108.28] | 6.82 (6.67–7.17) [10.76] | 7.10 (6.92–8.14) [11.37] |

### Ray casts (Raycast scene, 10,000 closest-hit rays after every step)

| Configuration | ms per 10,000 rays, median (range) | Hits in the run |
|---|---|---|
| Rapier det. (shipped), 1 thr. | 2.74 (2.73–2.77) | 4753000 |
| Rapier default, 1 thr. | 2.73 (2.72–2.84) | 4753000 |
| Rapier det.+parallel, 16 thr. | 2.91 (2.87–2.95) | 4753000 |
| Rapier det., x86-64-v2, 1 thr. | 2.65 (2.63–2.67) | 4753000 |
| Rapier det.+parallel, 8 thr. | 2.82 (2.78–2.83) | 4753000 |
| Rapier det., x86-64-v3, 1 thr. | 2.61 (2.57–2.74) | 4753000 |
| Rapier det.+parallel, 1 thr. | 2.95 (2.90–2.96) | 4753000 |

### Paired ratios of step time (within a round; median, n, range; above 1 means the first is slower)

| Ratio | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. / Rapier default, 1 thr. | 0.94 (n=7, 0.78–1.05) | 0.98 (n=7, 0.94–1.01) | 1.02 (n=7, 0.93–1.05) | 1.02 (n=7, 0.98–1.04) |
| det.+parallel / det., 1 thr. | 1.11 (n=7, 0.90–1.27) | 1.03 (n=7, 0.99–1.05) | 1.18 (n=7, 1.10–1.22) | 1.16 (n=7, 1.09–1.31) |
| det. x86-64-v2 / det. baseline, 1 thr. | 0.98 (n=7, 0.82–1.15) | 0.99 (n=7, 0.97–1.03) | 0.99 (n=7, 0.94–0.99) | 0.97 (n=7, 0.94–0.99) |
| det. x86-64-v3 / det. baseline, 1 thr. | 0.94 (n=7, 0.69–1.18) | 0.96 (n=7, 0.95–0.99) | 0.97 (n=7, 0.93–1.01) | 1.00 (n=7, 0.95–1.18) |
| det.+parallel 8 thr. / det. 1 thr. | 0.26 (n=7, 0.19–0.33) | 0.36 (n=7, 0.36–0.37) | 0.32 (n=7, 0.31–0.45) | 0.36 (n=7, 0.35–0.42) |
| det.+parallel 16 thr. / det. 1 thr. | 0.27 (n=7, 0.20–0.31) | 0.34 (n=7, 0.32–0.35) | 0.32 (n=7, 0.31–0.48) | 0.38 (n=7, 0.36–0.39) |

### Paired ratios, quiet pairs only (each one-thread run at most 15% whole-machine CPU)

| Ratio | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. / Rapier default, 1 thr. | 0.94 (n=7, 0.78–1.05) | 0.98 (n=7, 0.94–1.01) | 1.02 (n=7, 0.93–1.05) | 1.02 (n=7, 0.98–1.04) |
| det.+parallel / det., 1 thr. | 1.12 (n=6, 0.90–1.27) | 1.03 (n=7, 0.99–1.05) | 1.18 (n=7, 1.10–1.22) | 1.16 (n=7, 1.09–1.31) |
| det. x86-64-v2 / det. baseline, 1 thr. | 0.98 (n=7, 0.82–1.15) | 0.99 (n=7, 0.97–1.03) | 0.99 (n=7, 0.94–0.99) | 0.97 (n=7, 0.94–0.99) |
| det. x86-64-v3 / det. baseline, 1 thr. | 0.94 (n=7, 0.69–1.18) | 0.96 (n=7, 0.95–0.99) | 0.97 (n=7, 0.93–1.01) | 1.00 (n=7, 0.95–1.18) |
| det.+parallel 8 thr. / det. 1 thr. | 0.26 (n=7, 0.19–0.33) | 0.36 (n=7, 0.36–0.37) | 0.32 (n=7, 0.31–0.45) | 0.36 (n=7, 0.35–0.42) |
| det.+parallel 16 thr. / det. 1 thr. | 0.27 (n=7, 0.20–0.31) | 0.34 (n=7, 0.32–0.35) | 0.32 (n=7, 0.31–0.48) | 0.38 (n=7, 0.36–0.39) |

### Outcomes (where the dynamic bodies ended; every round)

| Configuration | Scene | top y | mean y | active at end | end hashes over rounds |
|---|---|---|---|---|---|
| Rapier det. (shipped), 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 7) |
| Rapier det. (shipped), 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 7) |
| Rapier det. (shipped), 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det. (shipped), 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier default, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x0b44ecb1c0a56994` (all 7) |
| Rapier default, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0x13f5a8b3bfce5348` (all 7) |
| Rapier default, 1 thr. | ConvexVsMesh | 10.27 | 1.94 | 1687 | `0x52cfe759f3afe395` (all 7) |
| Rapier default, 1 thr. | Raycast | 10.27 | 1.94 | 1687 | `0x52cfe759f3afe395` (all 7) |
| Rapier det.+parallel, 16 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 7) |
| Rapier det.+parallel, 16 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 7) |
| Rapier det.+parallel, 16 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det.+parallel, 16 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det., x86-64-v2, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 7) |
| Rapier det., x86-64-v2, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 7) |
| Rapier det., x86-64-v2, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det., x86-64-v2, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det.+parallel, 8 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 7) |
| Rapier det.+parallel, 8 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 7) |
| Rapier det.+parallel, 8 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det.+parallel, 8 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det., x86-64-v3, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 7) |
| Rapier det., x86-64-v3, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 7) |
| Rapier det., x86-64-v3, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det., x86-64-v3, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det.+parallel, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 7) |
| Rapier det.+parallel, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 7) |
| Rapier det.+parallel, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |
| Rapier det.+parallel, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 7) |

