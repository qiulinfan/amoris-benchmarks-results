//! Scratch (not committed): folds of per-tick hashes of every section except the physics cache,
//! for comparing layout 1 and layout 2 trajectories.

use pocket_physics::probe::{Snap, fork, fresh, ledger, level, sailing_world};
use pocket_sim::{NoHooks, Sim};

fn traj(s: &Snap) -> u64 {
    let mut h = 0xcbf2_9ce4_8422_2325u64;
    for (name, b) in &s.sections {
        if *name == "physics.rapier" {
            continue;
        }
        h = pocket_sim::rng::fnv1a64_extend(h, name.as_bytes());
        h = pocket_sim::rng::fnv1a64_extend(h, b);
    }
    h
}

fn fold(v: &[u64]) -> u64 {
    let mut h = 0xcbf2_9ce4_8422_2325u64;
    for x in v {
        h = pocket_sim::rng::fnv1a64_extend(h, &x.to_le_bytes());
    }
    h
}

fn run(mut sim: Sim, ticks: u32, fork_each: bool) -> (Vec<u64>, Vec<u64>) {
    let l = ledger();
    let mut t = vec![traj(&l.snapshot(sim.world()).unwrap())];
    let mut full = vec![l.snapshot(sim.world()).unwrap().hash()];
    for _ in 0..ticks {
        if fork_each {
            sim = fork(&l, &sim, fresh).unwrap();
        }
        let r = sim.step(&mut NoHooks).unwrap();
        assert!(r.errors.is_empty());
        let s = l.snapshot(sim.world()).unwrap();
        t.push(traj(&s));
        full.push(s.hash());
    }
    (t, full)
}

#[test]
fn trajectories() {
    let (a, fa) = run(sailing_world(), 1200, false);
    let (b, fb) = run(sailing_world(), 600, true);
    let (c, fc) = run(level::level_world(100, 3), 300, false);
    let (d, fd) = run(level::level_world(100, 3), 300, true);
    assert_eq!(&a[..601], &b[..]);
    assert_eq!(&fa[..601], &fb[..]);
    assert_eq!(c, d);
    assert_eq!(fc, fd);
    println!(
        "TRAJ sailing1200 {:016x} sailing600forked {:016x} level300 {:016x} level300forked {:016x}",
        fold(&a),
        fold(&b),
        fold(&c),
        fold(&d)
    );
    println!(
        "FULL sailing1200 {:016x} level300 {:016x}",
        fold(&fa),
        fold(&fc)
    );
}
