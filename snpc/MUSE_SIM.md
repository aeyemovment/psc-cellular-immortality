# Muse Spark own sim — SNpc DA-neuron resilience

**Lane:** Muse Spark · **tag** `muse_own` · **run** `20260921T132605Z`  
**policy** `CUSP-SNPC-DA-RESILIENCE-001` · precursor `NA-PSC-IMM-001`  
**JSON:** `runs/snpc_da_pd_precursor_20260920T222959Z/muse_finetune.json`  
**Run dir:** `runs/snpc_da_muse_own_20260921T132605Z/`

synthetic_only=true · research_prototype=true · compliance_ref="Addendum_5/C-00x"  
**Not a Parkinson's cure.** Post-mitotic (no TERT / Hayflick). `dt_ritual_run=false`. No send.

Independent of Astra probe `snpc_da_astra_probe_20260921T130059Z` and Grok published re-run `snpc_da_astra_finetune_20260921T130321Z`. Those dirs were not overwritten.

## Outcome

Own in-silico run with Muse-lane knobs only: seed **20260921** (visibly not Astra `20260920`); modest CUSP-HOLO modulator `cusp_m = 1.15` (derived modulator **1.1329**, ∈ [0.25, 3.0]); light cubic overlay `cusp_a = −0.42` (same negative-root branch as Astra `−0.45`); `cusp_b = 0.06` held. Astra biology knobs (η0 / pace / calb / SOD / leak / mito / DA / asyn / TX ticks) kept. `n_c` and `atp_per_rev` omitted (loader forces 8 and 3).

Ranking held:

- Combined deaths **SNpc 55 / VTA 59 / SNPC_TX 74**. SNpc more vulnerable than VTA. Transplant delays combined death by 19 y and does **not** prevent it.
- SNCA-alone SNpc death year **76** (asyn_end 0.7969, mitophagy POV). VTA SNCA and TX SNCA still alive@80.
- MPTP-alone: SNpc 55, VTA 71, TX alive@80 (no survival_lock).
- WT SNpc alive@80, ATP **1.6229** mM, no survival_lock, dominant POV **mitophagy** (high_ca_stress occupied 19/81 y).
- O2-off and CI-block still collapse: t½ **2.66** s, ATP_end = 0. Fast O2-on plateau **2.065** mM is the modest-modulator η_ref (0.872 vs Astra 0.924), not a new energy source.

S-box / CUSP-HOLO readout taste (observational, not a physics rewrite): combined SNpc dominant POV **degenerating**; WT SNpc mitophagy occupancy 62/81 y. Combined TX dominant POV **transplant_dock**. No AgentAPI `:8780` probe (optional; not required). Hosted NIMs not callable.

## Table vs Astra probe vs Grok published

| Quantity | Astra probe `T130059Z` | Grok published `T130321Z` | **Muse own `T132605Z`** |
|----------|------------------------|---------------------------|-------------------------|
| seed | 20260920 | 20260920 | **20260921** |
| `cusp_m` / modulator | 1.2 / 1.2000 | 1.2 / 1.2000 | **1.15 / 1.1329** |
| `cusp_a` | −0.45 | −0.45 | **−0.42** |
| Combined deaths (SNpc / VTA / TX) | 55 / 63 / 77 | 55 / 63 / 76 | **55 / 59 / 74** |
| TX combined delay vs SNpc | 22 y | 21 y | **19 y** (still dies) |
| WT SNpc ATP (mM) | 1.679 | 1.704 | **1.623** |
| WT SNpc lock / POV | False / mitophagy | False / mitophagy | **False / mitophagy** |
| SNCA SNpc death year | 77 | 79 | **76** |
| MPTP SNpc / VTA / TX | 55 / 76 / alive | 55 / 74 / alive | **55 / 71 / alive** |
| O2-off t½ (s), collapsed | 2.66, True | 2.66, True | **2.66, True** |
| CI-block t½ (s), collapsed | 2.66, True | 2.66, True | **2.66, True** |
| Fast O2-on ATP_end (mM) | 2.425 | 2.425 | **2.065** |
| Combined SNpc POV | high_ca_stress | degenerating | **degenerating** |

Gauss asyn ± ~1 y plus the modest modulator accounts for the year-shifts. Ranking is unchanged: SNpc dies first under combined load; VTA later; TX later still, not immortal.

## Muse knobs (vs Astra JSON)

| Field | Astra | Muse | Why |
|-------|-------|------|-----|
| `seed` | 20260920 | **20260921** | Independent Gauss draws; visibly Muse |
| `cusp_m` | 1.2 | **1.15** | Modest HOLO modulator; not the PSC peak hunt |
| `cusp_a` | −0.45 | **−0.42** | Light CUSP cubic overlay; order x 0.286 vs 0.282 |
| `cusp_b` | 0.06 | **0.06** | Held; do not cross b ≤ 0 |
| biology + TX ticks | Astra table | **unchanged** | Not a ranking break |

Omitted: `n_c`, `atp_per_rev`. VTA knobs, `mptp_ci_cut` 0.58, `mptp_year` 55, `tx_year` 45 untouched.

## Thermodynamic invariants

- `n_c = 8` · `atp_per_rev = 3`
- `cusp_m = 1.15` ∈ **[0.25, 3.0]**; derived modulator 1.1329 (loader clamps `cusp_m`)
- Rotation is not free energy. O2-off and CI-block collapse on the seconds scale.
- Yearly ATP is a quasi-steady snapshot, not a 30 s peak-pump integration.
- EGI `leak_tau` / core physics not rewritten. Severity modulator only.

## Not a PD cure

This is an in-silico precursor map of one post-mitotic DA neuron. Transplant is a bounded modulator of η, leak, SOD, calbindin-like buffering, mitophagy, and α-synuclein clearance — not a new energy source, not gene therapy, not a clinical protocol. Combined load still kills the transplanted cell at year 74. A 19-year delay in this run is not prevention and is not a clinical endpoint. Parkinson's disease is not cured, treated, or prevented here.

## DT#9

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-neuron simulation. Not a Parkinson's disease cure, treatment, diagnostic, gene therapy, or clinical protocol. Not perpetual motion. SNpc DA neurons are post-mitotic: survival under PD-like load is not telomere immortality. Rotary catalysis requires a proton-motive force; the proton-motive force requires electron transport, Complex I, and a terminal acceptor. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.

- synthetic_only=true
- research_prototype=true
- not_a_pd_cure=true
- post_mitotic=true
- dt_ritual_run=false
- compliance_ref="Addendum_5/C-00x"
- risk_flags=["no_clinical","unvalidated","not_perpetual_motion","not_a_pd_cure","hosted_nim_not_called","experimental_PDB_not_predicted_fold"]
- version: receipt `0.1.0` · theory_id `SNPC-DA-CI-ASYN-CA-TX-001` · wm_id `DT-SNPC-DA-RESILIENCE`
