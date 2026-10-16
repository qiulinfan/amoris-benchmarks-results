
<local-path>\out\shadowcull\quiet\games\games.json:

| Configuration | Scene | Max difference | Coverage L1 | Instances | Cascade instances off -> on | Cascade triangles off -> on |
|---|---|---|---|---|---|---|
| dx12:nvidia | samples/anim | 0 | 0.0 | 22 | 22->22 22->21 22->1 22->1 | 3,544 -> 1,752 |
| dx12:nvidia | samples/sailing | 0 | 0.0 | 5 | 2->2 4->4 5->5 5->5 | 2,285 -> 2,285 |
| dx12:nvidia | samples/gi-room | 0 | 0.0 | 8 | 0->0 0->0 0->0 0->0 | 0 -> 0 |
| dx12:nvidia | samples/pt-lab | 0 | 0.0 | 11 | 11->11 11->10 11->1 11->0 | 8,184 -> 5,902 |
| vulkan:nvidia | samples/anim | 0 | 0.0 | 22 | 22->22 22->21 22->1 22->1 | 3,544 -> 1,752 |
| vulkan:nvidia | samples/sailing | 0 | 0.0 | 5 | 2->2 4->4 5->5 5->5 | 2,285 -> 2,285 |
| vulkan:nvidia | samples/gi-room | 0 | 0.0 | 8 | 0->0 0->0 0->0 0->0 | 0 -> 0 |
| vulkan:nvidia | samples/pt-lab | 0 | 0.0 | 11 | 11->11 11->10 11->1 11->0 | 8,184 -> 5,902 |
| dx12:780m | samples/anim | 0 | 0.0 | 22 | 22->22 22->21 22->1 22->1 | 3,544 -> 1,752 |
| dx12:780m | samples/sailing | 0 | 0.0 | 5 | 2->2 4->4 5->5 5->5 | 2,285 -> 2,285 |
| dx12:780m | samples/gi-room | 0 | 0.0 | 8 | 0->0 0->0 0->0 0->0 | 0 -> 0 |
| dx12:780m | samples/pt-lab | 0 | 0.0 | 11 | 11->11 11->10 11->1 11->0 | 8,184 -> 5,902 |

<local-path>\out\shadowcull\quiet\compare\compare.json:

