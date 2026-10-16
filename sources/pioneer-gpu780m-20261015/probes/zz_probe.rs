//! Throwaway probes behind docs/bench/gpu-matrix.md 3 a to 3 c (track gpu780m, 2026-10-15). Not
//! committed: copied into crates/pocket-render/tests/ for a run, deleted afterwards. Each probe
//! prints what it measured; the logs are kept beside this file.
//!
//!   probe_timestamps     immediate vs deferred resolve, 40 rounds x 4 cases each (3 a)
//!   probe_calibration    the clock calibration's rounds, 8 variants x 4 rounds (3 a)
//!   probe_parallel_open  rounds of 12 parallel opens, without and with the open lock (3 b)
//!   probe_taa_edge       inline vs inline x (1 + e) under TAA and MSAA (3 c)
//!   probe_neural_taa     the neural constant material vs the inline one under TAA (3 c)

use pocket_assets::neural::{
    Channel, GridSpec, LatentGrid, LatentLevel, NeuralLayout, NeuralTexture, Sampling, f32_to_f16,
    full_mip_count, level_dims,
};
use pocket_render::gpu::{Minimal, instance_with};
use pocket_render::neural::train::srgb_to_linear;
use pocket_render::{Antialiasing, BackendChoice, Gpu, Renderer, demo};

fn gpu() -> Gpu {
    let gpu = Gpu::headless(BackendChoice::from_env()).expect("a GPU");
    eprintln!("probe on {} {} ({} {})", gpu.backend_name(), gpu.info.name, gpu.info.driver,
        gpu.info.driver_info);
    gpu
}

// ---- 3 a: timestamps ----

fn buffers(device: &wgpu::Device) -> (wgpu::QuerySet, wgpu::Buffer, wgpu::Buffer) {
    let q = device.create_query_set(&wgpu::QuerySetDescriptor {
        label: None,
        ty: wgpu::QueryType::Timestamp,
        count: 2,
    });
    let r = device.create_buffer(&wgpu::BufferDescriptor {
        label: None,
        size: 16,
        usage: wgpu::BufferUsages::QUERY_RESOLVE | wgpu::BufferUsages::COPY_SRC,
        mapped_at_creation: false,
    });
    let b = device.create_buffer(&wgpu::BufferDescriptor {
        label: None,
        size: 16,
        usage: wgpu::BufferUsages::MAP_READ | wgpu::BufferUsages::COPY_DST,
        mapped_at_creation: false,
    });
    (q, r, b)
}

fn read(gpu: &Gpu, b: &wgpu::Buffer) -> (u64, u64) {
    b.slice(..).map_async(wgpu::MapMode::Read, |_| {});
    gpu.device.poll(wgpu::PollType::wait_indefinitely()).unwrap();
    let v = {
        let d = b.slice(..).get_mapped_range().unwrap();
        (
            u64::from_le_bytes(d[..8].try_into().unwrap()),
            u64::from_le_bytes(d[8..16].try_into().unwrap()),
        )
    };
    b.unmap();
    v
}

/// Writes two timestamps with `f`, resolves them in the same command buffer (`deferred` false) or
/// in a later submission after the sampling one completed, and reads them.
fn ticks(gpu: &Gpu, deferred: bool, f: &dyn Fn(&mut wgpu::CommandEncoder, &wgpu::QuerySet)) -> (u64, u64) {
    let device = &gpu.device;
    let (q, r, b) = buffers(device);
    let mut enc = device.create_command_encoder(&Default::default());
    f(&mut enc, &q);
    if deferred {
        gpu.queue.submit([enc.finish()]);
        device.poll(wgpu::PollType::wait_indefinitely()).unwrap();
        enc = device.create_command_encoder(&Default::default());
    }
    enc.resolve_query_set(&q, 0..2, &r, 0);
    enc.copy_buffer_to_buffer(&r, 0, &b, 0, 16);
    gpu.queue.submit([enc.finish()]);
    read(gpu, &b)
}

