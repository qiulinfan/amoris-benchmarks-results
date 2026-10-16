## this, back to back

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 3 | 67.6 / 68.8 (+1.88 %) | +1.88 % | +1.76, +1.88, +5.52 | +3.22 % | +3.22, +2.75, +6.89 | +1.33 | 32.4 | 36.0 |
| sailing-course | 3 | 85.7 / 87.3 (+1.85 %) | +1.85 % | +2.77, +1.71, +1.85 | +2.11 % | +2.11, +2.63, +1.57 | +1.59 | 31.2 | 36.0 |

sailing, back to back, last run (3000 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0002 | 0.0013 |
| interface.intents | 0.0001 | 0.0011 |
| script:log | 0.0221 | 0.1039 |
| script:take_aboard | 0.0157 | 0.1770 |
| script.update | 0.0005 | 0.0137 |
| physics.wind | 0.0015 | 0.0297 |
| physics.buoyancy | 0.0184 | 0.0876 |
| physics.sail | 0.0012 | 0.0116 |
| physics.hull | 0.0017 | 0.0118 |
| physics.step | 0.0147 | 0.1236 |
| physics.contacts | 0.0001 | 0.0012 |
| interface.perception | 0.0001 | 0.0021 |
| interface.turns | 0.0001 | 0.0009 |
| assets.animate | 0.0001 | 0.0011 |
| sim.finish | 0.0003 | 0.0179 |
| tick.other | 0.0014 | 0.0383 |
| loop.present | 0.0000 | 0.0013 |
| loop.publish | 0.0001 | 0.0004 |
| loop.after | 0.0002 | 0.0089 |
| tick | 0.0779 | 0.2537 |

Phases (ms per tick): Begin 0.0002, Control 0.0001, Update 0.0383, Forces 0.0227, Physics 0.0148, Finish 0.0005

sailing-course, back to back, last run (3000 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0010 |
| interface.intents | 0.0006 | 0.0098 |
| script:take_aboard | 0.0157 | 0.0628 |
| script:rounding | 0.0221 | 0.0560 |
| script.update | 0.0004 | 0.0023 |
| physics.wind | 0.0013 | 0.0099 |
| physics.buoyancy | 0.0179 | 0.0706 |
| physics.sail | 0.0009 | 0.0070 |
| physics.hull | 0.0016 | 0.0137 |
| physics.step | 0.0136 | 0.0469 |
| physics.contacts | 0.0001 | 0.0005 |
| interface.perception | 0.0109 | 0.0419 |
| interface.turns | 0.0003 | 0.0049 |
| assets.animate | 0.0001 | 0.0006 |
| sim.finish | 0.0002 | 0.0022 |
| tick.other | 0.0011 | 0.0064 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0004 |
| loop.after | 0.0001 | 0.0182 |
| tick | 0.0868 | 0.1857 |

Phases (ms per tick): Begin 0.0001, Control 0.0006, Update 0.0382, Forces 0.0217, Physics 0.0137, Finish 0.0115

## this, paced 16.6667 ms

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 3 | 260.1 / 258.4 (-0.66 %) | -0.66 % | -0.66, -1.80, +2.66 | -0.95 % | -0.95, -7.61, +2.63 | -1.72 | 32.4 | 36.0 |
| sailing-course | 3 | 324.6 / 329.2 (+1.43 %) | +1.43 % | +1.43, -0.08, +2.74 | -0.36 % | -1.39, -0.36, +2.54 | +4.64 | 31.4 | 36.0 |

sailing, paced 16.6667 ms, last run (1800 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0007 | 0.0275 |
| interface.intents | 0.0010 | 0.0513 |
| script:log | 0.0984 | 0.2249 |
| script:take_aboard | 0.0352 | 0.2169 |
| script.update | 0.0047 | 0.0695 |
| physics.wind | 0.0085 | 0.0414 |
| physics.buoyancy | 0.0327 | 0.1909 |
| physics.sail | 0.0033 | 0.0230 |
| physics.hull | 0.0047 | 0.0108 |
| physics.step | 0.0589 | 0.4844 |
| physics.contacts | 0.0005 | 0.0014 |
| interface.perception | 0.0012 | 0.0176 |
| interface.turns | 0.0004 | 0.0015 |
| assets.animate | 0.0009 | 0.0029 |
| sim.finish | 0.0010 | 0.0045 |
| tick.other | 0.0108 | 0.0435 |
| loop.present | 0.0001 | 0.0001 |
| loop.publish | 0.0002 | 0.0006 |
| loop.after | 0.0006 | 0.0097 |
| tick | 0.2630 | 0.8791 |

Phases (ms per tick): Begin 0.0007, Control 0.0010, Update 0.1383, Forces 0.0491, Physics 0.0595, Finish 0.0035

sailing-course, paced 16.6667 ms, last run (1800 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0009 | 0.0222 |
| interface.intents | 0.0102 | 0.0745 |
| script:take_aboard | 0.0937 | 0.3568 |
| script:rounding | 0.0562 | 0.2994 |
| script.update | 0.0039 | 0.0130 |
| physics.wind | 0.0095 | 0.0219 |
| physics.buoyancy | 0.0328 | 0.0674 |
| physics.sail | 0.0028 | 0.0354 |
| physics.hull | 0.0050 | 0.0246 |
| physics.step | 0.0645 | 0.2954 |
| physics.contacts | 0.0006 | 0.0019 |
| interface.perception | 0.0479 | 0.0944 |
| interface.turns | 0.0026 | 0.0456 |
| assets.animate | 0.0010 | 0.0093 |
| sim.finish | 0.0009 | 0.0037 |
| tick.other | 0.0119 | 0.0609 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0002 | 0.0009 |
| loop.after | 0.0006 | 0.0089 |
| tick | 0.3441 | 0.6996 |

Phases (ms per tick): Begin 0.0009, Control 0.0102, Update 0.1537, Forces 0.0500, Physics 0.0650, Finish 0.0525

## this: what pacing alone does

| Project | Back to back: plain tick (us) | Paced: plain tick (us) | Ratio |
|---|---|---|---|
| sailing | 74.3 | 260.1 | 3.50x |
| sailing-course | 87.0 | 336.8 | 3.87x |

sailing: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0002 | 0.0007 | 3.50x |
| interface.intents | 0.0001 | 0.0010 | 10.00x |
| script:log | 0.0221 | 0.0984 | 4.45x |
| script:take_aboard | 0.0157 | 0.0352 | 2.24x |
| script.update | 0.0005 | 0.0047 | 9.40x |
| physics.wind | 0.0015 | 0.0085 | 5.67x |
| physics.buoyancy | 0.0184 | 0.0327 | 1.78x |
| physics.sail | 0.0012 | 0.0033 | 2.75x |
| physics.hull | 0.0017 | 0.0047 | 2.76x |
| physics.step | 0.0147 | 0.0589 | 4.01x |
| physics.contacts | 0.0001 | 0.0005 | 5.00x |
| interface.perception | 0.0001 | 0.0012 | 12.00x |
| interface.turns | 0.0001 | 0.0004 | 4.00x |
| assets.animate | 0.0001 | 0.0009 | 9.00x |
| sim.finish | 0.0003 | 0.0010 | 3.33x |
| tick.other | 0.0014 | 0.0108 | 7.71x |
| loop.publish | 0.0001 | 0.0002 | 2.00x |
| loop.after | 0.0002 | 0.0006 | 3.00x |

sailing-course: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0009 | 9.00x |
| interface.intents | 0.0006 | 0.0102 | 17.00x |
| script:take_aboard | 0.0157 | 0.0937 | 5.97x |
| script:rounding | 0.0221 | 0.0562 | 2.54x |
| script.update | 0.0004 | 0.0039 | 9.75x |
| physics.wind | 0.0013 | 0.0095 | 7.31x |
| physics.buoyancy | 0.0179 | 0.0328 | 1.83x |
| physics.sail | 0.0009 | 0.0028 | 3.11x |
| physics.hull | 0.0016 | 0.0050 | 3.12x |
| physics.step | 0.0136 | 0.0645 | 4.74x |
| physics.contacts | 0.0001 | 0.0006 | 6.00x |
| interface.perception | 0.0109 | 0.0479 | 4.39x |
| interface.turns | 0.0003 | 0.0026 | 8.67x |
| assets.animate | 0.0001 | 0.0010 | 10.00x |
| sim.finish | 0.0002 | 0.0009 | 4.50x |
| tick.other | 0.0011 | 0.0119 | 10.82x |
| loop.publish | 0.0001 | 0.0002 | 2.00x |
| loop.after | 0.0001 | 0.0006 | 6.00x |

