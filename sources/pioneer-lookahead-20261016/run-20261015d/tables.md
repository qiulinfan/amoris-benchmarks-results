
Fork costs: samples/sailing-course, seed 0, greedy skipper, tick 300, 14 entities, snapshot 66,405 bytes; 3 runs, median of the runs' medians (minimum to maximum)

| Operation | Wall time, us | Bytes allocated (median call) | Bytes held after the call (median) |
|---|---|---|---|
| snapshot | 82.8 (79.9 to 88.5) | 241,134 | 70,908 |
| restore into a kept branch | 188.5 (183.1 to 193.0) | 332,229 | 0 |
| fork into a kept branch (`fork_into`) | 252.7 (247.2 to 266.2) | 576,977 | 0 |
| fresh branch (`Game::fork`) | 21,060.7 (21,036.8 to 21,489.2) | 19,892,062 | 1,735,111 |
| dropping a fresh branch | 767.9 (695.5 to 769.5) | | |

A live fresh branch holds 1,735,063 bytes of Rust heap and 305,678 bytes of script heap (main's: 305,678); a branch tick takes 108.8 us (108.1 to 109.7).

CPU load at the start of each timed command (machine_conditions.py, inside the hold): fork 8 to 14%
