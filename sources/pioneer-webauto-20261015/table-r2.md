| Page | GPU | Loop | Chrome | Lag p50 (max) | Quantum, us | Kind | Before: decision at frames; prepass frames | After |
|---|---|---|---|---|---|---|---|---|
| dense | nvidia | uncapped | unsafe | 372 (373) | 0.032 | two | none, 9 timeouts; 31% | on at 1083; 100% |
| sphere | nvidia | uncapped | unsafe | 373 (373) | 0.032 | one | none, 5 timeouts; 39% | off at 1124; 16% |
| occluders | nvidia | uncapped | unsafe | 358 (360) | 0.032 | one | none, 15 timeouts; 29% | off at 1433; 4% |
| dense | nvidia | uncapped | default | 372 (373) | 65.536 | two | not reported; 29% | on at 1090; 100% |
| sphere | nvidia | uncapped | default | 373 (373) | 65.536 | one | not reported; 38% | off at 1124; 16% |
| occluders | nvidia | uncapped | default | 358 (360) | 65.536 | one | not reported; 27% | off at 2507; 9% |
| dense | nvidia | vsync | unsafe | 1 (5) | 0.032 | two | on at 8; 100% | on at 8; 100% |
| sphere | nvidia | vsync | unsafe | 1 (4) | 0.032 | one | off at 6; 1% | off at 5; 1% |
| occluders | nvidia | vsync | unsafe | 1 (3) | 0.032 | one | off at 5; 1% | off at 5; 1% |
| dense | nvidia | vsync | default | 1 (5) | 65.536 | two | not reported; 100% | on at 8; 92% |
| sphere | nvidia | vsync | default | 1 (4) | 65.536 | one | not reported; 1% | off at 7; 1% |
| occluders | nvidia | vsync | default | 1 (2) | 65.536 | one | not reported; 100% | off at 8; 8% |
| dense | 780m | uncapped | unsafe | 372 (373) | 0.01 | two | none, 4 timeouts; 41% | on at 477; 100% |
| sphere | 780m | uncapped | unsafe | 373 (373) | 0.01 | one | none, 3 timeouts; 53% | off at 1122; 10% |
| occluders | 780m | uncapped | unsafe | 372 (373) | 0.01 | one | off at 493, 5 timeouts; 8% | off at 113; 2% |
| dense | 780m | uncapped | default | 372 (373) | 65.536 | two | not reported; 100% | on at 462; 100% |
| sphere | 780m | uncapped | default | 373 (373) | 65.536 | one | not reported; 57% | off at 2247; 20% |
| occluders | 780m | uncapped | default | 372 (373) | 65.536 | one | not reported; 6% | off at 348; 2% |
| dense | 780m | vsync | unsafe | 1 (6) | 0.01 | two | on at 11; 100% | on at 13; 100% |
| sphere | 780m | vsync | unsafe | 5 (7) | 0.01 | one | off at 17; 1% | off at 20; 1% |
| occluders | 780m | vsync | unsafe | 1 (3) | 0.01 | one | off at 5; 1% | off at 5; 1% |
| dense | 780m | vsync | default | 1 (5) | 65.536 | two | not reported; 100% | on at 11; 100% |
| sphere | 780m | vsync | default | 2 (7) | 65.536 | one | not reported; 1% | off at 23; 1% |
| occluders | 780m | vsync | default | 1 (3) | 65.536 | one | not reported; 1% | off at 6; 1% |

Before: Canvas 1254x564; Chrome/155.0.8059.41, not recorded.
After: Canvas 1254x564; Chrome/155.0.8059.41.

| Page | GPU | Loop | Opaque ms, prepass on | Off | Cheaper |
|---|---|---|---|---|---|
| dense | nvidia | uncapped | 0.157 | 0.341 | on (-54%) |
| sphere | nvidia | uncapped | 2.911 | 2.149 | off (+35%) |
| occluders | nvidia | uncapped | 0.118 | 0.116 | off (+2%) |
| dense | nvidia | vsync | 0.143 | 0.305 | on (-53%) |
| sphere | nvidia | vsync | 2.754 | 1.925 | off (+43%) |
| occluders | nvidia | vsync | 0.111 | 0.107 | off (+4%) |
| dense | 780m | uncapped | 0.499 | 1.057 | on (-53%) |
| sphere | 780m | uncapped | 6.129 | 4.039 | off (+52%) |
| occluders | 780m | uncapped | 0.569 | 0.506 | off (+12%) |
| dense | 780m | vsync | 0.728 | 1.481 | on (-51%) |
| sphere | 780m | vsync | 4.878 | 4.323 | off (+13%) |
| occluders | 780m | vsync | 0.854 | 0.798 | off (+7%) |

Canvas 1254x564; Chrome/155.0.8059.41.

| Page | GPU | Loop | GPU ms, occlusion on | Off | Cheaper | Auto, unsafe: frames on, last half | Default |
|---|---|---|---|---|---|---|---|
| dense | nvidia | uncapped | 0.869 | 8.464 | on (-90%) | on, 100% | on, 100% |
| dense | nvidia | vsync | 0.930 | 8.618 | on (-89%) | on, 100% | on, 100% |
| dense | 780m | uncapped | 3.021 | 23.910 | on (-87%) | on, 100% | on, 100% |
| dense | 780m | vsync | 4.184 | 24.293 | on (-83%) | on, 100% | on, 100% |
| sphere | nvidia | uncapped | 2.925 | 2.617 | off (+12%) | off, 0% | off, 0% |
| occluders | nvidia | uncapped | 0.282 | 0.224 | off (+26%) | off, 0% | off, 0% |
| sphere | nvidia | vsync | 2.610 | 2.465 | off (+6%) | off, 0% | off, 0% |
| occluders | nvidia | vsync | 0.266 | 0.209 | off (+27%) | off, 0% | off, 0% |
| sphere | 780m | uncapped | 7.643 | 6.672 | off (+15%) | off, 0% | off, 0% |
| occluders | 780m | uncapped | 1.433 | 1.144 | off (+25%) | off, 0% | off, 0% |
| sphere | 780m | vsync | 8.439 | 6.646 | off (+27%) | off, 0% | off, 0% |
| occluders | 780m | vsync | 2.193 | 1.643 | off (+33%) | off, 0% | off, 0% |

Canvas 1254x564; Chrome/155.0.8059.41.
| Run | Kind | Prepass: decision at frames | Lag (max) | Occlusion: first decision | Prepass frames |
|---|---|---|---|---|---|
| r2native-dense-nvidia-dx12 | two | on at 5 | 1 (1) | on at 3 | {'auto-off': 1, 'auto-on': 599} |
| r2native-sphere-nvidia-dx12 | one | off at 5 | 1 (1) | off at 3 | {'auto-off': 594, 'auto-on': 6} |
| r2native-dense-780m-dx12 | two | on at 5 | 1 (1) | on at 3 | {'auto-off': 1, 'auto-on': 599} |
| r2native-sphere-780m-dx12 | one | off at 5 | 1 (1) | off at 3 | {'auto-off': 594, 'auto-on': 6} |