| Configuration | Draw path | Scene | Frames identical | Camera draws equal |
|---|---|---|---|---|
| dx12:nvidia | multi-draw | mixed | 3 / 3 | yes |
| dx12:nvidia | multi-draw | mixed-orbit | 24 / 24 | yes |
| dx12:nvidia | multi-draw | cubes-sphere | 8 / 8 | yes |
| dx12:nvidia | multi-draw | cubes-dense | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-0 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-0.5 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-off-0 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-off-0.5 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-fly | 24 / 24 | yes |
| dx12:nvidia | multi-draw | lod-off-fly | 24 / 24 | yes |
| vulkan:nvidia | multi-draw | mixed | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | mixed-orbit | 24 / 24 | yes |
| vulkan:nvidia | multi-draw | cubes-sphere | 8 / 8 | yes |
| vulkan:nvidia | multi-draw | cubes-dense | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-0 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-0.5 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-off-0 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-off-0.5 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-fly | 24 / 24 | yes |
| vulkan:nvidia | multi-draw | lod-off-fly | 24 / 24 | yes |
| dx12:780m | multi-draw | mixed | 3 / 3 | yes |
| dx12:780m | multi-draw | mixed-orbit | 24 / 24 | yes |
| dx12:780m | multi-draw | cubes-sphere | 8 / 8 | yes |
| dx12:780m | multi-draw | cubes-dense | 3 / 3 | yes |
| dx12:780m | multi-draw | lod-0 | 3 / 3 | yes |
| dx12:780m | multi-draw | lod-0.5 | 3 / 3 | yes |
| dx12:780m | multi-draw | lod-off-0 | 3 / 3 | yes |
| dx12:780m | multi-draw | lod-off-0.5 | 3 / 3 | yes |
| dx12:780m | multi-draw | lod-fly | 24 / 24 | yes |
| dx12:780m | multi-draw | lod-off-fly | 24 / 24 | yes |
| vulkan:780m | multi-draw | mixed | 3 / 3 | yes |
| vulkan:780m | multi-draw | mixed-orbit | 24 / 24 | yes |
| vulkan:780m | multi-draw | cubes-sphere | 8 / 8 | yes |
| vulkan:780m | multi-draw | cubes-dense | 3 / 3 | yes |
| vulkan:780m | multi-draw | lod-0 | 3 / 3 | yes |
| vulkan:780m | multi-draw | lod-0.5 | 3 / 3 | yes |
| vulkan:780m | multi-draw | lod-off-0 | 3 / 3 | yes |
| vulkan:780m | multi-draw | lod-off-0.5 | 3 / 3 | yes |
| vulkan:780m | multi-draw | lod-fly | 24 / 24 | yes |
| vulkan:780m | multi-draw | lod-off-fly | 24 / 24 | yes |
| dx12:nvidia+minimal | baseline | mixed | 3 / 3 | yes |
| dx12:nvidia+minimal | baseline | mixed-orbit | 24 / 24 | yes |
| dx12:nvidia+minimal | baseline | cubes-sphere | 8 / 8 | yes |
| dx12:nvidia+minimal | baseline | cubes-dense | 3 / 3 | yes |
| dx12:nvidia+minimal | baseline | lod-0 | 3 / 3 | yes |
| dx12:nvidia+minimal | baseline | lod-0.5 | 3 / 3 | yes |
| dx12:nvidia+minimal | baseline | lod-off-0 | 3 / 3 | yes |
| dx12:nvidia+minimal | baseline | lod-off-0.5 | 3 / 3 | yes |
| dx12:nvidia+minimal | baseline | lod-fly | 24 / 24 | yes |
| dx12:nvidia+minimal | baseline | lod-off-fly | 24 / 24 | yes |
| vulkan:780m+minimal | baseline | mixed | 3 / 3 | yes |
| vulkan:780m+minimal | baseline | mixed-orbit | 24 / 24 | yes |
| vulkan:780m+minimal | baseline | cubes-sphere | 8 / 8 | yes |
| vulkan:780m+minimal | baseline | cubes-dense | 3 / 3 | yes |
| vulkan:780m+minimal | baseline | lod-0 | 3 / 3 | yes |
| vulkan:780m+minimal | baseline | lod-0.5 | 3 / 3 | yes |
| vulkan:780m+minimal | baseline | lod-off-0 | 3 / 3 | yes |
| vulkan:780m+minimal | baseline | lod-off-0.5 | 3 / 3 | yes |
| vulkan:780m+minimal | baseline | lod-fly | 24 / 24 | yes |
| vulkan:780m+minimal | baseline | lod-off-fly | 24 / 24 | yes |

Per cascade, last frame (instances / triangles), off -> on:

