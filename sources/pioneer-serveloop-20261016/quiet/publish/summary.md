Paced every 16.667 ms, 1800 ticks a run, 5 runs: the median over the runs of each part's median (mean, p95) in us per tick

| Mode | step | streams | present | snapshot | publish | after_step |
|---|---|---|---|---|---|---|
| full | 267.2 (275.0, 358.0) | 0.5 (0.6, 0.9) | 9.7 (10.0, 13.2) | 141.6 (147.5, 194.5) | 5.0 (5.3, 7.3) | 157.2 (163.5, 216.7) |
| cached | 270.9 (276.9, 361.8) | 0.5 (0.6, 0.8) | 10.0 (10.4, 14.2) | 72.8 (75.7, 105.6) | 4.4 (4.6, 6.1) | 88.2 (91.0, 126.4) |
| base | 265.7 (272.8, 358.7) | 0.6 (0.7, 1.0) | 32.4 (33.5, 44.2) | 132.2 (136.3, 181.3) | 5.1 (5.3, 7.2) | 171.0 (175.8, 230.2) |

Sections changed per tick (ticks of the last run whose digest changed): cache:physics.rapier 1800, component:Boat 1800, component:Floater 1800, component:Log 1800, component:Transform 1800, component:Velocity 1800, resource:EventCounter 1, resource:EventInbox 2, resource:SimClock 1800

Anatomy (back to back, last run): {"hashing": 0.98, "registry_checks": 0.48, "section_digests": 39.19, "snapshot": 41.94}
