## this

| Project | Runs | Without hooks (us/tick) | With hooks (us/tick) | Overhead (median of runs) | Overhead per run | Clock reading (ns) | Readings per tick | Tick (ms) | Systems' share of the tick |
|---|---|---|---|---|---|---|---|---|---|
| sailing | 3 | 70.3 | 73.0 | +4.32% | +2.61%, +4.32%, +4.91% | 31.4 | 32.0 | 0.0737 | 98% |
| sailing-course | 3 | 87.9 | 89.8 | +1.37% | +1.37%, +0.35%, +2.14% | 31.8 | 32.0 | 0.0896 | 99% |

sailing, last run (3000 profiled ticks): ms per tick

| System | ms | max ms |
|---|---|---|
| script:log | 0.0205 | 0.0835 |
| physics.buoyancy | 0.0185 | 0.0589 |
| script:take_aboard | 0.0146 | 0.0960 |
| physics.step | 0.0137 | 0.0750 |
| physics.hull | 0.0017 | 0.0104 |
| physics.wind | 0.0013 | 0.0146 |
| tick.other | 0.0012 | 0.0185 |
| physics.sail | 0.0011 | 0.0188 |
| script.update | 0.0004 | 0.0072 |
| sim.finish | 0.0002 | 0.0033 |
| sim.begin | 0.0001 | 0.0006 |
| physics.contacts | 0.0001 | 0.0009 |
| interface.perception | 0.0001 | 0.0108 |
| assets.animate | 0.0001 | 0.0013 |
| interface.intents | 0.0000 | 0.0008 |
| interface.turns | 0.0000 | 0.0036 |
| loop.present | 0.0000 | 0.0000 |
| loop.publish | 0.0000 | 0.0000 |

Phases (ms per tick): Begin 0.0001, Control 0.0000, Update 0.0355, Forces 0.0226, Physics 0.0138, Finish 0.0004

sailing-course, last run (3000 profiled ticks): ms per tick

| System | ms | max ms |
|---|---|---|
| script:rounding | 0.0225 | 0.0564 |
| physics.buoyancy | 0.0186 | 0.0414 |
| script:take_aboard | 0.0161 | 0.0642 |
| physics.step | 0.0142 | 0.0618 |
| interface.perception | 0.0112 | 0.0441 |
| physics.hull | 0.0017 | 0.0107 |
| physics.wind | 0.0015 | 0.0098 |
| tick.other | 0.0012 | 0.0062 |
| physics.sail | 0.0009 | 0.0070 |
| interface.intents | 0.0006 | 0.0078 |
| script.update | 0.0004 | 0.0044 |
| interface.turns | 0.0003 | 0.0034 |
| sim.finish | 0.0002 | 0.0030 |
| sim.begin | 0.0001 | 0.0010 |
| physics.contacts | 0.0001 | 0.0012 |
| assets.animate | 0.0001 | 0.0046 |
| loop.present | 0.0000 | 0.0000 |
| loop.publish | 0.0000 | 0.0000 |

Phases (ms per tick): Begin 0.0001, Control 0.0006, Update 0.0390, Forces 0.0226, Physics 0.0143, Finish 0.0118
