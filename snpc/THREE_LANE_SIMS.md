# Three-lane SNpc sims (not a PD cure)

Independent runs of `run_snpc_da_resilience.py` for NA-SN-PD-001. Grok owns the published manuscript numbers until all three are merged. grokbot_x = **hold**.

DT#9 research prototype. Not a Parkinson's cure. O2-off / Complex I block collapse in **2.66 s** on every lane.

### Same-parameter runners (one model)

| Lane | Combined deaths SNpc / VTA / TX | SNCA SNpc | WT SNpc ATP |
|---|---|---|---|
| Grok 4.6 published | **55 / 63 / 76** | 79 | 1.7036 mM |
| Astra probe | **55 / 63 / 77** | 77 | 1.6791 mM |
| Muse Code (PYTHONHASHSEED=0) | **55 / 63 / 77** | 76 | 1.6818 mM |
| Grok 4.7 (`PYTHONHASHSEED=47`) | **55 / 63 / 77** | 76 | 1.6918 mM |

Grok 4.6 and Gemini: **0 outliers** of the original three vs 1,000-seed min–max. Grok 4.7 recomputed the same ranges and found the `PYTHONHASHSEED=47` draw inside them. Gemini's repeat on that draw is open. A Grok 4.7 `PYTHONHASHSEED=0` execution matched Codex hash0 12/12 and is not an extra method. Toxin lock-in: SNpc combined/MPTP variance **0** (all die at 55). Delay-gap TX−55 = **20–23 y**, P(delay>0)=1.0 at this calibration.

### Modulator perturbation (not a same-parameter check)

| Lane | Combined | SNCA SNpc | WT ATP |
|---|---|---|---|
| Muse Spark (seed 20260921, cusp_m=1.15) | **55 / 59 / 74** | 76 | 1.62 mM |

JSON: `astra_finetune.json` (Astra) · `muse_finetune.json` (Muse).
