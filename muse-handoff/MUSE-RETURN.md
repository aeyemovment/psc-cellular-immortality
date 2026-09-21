# Muse Spark return — own SNpc sim (NA-PSC-IMM-001 / NA-SN-PD-001)

**Muse Spark** (Spark Muse). Commander: Grok green. No send. No X. No email. No iMessage. No DT ritual. No grokbot post.  
kemar = operator = friend. Human gate: Text Kemar.

synthetic_only=true · research_prototype=true · compliance_ref="Addendum_5/C-00x"  
NOT clinical / diagnostic / production / regulatory. **Not a PD cure.** Claims bounded to this in-silico run.

## Own sim (not a copy of Astra)

Independent `--tag muse_own` run of `scripts/run_snpc_da_resilience.py`. Astra probe and Grok published dirs were not overwritten. PDF not edited.

**run_dir:** `/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_muse_own_20260921T132605Z`  
**finetune:** `/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_pd_precursor_20260920T222959Z/muse_finetune.json`  
**note:** `runs/snpc_da_muse_own_20260921T132605Z/MUSE_SIM.md`

Muse knobs: seed **20260921**; `cusp_m = 1.15` (modulator 1.1329 ∈ [0.25, 3.0]); `cusp_a = −0.42` (light CUSP-HOLO cubic overlay); `cusp_b = 0.06` held. Astra SNpc biology / TX ticks kept. `n_c` / `atp_per_rev` omitted (forced 8 / 3).

## Numbers for Grok merge

| Item | Muse own |
|------|----------|
| Combined deaths (SNpc / VTA / TX) | **55 / 59 / 74** |
| TX combined delay | 19 y (55 → 74); still dies — not prevention |
| WT SNpc ATP | **1.6229 mM**, alive@80, survival_lock=False, POV mitophagy |
| SNCA SNpc death year | **76** (asyn_end 0.7969, mitophagy) |
| O2-off t½ | **2.66 s**, collapsed=True, ATP_end=0 |
| CI-block t½ | **2.66 s**, collapsed=True, ATP_end=0 |
| Fast O2-on ATP_end | 2.065 mM, collapsed=False |

Ranking: SNpc more vulnerable than VTA (combined 55 vs 59; SNCA SNpc dies, VTA SNCA lives; MPTP 55 vs 71). Transplant delays combined death, does not prevent it. Post-mitotic: no TERT / Hayflick. Complex I pulse remains the sharper singular-cell killer (combined and MPTP both 55).

Vs Astra probe 55/63/77 and Grok published 55/63/76: Muse VTA and TX combined deaths move earlier (~4 y / ~2–3 y) under the modest modulator. Not a ranking break. Gauss ± ~1 y on asyn.

## cusp_holo_fusion summary

- **agentapi source:** not probed (optional; loopback `127.0.0.1:8780` not required for this sim). Do not claim :8780 is up.
- **holo n_active:** not observed (no infer payload this run)
- **severity_mod:** `cusp_m=1.15` → derived modulator **1.1329** (bounds 0.25–3.0). Core `n_c=8`, `atp_per_rev=3` invariant.
- **S-box POV:** combined SNpc dominant **degenerating**; WT mitophagy 62/81 y; TX combined **transplant_dock**
- **dt_ritual_run=false**

## Gaps

- searches did not locate a live AgentAPI `:8780` health probe this session (not run)
- searches did not locate hosted BioNeMo NIMs (`NGC_API_KEY` / `NVIDIA_API_KEY` not set); PDB Rg from local experimental files only
- no TERT in this neuron model (by design)
- no claim that 19 y delay is a clinical endpoint

## Gates

- `muse_complete: yes`
- `grokbot_x: hold`

Hand back to Grok commander to merge both sims into NA-PSC-IMM-001 / NA-SN-PD-001. Grok flips grokbot. Text Kemar before any public claim.
