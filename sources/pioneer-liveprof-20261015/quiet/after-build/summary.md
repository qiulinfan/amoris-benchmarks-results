## this, back to back

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 5 | 70.8 / 72.2 (+2.02 %) | +2.02 % | +2.02, +3.27, +2.85, +1.49, +1.91 | +1.55 % | +1.19, +3.15, +3.00, +1.55, +1.53 | +1.43 | 31.2 | 36.0 |
| sailing-course | 5 | 85.3 / 87.7 (+2.79 %) | +2.79 % | +2.05, +2.96, +4.26, +1.98, +2.79 | +2.43 % | +2.43, +2.43, +3.19, +1.74, +2.13 | +2.38 | 31.4 | 36.0 |

sailing, back to back, last run (3000 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0007 |
| interface.intents | 0.0000 | 0.0067 |
| script:log | 0.0187 | 0.0526 |
| script:take_aboard | 0.0138 | 0.0369 |
| script.update | 0.0003 | 0.0038 |
| physics.wind | 0.0012 | 0.0061 |
| physics.buoyancy | 0.0174 | 0.0297 |
| physics.sail | 0.0011 | 0.0030 |
| physics.hull | 0.0015 | 0.0260 |
| physics.step | 0.0122 | 0.0504 |
| physics.contacts | 0.0001 | 0.0007 |
| interface.perception | 0.0001 | 0.0007 |
| interface.turns | 0.0000 | 0.0003 |
| assets.animate | 0.0001 | 0.0004 |
| sim.finish | 0.0002 | 0.0009 |
| tick.other | 0.0010 | 0.0231 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0003 |
| loop.after | 0.0001 | 0.0060 |
| tick | 0.0679 | 0.1499 |

Phases (ms per tick): Begin 0.0001, Control 0.0000, Update 0.0328, Forces 0.0212, Physics 0.0123, Finish 0.0004

sailing-course, back to back, last run (3000 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0006 |
| interface.intents | 0.0005 | 0.0136 |
| script:take_aboard | 0.0157 | 0.0790 |
| script:rounding | 0.0223 | 0.1213 |
| script.update | 0.0004 | 0.0356 |
| physics.wind | 0.0013 | 0.0078 |
| physics.buoyancy | 0.0180 | 0.0400 |
| physics.sail | 0.0008 | 0.0067 |
| physics.hull | 0.0016 | 0.0069 |
| physics.step | 0.0136 | 0.0546 |
| physics.contacts | 0.0001 | 0.0007 |
| interface.perception | 0.0111 | 0.0526 |
| interface.turns | 0.0003 | 0.0020 |
| assets.animate | 0.0001 | 0.0006 |
| sim.finish | 0.0002 | 0.0018 |
| tick.other | 0.0011 | 0.0209 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0006 |
| loop.after | 0.0001 | 0.0064 |
| tick | 0.0873 | 0.3332 |

Phases (ms per tick): Begin 0.0001, Control 0.0005, Update 0.0384, Forces 0.0217, Physics 0.0137, Finish 0.0116

## this, paced 16.6667 ms

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 5 | 275.7 / 281.1 (+1.96 %) | +1.96 % | +4.29, +2.29, +1.84, +1.59, +1.96 | +1.21 % | +2.71, -1.24, +0.99, +1.57, +1.21 | +5.41 | 31.4 | 36.0 |
| sailing-course | 5 | 338.9 / 346.0 (+2.09 %) | +2.09 % | +1.05, +1.38, +3.45, +2.09, +3.35 | +2.58 % | +1.71, +2.61, +2.71, +1.83, +2.58 | +7.09 | 31.6 | 36.0 |

sailing, paced 16.6667 ms, last run (1800 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0010 | 0.0370 |
| interface.intents | 0.0008 | 0.0125 |
| script:log | 0.1051 | 0.2780 |
| script:take_aboard | 0.0370 | 0.2647 |
| script.update | 0.0052 | 0.0392 |
| physics.wind | 0.0092 | 0.0392 |
| physics.buoyancy | 0.0327 | 0.0697 |
| physics.sail | 0.0036 | 0.0089 |
| physics.hull | 0.0047 | 0.1761 |
| physics.step | 0.0637 | 0.1376 |
| physics.contacts | 0.0005 | 0.0020 |
| interface.perception | 0.0013 | 0.0037 |
| interface.turns | 0.0006 | 0.0411 |
| assets.animate | 0.0008 | 0.0024 |
| sim.finish | 0.0010 | 0.0295 |
| tick.other | 0.0118 | 0.1692 |
| loop.present | 0.0000 | 0.0002 |
| loop.publish | 0.0001 | 0.0007 |
| loop.after | 0.0006 | 0.0128 |
| tick | 0.2789 | 0.6522 |

Phases (ms per tick): Begin 0.0010, Control 0.0008, Update 0.1473, Forces 0.0502, Physics 0.0641, Finish 0.0037

sailing-course, paced 16.6667 ms, last run (1800 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0012 | 0.1446 |
| interface.intents | 0.0101 | 0.0695 |
| script:take_aboard | 0.0956 | 0.2955 |
| script:rounding | 0.0598 | 0.1430 |
| script.update | 0.0040 | 0.0360 |
| physics.wind | 0.0097 | 0.0442 |
| physics.buoyancy | 0.0335 | 0.2829 |
| physics.sail | 0.0033 | 0.0353 |
| physics.hull | 0.0053 | 0.2339 |
| physics.step | 0.0651 | 0.1267 |
| physics.contacts | 0.0005 | 0.0028 |
| interface.perception | 0.0488 | 0.2696 |
| interface.turns | 0.0027 | 0.0237 |
| assets.animate | 0.0008 | 0.0025 |
| sim.finish | 0.0009 | 0.0111 |
| tick.other | 0.0122 | 0.0711 |
| loop.present | 0.0001 | 0.0001 |
| loop.publish | 0.0001 | 0.0009 |
| loop.after | 0.0006 | 0.0115 |
| tick | 0.3533 | 0.9382 |

Phases (ms per tick): Begin 0.0012, Control 0.0101, Update 0.1594, Forces 0.0518, Physics 0.0655, Finish 0.0532

## this: what pacing alone does

| Project | Back to back: plain tick (us) | Paced: plain tick (us) | Ratio |
|---|---|---|---|
| sailing | 68.0 | 290.2 | 4.27x |
| sailing-course | 86.9 | 349.6 | 4.03x |

sailing: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0010 | 10.00x |
| script:log | 0.0187 | 0.1051 | 5.62x |
| script:take_aboard | 0.0138 | 0.0370 | 2.68x |
| script.update | 0.0003 | 0.0052 | 17.33x |
| physics.wind | 0.0012 | 0.0092 | 7.67x |
| physics.buoyancy | 0.0174 | 0.0327 | 1.88x |
| physics.sail | 0.0011 | 0.0036 | 3.27x |
| physics.hull | 0.0015 | 0.0047 | 3.13x |
| physics.step | 0.0122 | 0.0637 | 5.22x |
| physics.contacts | 0.0001 | 0.0005 | 5.00x |
| interface.perception | 0.0001 | 0.0013 | 13.00x |
| assets.animate | 0.0001 | 0.0008 | 8.00x |
| sim.finish | 0.0002 | 0.0010 | 5.00x |
| tick.other | 0.0010 | 0.0118 | 11.80x |
| loop.publish | 0.0001 | 0.0001 | 1.00x |
| loop.after | 0.0001 | 0.0006 | 6.00x |

sailing-course: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0012 | 12.00x |
| interface.intents | 0.0005 | 0.0101 | 20.20x |
| script:take_aboard | 0.0157 | 0.0956 | 6.09x |
| script:rounding | 0.0223 | 0.0598 | 2.68x |
| script.update | 0.0004 | 0.0040 | 10.00x |
| physics.wind | 0.0013 | 0.0097 | 7.46x |
| physics.buoyancy | 0.0180 | 0.0335 | 1.86x |
| physics.sail | 0.0008 | 0.0033 | 4.12x |
| physics.hull | 0.0016 | 0.0053 | 3.31x |
| physics.step | 0.0136 | 0.0651 | 4.79x |
| physics.contacts | 0.0001 | 0.0005 | 5.00x |
| interface.perception | 0.0111 | 0.0488 | 4.40x |
| interface.turns | 0.0003 | 0.0027 | 9.00x |
| assets.animate | 0.0001 | 0.0008 | 8.00x |
| sim.finish | 0.0002 | 0.0009 | 4.50x |
| tick.other | 0.0011 | 0.0122 | 11.09x |
| loop.publish | 0.0001 | 0.0001 | 1.00x |
| loop.after | 0.0001 | 0.0006 | 6.00x |

