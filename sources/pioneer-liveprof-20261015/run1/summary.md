## this

| Project | Runs | Without hooks (us/tick) | With hooks (us/tick) | Overhead (median of runs) | Overhead per run | Tick (ms) | Systems' share of the tick |
|---|---|---|---|---|---|---|---|
| sailing | 3 | 70.3 | 71.3 | +1.88% | +1.88%, +2.57%, +1.36% | 0.0711 | 98% |
| sailing-course | 3 | 88.8 | 91.3 | +1.82% | +1.45%, +3.81%, +1.82% | 0.0894 | 99% |

sailing, last run (3000 profiled ticks): ms per tick

| System | ms | max ms |
|---|---|---|
| script:log | 0.0198 | 0.0910 |
| physics.buoyancy | 0.0182 | 0.0324 |
| script:take_aboard | 0.0143 | 0.0342 |
| physics.step | 0.0128 | 0.0459 |
| physics.hull | 0.0016 | 0.0064 |
| physics.wind | 0.0012 | 0.0118 |
| physics.sail | 0.0011 | 0.0266 |
| tick.other | 0.0011 | 0.0165 |
| script.update | 0.0004 | 0.0017 |
| sim.finish | 0.0002 | 0.0016 |
| sim.begin | 0.0001 | 0.0007 |
| physics.contacts | 0.0001 | 0.0055 |
| interface.perception | 0.0001 | 0.0014 |
| assets.animate | 0.0001 | 0.0008 |
| interface.intents | 0.0000 | 0.0005 |
| interface.turns | 0.0000 | 0.0008 |
| loop.present | 0.0000 | 0.0000 |
| loop.publish | 0.0000 | 0.0000 |

Phases (ms per tick): Begin 0.0001, Control 0.0000, Update 0.0345, Forces 0.0221, Physics 0.0129, Finish 0.0004

sailing-course, last run (3000 profiled ticks): ms per tick

| System | ms | max ms |
|---|---|---|
| script:rounding | 0.0226 | 0.0564 |
| physics.buoyancy | 0.0182 | 0.0430 |
| script:take_aboard | 0.0162 | 0.0674 |
| physics.step | 0.0142 | 0.0539 |
| interface.perception | 0.0115 | 0.0494 |
| physics.hull | 0.0016 | 0.0069 |
| physics.wind | 0.0014 | 0.0120 |
| tick.other | 0.0011 | 0.0081 |
| physics.sail | 0.0009 | 0.0054 |
| interface.intents | 0.0005 | 0.0099 |
| script.update | 0.0004 | 0.0032 |
| interface.turns | 0.0003 | 0.0033 |
| sim.finish | 0.0002 | 0.0027 |
| sim.begin | 0.0001 | 0.0009 |
| physics.contacts | 0.0001 | 0.0039 |
| assets.animate | 0.0001 | 0.0014 |
| loop.present | 0.0000 | 0.0000 |
| loop.publish | 0.0000 | 0.0000 |

Phases (ms per tick): Begin 0.0001, Control 0.0005, Update 0.0392, Forces 0.0220, Physics 0.0143, Finish 0.0121

## v1

| Project | Runs | Without hooks (us/tick) | With hooks (us/tick) | Overhead (median of runs) | Overhead per run | Tick (ms) | Systems' share of the tick |
|---|---|---|---|---|---|---|---|
| sailing | 3 | 69.1 | 70.8 | +2.98% | +1.18%, +3.36%, +2.98% | 0.0709 | 98% |
| sailing-course | 3 | 87.0 | 89.1 | +2.41% | +1.56%, +3.18%, +2.41% | 0.0888 | 98% |

sailing, last run (3000 profiled ticks): ms per tick

| System | ms | max ms |
|---|---|---|
| script:log | 0.0197 | 0.1446 |
| physics.buoyancy | 0.0176 | 0.0484 |
| script:take_aboard | 0.0145 | 0.0349 |
| physics.step | 0.0127 | 0.0513 |
| tick.other | 0.0016 | 0.0188 |
| physics.hull | 0.0015 | 0.0079 |
| physics.wind | 0.0012 | 0.0094 |
| physics.sail | 0.0011 | 0.0055 |
| script.update | 0.0004 | 0.0042 |
| sim.finish | 0.0002 | 0.0078 |
| sim.begin | 0.0001 | 0.0009 |
| interface.intents | 0.0001 | 0.0006 |
| physics.contacts | 0.0001 | 0.0016 |
| interface.perception | 0.0001 | 0.0019 |
| assets.animate | 0.0001 | 0.0006 |
| interface.turns | 0.0000 | 0.0007 |
| loop.present | 0.0000 | 0.0000 |
| loop.publish | 0.0000 | 0.0000 |

Phases (ms per tick): Begin 0.0002, Control 0.0002, Update 0.0348, Forces 0.0217, Physics 0.0129, Finish 0.0006

sailing-course, last run (3000 profiled ticks): ms per tick

| System | ms | max ms |
|---|---|---|
| script:rounding | 0.0227 | 0.0698 |
| physics.buoyancy | 0.0181 | 0.0638 |
| script:take_aboard | 0.0159 | 0.0576 |
| physics.step | 0.0138 | 0.0547 |
| interface.perception | 0.0111 | 0.0456 |
| physics.hull | 0.0016 | 0.0082 |
| tick.other | 0.0016 | 0.0076 |
| physics.wind | 0.0013 | 0.0098 |
| physics.sail | 0.0009 | 0.0060 |
| interface.intents | 0.0005 | 0.0070 |
| script.update | 0.0005 | 0.0059 |
| interface.turns | 0.0002 | 0.0026 |
| sim.finish | 0.0002 | 0.0026 |
| sim.begin | 0.0001 | 0.0419 |
| physics.contacts | 0.0001 | 0.0008 |
| assets.animate | 0.0001 | 0.0010 |
| loop.present | 0.0000 | 0.0000 |
| loop.publish | 0.0000 | 0.0000 |

Phases (ms per tick): Begin 0.0002, Control 0.0006, Update 0.0392, Forces 0.0223, Physics 0.0140, Finish 0.0118
