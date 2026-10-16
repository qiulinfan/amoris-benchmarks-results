Paced every 16.667 ms, 1800 ticks a run, 3 runs: the median over the runs of each part's median (mean, p95) in us per tick

| Mode | step | streams | present | snapshot | publish | after_step |
|---|---|---|---|---|---|---|
| full | 331.6 (324.2, 384.1) | 0.7 (0.7, 1.1) | 12.2 (12.4, 15.8) | 169.2 (167.6, 208.0) | 2.1 (2.1, 2.6) | 184.5 (182.8, 227.3) |
| cached | 337.7 (341.7, 411.2) | 0.7 (0.8, 1.2) | 12.7 (13.4, 17.9) | 90.3 (93.9, 125.1) | 2.0 (2.1, 2.8) | 105.8 (110.2, 146.1) |
| base | 302.0 (304.6, 385.1) | 0.7 (0.7, 1.1) | 37.0 (36.6, 48.1) | 147.7 (147.5, 193.7) | 5.8 (5.9, 7.9) | 191.3 (190.6, 247.7) |

Sections changed per tick (ticks of the last run whose digest changed): cache:physics.rapier 1800, component:Boat 1800, component:Floater 1800, component:Log 1800, component:Transform 1800, component:Velocity 1800, resource:EventCounter 1, resource:EventInbox 2, resource:SimClock 1800

Anatomy (back to back, last run): {"hashing": 1.0, "registry_checks": 0.51, "section_digests": 39.32, "snapshot": 45.16}