#[test]
fn probe_timestamps() {
    let gpu = gpu();
    let device = gpu.device.clone();
    let target = device.create_texture(&wgpu::TextureDescriptor {
        label: None,
        size: wgpu::Extent3d { width: 1, height: 1, depth_or_array_layers: 1 },
        mip_level_count: 1,
        sample_count: 1,
        dimension: wgpu::TextureDimension::D2,
        format: wgpu::TextureFormat::Rgba8Unorm,
        usage: wgpu::TextureUsages::RENDER_ATTACHMENT,
        view_formats: &[],
    });
    let view = target.create_view(&Default::default());
    let color = || {
        Some(wgpu::RenderPassColorAttachment {
            view: &view,
            depth_slice: None,
            resolve_target: None,
            ops: wgpu::Operations { load: wgpu::LoadOp::Clear(wgpu::Color::BLACK), store: wgpu::StoreOp::Store },
        })
    };
    let compute = |enc: &mut wgpu::CommandEncoder, q: &wgpu::QuerySet| {
        let _ = enc.begin_compute_pass(&wgpu::ComputePassDescriptor {
            label: None,
            timestamp_writes: Some(wgpu::ComputePassTimestampWrites {
                query_set: q,
                beginning_of_pass_write_index: Some(0),
                end_of_pass_write_index: Some(1),
            }),
        });
    };
    let render = |enc: &mut wgpu::CommandEncoder, q: &wgpu::QuerySet| {
        let _ = enc.begin_render_pass(&wgpu::RenderPassDescriptor {
            label: None,
            color_attachments: &[color()],
            depth_stencil_attachment: None,
            timestamp_writes: Some(wgpu::RenderPassTimestampWrites {
                query_set: q,
                beginning_of_pass_write_index: Some(0),
                end_of_pass_write_index: Some(1),
            }),
            occlusion_query_set: None,
            multiview_mask: None,
        });
    };
    let encoder = |enc: &mut wgpu::CommandEncoder, q: &wgpu::QuerySet| {
        enc.write_timestamp(q, 0);
        enc.write_timestamp(q, 1);
    };
    let after_render = |enc: &mut wgpu::CommandEncoder, q: &wgpu::QuerySet| {
        let _ = enc.begin_render_pass(&wgpu::RenderPassDescriptor {
            label: None,
            color_attachments: &[color()],
            depth_stencil_attachment: None,
            timestamp_writes: None,
            occlusion_query_set: None,
            multiview_mask: None,
        });
        compute(enc, q);
    };
    let inside = device.features().contains(wgpu::Features::TIMESTAMP_QUERY_INSIDE_ENCODERS);
    let cases: Vec<(&str, &dyn Fn(&mut wgpu::CommandEncoder, &wgpu::QuerySet))> = {
        let mut c: Vec<(&str, &dyn Fn(&mut wgpu::CommandEncoder, &wgpu::QuerySet))> =
            vec![("compute", &compute), ("render", &render), ("compute after render", &after_render)];
        if inside {
            c.push(("encoder", &encoder));
        }
        c
    };
    const ROUNDS: usize = 40;
    for deferred in [false, true] {
        let mut seen: Vec<(u64, u64)> = Vec::new();
        let mut bad = vec![0usize; cases.len()];
        let mut zero = vec![0usize; cases.len()];
        for round in 0..ROUNDS {
            for (k, (name, f)) in cases.iter().enumerate() {
                let v = ticks(&gpu, deferred, *f);
                let wrong = v.0 == 0 || v.1 == 0 || v.1 < v.0 || seen.contains(&v);
                if wrong {
                    bad[k] += 1;
                    zero[k] += usize::from(v.0 == 0 || v.1 == 0);
                    if bad[k] <= 3 {
                        eprintln!("  {} round {round} {name}: {v:?}", mode(deferred));
                    }
                }
                seen.push(v);
            }
        }
        for (k, (name, _)) in cases.iter().enumerate() {
            eprintln!(
                "timestamps {}: {name}: {} of {ROUNDS} wrong ({} zero, {} repeated or reversed)",
                mode(deferred),
                bad[k],
                zero[k],
                bad[k] - zero[k]
            );
        }
    }
}

fn mode(deferred: bool) -> &'static str {
    if deferred { "resolve after completion" } else { "resolve in the sampling command buffer" }
}

