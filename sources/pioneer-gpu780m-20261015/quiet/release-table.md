| Test | 5060-dx12 | 5060-vulkan | 780m-dx12 | 780m-vulkan | 5060-dx12-minimal | 5060-auto | 780m-auto |
|---|---|---|---|---|---|---|---|
| `draw_paths every_draw_path_draws_the_same_frame` | pass | pass | pass | pass | pass | pass | pass |
| `forward_variants every_forward_variant_draws_its_material` | pass | pass | pass | pass | pass | pass | pass |
| `frame_trace a_headless_trace_places_gpu_work_inside_its_frame` | pass | pass | pass | pass | skip [1] | pass | pass |
| `frame_trace tracing_after_normal_frames_keeps_the_first_gpu_frame_and_can_finish_later` | pass | pass | pass | pass | skip [2] | pass | pass |
| `gpu_profiler asynchronous_frames_keep_their_queries_and_only_record_the_capture_window` | pass | pass | pass | pass | skip [3] | pass | pass |
| `hiz occlusion_test_never_hides_a_box_in_front_of_the_depth` | pass | pass | pass | pass | pass | pass | pass |
| `hiz pyramid_is_the_minimum_over_every_sample` | pass | pass | pass | pass | pass | pass | pass |
| `lib app::tests::walk_input_normalizes_diagonal_motion_and_consumes_press_edges` | pass | pass | pass | pass | pass | pass | pass |
| `lib camera::tests::the_point_ahead_is_inside_and_behind_is_outside` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::bvh_nearest_hit_respects_node_transform_and_front_faces` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::constant_sky_sh_has_correct_radiance_normalization_and_seed_reproducibility` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::invalid_or_excessive_grids_fail_without_allocating` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::inward_normal_map_preserves_sun_and_bounces_but_valid_maps_still_apply` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::path_tracing_accepts_atmosphere_and_glass_without_weakening_baker` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::point_falloff_and_spot_cone_match_forward_light_conventions` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::probes_inside_closed_solid_are_reported_and_disabled` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::project_loader_imports_default_nodes_and_mesh_selector_with_materials` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::reflected_directional_light_has_shadow_visibility_and_color_bleeding` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::sky_cube_routes_primary_and_secondary_misses_and_updates_signature` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::sky_primary_has_no_punctual_direct_component_and_emission_is_recovered` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::streaming_asset_signature_matches_previous_json_bytes` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::texture_sampling_decodes_srgb_before_bilinear_and_repeats` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bake::tests::two_bounces_recover_environment_seen_after_diffuse_surface` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bsdf::tests::fresnel_snell_and_total_internal_reflection` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bsdf::tests::roulette_compensation_preserves_expected_brightness` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bsdf::tests::smooth_reflection_and_transmission_are_energy_bounded` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::bsdf::tests::vndf_sampling_matches_direction_pdf_and_transport_integral` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::nrc::tests::backpropagation_matches_finite_differences` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::nrc::tests::invalid_config_rejected` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::nrc::tests::packed_contract_and_deterministic_initialization` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::pt::tests::color_resize_filters_linear_light_and_preserves_alpha` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::pt::tests::large_native_scene_capacity_uses_device_bytes_and_blas_limits` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::pt::tests::pt_gpu_abi_and_limits_are_explicit` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::pt::tests::ray_query_pt_transport_training_and_accumulation` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::pt::tests::texture_size_is_explicit_and_checked_against_layers_and_upload_bytes` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::area_measure_conversion_matches_directional_diffuse_estimator` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::receiver_reconnection_reevaluates_target_without_double_area_jacobian` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::reuse_rejects_dynamic_scene_epoch_mismatch_bad_normals_and_history_reset` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::seeded_ris_constant_integrator_converges_under_nonuniform_proposal_and_target` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::source_reservoir_merge_converges_and_counts_represented_candidates` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::standalone_reservoir_wgsl_parses_and_validates_without_tracer_globals` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::visibility_is_explicit_and_history_limit_preserves_normalization` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::reservoir::tests::zero_targets_count_without_selection_and_bad_numbers_do_not_mutate` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::rt::tests::ray_query_cache_requires_history_and_resets` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::rt::tests::ray_query_ris_matches_raw_and_bounds_history` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::sky_radiance::tests::all_faces_match_bake_shader_orientation` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::sky_radiance::tests::bilinear_sampling_interpolates_texel_centers` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::sky_radiance::tests::constant_cube_preserves_radiance_and_scales_ambient_once` | pass | pass | pass | pass | pass | pass | pass |
| `lib gi::sky_radiance::tests::rejects_bad_shapes_values_formats_and_unknown_fields` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::dxc::tests::an_old_dxc_is_passed_over_for_the_next_sdk_or_for_fxc` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::dxc::tests::fixed_file_info_is_found_in_a_resource_section` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::dxc::tests::sdk_versions_order_numerically` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::dxc::tests::the_newest_sdk_wins_when_its_dxc_is_supported` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::dxc::tests::versions_compare_by_major_minor_build` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::dxc::tests::windows_dll_versions_read` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::adapters_match_by_index_or_name` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::auto_picks_the_platform_default` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::backend_names_parse_in_any_case` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::browser_emulation_and_d3d12_keep_indirect_validation` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::direct3d_12_keeps_indirect_validation` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::indirect_draws_keep_their_first_instance` | pass | pass | pass | pass | skip [4] | pass | pass |
| `lib gpu::tests::the_adapter_under_test_is_named` | pass | pass | pass | pass | pass | pass | pass |
| `lib gpu::tests::validation_keeps_labels` | pass | pass | pass | pass | pass | pass | pass |
| `lib loader::tests::neural_texture_paths_are_recognized_in_any_script` | pass | pass | pass | pass | pass | pass | pass |
| `lib lod::tests::a_pixel_at_a_distance` | pass | pass | pass | pass | pass | pass | pass |
| `lib lod::tests::modes_parse` | pass | pass | pass | pass | pass | pass | pass |
| `lib meshes::tests::a_skinned_copys_occlusion_box_holds_its_grown_sphere` | pass | pass | pass | pass | pass | pass | pass |
| `lib neural::tests::channel_words_locate_each_group` | pass | pass | pass | pass | pass | pass | pass |
| `lib neural::tests::neural_shaders_validate` | pass | pass | pass | pass | pass | pass | pass |
| `lib neural::tests::profile_constants_are_consistent` | pass | pass | pass | pass | pass | pass | pass |
| `lib neural::tests::weights_pack_into_column_major_blocks` | pass | pass | pass | pass | pass | pass | pass |
| `lib neural::train::tests::mips_average_color_in_linear_light_and_renormalize_normals` | pass | pass | pass | pass | pass | pass | pass |
| `lib neural::train::tests::quantization_rounds_ties_to_even_and_clamps` | pass | pass | pass | pass | pass | pass | pass |
| `lib occlusion::tests::a_brief_probe_counts_readings_from_the_frame_after_activation` | pass | pass | pass | pass | pass | pass | pass |
| `lib occlusion::tests::auto_keeps_what_pays_and_drops_what_does_not` | pass | pass | pass | pass | pass | pass | pass |
| `lib occlusion::tests::levels_halve_down_to_one_texel` | pass | pass | pass | pass | pass | pass | pass |
| `lib occlusion::tests::modes_parse` | pass | pass | pass | pass | pass | pass | pass |
| `lib par::tests::a_panic_reaches_the_caller` | pass | pass | pass | pass | pass | pass | pass |
| `lib par::tests::nested_tasks_finish` | pass | pass | pass | pass | pass | pass | pass |
| `lib par::tests::tasks_return_their_results_in_order` | pass | pass | pass | pass | pass | pass | pass |
| `lib post::tests::defaults_by_adapter` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::a_browser_readback_lag_of_hundreds_of_frames_decides` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::a_much_slower_way_is_drawn_for_one_frame_per_probe` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::a_probe_gives_up_after_its_timeout_in_frames_of_any_kind` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::a_probe_keeps_waiting_when_the_readback_lag_falls` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::a_probe_measures_both_ways_whatever_readings_are_lost` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::a_somewhat_slower_way_is_drawn_one_frame_at_a_time` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::auto_probes_again_and_follows_a_change_with_hysteresis` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::auto_turns_on_where_the_prepass_pays_and_stays_off_where_it_does_not` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::frames_without_instances_never_decide` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::modes_without_timings_and_without_instances` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::one_and_two_phase_frames_decide_separately` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::probes_back_off_while_the_choice_holds` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::quantized_timestamps_decide_by_differences_beyond_their_resolution` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::readings_from_before_a_restart_do_not_count` | pass | pass | pass | pass | pass | pass | pass |
| `lib prepass::tests::readings_sum_the_opaque_passes_and_the_prepass` | pass | pass | pass | pass | pass | pass | pass |
| `lib profiler::tests::timestamps_resolve_late_where_early_resolves_read_stale_values` | pass | pass | pass | pass | pass | pass | pass |
| `lib rt_shadows::tests::forward_variant_replaces_only_the_shadow_lookup` | pass | pass | pass | pass | pass | pass | pass |
| `lib rt_shadows::tests::transforms_interpolate_like_the_cull_pass` | pass | pass | pass | pass | pass | pass | pass |
| `lib scene::tests::a_tick_moving_every_instance_costs_about_what_making_them_does` | pass | pass | pass | pass | pass | pass | pass |
| `lib scene::tests::a_tick_moving_every_instance_lists_each_once_by_its_mark` | pass | pass | pass | pass | pass | pass | pass |
| `lib scene::tests::applied_frames_move_and_stop_slots_as_their_poses_say` | pass | pass | pass | pass | pass | pass | pass |
| `lib scene::tests::pending_or_empty_assets_do_not_enable_prepass_probes` | pass | pass | pass | pass | pass | pass | pass |
| `lib scene::tests::visible_instances_follow_hide_remove_reuse_and_reset_without_shrinking_slots` | pass | pass | pass | pass | pass | pass | pass |
| `lib shaders::tests::forward_clip_positions_are_invariant_in_every_backend` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::cloud::tests::halves_round_trip` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::cloud::tests::quaternions_round_trip` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::loader::tests::ply_round_trips` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::loader::tests::rejects_other_plys` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::loader::tests::splat_format_decodes` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::sort::tests::sorts_like_a_stable_cpu_sort` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::sort::tests::the_tile_matches_the_shaders` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::antialias_fades_subpixel_splats` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::growth_respects_binding_limit` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::pair_overflow_is_reported` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::picking_sees_splats` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::quads_are_the_default_rasterizer` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::splat_overflow_is_reported` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::subtile_culling_limits_tests` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::ties_are_stable` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::tiles_match_quads` | pass | pass | pass | pass | pass | pass | pass |
| `lib splat::tile::tests::transient_pair_drops_are_reported` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::brackets_intersect_to_the_tightest_offset` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::calibrations_combine_or_drift` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::drifting_clocks_place_gpu_passes_between_the_calibrations` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::export_places_gpu_passes_with_the_calibration` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::export_without_a_calibration_starts_gpu_work_after_the_submit` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::gpu_clock_samples_are_current_and_bound_by_the_cpu_brackets` | pass | pass | pass | pass | skip [5] | pass | pass |
| `lib trace::tests::overlapping_spans_get_their_own_lanes` | pass | pass | pass | pass | pass | pass | pass |
| `lib trace::tests::specs_parse_and_refuse` | pass | pass | pass | pass | pass | pass | pass |
| `lib upload::tests::batches_cover_every_slot_once_in_order` | pass | pass | pass | pass | pass | pass | pass |
| `lib upload::tests::written_slots_reach_the_instance_buffer` | pass | pass | pass | pass | pass | pass | pass |
| `lod cascades_pick_levels_by_their_texels` | pass | pass | pass | pass | pass | pass | pass |
| `lod every_draw_path_and_occlusion_draw_the_same_levels` | pass | pass | pass | pass | pass | pass | pass |
| `lod hysteresis_holds_a_level_until_the_margin` | pass | pass | pass | pass | pass | pass | pass |
| `lod levels_cut_triangles_and_stay_within_a_pixel` | pass | pass | pass | pass | pass | pass | pass |
| `lod levels_give_way_at_the_binding_limit` | pass | pass | pass | pass | pass | pass | pass |
| `lod skinned_levels_follow_the_pose` | pass | pass | pass | pass | pass | pass | pass |
| `neural training_is_deterministic_for_a_seed` | pass | pass | pass | pass | pass | pass | pass |
| `neural trains_and_decodes_like_the_reference` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material a_constant_neural_material_draws_like_the_inline_one` | pass | pass | pass | pass | skip [6] | pass | pass |
| `neural_material a_constant_neural_material_draws_on_the_webgpu_baseline` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material a_grown_latent_table_keeps_the_textures_it_holds` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material a_loaded_neural_texture_leaves_other_materials_alone` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material a_neural_material_draws_under_taa_with_splats` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material material_names_that_are_not_ascii_do_not_crash_the_renderer` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material textures_with_other_channel_sets_share_the_pipelines` | pass | pass | pass | pass | pass | pass | pass |
| `neural_material the_level_of_detail_selects_and_blends_mips_like_the_reference` | pass | pass | pass | pass | skip [7] | pass | pass |
| `neural_mlp neural_mlp_wgsl_is_current` | pass | pass | pass | pass | pass | pass | pass |
| `occlusion occlusion_culling_never_drops_a_visible_instance` | pass | pass | pass | pass | skip [8] | pass | pass |
| `prepass coplanar_masks_preserve_holes_and_valid_ties_follow_draw_order` | pass | pass | pass | pass | pass | pass | pass |
| `prepass the_depth_prepass_leaves_the_image_alone` | pass | pass | pass | pass | skip [9] | pass | pass |
| `rt_shadows ray_traced_shadows_fall_where_cascades_do` | pass | pass | pass | pass | skip [10] | pass | pass |
| `scene_changes exposure_and_resizes_reach_the_display_transform` | pass | pass | pass | pass | pass | pass | pass |
| `scene_changes moved_instances_draw_where_they_were_moved` | pass | pass | pass | pass | pass | pass | pass |
| `scene_changes skinned_characters_added_later_draw_in_their_own_poses` | pass | pass | pass | pass | pass | pass | pass |
| `skinned_bounds skinned_occlusion_boxes_hold_every_pose_their_spheres_do` | pass | pass | pass | pass | pass | pass | pass |
| `taa a_still_capture_settles_taa` | pass | pass | pass | pass | pass | pass | pass |
| `taa camera_cuts_and_resizes_drop_the_history` | pass | pass | pass | pass | pass | pass | pass |
| `taa gtao_darkens_only_indirect_light` | pass | pass | pass | pass | pass | pass | pass |
| `taa gtao_normals_from_the_target_match_the_depth` | pass | pass | pass | pass | pass | pass | pass |
| `taa msaa_with_taa_converges_beyond_msaa` | pass | pass | pass | pass | pass | pass | pass |
| `taa object_motion_reprojects_a_moving_board_exactly` | pass | pass | pass | pass | pass | pass | pass |
| `taa skinned_motion_reprojects_a_sliding_board_exactly` | pass | pass | pass | pass | pass | pass | pass |
| `taa splats_behind_meshes_are_stable_under_taa` | pass | pass | pass | pass | pass | pass | pass |
| `taa taa_reprojects_a_whole_pixel_pan_exactly` | pass | pass | pass | pass | pass | pass | pass |
| `taa the_entity_id_pass_is_not_jittered` | pass | pass | pass | pass | pass | pass | pass |
| `taa the_sea_hides_what_lies_under_it` | pass | pass | pass | pass | pass | pass | pass |
| totals | 168 pass | 168 pass | 168 pass | 168 pass | 158 pass, 10 skip | 168 pass | 168 pass |

1. 5060-dx12-minimal, `frame_trace a_headless_trace_places_gpu_work_inside_its_frame`: no GPU timestamps: placement not checked
2. 5060-dx12-minimal, `frame_trace tracing_after_normal_frames_keeps_the_first_gpu_frame_and_can_finish_later`: no GPU timestamps: GPU capture not checked
3. 5060-dx12-minimal, `gpu_profiler asynchronous_frames_keep_their_queries_and_only_record_the_capture_window`: no GPU timestamps: skipped
4. 5060-dx12-minimal, `lib gpu::tests::indirect_draws_keep_their_first_instance`: Direct3D 12: no INDIRECT_FIRST_INSTANCE, skipped
5. 5060-dx12-minimal, `lib trace::tests::gpu_clock_samples_are_current_and_bound_by_the_cpu_brackets`: no GPU timestamps: skipped
6. 5060-dx12-minimal, `neural_material a_constant_neural_material_draws_like_the_inline_one`: no shader-f16: f16 not checked
7. 5060-dx12-minimal, `neural_material the_level_of_detail_selects_and_blends_mips_like_the_reference`: no shader-f16: f16 not checked
8. 5060-dx12-minimal, `occlusion occlusion_culling_never_drops_a_visible_instance`: no INDIRECT_FIRST_INSTANCE: the default device takes the baseline path; first-instance paths not checked
9. 5060-dx12-minimal, `prepass the_depth_prepass_leaves_the_image_alone`: no INDIRECT_FIRST_INSTANCE: the default device takes the baseline path; first-instance paths not checked
10. 5060-dx12-minimal, `rt_shadows ray_traced_shadows_fall_where_cascades_do`: Dx12 on NVIDIA GeForce RTX 5060 Laptop GPU: no ray queries, skipped

- 5060-dx12: Direct3D 12 on NVIDIA GeForce RTX 5060 Laptop GPU (DiscreteGpu), driver 32.0.16.1714 ; timestamp period 1 ns; Capabilities { indirect_first_instance: true, multi_draw_indirect: true, timestamps: true, shader_f16: true, float32_filterable: true, ray_query: false }
- 5060-vulkan: Vulkan on NVIDIA GeForce RTX 5060 Laptop GPU (DiscreteGpu), driver NVIDIA 617.14; timestamp period 1 ns; Capabilities { indirect_first_instance: true, multi_draw_indirect: true, timestamps: true, shader_f16: true, float32_filterable: true, ray_query: false }
- 780m-dx12: Direct3D 12 on AMD Radeon 780M Graphics (IntegratedGpu), driver 32.0.13062.3005 ; timestamp period 10 ns; Capabilities { indirect_first_instance: true, multi_draw_indirect: true, timestamps: true, shader_f16: true, float32_filterable: true, ray_query: false }
- 780m-vulkan: Vulkan on AMD Radeon 780M Graphics (IntegratedGpu), driver AMD proprietary driver 24.30.62.03 (LLPC); timestamp period 10 ns; Capabilities { indirect_first_instance: true, multi_draw_indirect: true, timestamps: true, shader_f16: true, float32_filterable: true, ray_query: false }
- 5060-dx12-minimal: Direct3D 12 on NVIDIA GeForce RTX 5060 Laptop GPU (DiscreteGpu), driver 32.0.16.1714 ; timestamp period 1 ns; Capabilities { indirect_first_instance: false, multi_draw_indirect: true, timestamps: false, shader_f16: false, float32_filterable: false, ray_query: false }
- 5060-auto: Direct3D 12 on NVIDIA GeForce RTX 5060 Laptop GPU (DiscreteGpu), driver 32.0.16.1714 ; timestamp period 1 ns; Capabilities { indirect_first_instance: true, multi_draw_indirect: true, timestamps: true, shader_f16: true, float32_filterable: true, ray_query: false }
- 780m-auto: Direct3D 12 on AMD Radeon 780M Graphics (IntegratedGpu), driver 32.0.13062.3005 ; timestamp period 10 ns; Capabilities { indirect_first_instance: true, multi_draw_indirect: true, timestamps: true, shader_f16: true, float32_filterable: true, ray_query: false }
