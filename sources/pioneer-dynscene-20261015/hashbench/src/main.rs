use std::collections::HashMap;
use std::hint::black_box;
use std::time::Instant;

type Map<H> = HashMap<u64, E, H>;

#[derive(Clone, Copy)]
#[allow(dead_code)]
struct E { pose: [f32; 10], look: usize, slot: u32, tag: u32, pending: bool }

#[derive(Clone)]
#[allow(dead_code)]
struct Update { id: u64, pose: Option<[f32; 10]>, pad: [u64; 19] }

#[derive(Clone, Copy, Default)]
#[allow(dead_code)]
struct Slot { pos: [f32; 3], mesh: u32, rot: [f32; 4], scale: [f32; 3], mat: u32, ppos: [f32; 3], flags: u32, prot: [f32; 4] }

struct World<H> { map: Map<H>, slots: Vec<Slot>, moved_at: Vec<u32>, dirty: Vec<u64>, list: Vec<u32>, moving: Vec<u32> }

impl<H: std::hash::BuildHasher> World<H> {
    fn update(&mut self, u: Update, mark: u32) {
        if let Some(e) = self.map.get_mut(&u.id) {
            if let Some(p) = u.pose { e.pose = p; }
            if !e.pending {
                let s = e.slot as usize;
                let i = &mut self.slots[s];
                i.ppos = i.pos; i.prot = i.rot;
                i.pos = [e.pose[0], e.pose[1], e.pose[2]];
                i.rot = [e.pose[3], e.pose[4], e.pose[5], e.pose[6]];
                i.scale = [e.pose[7], e.pose[8], e.pose[9]];
                if self.moved_at[s] != mark { self.moved_at[s] = mark; self.moving.push(s as u32); }
                let (w, b) = (s >> 6, 1u64 << (s & 63));
                if self.dirty[w] & b == 0 { self.dirty[w] |= b; self.list.push(s as u32); }
            }
        }
    }
}

fn frame(ids: &[u64], t: u32) -> Vec<Update> {
    ids.iter().map(|&id| Update { id, pose: Some([t as f32; 10]), pad: [0; 19] }).collect()
}

fn main() {
    run::<foldhash::fast::RandomState>("foldhash");
    run::<std::hash::RandomState>("sip");
}

fn run<H: std::hash::BuildHasher + Default>(name: &str) {
    let n = 1_600_000u64;
    let mut w = World { map: Map::<H>::default(), slots: vec![Slot::default(); n as usize], moved_at: vec![0; n as usize],
                        dirty: vec![0; (n as usize).div_ceil(64)], list: Vec::new(), moving: Vec::new() };
    for id in 1..=n { w.map.insert(id, E { pose: [0.0; 10], look: 0, slot: (id - 1) as u32, tag: 0, pending: false }); }
    for &(moved, stride) in &[(100_000u64, 1u64), (100_000, 16)] {
        let ids: Vec<u64> = (0..moved).map(|k| 1 + k * stride).collect();
        for chunk in [0usize, 64, 256, 1024, 4096] {
            let mut best = f64::MAX;
            for t in 1..6u32 {
                let f = frame(&ids, t);
                w.list.clear(); w.moving.clear(); for x in w.dirty.iter_mut() { *x = 0; }
                let s = Instant::now();
                if chunk == 0 {
                    for u in f { w.update(u, t); }
                } else {
                    let mut it = f.into_iter();
                    loop {
                        let ahead = it.as_slice();
                        if ahead.is_empty() { break; }
                        for u in &ahead[..ahead.len().min(chunk)] {
                            if let Some(e) = w.map.get(&u.id) { black_box(e.slot); }
                        }
                        for u in it.by_ref().take(chunk) { w.update(u, t); }
                    }
                }
                best = best.min(s.elapsed().as_secs_f64());
            }
            println!("{name:8} moved {moved} stride {stride:2} warm chunk {chunk:5}: {:6.1} ns per update", best * 1e9 / moved as f64);
        }
    }
}
