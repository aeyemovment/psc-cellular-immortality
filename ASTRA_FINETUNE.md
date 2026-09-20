# Astra fine-tune note — PSC cellular immortality (run `20260920T220655Z`)

**Lane:** Astra / Grok fused peer · **policy** `CUSP-PSC-IMMORTALITY-001` · **tag** baseline → finetune  
**File:** `astra_finetune.json` (Params fields only; Grok re-runs with `--finetune`)  
**Seed:** `20260920` kept so TERT Gauss draws stay comparable to baseline.

synthetic_only=true · research_prototype=true · compliance_ref="Addendum_5/C-00x"  
NOT for clinical / diagnostic / production / regulatory use. Claims bounded to this in-silico run.

## Outcome

Baseline already gets the physics and the three-arm contrast right: O2-off ATP t_half = 3.82 s and collapsed = true; FIB Hayflick-like senesce_pd = 59, L_end = 1.99 kb, immortal_lock = false; PSC immortal_lock = true with L_end = 9.72 kb and no senescence; PSC_TX overlay-locks immortal_lock with L_end = 10.96 kb, eta_end = 0.78, rps_ss = 104 vs PSC 69, ROS 0.013 vs 0.047.

Tune targets, all from this receipt / sweep / traces (not a new run):

1. **PSC η is low vs primed-iPSC OXPHOS.** Trace `trace_PSC.csv`: η starts 0.621 and decays under ROS to **0.558** by PD 200 — below FIB η_end 0.637, inverted vs primed (epiblast-like) iPSC coupling (~0.65–0.80 in-silico target band), which should sit *under* fibroblast η0 = 0.80 but not under fibroblast terminal η.
2. **CUSP sweep has a better m.** Measured sweep (not interpolated): m = 1.2 is the designed modulator peak (`cusp_modulator` comment; value 1.2000). PSC η_end 0.620 / L_end 10.67 kb; PSC_TX L_end **11.39 kb** (best in sweep) / η 0.835 / rps 115. FIB senesce_pd stays 59 at every m. m = 1.5 has a slightly higher raw modulator (1.266) and PSC L_end 11.23 kb but *worse* PSC_TX L_end (11.08 kb). Pick the measured peak **m = 1.2**.
3. **S-box overlay vs scramble.** Overlay fires only when `transplanted and L>8 and tert>0.85 and ros<0.2` (`slow_lineage`). Baseline PSC (not transplanted) is a 67/67 tie S_replication vs immortal_lock plus 34 transplant_dock — scramble leak. At m ≥ 1.2, η stays > 0.6 (bit4), so AES maps the high-health byte to G1 / transplant_dock (~100/101). That is the scramble. TX overlay still stamps immortal_lock (~193/201). Fine-tune *keeps* that overlay-vs-scramble split rather than chasing η below 0.6 to fake a cell-cycle POV.

Expected direction after Grok `--finetune` (formula projection on the η/ROS loop that reproduced baseline 0.5579 / 0.0469 / 0.7756 / 0.0126 exactly; TERT length still stochastic): PSC η_end ~0.68, ROS ~0.025; PSC_TX η_end ~0.85, ROS ~0.010, dominant POV immortal_lock; PSC scramble G1/transplant_dock; FIB Hayflick unchanged (fib knobs not touched). O2-off must still collapse — not a prediction of a new t_half.

Did **not** flip the sign of `cusp_b` (that jumps order_x 0.26 → ~0.72, a branch switch, not a fine-tune). Did **not** change `n_c` or `atp_per_rev`.

## Parameter changes

| Field | Baseline | Fine-tune | Notes |
|-------|----------|-----------|-------|
| `cusp_m` | 1.0 | **1.2** | Sweep peak; modulator = 1.2 ∈ [0.25, 3.0] |
| `cusp_a` | −0.55 | **−0.45** | Same negative-root branch; order_x 0.261 → ~0.282 |
| `cusp_b` | 0.12 | **0.06** | Milder asymmetry; do not cross b ≤ 0 |
| `eta0_psc` | 0.72 | **0.76** | Primed-iPSC coupling; still < `eta0_fib` 0.80 |
| `sod_psc` | 0.70 | **0.80** | Cut ROS drag on η; MnSOD still < TX after boost |
| `leak_frac_psc` | 0.018 | **0.015** | Still leakier than FIB 0.012 |
| `tx_eta_boost` | 0.18 | **0.15** | Baseline η is higher; avoid η → 0.98 clamp |
| `tx_leak_cut` | 0.55 | **0.50** | Keep overlay `ros < 0.2` robust |
| `tx_sod_boost` | 0.25 | **0.22** | m = 1.2 already scales SOD; stay under 1.3 clamp |
| `seed` | 20260920 | **20260920** | Reproducibility vs baseline TERT noise |

Omitted on purpose: `n_c`, `atp_per_rev` (invariants; loader forces 8 and 3). Fibroblast knobs untouched.

## Why

- **η0_psc + SOD + leak:** Baseline ROS 0.047 × 0.012 / PD compounds to η × ~0.89 over 200 PD. Raising SOD and cutting leak slows that drag so primed-like η_end can hold in the 0.65–0.70 band without claiming fibroblast-level coupling.
- **cusp_m = 1.2:** Only sweep point that jointly lifts PSC η/L and maximizes PSC_TX L_end while leaving Hayflick invariant. m = 0.25/0.5 under-couples (PSC η ~0.42, L ~7.6 kb). m = 3.0 folds back (modulator 0.915 ≈ m = 1.0).
- **cusp_a/b:** Tiny cubic trim on the same attractor. A b-sign flip would be a different model.
- **TX trims:** Transplant remains a bounded efficiency / leak / SOD / TERT-lock modulator, not a new energy source. Overlay-vs-scramble contrast is the point of the S-box, not making PSC POV look like a cell-cycle clock.

## Thermodynamic invariants preserved

- `n_c = 8` protons/rev · `atp_per_rev = 3` · not present in this JSON.
- CUSP `cusp_m = 1.2` ∈ **[0.25, 3.0]**; derived modulator also 1.2 (loader clamps `cusp_m`).
- Rotation is not free energy. Δp requires ETC + terminal acceptor. O2-off must still collapse on the seconds scale (baseline t_half = 3.82 s). Higher fast `eta_ref` (η0_psc × modulator) changes leak vs reverse-ATPase rates; it does not create ATP without O2.
- Not perpetual motion. TERT maintenance is an ATP-consuming polymerase proxy, not a thermodynamic loophole.

## DT#9 disclaimer

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-cell simulation. Not a clinical therapy, gene-therapy product, anti-aging treatment, or perpetual-motion device. Rotary catalysis requires a proton-motive force; the proton-motive force requires electron transport and a terminal acceptor. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.

- synthetic_only=true
- research_prototype=true
- compliance_ref="Addendum_5/C-00x"
- risk_flags=["no_clinical","unvalidated","not_perpetual_motion","hosted_nim_not_called","experimental_PDB_not_predicted_fold"]
- version: baseline receipt `0.1.0` · theory_id `PSC-ATP-TERT-TX-CUSP-SBOX-001` · wm_id `DT-PSC-CELLULAR-IMMORTALITY`
