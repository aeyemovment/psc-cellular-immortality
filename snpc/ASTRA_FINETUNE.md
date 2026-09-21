# Astra fine-tune note — SNpc DA-neuron resilience (run `20260920T222959Z`)

**Lane:** Astra / Grok fused peer · **policy** `CUSP-SNPC-DA-RESILIENCE-001` · **tag** pd_precursor → finetune  
**File:** `astra_finetune.json` (Params fields only; Grok re-runs with `--finetune`)  
**Seed:** `20260920` kept so Gauss asyn draws stay comparable to the precursor run.  
**Probe (not published):** `runs/snpc_da_astra_probe_20260921T130059Z/` — Grok still owns the published re-run.

synthetic_only=true · research_prototype=true · compliance_ref="Addendum_5/C-00x"  
NOT for clinical / diagnostic / production / regulatory use. Claims bounded to this in-silico run.  
**Not a Parkinson's cure, treatment, or prevention.** A delay is not a cure. SNpc is post-mitotic: no TERT / Hayflick.

## Outcome

Precursor already gets the ranking and the thermodynamics right: O2-off and CI-block ATP t_half = 2.66 s, collapsed = true; O2-on ATP_end = 2.17 mM, collapsed = false; combined deaths SNpc 55, VTA 63, SNPC_TX 76; MPTP-alone SNpc 55, VTA 73, TX alive@80; CUSP m = 1.2 inherited from PSC Astra (sweep peak, modulator 1.2000). VTA knobs and MPTP pulse (year 55, cut 0.58) are left in place.

Two precursor tensions, both from this receipt / traces (not invented):

1. **WT SNpc ATP 1.51 mM is mixed artifact + aging.** Yearly ATP is the algebraic snapshot `setpoint · η · CI / (1 + 0.32 Ca + 0.22 ROS)`, not the 30 s peak-pump ODE. Ca is already inside η as `(1 − 0.12 Ca)`, then taxed again at 0.32 Ca. Year 0 WT ATP is 2.64 mM; year 80 is 1.51 — near `atp_fail` 1.05 and below survival_lock 2.0 — while fast O2-on (same cell, seconds) settles at 2.17 mM. That yearly terminal is an energy-crisis reading of a double-counted pacemaker tax plus 80-year CI / ROS / mito-floor compounding. Params cannot delete the hardcoded 0.32 coefficient. Offsetting via pace / calbindin / SOD / leak / η0 lifts WT ATP without erasing Cav1.3 vs VTA. Pushing WT ATP to the fast plateau (~2.2 mM) either flattens pacemaking or lets TX survive combined load — both ranking failures. Feasible band is ~1.68 mM: above the 1.4 p_deg energy term, still below VTA (~2.41), still no survival_lock.

2. **SNCA-alone alive@80 with asyn 0.68 is a real tension vs dosage literature.** Precursor p_deg ~0.71 at asyn 0.68, ATP 1.12, mitophagy POV — not a no-op, but not a kill. Singleton triplication is not a 2.4× production proxy that should be silent at year 80. Move with knobs: `asyn_prod_sn` 0.0045 → 0.0056 and `asyn_fail` 0.86 → 0.82. Probe: SNpc SNCA-alone dies at year **77**, asyn_end **0.78**, mitophagy POV; VTA SNCA and TX SNCA still alive@80. Combined death stays year 55 (MPTP ATP-fail), so the Complex I pulse remains the sharper singular-cell killer. α-synuclein is not claimed irrelevant.

CUSP cubic held on the PSC Astra branch (`m = 1.2`, `a = −0.45`, `b = 0.06`). Deeper `mptp_ci_cut` (0.50–0.54) was tested and rejected: VTA dies at the pulse and the ranking collapses. TX boosts trimmed one tick so the WT ATP lift does not carry combined TX past year 80.

Expected direction after Grok `--finetune` (probe `20260921T130059Z`; asyn Gauss ± ~1 y): combined SNpc **55**, VTA **63**, TX **77** (22 y delay, not prevention); WT SNpc alive, ATP **1.68** mM, no survival_lock, dominant POV mitophagy (high_ca_stress remains occupied, 19/81 y); SNCA-alone SNpc death **~77**; MPTP-alone SNpc 55, TX alive@80; O2-off / CI-block still collapse at t½ = 2.66 s. Fast O2-on ATP_end ~2.42 mM is the η0_sn × modulator lift on the seconds window, not a new energy source.

Did **not** flip `cusp_b`. Did **not** change `n_c` or `atp_per_rev`. Did **not** put TERT/Hayflick into the neuron. Did **not** deepen the MPTP pulse.

## Parameter table

