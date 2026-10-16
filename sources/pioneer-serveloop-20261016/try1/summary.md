| Build | Clients | Plays | busy_ms | tick_ms | loop.publish | loop.present | loop.after | script:log | physics.step |
|---|---|---|---|---|---|---|---|---|---|
| base | none | 1 | 0.628 | 0.373 | 0.2052 | 0.0475 | 0.0018 | 0.1416 | 0.0985 |
| base | sockets | 1 | 0.627 | 0.375 | 0.2024 | 0.0477 | 0.0016 | 0.1410 | 0.0963 |
| base | editor | 1 | 0.808 | 0.484 | 0.2604 | 0.0618 | 0.0022 | 0.1897 | 0.1227 |
| base | editor-dgpu | 1 | 1.040 | 0.676 | 0.2960 | 0.0652 | 0.0027 | 0.2735 | 0.1678 |

| Build | Idle, clients | CPU (% of one core) | /render messages/s |
|---|---|---|---|
| base | none | 0.00 | 0.0 |
| base | sockets | 1.09 | 0.0 |
