| Build | Clients | Plays | busy_ms | tick_ms | loop.publish | loop.present | loop.after | script:log | physics.step | /render frames/s (each play) |
|---|---|---|---|---|---|---|---|---|---|---|
| base | none | 3 | 0.421 | 0.251 | 0.1379 | 0.0309 | 0.0011 | 0.0918 | 0.0583 |  |
| base | sockets | 3 | 0.434 | 0.258 | 0.1433 | 0.0324 | 0.0011 | 0.0941 | 0.0614 | 55.0 (55.0, 54.4, 56.2) |
| base | editor | 3 | 0.632 | 0.382 | 0.2005 | 0.0468 | 0.0016 | 0.1470 | 0.0951 |  |
| new | none | 3 | 0.354 | 0.263 | 0.0803 | 0.0092 | 0.0009 | 0.0951 | 0.0632 |  |
| new | sockets | 3 | 0.364 | 0.265 | 0.0892 | 0.0093 | 0.0009 | 0.0971 | 0.0616 | 60.0 (60.0, 60.0, 60.0) |
| new | editor | 3 | 0.541 | 0.389 | 0.1361 | 0.0158 | 0.0014 | 0.1475 | 0.0954 |  |

Idle, every try: % of one core by cycles (by CPU time); median by cycles

| Build | Clients | Tries | Median | /render messages/s |
|---|---|---|---|---|
| base | none | 0.447 (0.36), 0.456 (0.52) | 0.452 | 0.0 |
| base | sockets | 0.842 (0.42), 0.856 (0.94) | 0.849 | 0.0 |
| new | none | 0.243 (0.16), 0.245 (0.05) | 0.244 | 0.0 |
| new | sockets | 0.302 (0.31), 0.301 (0.21) | 0.302 | 0.0 |
