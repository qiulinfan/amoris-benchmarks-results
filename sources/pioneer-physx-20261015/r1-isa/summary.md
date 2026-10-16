Rounds 1–3 (3), 60 runs; whole-machine CPU use during the runs: median 12.7%, range 9.3–61.9%.

### Step time

Mean ms per step over 500 steps: median over rounds (fastest–slowest round); p95 of the steps, median over rounds, in brackets.

| Configuration | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. (shipped), 1 thr. | 7.64 (6.99–9.85) [10.58] | 94.73 (89.42–99.87) [119.79] | 5.92 (5.75–5.98) [9.70] | 6.10 (6.00–6.11) [9.61] |
| Rapier default, 1 thr. | 6.66 (6.20–6.94) [7.82] | 90.97 (90.96–92.48) [100.29] | 5.69 (5.64–5.75) [9.49] | 5.92 (5.75–7.12) [9.43] |
| Rapier det., x86-64-v2, 1 thr. | 6.86 (5.99–8.86) [8.48] | 94.35 (91.18–107.63) [117.22] | 5.77 (5.63–5.85) [9.33] | 6.01 (5.91–6.54) [9.91] |
| Rapier det., x86-64-v3, 1 thr. | 6.74 (6.07–7.43) [8.01] | 90.65 (86.96–92.11) [105.71] | 5.61 (5.55–5.66) [9.19] | 5.82 (5.75–7.17) [9.43] |
| Rapier det.+parallel, 1 thr. | 7.62 (7.48–7.73) [8.57] | 94.53 (93.06–118.10) [106.90] | 6.87 (6.79–6.99) [10.78] | 7.23 (7.07–7.68) [11.30] |

### Ray casts (Raycast scene, 10,000 closest-hit rays after every step)

| Configuration | ms per 10,000 rays, median (range) | Hits in the run |
|---|---|---|
| Rapier det. (shipped), 1 thr. | 2.72 (2.71–2.73) | 4753000 |
| Rapier default, 1 thr. | 2.72 (2.67–2.87) | 4753000 |
| Rapier det., x86-64-v2, 1 thr. | 2.62 (2.61–2.62) | 4753000 |
| Rapier det., x86-64-v3, 1 thr. | 2.55 (2.54–2.57) | 4753000 |
| Rapier det.+parallel, 1 thr. | 3.01 (2.99–3.04) | 4753000 |

### Paired ratios of step time (within a round; median, n, range; above 1 means the first is slower)

| Ratio | Pyramid | Pyramid30 | ConvexVsMesh | Raycast |
|---|---|---|---|---|
| Rapier det. / Rapier default, 1 thr. | 1.15 (n=3, 1.13–1.42) | 1.04 (n=3, 0.97–1.10) | 1.03 (n=3, 1.02–1.05) | 1.03 (n=3, 0.84–1.06) |
| det.+parallel / det., 1 thr. | 1.01 (n=3, 0.76–1.09) | 1.04 (n=3, 1.00–1.18) | 1.18 (n=3, 1.14–1.19) | 1.18 (n=3, 1.16–1.28) |
| det. x86-64-v2 / det. baseline, 1 thr. | 0.90 (n=3, 0.86–0.90) | 1.02 (n=3, 0.94–1.14) | 0.98 (n=3, 0.94–1.02) | 0.98 (n=3, 0.97–1.09) |
| det. x86-64-v3 / det. baseline, 1 thr. | 0.87 (n=3, 0.75–0.88) | 0.96 (n=3, 0.92–0.97) | 0.95 (n=3, 0.95–0.96) | 0.95 (n=3, 0.94–1.19) |

### Outcomes (where the dynamic bodies ended; every round)

| Configuration | Scene | top y | mean y | active at end | end hashes over rounds |
|---|---|---|---|---|---|
| Rapier det. (shipped), 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 3) |
| Rapier det. (shipped), 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 3) |
| Rapier det. (shipped), 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier det. (shipped), 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier default, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x0b44ecb1c0a56994` (all 3) |
| Rapier default, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0x13f5a8b3bfce5348` (all 3) |
| Rapier default, 1 thr. | ConvexVsMesh | 10.27 | 1.94 | 1687 | `0x52cfe759f3afe395` (all 3) |
| Rapier default, 1 thr. | Raycast | 10.27 | 1.94 | 1687 | `0x52cfe759f3afe395` (all 3) |
| Rapier det., x86-64-v2, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 3) |
| Rapier det., x86-64-v2, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 3) |
| Rapier det., x86-64-v2, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier det., x86-64-v2, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier det., x86-64-v3, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 3) |
| Rapier det., x86-64-v3, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 3) |
| Rapier det., x86-64-v3, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier det., x86-64-v3, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier det.+parallel, 1 thr. | Pyramid | 28.99 | 7.77 | 1240 | `0x35b8325978916b7f` (all 3) |
| Rapier det.+parallel, 1 thr. | Pyramid30 | 58.97 | 15.25 | 9455 | `0xae1548844c93a7b8` (all 3) |
| Rapier det.+parallel, 1 thr. | ConvexVsMesh | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |
| Rapier det.+parallel, 1 thr. | Raycast | 10.35 | 1.93 | 1624 | `0x9ae30402cc5cb77b` (all 3) |