/// The trace clock calibration's shape: an empty timestamped compute pass per round; `poll`: wait
/// for the GPU before submitting; `reuse`: one query set and buffers for every round.
fn calibration(gpu: &Gpu, deferred: bool, poll: bool, reuse: bool) -> Vec<(u64, u64)> {
    let device = &gpu.device;
    let mut set = buffers(device);
    let mut out = Vec::new();
    for _ in 0..4 {
        if !reuse {
            set = buffers(device);
        }
        let (q, r, b) = &set;
        let mut enc = device.create_command_encoder(&Default::default());
        {
            let _pass = enc.begin_compute_pass(&wgpu::ComputePassDescriptor {
                label: None,
                timestamp_writes: Some(wgpu::ComputePassTimestampWrites {
                    query_set: q,
                    beginning_of_pass_write_index: Some(0),
                    end_of_pass_write_index: Some(1),
                }),
            });
        }
        let resolve = |enc: &mut wgpu::CommandEncoder| {
            enc.resolve_query_set(q, 0..2, r, 0);
            enc.copy_buffer_to_buffer(r, 0, b, 0, 16);
        };
        if !deferred {
            resolve(&mut enc);
        }
        let c = enc.finish();
        if poll {
            device.poll(wgpu::PollType::wait_indefinitely()).unwrap();
        }
        gpu.queue.submit([c]);
        device.poll(wgpu::PollType::wait_indefinitely()).unwrap();
        if deferred {
            let mut e = device.create_command_encoder(&Default::default());
            resolve(&mut e);
            gpu.queue.submit([e.finish()]);
        }
        out.push(read(gpu, b));
    }
    out
}

#[test]
fn probe_calibration() {
    let gpu = gpu();
    let mut totals = [(0usize, 0usize); 2];
    for deferred in [false, true] {
        for poll in [false, true] {
            for reuse in [false, true] {
                let rounds = calibration(&gpu, deferred, poll, reuse);
                let wrong = rounds
                    .iter()
                    .enumerate()
                    .filter(|(i, v)| v.0 == 0 || v.1 < v.0 || rounds[..*i].contains(v))
                    .count();
                let t = &mut totals[usize::from(deferred)];
                t.0 += rounds.len();
                t.1 += wrong;
                eprintln!(
                    "calibration {} poll {poll} reuse {reuse}: {wrong} of 4 wrong {rounds:?}",
                    mode(deferred)
                );
            }
        }
    }
    for deferred in [false, true] {
        let (n, w) = totals[usize::from(deferred)];
        eprintln!("calibration {}: {w} of {n} rounds wrong", mode(deferred));
    }
}

// ---- 3 b: parallel opens ----

#[test]
fn probe_parallel_open() {
    let choice = BackendChoice::from_env();
    const THREADS: usize = 12;
    const ROUNDS: usize = 12;
    for locked in [false, true] {
        let mut failed = 0;
        let mut first = None;
        for _ in 0..ROUNDS {
            let errors: Vec<String> = std::thread::scope(|s| {
                let hs: Vec<_> = (0..THREADS)
                    .map(|_| {
                        s.spawn(move || {
                            let opened = if locked {
                                Gpu::headless(choice)
                            } else {
                                let m = Minimal::from_env();
                                pollster::block_on(Gpu::new_with(instance_with(choice, m), None, m))
                            };
                            opened.err().map(|e| e.to_string())
                        })
                    })
                    .collect();
                hs.into_iter().filter_map(|h| h.join().unwrap()).collect()
            });
            failed += errors.len();
            if first.is_none() {
                first = errors.into_iter().next();
            }
        }
        eprintln!(
            "parallel opens {choice:?} {}: {failed} of {} failed; first error {first:?}",
            if locked { "with the open lock (Gpu::headless)" } else { "without a lock" },
            ROUNDS * THREADS
        );
    }
}

// ---- 3 c: TAA ----

fn orm(base: [f32; 3], roughness: f32) -> Vec<(Channel, f32)> {
    vec![
        (Channel::BaseR, base[0]),
        (Channel::BaseG, base[1]),
        (Channel::BaseB, base[2]),
        (Channel::NormalX, 0.5),
        (Channel::NormalY, 0.5),
        (Channel::Occlusion, 1.0),
        (Channel::Roughness, roughness),
        (Channel::Metallic, 0.0),
    ]
}