| Field | Precursor | Fine-tune | Notes |
|-------|-----------|-----------|-------|
| `cusp_m` | 1.2 | **1.2** | Held; PSC Astra peak; modulator = 1.2 ∈ [0.25, 3.0] |
| `cusp_a` | −0.45 | **−0.45** | Same negative-root branch |
| `cusp_b` | 0.06 | **0.06** | Do not cross b ≤ 0 |
| `seed` | 20260920 | **20260920** | Reproducibility vs precursor Gauss noise |
| `eta0_sn` | 0.74 | **0.77** | Still ≤ `eta0_vta` 0.78 |
| `pace_sn` | 0.85 | **0.72** | Cuts double-counted Ca tax; still ≫ `pace_vta` 0.40 |
| `calb_sn` | 0.18 | **0.22** | Modest buffer; still ≪ `calb_vta` 0.82 |
| `sod_sn` | 0.62 | **0.68** | ROS drag on η and on the 0.22 ROS tax |
| `leak_sn` | 0.022 | **0.018** | Still leakier than `leak_vta` 0.014 |
| `mito_sn` | 0.70 | **0.75** | Delays PINK1/Parkin-proxy floor; formula still contracts |
| `da_sn` | 0.80 | **0.74** | Modest cytosolic-DA ROS trim; VTA `da_vta` 0.55 untouched |
| `asyn_prod_sn` | 0.0045 | **0.0056** | SNCA dose is a late kill, not a no-op |
| `asyn_fail` | 0.86 | **0.82** | Hard-fail nearer the 0.78 asyn band |
| `tx_eta_boost` | 0.12 | **0.11** | WT ATP lift must not immortalize combined TX |
| `tx_ci_rescue` | 0.18 | **0.16** | Pulse still survived; combined still dies |
| `tx_calb_boost` | 0.45 | **0.40** | Ca buffer remains a transplant term, not VTA-level |
| `tx_sod_boost` | 0.22 | **0.20** | m = 1.2 already scales SOD |
| `tx_mito_boost` | 0.20 | **0.18** | Bounded mitophagy overlay |
| `tx_asyn_clear` | 0.35 | **0.33** | Combined asyn still below SNpc SNCA-alone |

Omitted on purpose: `n_c`, `atp_per_rev` (invariants; loader forces 8 and 3). VTA knobs, `mptp_ci_cut` 0.58, `mptp_year` 55, `tx_year` 45, `atp_fail_mM` 1.05, `ros_fail` 0.92, `ci_age_per_year` 0.0022 untouched.

## Why

- **pace_sn + calb_sn:** Direct offset of the algebraic Ca tax without rewriting the snapshot formula. Year-80 Ca ~0.60 vs VTA ~0.15 (still 4×). Cav1.3 identity is the remaining Ca, not the 0.85→0.72 trim.
- **eta0_sn + sod_sn + leak_sn:** Same pattern as PSC Astra (η0 / SOD / leak). Raises the quasi-steady ATP numerator and cuts ROS in the tax. Stops short of survival_lock (ATP 1.68 < 2.0) so WT SNpc is metabolically adequate, not locked.
- **asyn_prod_sn + asyn_fail:** Moves SNCA-alone from “alive@80, asyn 0.68, p_deg ~0.71” to late death ~77 at asyn ~0.78. Combined still dies at the year-55 CI pulse (ATP 0.16 < 1.05). VTA SNCA and TX SNCA remain alive. That is the literature-aligned dose without making α-syn the sharper killer.
- **TX one-tick trim:** Precursor TX combined dies when post-pulse ATP bleeds through 1.05 at year 76. A WT ATP lift with stock TX boosts carried combined TX to year 80 in probe grids (prevention — rejected). Trim keeps delay ~22 y (55 → 77) and TX MPTP-alone alive@80.
- **cusp_m = 1.2 held:** Precursor sweep already peaks here (TX combined 76 vs 62 at m = 1.0 and 62 at m = 3.0). This is an SNpc pass on Ca / asyn / TX, not a second CUSP hunt.
- **mptp_ci_cut held at 0.58:** Cuts 0.50–0.54 killed VTA at year 55. Ranking is a pulse-calibration fact, not a taste knob.

## Thermodynamic invariants

- `n_c = 8` protons/rev · `atp_per_rev = 3` · not present in this JSON.
- CUSP `cusp_m = 1.2` ∈ **[0.25, 3.0]**; derived modulator also 1.2 (loader clamps `cusp_m`).
- Rotation is not free energy. Δp requires ETC + terminal acceptor + Complex I. O2-off and CI-block must still collapse on the seconds scale (precursor and probe t_half = 2.66 s, ATP_end = 0, collapsed = true). Higher fast `eta_ref` (η0_sn × modulator) changes the O2-on plateau (2.17 → ~2.42 mM); it does not create ATP without O2 or with CI = 0.05.
- Not perpetual motion. Yearly ATP is a quasi-steady snapshot, not a 30 s peak-pump integration.

## Not a PD cure

This is an in-silico precursor map of one post-mitotic DA neuron. Transplant is a bounded modulator of η, leak, SOD, calbindin-like buffering, mitophagy, and α-synuclein clearance — not a new energy source, not gene therapy, not a clinical protocol. Combined load still kills the transplanted cell. A 22-year delay in this run is not prevention and is not a clinical endpoint. Parkinson's disease is not cured, treated, or prevented here. Claims are bounded to this in-silico run.

## DT#9

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-neuron simulation. Not a Parkinson's disease cure, treatment, diagnostic, gene therapy, or clinical protocol. Not perpetual motion. SNpc DA neurons are post-mitotic: survival under PD-like load is not telomere immortality. Rotary catalysis requires a proton-motive force; the proton-motive force requires electron transport, Complex I, and a terminal acceptor. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.

- synthetic_only=true
- research_prototype=true
- not_a_pd_cure=true
- post_mitotic=true
- compliance_ref="Addendum_5/C-00x"
- risk_flags=["no_clinical","unvalidated","not_perpetual_motion","not_a_pd_cure","hosted_nim_not_called","experimental_PDB_not_predicted_fold"]
- version: precursor receipt `0.1.0` · theory_id `SNPC-DA-CI-ASYN-CA-TX-001` · wm_id `DT-SNPC-DA-RESILIENCE`