| Scene | Cascade 0 | Cascade 1 | Cascade 2 | Cascade 3 | Shadow triangles | Camera triangles |
|---|---|---|---|---|---|---|
| mixed | 2 / 1,026 -> 1 / 2 | 64 / 10,984 -> 41 / 6,980 | 65 / 5,854 -> 65 / 5,854 | 65 / 2,612 -> 58 / 2,206 | 20,476 -> 15,042 (0.73x) | 8,188 |
| mixed-orbit | 12 / 482 -> 7 / 290 | 73 / 10,964 -> 47 / 6,170 | 77 / 6,358 -> 77 / 6,358 | 77 / 3,116 -> 53 / 2,052 | 20,920 -> 14,870 (0.71x) | 8,189 |
| cubes-sphere | 0 / 0 -> 0 / 0 | 0 / 0 -> 0 / 0 | 0 / 0 -> 0 / 0 | 222 / 2,664 -> 0 / 0 | 2,664 -> 0 (0.00x) | 281,412 |
| cubes-dense | 0 / 0 -> 0 / 0 | 12 / 144 -> 0 / 0 | 43,910 / 526,920 -> 13,438 / 161,256 | 200,000 / 2,400,000 -> 200,000 / 2,400,000 | 2,927,064 -> 2,561,256 (0.88x) | 2,399,952 |
| lod-0 | 12 / 27,906 -> 6 / 11,522 | 43 / 43,778 -> 22 / 22,018 | 208 / 129,538 -> 94 / 57,986 | 2,134 / 1,229,698 -> 1,179 / 681,730 | 1,430,920 -> 773,256 (0.54x) | 1,441,538 |
| lod-0.5 | 22 / 52,482 -> 9 / 17,922 | 76 / 85,378 -> 25 / 27,906 | 379 / 237,186 -> 112 / 68,866 | 2,297 / 1,322,498 -> 1,268 / 728,450 | 1,697,544 -> 843,144 (0.50x) | 896,386 |
| lod-off-0 | 12 / 835,586 -> 6 / 409,602 | 43 / 3,145,730 -> 22 / 1,589,250 | 208 / 15,351,810 -> 94 / 6,930,434 | 2,134 / 157,401,090 -> 1,179 / 87,261,186 | 176,734,216 -> 96,190,472 (0.54x) | 169,869,314 |
| lod-off-0.5 | 22 / 1,523,714 -> 9 / 655,362 | 76 / 5,488,642 -> 25 / 1,736,706 | 379 / 27,852,802 -> 112 / 8,077,314 | 2,297 / 169,279,490 -> 1,268 / 93,241,346 | 204,144,648 -> 103,710,728 (0.51x) | 97,042,434 |
| lod-fly | 17 / 40,450 -> 7 / 14,594 | 77 / 78,082 -> 26 / 28,162 | 374 / 232,578 -> 117 / 70,914 | 2,137 / 1,228,546 -> 676 / 386,178 | 1,579,656 -> 499,848 (0.32x) | 378,754 |
| lod-off-fly | 17 / 1,179,650 -> 7 / 458,754 | 77 / 5,570,562 -> 26 / 1,851,394 | 374 / 27,410,434 -> 117 / 8,486,914 | 2,137 / 157,253,634 -> 676 / 49,430,530 | 191,414,280 -> 60,227,592 (0.31x) | 44,236,802 |

note: dx12:780m cubes-dense counts differ from the first configuration: {'off': [{'instances': 0, 'triangles': 0}, {'instances': 36, 'triangles': 432}, {'instances': 131730, 'triangles': 1580760}, {'instances': 600000, 'triangles': 7200000}], 'on': [{'instances': 0, 'triangles': 0}, {'instances': 0, 'triangles': 0}, {'instances': 40348, 'triangles': 484176}, {'instances': 600000, 'triangles': 7200000}]}

note: dx12:780m lod-0 counts differ from the first configuration: {'off': [{'instances': 36, 'triangles': 83718}, {'instances': 129, 'triangles': 131334}, {'instances': 624, 'triangles': 388614}, {'instances': 6402, 'triangles': 3689094}], 'on': [{'instances': 18, 'triangles': 34566}, {'instances': 66, 'triangles': 66054}, {'instances': 282, 'triangles': 173958}, {'instances': 3538, 'triangles': 2045574}]}

note: dx12:780m lod-0.5 counts differ from the first configuration: {'off': [{'instances': 66, 'triangles': 157446}, {'instances': 228, 'triangles': 256134}, {'instances': 1137, 'triangles': 711558}, {'instances': 6891, 'triangles': 3967494}], 'on': [{'instances': 27, 'triangles': 53766}, {'instances': 75, 'triangles': 83718}, {'instances': 336, 'triangles': 206598}, {'instances': 3805, 'triangles': 2185734}]}

note: dx12:780m lod-off-0 counts differ from the first configuration: {'off': [{'instances': 36, 'triangles': 2506758}, {'instances': 129, 'triangles': 9437190}, {'instances': 624, 'triangles': 46055430}, {'instances': 6402, 'triangles': 472203270}], 'on': [{'instances': 18, 'triangles': 1228806}, {'instances': 66, 'triangles': 4767750}, {'instances': 282, 'triangles': 20791302}, {'instances': 3538, 'triangles': 261832710}]}

note: dx12:780m lod-off-0.5 counts differ from the first configuration: {'off': [{'instances': 66, 'triangles': 4571142}, {'instances': 228, 'triangles': 16465926}, {'instances': 1137, 'triangles': 83558406}, {'instances': 6891, 'triangles': 507838470}], 'on': [{'instances': 27, 'triangles': 1966086}, {'instances': 75, 'triangles': 5210118}, {'instances': 336, 'triangles': 24231942}, {'instances': 3805, 'triangles': 279773190}]}