/// neural_material.rs's constant texture.
fn constant(values: &[(Channel, f32)]) -> NeuralTexture {
    let layout = NeuralLayout {
        channels: values.iter().map(|(c, _)| *c).collect(),
        fine: GridSpec { features: 8, bits: 8 },
        coarse: GridSpec { features: 8, bits: 8 },
        fine_shift: 2,
        sampling: Sampling::Bilinear,
        pe_octaves: 2,
        hidden: [32, 32],
    };
    let size = 64;
    let mips = full_mip_count(size, size);
    let levels = level_dims(&layout, size, size, mips)
        .iter()
        .map(|d| {
            let grid = |[w, h]: [u32; 2]| LatentGrid {
                width: w,
                height: h,
                words: (0..2 * w * h).map(|i| i.wrapping_mul(2_654_435_761)).collect(),
            };
            LatentLevel { fine: grid(d.fine), coarse: grid(d.coarse) }
        })
        .collect();
    let mut weights = vec![0u16; layout.weight_count()];
    let [_, _, (_, b3)] = layout.offsets();
    for (i, (_, v)) in values.iter().enumerate() {
        weights[b3 + i] = f32_to_f16(*v);
    }
    NeuralTexture { name: "constant".into(), width: size, height: size, mip_count: mips, layout, levels, weights }
}

/// neural_material.rs's walker view with `aa`, `frames` frames at the test's fixed time.
fn shoot(
    gpu: &Gpu,
    aa: Antialiasing,
    frames: usize,
    frame: pocket_assets::RenderFrame,
    neural: Option<(&NeuralTexture, bool)>,
) -> Vec<u8> {
    let mut r = Renderer::new(gpu, wgpu::TextureFormat::Rgba8UnormSrgb, 320, 180);
    r.set_antialiasing(aa);
    r.add_model(demo::NEURAL_GROUND, &demo::neural_ground_model(40.0, 8.0));
    if let Some((texture, f16)) = neural {
        r.set_neural_half_precision(f16);
        r.add_neural_texture("materials/constant.ntex", texture).expect("the texture loads");
    }
    r.apply(frame, 0.0);
    r.set_camera_override(Some(demo::neural_camera(1)));
    let mut rgba = Vec::new();
    for _ in 0..frames {
        rgba = r.capture_rgba(1.0 / 60.0).2;
    }
    rgba
}

fn worst(a: &[u8], b: &[u8]) -> (u8, usize) {
    let mut worst = 0;
    let mut over = 0;
    for (p, q) in a.chunks(4).zip(b.chunks(4)) {
        let d = (0..3).map(|i| p[i].abs_diff(q[i])).max().unwrap();
        worst = worst.max(d);
        over += usize::from(d > 2);
    }
    (worst, over)
}

#[test]
fn probe_taa_edge() {
    let gpu = gpu();
    let linear = [0.8f32, 0.35, 0.1].map(srgb_to_linear);
    let scene = |e: f32| {
        let l = linear.map(|c| c * (1.0 + e));
        demo::neural_scene("", [l[0], l[1], l[2], 1.0], 0.6)
    };
    for (aa, frames) in [(Antialiasing::Taa, 3), (Antialiasing::Msaa, 3), (Antialiasing::Taa, 20)] {
        let a = shoot(&gpu, aa, frames, scene(0.0), None);
        let line: Vec<String> = [0.0f32, 0.001, 0.003, 0.01]
            .iter()
            .map(|&e| {
                let (d, over) = worst(&a, &shoot(&gpu, aa, frames, scene(e), None));
                format!("e={e}: {d}/{over}")
            })
            .collect();
        eprintln!("taa edge {aa:?} {frames} frames (worst / pixels over 2): {}", line.join(", "));
    }
}

#[test]
fn probe_neural_taa() {
    let gpu = gpu();
    let base = [0.8, 0.35, 0.1];
    let texture = constant(&orm(base, 0.6));
    let linear = base.map(srgb_to_linear);
    for aa in [Antialiasing::Taa, Antialiasing::Msaa, Antialiasing::Off] {
        let inline = shoot(&gpu, aa, 3, demo::neural_scene("", [linear[0], linear[1], linear[2], 1.0], 0.6), None);
        let precisions: &[bool] = if gpu.caps.shader_f16 { &[true, false] } else { &[false] };
        for &f16 in precisions {
            let neural = shoot(
                &gpu,
                aa,
                3,
                demo::neural_scene("materials/constant.ntex", [1.0; 4], 0.6),
                Some((&texture, f16)),
            );
            let (d, over) = worst(&inline, &neural);
            eprintln!("neural vs inline {aa:?} f16 {f16}: worst {d}, {over} pixels over 2");
        }
    }
}
