Course: seeds 0 to 30 (31 variants)

| Condition | Model | Finished | Ticks to finish, mean (median) | Crates aboard, mean | Score, mean | Decisions, mean | Acts, mean | Forks, mean | Branch ticks, mean | Overrides, mean | Wall s, mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| perception | greedy | 31/31 | 7501 (6881) | 1.87 | 5630 | 110.0 | 106.7 | 0.0 | 0 | 0.0 | 2.15 |
| perception | lookahead | 31/31 | 6671 (5936) | 2.35 | 4316 | 78.9 | 75.4 | 24.0 | 4703 | 1.6 | 3.11 |
| omniscient | greedy | 31/31 | 6461 (6123) | 1.58 | 4881 | 7.2 | 6.4 | 0.0 | 0 | 0.0 | 1.42 |
| omniscient | lookahead | 31/31 | 6651 (5921) | 2.26 | 4393 | 75.5 | 74.9 | 16.6 | 3290 | 1.0 | 2.81 |

Paired by variant, lookahead minus greedy:

| Condition | Score, mean (median) | Crates, mean | Ticks, both finished, mean (n) | Variants better / equal / worse | Finished only by greedy / only by lookahead |
|---|---|---|---|---|---|
| perception | -1314 (-957) | +0.48 | -830 (31) | 22 / 6 / 3 | 0 / 0 |
| omniscient | -487 (-948) | +0.68 | +190 (31) | 19 / 10 / 2 | 0 / 0 |

Omniscient minus perception, by model:

| Model | Score, mean | Crates, mean | Decisions, mean |
|---|---|---|---|
| greedy | -749 | -0.29 | -102.9 |
| lookahead | +77 | -0.10 | -3.3 |

Fork costs: samples/sailing-course, seed 0, greedy skipper, tick 300, 14 entities, snapshot 66405 bytes; 3 runs, median of the runs' medians (minimum to maximum)

| Operation | Wall time, us | Bytes allocated (median call) |
|---|---|---|
| snapshot | 74.7 (69.9 to 117.3) | 241,134 |
| restore into a kept branch | 282.3 (278.8 to 441.1) | 332,229 |
| fork into a kept branch (`fork_into`) | 411.9 (363.6 to 546.7) | 576,977 |
| fresh branch (`Game::fork`) | 36,818.8 (24,419.9 to 38,728.2) | 19,891,870 |

A live fresh branch holds 1,735,111 bytes of Rust heap and 305,678 bytes of script heap (main's: 305,678); a branch tick takes 149.4 us (119.5 to 205.5).