note: dx12:780m lod-fly counts differ from the first configuration: {'off': [{'instances': 472, 'triangles': 1093168}, {'instances': 1771, 'triangles': 1896496}, {'instances': 8346, 'triangles': 5219120}, {'instances': 54032, 'triangles': 31107120}], 'on': [{'instances': 179, 'triangles': 376112}, {'instances': 600, 'triangles': 631216}, {'instances': 2732, 'triangles': 1701552}, {'instances': 27638, 'triangles': 15877680}]}

note: dx12:780m lod-off-fly counts differ from the first configuration: {'off': [{'instances': 472, 'triangles': 32833584}, {'instances': 1771, 'triangles': 128663600}, {'instances': 8346, 'triangles': 613777456}, {'instances': 54032, 'triangles': 3981705264}], 'on': [{'instances': 179, 'triangles': 11321392}, {'instances': 600, 'triangles': 42172464}, {'instances': 2732, 'triangles': 199262256}, {'instances': 27638, 'triangles': 2032336944}]}

note: vulkan:780m cubes-dense counts differ from the first configuration: {'off': [{'instances': 0, 'triangles': 0}, {'instances': 36, 'triangles': 432}, {'instances': 131730, 'triangles': 1580760}, {'instances': 600000, 'triangles': 7200000}], 'on': [{'instances': 0, 'triangles': 0}, {'instances': 0, 'triangles': 0}, {'instances': 40348, 'triangles': 484176}, {'instances': 600000, 'triangles': 7200000}]}

note: vulkan:780m lod-0 counts differ from the first configuration: {'off': [{'instances': 36, 'triangles': 83718}, {'instances': 129, 'triangles': 131334}, {'instances': 624, 'triangles': 388614}, {'instances': 6402, 'triangles': 3689094}], 'on': [{'instances': 18, 'triangles': 34566}, {'instances': 66, 'triangles': 66054}, {'instances': 282, 'triangles': 173958}, {'instances': 3538, 'triangles': 2045574}]}

note: vulkan:780m lod-0.5 counts differ from the first configuration: {'off': [{'instances': 66, 'triangles': 157446}, {'instances': 228, 'triangles': 256134}, {'instances': 1137, 'triangles': 711558}, {'instances': 6891, 'triangles': 3967494}], 'on': [{'instances': 27, 'triangles': 53766}, {'instances': 75, 'triangles': 83718}, {'instances': 336, 'triangles': 206598}, {'instances': 3805, 'triangles': 2185734}]}

note: vulkan:780m lod-off-0 counts differ from the first configuration: {'off': [{'instances': 36, 'triangles': 2506758}, {'instances': 129, 'triangles': 9437190}, {'instances': 624, 'triangles': 46055430}, {'instances': 6402, 'triangles': 472203270}], 'on': [{'instances': 18, 'triangles': 1228806}, {'instances': 66, 'triangles': 4767750}, {'instances': 282, 'triangles': 20791302}, {'instances': 3538, 'triangles': 261832710}]}

note: vulkan:780m lod-off-0.5 counts differ from the first configuration: {'off': [{'instances': 66, 'triangles': 4571142}, {'instances': 228, 'triangles': 16465926}, {'instances': 1137, 'triangles': 83558406}, {'instances': 6891, 'triangles': 507838470}], 'on': [{'instances': 27, 'triangles': 1966086}, {'instances': 75, 'triangles': 5210118}, {'instances': 336, 'triangles': 24231942}, {'instances': 3805, 'triangles': 279773190}]}

note: vulkan:780m lod-fly counts differ from the first configuration: {'off': [{'instances': 472, 'triangles': 1093168}, {'instances': 1771, 'triangles': 1896496}, {'instances': 8346, 'triangles': 5219120}, {'instances': 54032, 'triangles': 31107120}], 'on': [{'instances': 179, 'triangles': 376112}, {'instances': 600, 'triangles': 631216}, {'instances': 2732, 'triangles': 1701552}, {'instances': 27638, 'triangles': 15877680}]}

note: vulkan:780m lod-off-fly counts differ from the first configuration: {'off': [{'instances': 472, 'triangles': 32833584}, {'instances': 1771, 'triangles': 128663600}, {'instances': 8346, 'triangles': 613777456}, {'instances': 54032, 'triangles': 3981705264}], 'on': [{'instances': 179, 'triangles': 11321392}, {'instances': 600, 'triangles': 42172464}, {'instances': 2732, 'triangles': 199262256}, {'instances': 27638, 'triangles': 2032336944}]}

