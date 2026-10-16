## this, back to back

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 5 | 65.5 / 67.3 (+2.68 %) | +2.68 % | +2.94, +2.25, +3.60, +2.68, +1.73 | +2.08 % | +1.85, +2.01, +2.08, +2.31, +2.39 | +1.76 | 31.3 | 36.0 |
| sailing-course | 5 | 82.2 / 83.6 (+1.71 %) | +1.71 % | +1.41, +1.71, +2.64, +1.92, +1.31 | +1.93 % | +1.72, +1.93, +2.22, +1.93, +2.62 | +1.40 | 31.1 | 36.0 |

sailing, back to back, last run (3000 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0007 |
| interface.intents | 0.0000 | 0.0003 |
| script:log | 0.0185 | 0.0497 |
| script:take_aboard | 0.0136 | 0.0393 |
| script.update | 0.0003 | 0.0022 |
| physics.wind | 0.0011 | 0.0045 |
| physics.buoyancy | 0.0172 | 0.0485 |
| physics.sail | 0.0010 | 0.0049 |
| physics.hull | 0.0015 | 0.0062 |
| physics.step | 0.0118 | 0.0251 |
| physics.contacts | 0.0001 | 0.0006 |
| interface.perception | 0.0001 | 0.0008 |
| interface.turns | 0.0000 | 0.0002 |
| assets.animate | 0.0000 | 0.0005 |
| sim.finish | 0.0002 | 0.0013 |
| tick.other | 0.0010 | 0.0216 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0003 |
| loop.after | 0.0001 | 0.0064 |
| tick | 0.0666 | 0.1293 |

Phases (ms per tick): Begin 0.0001, Control 0.0000, Update 0.0324, Forces 0.0208, Physics 0.0119, Finish 0.0003

sailing-course, back to back, last run (3000 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0007 |
| interface.intents | 0.0005 | 0.0093 |
| script:take_aboard | 0.0154 | 0.0593 |
| script:rounding | 0.0219 | 0.0581 |
| script.update | 0.0004 | 0.0028 |
| physics.wind | 0.0013 | 0.0044 |
| physics.buoyancy | 0.0177 | 0.0457 |
| physics.sail | 0.0009 | 0.0066 |
| physics.hull | 0.0016 | 0.0078 |
| physics.step | 0.0137 | 0.0640 |
| physics.contacts | 0.0001 | 0.0009 |
| interface.perception | 0.0110 | 0.0480 |
| interface.turns | 0.0002 | 0.0025 |
| assets.animate | 0.0001 | 0.0007 |
| sim.finish | 0.0002 | 0.0015 |
| tick.other | 0.0011 | 0.0076 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0007 |
| loop.after | 0.0001 | 0.0051 |
| tick | 0.0862 | 0.2358 |

Phases (ms per tick): Begin 0.0001, Control 0.0005, Update 0.0377, Forces 0.0215, Physics 0.0138, Finish 0.0115

## this, paced 16.6667 ms

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 5 | 274.5 / 278.9 (+1.62 %) | +1.62 % | +4.70, +1.62, +1.37, -0.14, +1.95 | +2.33 % | +4.70, +1.84, +2.33, +0.17, +3.00 | +4.45 | 31.1 | 36.0 |
| sailing-course | 5 | 336.1 / 346.8 (+3.20 %) | +3.20 % | +2.50, +4.02, +3.57, +3.20, +2.55 | +3.21 % | +1.74, +3.62, +3.21, +4.36, +2.65 | +10.76 | 31.0 | 36.0 |

sailing, paced 16.6667 ms, last run (1800 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0009 | 0.0419 |
| interface.intents | 0.0009 | 0.0307 |
| script:log | 0.1089 | 0.2998 |
| script:take_aboard | 0.0381 | 0.2281 |
| script.update | 0.0056 | 0.0894 |
| physics.wind | 0.0097 | 0.0223 |
| physics.buoyancy | 0.0330 | 0.0631 |
| physics.sail | 0.0038 | 0.0112 |
| physics.hull | 0.0048 | 0.0239 |
| physics.step | 0.0645 | 0.2179 |
| physics.contacts | 0.0005 | 0.0089 |
| interface.perception | 0.0014 | 0.0167 |
| interface.turns | 0.0006 | 0.0018 |
| assets.animate | 0.0008 | 0.0023 |
| sim.finish | 0.0011 | 0.0178 |
| tick.other | 0.0128 | 0.0605 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0008 |
| loop.after | 0.0006 | 0.0096 |
| tick | 0.2877 | 0.5932 |

Phases (ms per tick): Begin 0.0009, Control 0.0009, Update 0.1527, Forces 0.0514, Physics 0.0650, Finish 0.0040

sailing-course, paced 16.6667 ms, last run (1800 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0010 | 0.0306 |
| interface.intents | 0.0103 | 0.0658 |
| script:take_aboard | 0.0954 | 0.2280 |
| script:rounding | 0.0581 | 0.3394 |
| script.update | 0.0041 | 0.0309 |
| physics.wind | 0.0098 | 0.0340 |
| physics.buoyancy | 0.0329 | 0.1941 |
| physics.sail | 0.0031 | 0.0275 |
| physics.hull | 0.0048 | 0.0428 |
| physics.step | 0.0650 | 0.1416 |
| physics.contacts | 0.0004 | 0.0023 |
| interface.perception | 0.0497 | 0.1134 |
| interface.turns | 0.0026 | 0.0071 |
| assets.animate | 0.0008 | 0.0059 |
| sim.finish | 0.0010 | 0.0096 |
| tick.other | 0.0119 | 0.0442 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0081 |
| loop.after | 0.0006 | 0.0102 |
| tick | 0.3509 | 0.8374 |

Phases (ms per tick): Begin 0.0010, Control 0.0103, Update 0.1576, Forces 0.0506, Physics 0.0654, Finish 0.0541

## this: what pacing alone does

| Project | Back to back: plain tick (us) | Paced: plain tick (us) | Ratio |
|---|---|---|---|
| sailing | 66.5 | 273.3 | 4.11x |
| sailing-course | 85.5 | 339.3 | 3.97x |

sailing: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0009 | 9.00x |
| script:log | 0.0185 | 0.1089 | 5.89x |
| script:take_aboard | 0.0136 | 0.0381 | 2.80x |
| script.update | 0.0003 | 0.0056 | 18.67x |
| physics.wind | 0.0011 | 0.0097 | 8.82x |
| physics.buoyancy | 0.0172 | 0.0330 | 1.92x |
| physics.sail | 0.0010 | 0.0038 | 3.80x |
| physics.hull | 0.0015 | 0.0048 | 3.20x |
| physics.step | 0.0118 | 0.0645 | 5.47x |
| physics.contacts | 0.0001 | 0.0005 | 5.00x |
| interface.perception | 0.0001 | 0.0014 | 14.00x |
| sim.finish | 0.0002 | 0.0011 | 5.50x |
| tick.other | 0.0010 | 0.0128 | 12.80x |
| loop.publish | 0.0001 | 0.0001 | 1.00x |
| loop.after | 0.0001 | 0.0006 | 6.00x |

sailing-course: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0010 | 10.00x |
| interface.intents | 0.0005 | 0.0103 | 20.60x |
| script:take_aboard | 0.0154 | 0.0954 | 6.19x |
| script:rounding | 0.0219 | 0.0581 | 2.65x |
| script.update | 0.0004 | 0.0041 | 10.25x |
| physics.wind | 0.0013 | 0.0098 | 7.54x |
| physics.buoyancy | 0.0177 | 0.0329 | 1.86x |
| physics.sail | 0.0009 | 0.0031 | 3.44x |
| physics.hull | 0.0016 | 0.0048 | 3.00x |
| physics.step | 0.0137 | 0.0650 | 4.74x |
| physics.contacts | 0.0001 | 0.0004 | 4.00x |
| interface.perception | 0.0110 | 0.0497 | 4.52x |
| interface.turns | 0.0002 | 0.0026 | 13.00x |
| assets.animate | 0.0001 | 0.0008 | 8.00x |
| sim.finish | 0.0002 | 0.0010 | 5.00x |
| tick.other | 0.0011 | 0.0119 | 10.82x |
| loop.publish | 0.0001 | 0.0001 | 1.00x |
| loop.after | 0.0001 | 0.0006 | 6.00x |

