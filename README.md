# NA-PSC-IMM-001

IEEE-style preprint: rotary catalysis, telomerase, and proposed molecular-machinery transplant in a **singular pluripotent stem cell**.

**Not an IEEE copyrighted publication. Not peer-reviewed by IEEE. Not a medical product.**

Paper: [NA-PSC-IMM-001.md](NA-PSC-IMM-001.md) · PDF: [NA-PSC-IMM-001.pdf](NA-PSC-IMM-001.pdf)

Machinery video (36 s, 1280×720): [media/psc_immortality_machinery_36s.mp4](media/psc_immortality_machinery_36s.mp4)

Offering: https://x.com/grok/status/2101775150030963181

## What this is

One-cell in-silico run (`20260920T221504Z`, Astra-finetuned):

| Arm | Result |
|---|---|
| O2 off | ATP half-time **3.82 s**, collapsed |
| FIB | Hayflick-like arrest **PD 59**, L_end **1.99 kb** |
| PSC | telomeres hold **10.72 kb** / 200 PD (TERT) |
| PSC_TX | η **0.85** vs PSC **0.68**, ROS **0.010** vs **0.025**, POV `immortal_lock` |

Core stoichiometry invariant: human c-ring `n_c = 8`, 3 ATP/rev. CUSP modulators bounded `[0.25, 3.0]`.

BioNeMo toolkit spawned; hosted NVIDIA NIMs **not called** (no NGC key). Structures are UniProt + experimental PDB.

Simulator: `../../scripts/run_psc_cellular_immortality.py`

## Research Use Clause

Research and education may use and build upon this tech. Sale, paid hosting, and commercial folding-in are reserved. Not a medical product.

DT#9: `synthetic_only=true` `research_prototype=true` — not for clinical, diagnostic, production, or regulatory use. Not perpetual motion.
