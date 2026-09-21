# Scope

## A. NA-PSC-IMM-001 — already Astra-done (review only)

| Item | Path |
|---|---|
| Simulator | `/Users/lesharicotsverts/bionemo-agent-toolkit/scripts/run_psc_cellular_immortality.py` |
| Astra JSON (applied) | `…/runs/psc_immortality_baseline_20260920T220655Z/astra_finetune.json` |
| Astra note | `…/runs/psc_immortality_baseline_20260920T220655Z/ASTRA_FINETUNE.md` |
| Published run | `…/runs/psc_immortality_astra_finetune_20260920T221504Z/` |
| Paper | git `NA-PSC-IMM-001.md` / `.pdf` |
| Video | git `media/psc_immortality_machinery_36s.mp4` |

Published (do not invent): O2-off t½ **3.82 s**; FIB PD **59**, L_end **1.99 kb**; PSC L_end **10.72 kb** immortal_lock; PSC_TX η **0.846** vs **0.677**, ROS **0.010** vs **0.025**.

**Job:** confirm hold, or name one defect with a Params field. Do not redo the PSC sweep for taste.

## B. NA-SN-PD-001 — needs Astra (primary)

| Item | Path |
|---|---|
| Simulator | `/Users/lesharicotsverts/bionemo-agent-toolkit/scripts/run_snpc_da_resilience.py` |
| Current run | `…/runs/snpc_da_pd_precursor_20260920T222959Z/` |
| Fusion | that dir `fusion_report.md` |
| Paper | git `snpc/NA-SN-PD-001.md` / `.pdf` |

Grok retuned locally (single-pulse MPTP, yearly algebraic ATP). CUSP `m = 1.2` was **inherited** from PSC Astra, not an SNpc pass.

Current combined-load deaths: SNpc **55**, VTA **63**, SNPC_TX **76**. WT SNpc alive@80 but high-Ca stress (ATP 1.51). VTA WT survival_lock. SNCA-alone does not kill by 80. MPTP-alone: SNpc 55, VTA 73, TX survives.

**Job:** fine-tune SNpc Params. Keep the ranking (SNpc more vulnerable than VTA; transplant delays, does not prevent combined death). Tune Ca/CI/asyn/TX so WT SNpc ATP is not an energy-crisis at 1.51 mM if that is an artifact, and so SNCA dose is not a no-op relative to literature (asyn 0.68, still alive@80 is a known tension — either defend it or move it with a knob, do not silently claim α-syn is irrelevant).

## Allowed SNpc JSON keys (Params fields only)

`cusp_m, cusp_a, cusp_b, seed,`  
`eta0_sn, leak_sn, sod_sn, calb_sn, pace_sn, da_sn, asyn_prod_sn, mito_sn,`  
`eta0_vta, leak_vta, sod_vta, calb_vta, pace_vta, da_vta, asyn_prod_vta, mito_vta,`  
`tx_eta_boost, tx_leak_cut, tx_sod_boost, tx_calb_boost, tx_mito_boost, tx_asyn_clear, tx_ci_rescue,`  
`mptp_year, mptp_years, mptp_ci_cut, tx_year,`  
`atp_fail_mM, asyn_fail, ros_fail, ci_age_per_year`

Omit `n_c` and `atp_per_rev`.
