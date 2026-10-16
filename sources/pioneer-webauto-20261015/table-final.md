| Page | GPU | Loop | Chrome | Lag p50 (max) | Quantum, us | Kind | Before: decision at frames; prepass frames | After |
|---|---|---|---|---|---|---|---|---|
| dense | nvidia | uncapped | unsafe | 372 (373) | 0.032 | two | none, 9 timeouts; 31% | on at 1040; 100% |
| sphere | nvidia | uncapped | unsafe | 373 (373) | 0.032 | one | none, 5 timeouts; 39% | off at 1120; 16% |
| occluders | nvidia | uncapped | unsafe | 358 (359) | 0.032 | one | none, 15 timeouts; 29% | off at 1430; 5% |
| dense | nvidia | uncapped | default | 366 (373) | 65.536 | two | none, 11 timeouts; 30% | on at 1015; 100% |
| sphere | nvidia | uncapped | default | 373 (373) | 65.536 | one | none, 5 timeouts; 39% | off at 1123; 16% |
| occluders | nvidia | uncapped | default | 358 (360) | 65.536 | one | none, 20 timeouts; 27% | off at 1431; 4% |
| dense | nvidia | vsync | unsafe | 1 (5) | 0.032 | two | on at 8; 100% | on at 8; 100% |
| sphere | nvidia | vsync | unsafe | 1 (4) | 0.032 | one | off at 6; 1% | off at 5; 1% |
| occluders | nvidia | vsync | unsafe | 1 (4) | 0.032 | one | off at 5; 1% | off at 5; 1% |
| dense | nvidia | vsync | default | 1 (5) | 65.536 | two | on at 8; 100% | off at 8; 1% |
| sphere | nvidia | vsync | default | 1 (4) | 65.536 | one | off at 5; 1% | off at 5; 1% |
| occluders | nvidia | vsync | default | 1 (3) | 65.536 | one | on at 5; 100% | off at 5; 1% |
| dense | 780m | uncapped | unsafe | 373 (373) | 0.01 | two | none, 4 timeouts; 41% | on at 1108; 100% |
| sphere | 780m | uncapped | unsafe | 373 (373) | 0.01 | one | none, 3 timeouts; 53% | off at 695; 29% |
| occluders | 780m | uncapped | unsafe | 372 (373) | 0.01 | one | off at 493, 5 timeouts; 8% | off at 1093; 16% |
| dense | 780m | uncapped | default | 372 (372) | 65.536 | two | on at 323, 4 timeouts; 100% | on at 441; 100% |
| sphere | 780m | uncapped | default | 373 (373) | 65.536 | one | none, 3 timeouts; 56% | off at 1123; 61% |
| occluders | 780m | uncapped | default | 372 (373) | 65.536 | one | none, 6 timeouts; 41% | off at 110; 5% |
| dense | 780m | vsync | unsafe | 1 (5) | 0.01 | two | on at 11; 100% | on at 11; 100% |
| sphere | 780m | vsync | unsafe | 4 (7) | 0.01 | one | off at 17; 1% | off at 19; 1% |
| occluders | 780m | vsync | unsafe | 1 (2) | 0.01 | one | off at 5; 1% | off at 5; 1% |
| dense | 780m | vsync | default | 2 (4) | 65.536 | two | on at 12; 100% | on at 11; 100% |
| sphere | 780m | vsync | default | 6 (7) | 65.536 | one | off at 21; 1% | off at 20; 2% |
| occluders | 780m | vsync | default | 1 (3) | 65.536 | one | off at 6; 1% | off at 5; 1% |

