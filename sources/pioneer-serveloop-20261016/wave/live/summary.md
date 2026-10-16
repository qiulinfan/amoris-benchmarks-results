| Build | Clients | Plays | busy_ms | tick_ms | loop.publish | loop.present | loop.after | script:log | physics.step |
|---|---|---|---|---|---|---|---|---|---|
| base | none | 3 | 0.495 | 0.298 | 0.1589 | 0.0366 | 0.0013 | 0.1114 | 0.0747 |
| base | sockets | 3 | 0.547 | 0.328 | 0.1719 | 0.0408 | 0.0013 | 0.1241 | 0.0809 |
| base | editor | 3 | 0.631 | 0.380 | 0.2018 | 0.0481 | 0.0015 | 0.1463 | 0.0949 |
| new | none | 3 | 0.424 | 0.312 | 0.0982 | 0.0118 | 0.0010 | 0.1174 | 0.0775 |
| new | sockets | 3 | 0.374 | 0.269 | 0.0939 | 0.0098 | 0.0009 | 0.0982 | 0.0640 |
| new | editor | 3 | 0.537 | 0.384 | 0.1369 | 0.0154 | 0.0013 | 0.1474 | 0.0948 |

| Build | Idle, clients | CPU (% of one core) | /render messages/s |
|---|---|---|---|
| base | none | 0.39 | 0.0 |
| base | sockets | 0.55 | 0.0 |
| new | none | 0.31 | 0.0 |
| new | sockets | 0.16 | 0.0 |
