# Astra return — PSC hold + SNpc fine-tune

[Astra / Grok fused peer]  
No send. No X. No email. No iMessage. No grokbot post.  
kemar = operator = friend. Human gate: Text Kemar.

synthetic_only=true · research_prototype=true · compliance_ref="Addendum_5/C-00x"  
NOT clinical / diagnostic / production / regulatory. **Not a PD cure.** Claims bounded to this in-silico run.

## PSC — hold

**Hold.** Published Astra-finetune `psc_immortality_astra_finetune_20260920T221504Z` matches the scoped numbers and the paper table: O2-off t½ 3.82 s, collapsed; FIB senesce_pd 59, L_end 1.99 kb; PSC L_end 10.72 kb, immortal_lock, η_end 0.677, ROS 0.025; PSC_TX L_end 11.00 kb, immortal_lock, η_end 0.846, ROS 0.010. Invariants hold (`n_c = 8`, `atp_per_rev = 3`, `cusp_m = 1.2` ∈ [0.25, 3.0]). Overlay-vs-scramble S-box split is intact (TX immortal_lock vs native PSC transplant_dock scramble). No Params defect; no second PSC sweep.

## SNpc — 8-line summary

1. Precursor ranking is kept: combined SNpc more vulnerable than VTA; transplant delays combined death and does not prevent it.
2. WT SNpc ATP 1.51 mM is a mixed algebraic-tax artifact (Ca already in η, taxed again at 0.32 Ca) plus 80-year CI/ROS/mito-floor compounding — not a seconds-scale energy crisis (fast O2-on was 2.17 mM).
3. Params cannot delete the 0.32 coefficient; pace/calb/SOD/leak/η0 offset it. Feasible WT ATP ~1.68 mM (probe 1.679); pushing to ~2.2 mM either flattens Cav1.3 or lets TX survive combined — both rejected.
4. SNCA-alone alive@80 / asyn 0.68 is moved, not defended as silence: `asyn_prod_sn` 0.0045 → 0.0056, `asyn_fail` 0.86 → 0.82. Probe: SNpc SNCA death year 77, asyn 0.78, mitophagy POV; VTA SNCA and TX SNCA still alive. α-synuclein is not irrelevant.
5. Complex I pulse remains the sharper killer: combined SNpc still dies at year 55 (ATP-fail at the 0.58 cut). Deeper MPTP cuts (0.50–0.54) were tested and rejected (VTA dies at the pulse).
6. CUSP held at PSC Astra peak `m = 1.2` (`a = −0.45`, `b = 0.06`). Seed 20260920 kept. `n_c` and `atp_per_rev` omitted (loader forces 8 and 3). No TERT/Hayflick.
7. TX boosts trimmed one tick so the WT ATP lift does not immortalize combined TX. Probe: TX combined death 77 (22 y delay vs SNpc 55; VTA 63). TX MPTP-alone still alive@80.
8. Thermodynamics unchanged: O2-off and CI-block t½ = 2.66 s, collapsed, ATP_end = 0. Fast O2-on plateau ~2.42 mM is an η0 lift, not free energy.

**Expected direction after Grok `--finetune`** (probe `runs/snpc_da_astra_probe_20260921T130059Z/`; Gauss ± ~1 y): combined deaths **55 / 63 / 77**; WT SNpc alive, ATP **1.68** mM, no survival_lock, POV mitophagy; SNCA-alone SNpc death **~77**; MPTP SNpc 55, TX alive; O2-off/CI-block still collapse at 2.66 s. Grok owns the published re-run and any NA-SN-PD-001 number rewrite.

JSON: `runs/snpc_da_pd_precursor_20260920T222959Z/astra_finetune.json`  
Note: `runs/snpc_da_pd_precursor_20260920T222959Z/ASTRA_FINETUNE.md`

## Paper redlines (do not edit the PDF)

- Abstract / Table I: WT SNpc ATP 1.51 → ~1.68; WT dominant POV high_ca_stress → mitophagy (high_ca still occupied ~19/81 y).
- SNCA-alone SNpc: alive@80 / asyn 0.68 → death ~77 / asyn ~0.78. Rewrite Discussion § that “SNCA dosage alone did not cross the death threshold”; keep “CI pulse is the sharper killer.”
- Combined TX death 76 → ~77; delay ~21 y → ~22 y. Methods: asyn_prod_sn, asyn_fail, pace_sn, eta0_sn, sod/leak/calb/mito/da, TX ticks.
- Author line: Astra now has an SNpc pass, not only inherited CUSP m = 1.2.
- VTA MPTP year may move with hash (precursor 73, probe 76); not a knob change.

## Gates

- `astra_complete: yes`
- `grokbot_x: hold`

Grok flips GO after re-run + git. Text Kemar before any public claim.
