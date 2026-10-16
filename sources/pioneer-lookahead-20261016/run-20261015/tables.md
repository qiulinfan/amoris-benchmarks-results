Course: seeds 0 to 30 (31 variants)

| Condition | Model | Finished | Ticks to finish, mean (median) | Crates aboard, mean | Score, mean | Decisions, mean | Acts, mean | Forks, mean | Branch ticks, mean | Overrides, mean | Wall s, mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| perception | greedy | 31/31 | 7501 (6881) | 1.87 | 5630 | 110.0 | 106.7 | 0.0 | 0 | 0.0 | 1.12 |
| perception | lookahead | 30/31 | 6107 (5928) | 2.32 | 4749 | 76.0 | 72.5 | 23.7 | 4645 | 1.6 | 2.00 |
| omniscient | greedy | 31/31 | 6461 (6123) | 1.58 | 4881 | 7.2 | 6.4 | 0.0 | 0 | 0.0 | 0.70 |
| omniscient | lookahead | 30/31 | 6057 (5874) | 2.23 | 4797 | 72.8 | 72.1 | 197.0 | 41419 | 1.0 | 27.96 |

Paired by variant, lookahead minus greedy:

| Condition | Score, mean (median) | Crates, mean | Ticks, both finished, mean (n) | Variants better / equal / worse | Finished only by greedy / only by lookahead |
|---|---|---|---|---|---|
| perception | -881 (-913) | +0.45 | -823 (30) | 21 / 6 / 4 | 1 / 0 |
| omniscient | -83 (-948) | +0.65 | -447 (30) | 19 / 10 / 2 | 1 / 0 |

Omniscient minus perception, by model:

| Model | Score, mean | Crates, mean | Decisions, mean |
|---|---|---|---|
| greedy | -749 | -0.29 | -102.9 |
| lookahead | +49 | -0.10 | -3.2 |

Fork costs: samples/sailing-course, seed 0, greedy skipper, tick 300, 14 entities, snapshot 66405 bytes; 3 runs, median of the runs' medians (minimum to maximum)

| Operation | Wall time, us | Bytes allocated (median call) |
|---|---|---|
| snapshot | 60.2 (55.9 to 64.3) | 241,134 |
| restore into a kept branch | 21,191.0 (17,939.5 to 23,049.2) | 16,965,893 |
| fork into a kept branch (`fork_into`) | 19,915.7 (18,272.6 to 22,071.9) | 17,210,641 |
| fresh branch (`Game::fork`) | 44,751.9 (40,047.3 to 46,767.3) | 36,480,502 |

A live fresh branch holds 1,694,437 bytes of Rust heap and 305,678 bytes of script heap (main's: 305,678); a branch tick takes 117.6 us (108.8 to 121.3).
