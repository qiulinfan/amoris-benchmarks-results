Paced every 16.667 ms, 1800 ticks a run, 3 runs: the median over the runs of each part's median (mean, p95) in us per tick

| Mode | step | streams | present | snapshot | publish | after_step |
|---|---|---|---|---|---|---|
| full | 243.7 (250.5, 335.4) | 0.5 (0.5, 0.8) | 8.2 (8.8, 12.4) | 130.1 (135.7, 177.0) | 4.8 (5.1, 7.0) | 143.8 (150.0, 196.5) |
| cached | 247.5 (254.6, 343.1) | 0.5 (0.5, 0.8) | 8.2 (8.8, 12.4) | 67.0 (69.5, 93.1) | 4.0 (4.2, 5.7) | 79.7 (82.9, 110.4) |
| base | 248.7 (255.9, 340.1) | 0.5 (0.5, 0.9) | 29.6 (30.6, 40.1) | 122.4 (126.7, 163.7) | 4.7 (5.0, 6.7) | 156.6 (162.0, 211.1) |

Sections changed per tick (ticks of the last run whose digest changed): cache:physics.rapier 1800, component:Boat 1800, component:Floater 1800, component:Log 1800, component:Transform 1800, component:Velocity 1800, resource:EventCounter 1, resource:EventInbox 2, resource:SimClock 1800

Anatomy (back to back, last run): {"hashing": 0.99, "registry_checks": 0.48, "section_digests": 42.24, "snapshot": 49.97}
