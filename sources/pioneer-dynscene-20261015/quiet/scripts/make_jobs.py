"""Writes jobs.json: the commands of docs/bench/dynamic-scenes.md 7, each split into one
invocation per round (the tool loops rounds outermost, so the order of runs is the same)."""
import json

Q = "<local-path>/out/dynscene/quiet"
NOTE = ("quiet re-measurement 2026-10-15: idle machine (no other agents' work), AC power, "
        "balanced plan; one invocation per round, RTX below 70 C before each")
T = ["--frames", "60", "--warm", "30", "--settle", "5"]
jobs = []


def bench(name, builds, cases, rounds, extra, conditions=True):
    for r in range(rounds):
        n = f"{name}-r{r}"
        argv = ["python", "tools/dynamic_scenes_bench.py"]
        for b in builds:
            argv += ["--build", f"{b}={Q}/{b}"]
        argv += [*extra, "--cases", cases, "--backends", "dx12,vulkan", "--rounds", "1",
                 "--out", f"{Q}/traces", "--summary", f"{Q}/{n}.json", "--note", NOTE]
        if conditions:
            argv += ["--conditions", f"{Q}/{n}-conditions"]
        jobs.append({"name": n, "argv": argv})


bench("rtx", ["before", "after"],
      "static,moving-1k,moving-10k,moving-100k,sparse-1k,sparse-10k,sparse-100k", 3, T)
bench("1.6m", ["g", "after"], "moving-1.6m", 3, T)
for x, y in [("before", "a"), ("a", "c"), ("c", "e"), ("e", "g")]:
    bench(f"step-{x}-{y}", [x, y], "moving-10k,moving-100k,sparse-10k,sparse-100k", 3, T)
bench("780m", ["before", "after"], "static,moving-10k,moving-100k,sparse-10k,sparse-100k", 3,
      [*T, "--adapters", "780m"])
bench("crowd", ["e", "d"], "crowd", 5, ["--warm", "30", "--crowd-frames", "120", "--settle", "5"])
bench("rt", ["before", "after"], "rt-200k-moving", 3,
      ["--rt-frames", "60", "--settle", "5", "--rt-first"])
bench("rt-stall", ["after"], "rt-200k-moving", 1,
      ["--rt-frames", "60", "--settle", "5", "--rt-first", "--stall", "900"])
bench("ctl", ["before", "after"], "moving-100k", 3, T)
bench("ctl-stall", ["after"], "moving-100k", 3, [*T, "--stall", "275"])
json.dump(jobs, open(f"{Q}/scripts/jobs.json", "w", encoding="utf-8"), indent=1)
print(len(jobs), "jobs")
