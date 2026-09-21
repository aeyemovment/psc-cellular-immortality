# Grok's version — independent analysis of Grok / Astra / Muse methods and findings

**For Fable.** Commander: Grok green. grokbot_x = **hold**. No send. No X.

synthetic_only=true · research_prototype=true · NOT clinical/diagnostic/production/regulatory · **NOT a PD cure** · in-silico only.
Computed 2026-09-21 from files cited. Recomputed from `ensemble/outcomes.csv` (12,000 rows). SHA-256 of that CSV matches the bundle receipt (`a8f39ba2…f9f7587`).

Gemini's review (`/tmp/muse-code-own-sim/REVIEW_MUSE_CODE.md`) was read **after** the criterion below was written and **after** the ensemble recompute. Agreement is reported, not copied.

## 0. What the three (plus one) methods actually are

| Label | What it is | Combined SNpc/VTA/TX | Same 53/44 params? |
|---|---|---|---|
| Grok published | Archive / unrecorded PYTHONHASHSEED | 55 / 63 / **76** | yes (one draw) |
| Astra probe | Same knobs, Astra JSON | 55 / 63 / **77** | yes (one draw) |
| Muse Code own | Independent runner, PYTHONHASHSEED=0, no retune | 55 / 63 / **77** | yes (12/12 vs Codex hash0) |
| Muse Spark own | **Different** seed 20260921, cusp_m=1.15 | 55 / 59 / **74** | **no** — modulator perturbation |

Honesty flag (agree with Gemini): “3 methods” on the same-parameter axis = 3 **runners** on **one** calibrated model, ~2–3 RNG streams. The 1,000-seed ensemble is the stochastic evidence. Muse Spark 55/59/74 is a fourth **parameter** lane, not a same-parameter check.

## 1. Criterion (stated before the outlier test)

Same-parameter realizations are consistent iff (a) 53 SNpc + 44 PSC nominal params match, (b) every event year sits in the ensemble min–max for that condition, (c) alive/censored pattern matches conditions with death fraction 0 or 1. Outside min–max, or an alive/dead flip against a 0/1 fraction, would be implementation error.

**Result: pass.** 0 outliers in 21 event-year checks + 3 WT-ATP checks (all three ATP values inside ensemble p2.5–p97.5 1.665–1.707 mM). SHA-256 of `outcomes.csv` matches `ensemble/summary.json` artifacts field. Bundle medians recomputed identically.

Gemini's outlier count (36) counted more cells; the pass/fail is the same. I do **not** treat Gemini's 36 vs my 21 as a conflict — different cell lists, same conclusion.

## 2. Statistics (RNG-draw spread at one calibration — not biology CIs)

Recomputed numpy-linear quantiles, n=1,000/condition:

| Condition | Deaths | Fraction | Median | p2.5–p97.5 | Min–max | Sample var |
|---|---|---|---|---|---|---|
| SNpc COMBINED | 1,000 | 1.000 | 55 | 55–55 | 55–55 | **0** |
| SNpc MPTP | 1,000 | 1.000 | 55 | 55–55 | 55–55 | **0** |
| SNpc SNCA | 999 | 0.999 | 78 | 76–79 | 75–80 | 0.87 |
| VTA COMBINED | 1,000 | 1.000 | 63 | 62–64 | 61–64 | 0.38 |
| VTA MPTP | 1,000 | 1.000 | 75 | 73–76 | 72–77 | 0.67 |
| TX COMBINED | 1,000 | 1.000 | 76 | 75–78 | 75–78 | 0.41 |
| WT all + VTA SNCA + TX SNCA + TX MPTP | 0 | 0.000 | — | — | censored@80 | — |

Trio vs ranges: SNCA 79/77/76 ∈ [75,80]; TX combined 76/77/77 ∈ [75,78]; VTA MPTP 74/76/74 ∈ [72,77].

## 3. New methods used here (not in Gemini's write-up)

1. **CSV integrity:** SHA-256 of `outcomes.csv` vs bundle `summary.json` artifacts hash — match.
2. **Lock-in test:** sample variance of death year identically 0 for SNpc COMBINED and SNpc MPTP. That is structural coupling to the year-55 toxin pulse, not “robustness.”
3. **Delay-gap distribution:** because SNpc combined is locked at 55, TX combined death − 55 is the delay. Ensemble: median **21 y**, min–max **20–23 y**, P(delay > 0) = **1.0**, P(TX survives combined) = **0**. The transplant-delay claim is **certain at this calibration** and **untested under parameter perturbation** (except Muse Spark's cusp_m=1.15, which still delays: 55→74).

## 4. Top-3 untested assumptions (agree with Gemini; wording is Grok's)

1. Calibration was aimed at late SNCA death + delay-without-prevention (Astra finetune note). TX ticks were trimmed until combined TX still died.
2. Ensemble varies RNG only. Toxin schedule, thresholds, and TX magnitudes are point values.
3. Year-80 fields on dead trajectories are algorithmic continuations. No network, immune, or graft biology.

## 5. Verdict

VERDICT: include with revision — same as Gemini on the three-way table (55/63/76 vs 55/63/77 vs 55/63/77), toxin lock-in, and the three caveats. **Add** the delay-gap (20–23 y, P>0 = 1 at this calibration) and **label Muse Spark 55/59/74 as a modulator perturbation, not a third same-parameter method.** Fold into NA-SN-PD-001 Methods + Discussion. grokbot stays hold until Fable returns.

## Paper edits Grok will make (this pass)

- Co-authors: Astra, Muse Spark, Muse Code, Gemini (independent stats), Codex (ensemble); K. E. Green senior.
- Methods: same-parameter trio, 1,000-seed ensemble, hash-seed caveat, Grok lock-in + delay-gap.
- Discussion: Table of three-way deaths; lock-in; delay-gap; three assumptions; Muse Spark variant separate.
- Do not call percentiles confidence intervals. Do not call this a PD cure.

## Paths

- This file: `Desktop/GROK-TERMINAL-AUDIT/fable-psc-snpc-handoff/GROK-OWN-REVIEW.md`
- Gemini (for Fable, not overwritten): `/tmp/muse-code-own-sim/REVIEW_MUSE_CODE.md`
- Muse Code sim: `Desktop/GROK-TERMINAL-AUDIT/muse-psc-snpc-handoff/MUSE-CODE-OWN-SIM.md`
- Ensemble: `Desktop/GROK-TERMINAL-AUDIT/codex-psc-snpc-reproduction-20260921/ensemble/`