note: vulkan:780m+minimal cubes-dense counts differ from the first configuration: {'off': [{'instances': 0, 'triangles': 0}, {'instances': 36, 'triangles': 432}, {'instances': 131730, 'triangles': 1580760}, {'instances': 600000, 'triangles': 7200000}], 'on': [{'instances': 0, 'triangles': 0}, {'instances': 0, 'triangles': 0}, {'instances': 40348, 'triangles': 484176}, {'instances': 600000, 'triangles': 7200000}]}

note: vulkan:780m+minimal lod-0 counts differ from the first configuration: {'off': [{'instances': 36, 'triangles': 83718}, {'instances': 129, 'triangles': 131334}, {'instances': 624, 'triangles': 388614}, {'instances': 6402, 'triangles': 3689094}], 'on': [{'instances': 18, 'triangles': 34566}, {'instances': 66, 'triangles': 66054}, {'instances': 282, 'triangles': 173958}, {'instances': 3538, 'triangles': 2045574}]}

note: vulkan:780m+minimal lod-0.5 counts differ from the first configuration: {'off': [{'instances': 66, 'triangles': 157446}, {'instances': 228, 'triangles': 256134}, {'instances': 1137, 'triangles': 711558}, {'instances': 6891, 'triangles': 3967494}], 'on': [{'instances': 27, 'triangles': 53766}, {'instances': 75, 'triangles': 83718}, {'instances': 336, 'triangles': 206598}, {'instances': 3805, 'triangles': 2185734}]}

note: vulkan:780m+minimal lod-off-0 counts differ from the first configuration: {'off': [{'instances': 36, 'triangles': 2506758}, {'instances': 129, 'triangles': 9437190}, {'instances': 624, 'triangles': 46055430}, {'instances': 6402, 'triangles': 472203270}], 'on': [{'instances': 18, 'triangles': 1228806}, {'instances': 66, 'triangles': 4767750}, {'instances': 282, 'triangles': 20791302}, {'instances': 3538, 'triangles': 261832710}]}

note: vulkan:780m+minimal lod-off-0.5 counts differ from the first configuration: {'off': [{'instances': 66, 'triangles': 4571142}, {'instances': 228, 'triangles': 16465926}, {'instances': 1137, 'triangles': 83558406}, {'instances': 6891, 'triangles': 507838470}], 'on': [{'instances': 27, 'triangles': 1966086}, {'instances': 75, 'triangles': 5210118}, {'instances': 336, 'triangles': 24231942}, {'instances': 3805, 'triangles': 279773190}]}

note: vulkan:780m+minimal lod-fly counts differ from the first configuration: {'off': [{'instances': 472, 'triangles': 1093168}, {'instances': 1771, 'triangles': 1896496}, {'instances': 8346, 'triangles': 5219120}, {'instances': 54032, 'triangles': 31107120}], 'on': [{'instances': 179, 'triangles': 376112}, {'instances': 600, 'triangles': 631216}, {'instances': 2732, 'triangles': 1701552}, {'instances': 27638, 'triangles': 15877680}]}

note: vulkan:780m+minimal lod-off-fly counts differ from the first configuration: {'off': [{'instances': 472, 'triangles': 32833584}, {'instances': 1771, 'triangles': 128663600}, {'instances': 8346, 'triangles': 613777456}, {'instances': 54032, 'triangles': 3981705264}], 'on': [{'instances': 179, 'triangles': 11321392}, {'instances': 600, 'triangles': 42172464}, {'instances': 2732, 'triangles': 199262256}, {'instances': 27638, 'triangles': 2032336944}]}

<local-path>\out\shadowcull\quiet\compare-occlusion\compare-on.json:

