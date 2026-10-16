| Page | GPU | Loop | Opaque ms, prepass on | Off | Cheaper |
|---|---|---|---|---|---|
| dense | nvidia | uncapped | 0.159 | 0.346 | on (-54%) |
| sphere | nvidia | uncapped | 2.896 | 2.078 | off (+39%) |
| occluders | nvidia | uncapped | 0.110 | 0.106 | off (+4%) |
| dense | nvidia | vsync | 0.143 | 0.298 | on (-52%) |
| sphere | nvidia | vsync | 2.754 | 1.923 | off (+43%) |
| occluders | nvidia | vsync | 0.109 | 0.106 | off (+3%) |
| dense | 780m | uncapped | 0.434 | 0.977 | on (-56%) |
| sphere | 780m | uncapped | 4.931 | 3.871 | off (+27%) |
| occluders | 780m | uncapped | 0.560 | 0.493 | off (+14%) |
| dense | 780m | vsync | 0.714 | 1.438 | on (-50%) |
| sphere | 780m | vsync | 4.700 | 4.280 | off (+10%) |
| occluders | 780m | vsync | 0.855 | 0.812 | off (+5%) |

| Page | GPU | Loop | GPU ms, occlusion on | Off | Cheaper | Auto, unsafe: frames on, last half | Default |
|---|---|---|---|---|---|---|---|
| dense | nvidia | uncapped | 0.871 | 8.471 | on (-90%) | on, 100% | on, 100% |
| sphere | nvidia | uncapped | 2.927 | 2.618 | off (+12%) | off, 0% | off, 0% |
| occluders | nvidia | uncapped | 0.265 | 0.208 | off (+27%) | off, 0% | off, 0% |
| dense | nvidia | vsync | 0.935 | 8.621 | on (-89%) | on, 100% | on, 100% |
| sphere | nvidia | vsync | 2.619 | 2.338 | off (+12%) | off, 0% | off, 0% |
| occluders | nvidia | vsync | 0.268 | 0.207 | off (+29%) | off, 0% | off, 0% |
| dense | 780m | uncapped | 3.312 | 24.499 | on (-86%) | on, 100% | on, 100% |
| sphere | 780m | uncapped | 6.370 | 5.465 | off (+17%) | off, 0% | off, 0% |
| occluders | 780m | uncapped | 1.323 | 1.066 | off (+24%) | off, 0% | off, 0% |
| dense | 780m | vsync | 4.105 | 23.981 | on (-83%) | on, 100% | on, 100% |
| sphere | 780m | vsync | 6.577 | 5.722 | off (+15%) | off, 0% | off, 0% |
| occluders | 780m | vsync | 2.174 | 1.478 | off (+47%) | off, 0% | off, 0% |

Canvas 1254x564; Chrome/155.0.8059.41.

| Page | GPU | Loop | Chrome | Lag p50 (max) | Quantum, us | Kind | Before: decision at frames; prepass frames | After |
|---|---|---|---|---|---|---|---|---|
| dense | nvidia | uncapped | default | 372 (373) | 65.536 | two | not reported; 30% | on at 1080; 100% |
| sphere | nvidia | uncapped | default | 373 (373) | 65.536 | one | not reported; 39% | off at 1123; 16% |
| occluders | nvidia | uncapped | default | 358 (358) | 65.536 | one | not reported; 28% | off at 1075; 4% |
| dense | nvidia | vsync | default | 1 (5) | 65.536 | two | not reported; 100% | on at 8; 100% |
| sphere | nvidia | vsync | default | 1 (4) | 65.536 | one | not reported; 1% | off at 5; 1% |
| occluders | nvidia | vsync | default | 1 (3) | 65.536 | one | not reported; 100% | off at 5; 1% |
| dense | 780m | uncapped | default | 372 (373) | 65.536 | two | not reported; 100% | on at 400; 100% |
| sphere | 780m | uncapped | default | 373 (373) | 65.536 | one | not reported; 55% | off at 1099; 9% |
| occluders | 780m | uncapped | default | 372 (373) | 65.536 | one | not reported; 5% | off at 186; 2% |
| dense | 780m | vsync | default | 1 (6) | 65.536 | two | not reported; 100% | on at 13; 100% |
| sphere | 780m | vsync | default | 2 (7) | 65.536 | one | not reported; 1% | off at 19; 1% |
| occluders | 780m | vsync | default | 1 (3) | 65.536 | one | not reported; 1% | off at 5; 1% |
| dense | nvidia | uncapped | unsafe | 372 (373) | 0.032 | two | - | on at 1052; 100% |
| sphere | nvidia | uncapped | unsafe | 373 (373) | 0.032 | one | - | off at 1125; 16% |
| occluders | nvidia | uncapped | unsafe | 358 (359) | 0.032 | one | - | off at 1075; 4% |
| dense | nvidia | vsync | unsafe | 1 (5) | 0.032 | two | - | on at 8; 100% |
| sphere | nvidia | vsync | unsafe | 1 (4) | 0.032 | one | - | off at 5; 1% |
| occluders | nvidia | vsync | unsafe | 1 (3) | 0.032 | one | - | off at 5; 1% |
| dense | 780m | vsync | unsafe | 1 (7) | 0.01 | two | - | on at 13; 100% |
| sphere | 780m | vsync | unsafe | 2 (7) | 0.01 | one | - | off at 21; 1% |
| occluders | 780m | vsync | unsafe | 1 (3) | 0.01 | one | - | off at 5; 1% |
| dense | 780m | uncapped | unsafe | 372 (373) | 0.01 | two | - | on at 366; 100% |
| sphere | 780m | uncapped | unsafe | 373 (373) | 0.01 | one | - | off at 1079; 9% |
| occluders | 780m | uncapped | unsafe | 372 (373) | 0.01 | one | - | off at 151; 2% |

Before: Canvas 1254x564; Chrome/155.0.8059.41.
After: Canvas 1254x564; Chrome/155.0.8059.41.

| Run | Kind | Prepass: decision at frames | Lag (max) | Occlusion: first decision | Prepass frames |
|---|---|---|---|---|---|
| native-dense-nvidia-dx12 | two | on at 5 | 1 (1) | on at 3 | {'auto-off': 1, 'auto-on': 599} |
| native-sphere-nvidia-dx12 | one | off at 5 | 1 (1) | off at 3 | {'auto-off': 594, 'auto-on': 6} |
| native-dense-780m-dx12 | two | on at 5 | 1 (1) | on at 3 | {'auto-off': 1, 'auto-on': 599} |
| native-sphere-780m-dx12 | one | off at 5 | 1 (1) | off at 3 | {'auto-off': 594, 'auto-on': 6} |
