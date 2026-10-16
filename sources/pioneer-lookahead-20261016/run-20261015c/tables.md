Course: seeds 0 to 30 (31 variants), models greedy, lookahead, nofork

| Condition | Model | Finished | Ticks to finish, mean (median) | Crates aboard, mean | Score, mean | Decisions, mean (median) | Forks, mean | Branch ticks, mean | Overrides, mean | Wall s, median |
|---|---|---|---|---|---|---|---|---|---|---|
| perception | greedy | 31/31 | 7,501 (6,881) | 1.87 | 5,630 | 110.0 (11) | | | | 0.90 |
| perception | lookahead | 31/31 | 6,671 (5,936) | 2.35 | 4,316 | 78.9 (12) | 24.0 | 4,703 | 1.6 | 1.53 |
| perception | nofork | 31/31 | 6,613 (6,513) | 3.16 | 3,452 | 40.5 (14) | 0.0 | 0 | 3.0 | 0.79 |
| omniscient | greedy | 31/31 | 6,461 (6,123) | 1.58 | 4,881 | 7.2 (6) | | | | 0.74 |
| omniscient | lookahead | 31/31 | 6,651 (5,921) | 2.26 | 4,393 | 75.5 (10) | 16.6 | 3,290 | 1.0 | 1.06 |
| omniscient | nofork | 31/31 | 6,706 (6,525) | 3.19 | 3,513 | 54.8 (10) | 0.0 | 0 | 2.3 | 0.75 |

Paired by variant (first model minus second):

| Condition | Pair | Score, mean (median) | Crates, mean | Ticks, mean (median) | Variants better / equal / worse | More / fewer crates | Faster / slower |
|---|---|---|---|---|---|---|---|
| perception | lookahead - greedy | -1,314 (-957) | +0.48 | -830 (-83) | 22 / 6 / 3 | 12 / 3 | 16 / 9 |
| omniscient | lookahead - greedy | -487 (-948) | +0.68 | +190 (+0) | 19 / 10 / 2 | 15 / 2 | 10 / 11 |
| perception | nofork - greedy | -2,178 (-1,501) | +1.29 | -888 (-135) | 29 / 0 / 2 | 23 / 3 | 16 / 15 |
| omniscient | nofork - greedy | -1,368 (-1,404) | +1.61 | +245 (+103) | 26 / 0 / 5 | 27 / 2 | 12 / 19 |
| perception | lookahead - nofork | +864 (+205) | -0.81 | +58 (-2) | 6 / 4 / 21 | 1 / 15 | 16 / 11 |
| omniscient | lookahead - nofork | +881 (+16) | -0.94 | -55 (-231) | 9 / 5 / 17 | 1 / 18 | 20 / 6 |

The crate's weight in the score (ticks a crate is worth; the bench and the lookahead's value use 1000): variants better / equal / worse

| Condition | Pair | 0 | 250 | 500 | 1000 | 2000 |
|---|---|---|---|---|---|---|
| perception | lookahead - greedy | 16 / 6 / 9 | 21 / 6 / 4 | 22 / 6 / 3 | 22 / 6 / 3 | 22 / 6 / 3 |
| omniscient | lookahead - greedy | 10 / 10 / 11 | 16 / 10 / 5 | 18 / 10 / 3 | 19 / 10 / 2 | 19 / 10 / 2 |
| perception | nofork - greedy | 16 / 0 / 15 | 20 / 0 / 11 | 26 / 0 / 5 | 29 / 0 / 2 | 28 / 0 / 3 |
| omniscient | nofork - greedy | 12 / 0 / 19 | 16 / 0 / 15 | 22 / 0 / 9 | 26 / 0 / 5 | 27 / 0 / 4 |
| perception | lookahead - nofork | 16 / 4 / 11 | 13 / 4 / 14 | 9 / 4 / 18 | 6 / 4 / 21 | 6 / 4 / 21 |
| omniscient | lookahead - nofork | 20 / 5 / 6 | 17 / 5 / 9 | 13 / 5 / 13 | 9 / 5 / 17 | 8 / 5 / 18 |

Without the variants where an episode livelocked aground (more than 300 decisions):

| Condition | Pair | Variants left (left out) | Score, mean (median) | Ticks, mean (median) |
|---|---|---|---|---|
| perception | lookahead - greedy | 29 (18, 28) | -1,001 (-913) | -484 (+0) |
| perception | nofork - greedy | 29 (18, 28) | -1,392 (-1,500) | -82 (+22) |
| perception | lookahead - nofork | 29 (18, 28) | +392 (+205) | -401 (-4) |
| omniscient | lookahead - greedy | 30 (18) | -1,113 (-969) | -447 (+0) |
| omniscient | nofork - greedy | 30 (18) | -1,511 (-1,450) | +89 (+97) |
| omniscient | lookahead - nofork | 30 (18) | +398 (+12) | -535 (-342) |

Cost of a weighed decision (wall time inside the model's decisions over the decisions that weighed candidates):

| Condition | Model | Weighed decisions | Wall ms a weighed decision | Forks a weighed decision | Branch ticks a weighed decision | Branch ticks / main ticks |
|---|---|---|---|---|---|---|
| perception | lookahead | 243 | 102.5 | 3.06 | 600 | 0.71 |
| perception | nofork | 253 | 0.1 | 0.00 | 0 | 0.00 |
| omniscient | lookahead | 170 | 146.1 | 3.03 | 600 | 0.49 |
| omniscient | nofork | 161 | 0.1 | 0.00 | 0 | 0.00 |

Branches charged for a land warning (2425 branches weighed, 0 refused their first act):

| Model | Condition | Plan | Branches charged |
|---|---|---|---|
| lookahead | omniscient | crate | 58 |
| lookahead | omniscient | greedy | 23 |
| lookahead | perception | crate | 10 |

Decisions whose choice the charge changed: 0

Omniscient minus perception, by model:

| Model | Score, mean | Crates, mean | Decisions, mean |
|---|---|---|---|
| greedy | -749 | -0.29 | -102.9 |
| lookahead | +77 | -0.10 | -3.3 |
| nofork | +61 | +0.03 | +14.3 |

Fork costs: samples/sailing-course, seed 0, greedy skipper, tick 300, 14 entities, snapshot 66,405 bytes; 3 runs, median of the runs' medians (minimum to maximum)

| Operation | Wall time, us | Bytes allocated (median call) | Bytes held after the call (median) |
|---|---|---|---|
| snapshot | 188.0 (108.5 to 206.9) | 241,134 | 70,908 |
| restore into a kept branch | 502.6 (241.4 to 506.7) | 332,229 | 0 |
| fork into a kept branch (`fork_into`) | 772.2 (372.4 to 777.0) | 576,977 | 0 |
| fresh branch (`Game::fork`) | 36,570.2 (30,350.3 to 51,196.5) | 19,892,270 | 1,735,215 |
| dropping a fresh branch | 1,715.4 (1,343.7 to 1,791.5) | | |

A live fresh branch holds 1,735,215 bytes of Rust heap and 305,678 bytes of script heap (main's: 305,678); a branch tick takes 219.7 us (160.8 to 302.7).

CPU load at the start of each timed command (machine_conditions.py, inside the hold): course 8 to 58%; fork 56 to 76%
