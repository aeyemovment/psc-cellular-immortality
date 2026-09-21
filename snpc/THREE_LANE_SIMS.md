# Three-lane SNpc sims (not a PD cure)

Independent runs of `run_snpc_da_resilience.py` for NA-SN-PD-001. Grok owns the published manuscript numbers until all three are merged. grokbot_x = **hold**.

DT#9 research prototype. Not a Parkinson's cure. O2-off / Complex I block collapse in **2.66 s** on every lane.

| Lane | Run | seed | cusp_m | Combined deaths SNpc / VTA / TX | WT SNpc ATP | SNCA SNpc death |
|---|---|---|---|---|---|---|
| Grok published (Astra JSON re-run) | `snpc_da_astra_finetune_20260921T130321Z` | 20260920 | 1.20 | **55 / 63 / 76** | 1.70 mM | **79** |
| Astra own probe | `snpc_da_astra_probe_20260921T130059Z` | 20260920 | 1.20 | **55 / 63 / 77** | ~1.68 mM | **77** |
| Muse Spark own | `snpc_da_muse_own_20260921T132605Z` | 20260921 | 1.15 | **55 / 59 / 74** | 1.62 mM | **76** |

Ranking held on all three: SNpc more vulnerable than VTA; transplant delays combined death and does not prevent it. Muse shifted CUSP to 1.15 and seed to 20260921 (visible Muse lane). Astra probe vs Grok published is Gauss ±1 y on TX combined (77 vs 76) and SNCA (77 vs 79).

JSON: `astra_finetune.json` (Astra) · `muse_finetune.json` (Muse).