| Configuration | Draw path | Scene | Frames identical | Camera draws equal |
|---|---|---|---|---|
| dx12:nvidia | multi-draw | mixed | 3 / 3 | yes |
| dx12:nvidia | multi-draw | mixed-orbit | 24 / 24 | yes |
| dx12:nvidia | multi-draw | cubes-sphere | 8 / 8 | yes |
| dx12:nvidia | multi-draw | cubes-dense | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-0 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-0.5 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-off-0 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-off-0.5 | 3 / 3 | yes |
| dx12:nvidia | multi-draw | lod-fly | 24 / 24 | yes |
| dx12:nvidia | multi-draw | lod-off-fly | 24 / 24 | yes |
| vulkan:nvidia | multi-draw | mixed | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | mixed-orbit | 24 / 24 | yes |
| vulkan:nvidia | multi-draw | cubes-sphere | 8 / 8 | yes |
| vulkan:nvidia | multi-draw | cubes-dense | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-0 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-0.5 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-off-0 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-off-0.5 | 3 / 3 | yes |
| vulkan:nvidia | multi-draw | lod-fly | 24 / 24 | yes |
| vulkan:nvidia | multi-draw | lod-off-fly | 24 / 24 | yes |

Per cascade, last frame (instances / triangles), off -> on:

| Scene | Cascade 0 | Cascade 1 | Cascade 2 | Cascade 3 | Shadow triangles | Camera triangles |
|---|---|---|---|---|---|---|
| mixed | 2 / 1,026 -> 1 / 2 | 64 / 10,984 -> 41 / 6,980 | 65 / 5,854 -> 65 / 5,854 | 65 / 2,612 -> 58 / 2,206 | 20,476 -> 15,042 (0.73x) | 8,188 |
| mixed-orbit | 12 / 482 -> 7 / 290 | 73 / 10,964 -> 47 / 6,170 | 77 / 6,358 -> 77 / 6,358 | 77 / 3,116 -> 53 / 2,052 | 20,920 -> 14,870 (0.71x) | 8,189 |
| cubes-sphere | 0 / 0 -> 0 / 0 | 0 / 0 -> 0 / 0 | 0 / 0 -> 0 / 0 | 222 / 2,664 -> 0 / 0 | 2,664 -> 0 (0.00x) | 281,412 |
| cubes-dense | 0 / 0 -> 0 / 0 | 12 / 144 -> 0 / 0 | 43,910 / 526,920 -> 13,438 / 161,256 | 200,000 / 2,400,000 -> 200,000 / 2,400,000 | 2,927,064 -> 2,561,256 (0.88x) | 260,676 |
| lod-0 | 12 / 27,906 -> 6 / 11,522 | 43 / 43,778 -> 22 / 22,018 | 208 / 129,538 -> 94 / 57,986 | 2,134 / 1,229,698 -> 1,179 / 681,730 | 1,430,920 -> 773,256 (0.54x) | 1,260,546 |
| lod-0.5 | 22 / 52,482 -> 9 / 17,922 | 76 / 85,378 -> 25 / 27,906 | 379 / 237,186 -> 112 / 68,866 | 2,297 / 1,322,498 -> 1,268 / 728,450 | 1,697,544 -> 843,144 (0.50x) | 668,290 |
| lod-off-0 | 12 / 835,586 -> 6 / 409,602 | 43 / 3,145,730 -> 22 / 1,589,250 | 208 / 15,351,810 -> 94 / 6,930,434 | 2,134 / 157,401,090 -> 1,179 / 87,261,186 | 176,734,216 -> 96,190,472 (0.54x) | 147,079,170 |
| lod-off-0.5 | 22 / 1,523,714 -> 9 / 655,362 | 76 / 5,488,642 -> 25 / 1,736,706 | 379 / 27,852,802 -> 112 / 8,077,314 | 2,297 / 169,279,490 -> 1,268 / 93,241,346 | 204,144,648 -> 103,710,728 (0.51x) | 68,173,826 |
| lod-fly | 17 / 40,450 -> 7 / 14,594 | 77 / 78,082 -> 26 / 28,162 | 374 / 232,578 -> 117 / 70,914 | 2,137 / 1,228,546 -> 676 / 386,178 | 1,579,656 -> 499,848 (0.32x) | 373,762 |
| lod-off-fly | 17 / 1,179,650 -> 7 / 458,754 | 77 / 5,570,562 -> 26 / 1,851,394 | 374 / 27,410,434 -> 117 / 8,486,914 | 2,137 / 157,253,634 -> 676 / 49,430,530 | 191,414,280 -> 60,227,592 (0.31x) | 43,597,826 |
