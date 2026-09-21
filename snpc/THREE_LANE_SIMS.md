# Three-lane SNpc sims (not a PD cure)

Independent runs of `run_snpc_da_resilience.py` for NA-SN-PD-001. Grok owns the published manuscript numbers until all three are merged. grokbot_x = **hold**.

DT#9 research prototype. Not a Parkinson's cure. O2-off / Complex I block collapse in **2.66 s** on every lane.

### Same-parameter trio (one model, three runners)

| Lane | Combined deaths SNpc / VTA / TX | SNCA SNpc | WT SNpc ATP |
|---|---|---|---|
| Grok published | **55 / 63 / 76** | 79 | 1.7036 mM |
| Astra probe | **55 / 63 / 77** | 77 | 1.6791 mM |
| Muse Code (PYTHONHASHSEED=0) | **55 / 63 / 77** | 76 | 1.6818 mM |

Gemini + Grok independent reviews: **0 outliers** vs 1,000-seed min–max. Toxin lock-in: SNpc combined/MPTP variance **0** (all die at 55). Delay-gap TX−55 = **20–23 y**, P(delay>0)=1.0 at this calibration.

### Modulator perturbation (not a same-parameter check)

| Lane | Combined | SNCA SNpc | WT ATP |
|---|---|---|---|
| Muse Spark (seed 20260921, cusp_m=1.15) | **55 / 59 / 74** | 76 | 1.62 mM |

JSON: `astra_finetune.json` (Astra) · `muse_finetune.json` (Muse).
