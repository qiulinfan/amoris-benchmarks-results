Paced every 16.667 ms, 1800 ticks a run, 3 runs: the median over the runs of each part's median (mean, p95) in us per tick

| Mode | step | streams | present | snapshot | publish | after_step |
|---|---|---|---|---|---|---|
| full | 353.4 (355.7, 454.4) | 0.7 (0.8, 1.2) | 13.2 (13.6, 17.4) | 201.8 (199.5, 258.3) | 6.7 (7.0, 9.7) | 222.6 (220.9, 287.1) |
| cached | 343.1 (344.6, 444.6) | 0.7 (0.7, 1.1) | 12.7 (13.1, 17.2) | 92.8 (94.2, 125.9) | 5.2 (5.4, 7.2) | 111.9 (113.4, 150.9) |
| base | 340.6 (349.6, 454.4) | 0.8 (0.8, 1.3) | 44.9 (45.1, 59.5) | 181.7 (182.7, 253.9) | 6.4 (7.0, 9.2) | 234.1 (234.6, 325.4) |

Sections changed per tick (ticks of the last run whose digest changed): cache:physics.rapier 1800, component:Boat 1800, component:Floater 1800, component:Log 1800, component:Transform 1800, component:Velocity 1800, resource:EventCounter 1, resource:EventInbox 2, resource:SimClock 1800

Anatomy (back to back, last run): {"hashing": 1.5, "registry_checks": 0.72, "section_digests": 66.24, "snapshot": 91.94}
