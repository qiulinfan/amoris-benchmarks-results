## this, back to back

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 1 | 68.0 / 72.5 (+6.58 %) | +6.58 % | +6.58 | +6.58 % | +6.58 | +4.47 | 31.9 | 36.0 |
| sailing-course | 1 | 105.3 / 91.1 (-13.45 %) | -13.45 % | -13.45 | -13.45 % | -13.45 | -14.15 | 32.4 | 36.0 |

sailing, back to back, last run (500 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0006 |
| interface.intents | 0.0000 | 0.0004 |
| script:log | 0.0212 | 0.1340 |
| script:take_aboard | 0.0151 | 0.0531 |
| script.update | 0.0004 | 0.0025 |
| physics.wind | 0.0013 | 0.0057 |
| physics.buoyancy | 0.0160 | 0.0438 |
| physics.sail | 0.0011 | 0.0043 |
| physics.hull | 0.0016 | 0.0052 |
| physics.step | 0.0134 | 0.0462 |
| physics.contacts | 0.0001 | 0.0004 |
| interface.perception | 0.0001 | 0.0008 |
| interface.turns | 0.0000 | 0.0002 |
| assets.animate | 0.0001 | 0.0009 |
| sim.finish | 0.0002 | 0.0010 |
| tick.other | 0.0015 | 0.0146 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0003 |
| loop.after | 0.0002 | 0.0050 |
| tick | 0.0721 | 0.2885 |

Phases (ms per tick): Begin 0.0001, Control 0.0000, Update 0.0366, Forces 0.0199, Physics 0.0135, Finish 0.0004

sailing-course, back to back, last run (500 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0001 | 0.0007 |
| interface.intents | 0.0006 | 0.0074 |
| script:take_aboard | 0.0166 | 0.0533 |
| script:rounding | 0.0231 | 0.0605 |
| script.update | 0.0004 | 0.0016 |
| physics.wind | 0.0014 | 0.0063 |
| physics.buoyancy | 0.0179 | 0.0350 |
| physics.sail | 0.0008 | 0.0036 |
| physics.hull | 0.0016 | 0.0050 |
| physics.step | 0.0145 | 0.0338 |
| physics.contacts | 0.0001 | 0.0005 |
| interface.perception | 0.0117 | 0.0341 |
| interface.turns | 0.0003 | 0.0021 |
| assets.animate | 0.0001 | 0.0006 |
| sim.finish | 0.0002 | 0.0008 |
| tick.other | 0.0014 | 0.0042 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0001 | 0.0003 |
| loop.after | 0.0002 | 0.0043 |
| tick | 0.0907 | 0.1851 |

Phases (ms per tick): Begin 0.0001, Control 0.0006, Update 0.0402, Forces 0.0217, Physics 0.0146, Finish 0.0123

## this, paced 16.6667 ms

| Project | Runs | Run with the median overhead: without / with (us/tick) | Overhead (mean of blocks): median of runs | per run | Overhead (median block): median of runs | per run | With - without (us/tick), median of runs | Clock reading (ns) | Readings per tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 1 | 267.8 / 290.6 (+8.51 %) | +8.51 % | +8.51 | +8.51 % | +8.51 | +22.79 | 32.0 | 36.0 |
| sailing-course | 1 | 336.1 / 313.6 (-6.69 %) | -6.69 % | -6.69 | -6.69 % | -6.69 | -22.49 | 31.7 | 36.0 |

sailing, paced 16.6667 ms, last run (200 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0010 | 0.0243 |
| interface.intents | 0.0010 | 0.0018 |
| script:log | 0.1105 | 0.1653 |
| script:take_aboard | 0.0360 | 0.0522 |
| script.update | 0.0058 | 0.0219 |
| physics.wind | 0.0099 | 0.0179 |
| physics.buoyancy | 0.0292 | 0.0397 |
| physics.sail | 0.0036 | 0.0066 |
| physics.hull | 0.0048 | 0.0087 |
| physics.step | 0.0678 | 0.0973 |
| physics.contacts | 0.0006 | 0.0011 |
| interface.perception | 0.0014 | 0.0025 |
| interface.turns | 0.0005 | 0.0008 |
| assets.animate | 0.0010 | 0.0019 |
| sim.finish | 0.0012 | 0.0250 |
| tick.other | 0.0148 | 0.0290 |
| loop.present | 0.0000 | 0.0001 |
| loop.publish | 0.0002 | 0.0005 |
| loop.after | 0.0007 | 0.0081 |
| tick | 0.2887 | 0.3863 |

Phases (ms per tick): Begin 0.0010, Control 0.0010, Update 0.1523, Forces 0.0473, Physics 0.0683, Finish 0.0042

sailing-course, paced 16.6667 ms, last run (200 profiled ticks): ms per tick

| Row | ms | max ms |
|---|---|---|
| sim.begin | 0.0007 | 0.0018 |
| interface.intents | 0.0079 | 0.0351 |
| script:take_aboard | 0.0875 | 0.1572 |
| script:rounding | 0.0538 | 0.1159 |
| script.update | 0.0033 | 0.0091 |
| physics.wind | 0.0079 | 0.0162 |
| physics.buoyancy | 0.0315 | 0.0508 |
| physics.sail | 0.0027 | 0.0049 |
| physics.hull | 0.0049 | 0.0079 |
| physics.step | 0.0565 | 0.0964 |
| physics.contacts | 0.0004 | 0.0013 |
| interface.perception | 0.0411 | 0.0650 |
| interface.turns | 0.0021 | 0.0052 |
| assets.animate | 0.0008 | 0.0020 |
| sim.finish | 0.0008 | 0.0028 |
| tick.other | 0.0105 | 0.0189 |
| loop.present | 0.0001 | 0.0001 |
| loop.publish | 0.0001 | 0.0007 |
| loop.after | 0.0006 | 0.0069 |
| tick | 0.3122 | 0.4654 |

Phases (ms per tick): Begin 0.0007, Control 0.0079, Update 0.1446, Forces 0.0469, Physics 0.0569, Finish 0.0448

## this: what pacing alone does

| Project | Back to back: plain tick (us) | Paced: plain tick (us) | Ratio |
|---|---|---|---|
| sailing | 68.0 | 267.8 | 3.94x |
| sailing-course | 105.3 | 336.1 | 3.19x |

sailing: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0010 | 10.00x |
| script:log | 0.0212 | 0.1105 | 5.21x |
| script:take_aboard | 0.0151 | 0.0360 | 2.38x |
| script.update | 0.0004 | 0.0058 | 14.50x |
| physics.wind | 0.0013 | 0.0099 | 7.62x |
| physics.buoyancy | 0.0160 | 0.0292 | 1.82x |
| physics.sail | 0.0011 | 0.0036 | 3.27x |
| physics.hull | 0.0016 | 0.0048 | 3.00x |
| physics.step | 0.0134 | 0.0678 | 5.06x |
| physics.contacts | 0.0001 | 0.0006 | 6.00x |
| interface.perception | 0.0001 | 0.0014 | 14.00x |
| assets.animate | 0.0001 | 0.0010 | 10.00x |
| sim.finish | 0.0002 | 0.0012 | 6.00x |
| tick.other | 0.0015 | 0.0148 | 9.87x |
| loop.publish | 0.0001 | 0.0002 | 2.00x |
| loop.after | 0.0002 | 0.0007 | 3.50x |

sailing-course: paced / back to back, per row (profiled ticks)

| Row | Back to back (ms) | Paced (ms) | Ratio |
|---|---|---|---|
| sim.begin | 0.0001 | 0.0007 | 7.00x |
| interface.intents | 0.0006 | 0.0079 | 13.17x |
| script:take_aboard | 0.0166 | 0.0875 | 5.27x |
| script:rounding | 0.0231 | 0.0538 | 2.33x |
| script.update | 0.0004 | 0.0033 | 8.25x |
| physics.wind | 0.0014 | 0.0079 | 5.64x |
| physics.buoyancy | 0.0179 | 0.0315 | 1.76x |
| physics.sail | 0.0008 | 0.0027 | 3.38x |
| physics.hull | 0.0016 | 0.0049 | 3.06x |
| physics.step | 0.0145 | 0.0565 | 3.90x |
| physics.contacts | 0.0001 | 0.0004 | 4.00x |
| interface.perception | 0.0117 | 0.0411 | 3.51x |
| interface.turns | 0.0003 | 0.0021 | 7.00x |
| assets.animate | 0.0001 | 0.0008 | 8.00x |
| sim.finish | 0.0002 | 0.0008 | 4.00x |
| tick.other | 0.0014 | 0.0105 | 7.50x |
| loop.publish | 0.0001 | 0.0001 | 1.00x |
| loop.after | 0.0002 | 0.0006 | 3.00x |

