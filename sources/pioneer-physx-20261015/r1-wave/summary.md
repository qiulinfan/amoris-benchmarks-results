Rounds 1–5 (5), 100 runs; whole-machine CPU use during the runs: median 43.25%, range 9.3–97.4%.

### Step time

Mean ms per step over 500 steps: median over rounds (fastest–slowest round); p95 of the steps, median over rounds, in brackets.

| Configuration | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. (shipped), 1 thr. | 6.49 (6.07–13.82) [7.44] | 93.81 (90.21–133.25) [119.15] | 6.07 (5.82–9.85) [10.19] | 6.28 (5.97–9.58) [10.40] |
| Rapier default, 1 thr. | 7.54 (6.12–11.90) [9.75] | 106.56 (91.07–142.02) [149.72] | 5.73 (5.53–9.23) [9.54] | 6.48 (5.74–9.30) [11.95] |
| Rapier det.+parallel, 1 thr. | 7.00 (6.78–11.45) [8.05] | 94.07 (90.71–108.22) [102.44] | 6.81 (6.67–12.16) [10.73] | 8.43 (6.95–11.93) [13.12] |
| Rapier det.+parallel, 8 thr. | 1.64 (1.51–2.92) [2.29] | 31.77 (29.87–45.24) [37.45] | 2.16 (1.76–3.26) [3.12] | 3.17 (2.20–3.52) [4.48] |
| Rapier det.+parallel, 16 thr. | 2.06 (1.58–3.02) [3.21] | 31.31 (29.66–43.60) [36.71] | 2.05 (1.92–3.17) [3.10] | 2.32 (2.23–3.07) [3.29] |

### Ray casts (Raycast scene, 10,000 closest-hit rays after every step)

| Configuration | ms per 10,000 rays, median (range) | Hits in the run |
|---|---|---|
| Rapier det. (shipped), 1 thr. | 2.80 (2.71–3.60) | 4753000 |
| Rapier default, 1 thr. | 2.80 (2.69–3.56) | 4753000 |
| Rapier det.+parallel, 1 thr. | 3.22 (2.94–3.80) | 4753000 |
| Rapier det.+parallel, 8 thr. | 3.62 (2.79–3.97) | 4753000 |
| Rapier det.+parallel, 16 thr. | 2.97 (2.87–3.65) | 4753000 |

### Paired ratios of step time (within a round; median, n, range; above 1 means the first is slower)

| Ratio | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. / Rapier default, 1 thr. | 0.97 (n=5, 0.80–1.16) | 0.98 (n=5, 0.66–1.25) | 1.06 (n=5, 1.03–1.08) | 1.03 (n=5, 0.97–1.04) |
| det.+parallel / det., 1 thr. | 1.05 (n=5, 0.83–1.15) | 1.00 (n=5, 0.81–1.05) | 1.15 (n=5, 1.12–1.23) | 1.16 (n=5, 1.00–1.35) |
| det.+parallel 8 thr. / det. 1 thr. | 0.25 (n=5, 0.21–0.36) | 0.34 (n=5, 0.24–0.45) | 0.33 (n=5, 0.30–0.40) | 0.38 (n=5, 0.33–0.53) |
| det.+parallel 16 thr. / det. 1 thr. | 0.31 (n=5, 0.22–0.41) | 0.33 (n=5, 0.33–0.36) | 0.33 (n=5, 0.32–0.36) | 0.36 (n=5, 0.31–0.37) |

### Outcomes (where the dynamic bodies ended; every round)

| Configuration | Scene | top y | mean y | active at end | end hashes over rounds |
|---|---|---|---|---|---|
| Rapier det. (shipped), 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 5) |
| Rapier det. (shipped), 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 5) |
| Rapier det. (shipped), 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier det. (shipped), 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier default, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x0b44ecb1c0a56994` (all 5) |
| Rapier default, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0x13f5a8b3bfce5348` (all 5) |
| Rapier default, 1 thr. | ConvexVsMesh | 10.27 | 1.94 | 1687 | `0x52cfe759f3afe395` (all 5) |
| Rapier default, 1 thr. | Raycast | 10.27 | 1.94 | 1687 | `0x52cfe759f3afe395` (all 5) |
| Rapier det.+parallel, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 5) |
| Rapier det.+parallel, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 5) |
| Rapier det.+parallel, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier det.+parallel, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier det.+parallel, 8 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 5) |
| Rapier det.+parallel, 8 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 5) |
| Rapier det.+parallel, 8 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier det.+parallel, 8 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier det.+parallel, 16 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 5) |
| Rapier det.+parallel, 16 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 5) |
| Rapier det.+parallel, 16 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |
| Rapier det.+parallel, 16 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 5) |

