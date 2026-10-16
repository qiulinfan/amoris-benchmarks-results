Paced every 16.667 ms, 1800 ticks a run, 3 runs: the median over the runs of each part's median (mean, p95) in us per tick

| Mode | step | streams | present | snapshot | publish | after_step |
|---|---|---|---|---|---|---|
| full | 295.1 (293.8, 341.0) | 0.5 (0.5, 0.8) | 36.3 (36.4, 42.6) | 149.0 (148.3, 173.7) | 2.0 (2.0, 2.6) | 187.6 (186.6, 218.1) |
| cached | 304.9 (305.3, 349.8) | 0.5 (0.5, 0.8) | 37.5 (37.3, 42.9) | 78.4 (80.0, 101.3) | 2.0 (2.0, 2.5) | 118.8 (119.9, 145.1) |

Sections changed per tick (ticks of the last run whose digest changed): cache:physics.rapier 1800, component:Boat 1800, component:Floater 1800, component:Log 1800, component:Transform 1800, component:Velocity 1800, resource:EventCounter 1, resource:EventInbox 2, resource:SimClock 1800

Anatomy (back to back, last run): {"hashing": 1.0, "registry_checks": 0.5, "section_digests": 42.17, "snapshot": 44.79}
