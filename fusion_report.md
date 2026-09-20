# Singular PSC cellular-immortality simulation

**Run** `20260920T221504Z` · **tag** `astra_finetune` · **policy** `CUSP-PSC-IMMORTALITY-001`

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-cell simulation. Not a clinical therapy, gene-therapy product, anti-aging treatment, or perpetual-motion device. Rotary catalysis requires a proton-motive force; the proton-motive force requires electron transport and a terminal acceptor. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.

## Equation (research model)

```
e− → CI–CIV → O2 (terminal acceptor) → Δp
Δp → ATP synthase (n_c protons/rev, 3 ATP/rev) → ATP
L_{n+1} = L_n − δ + TERT_add · activity
CUSP: x^3 + a x + b = 0  (modulates η, TERT, SOD in [0.25, 3.0])
S-box: AES_SBOX[state_byte] → POV class
```

## Fast OXPHOS (one cell, seconds)

- O2 on: ATP_end = 3.365 mM, mean |rps| = 167.2, collapsed = False
- O2 off: ATP_end = 0.000 mM, t_half = 3.8200000000000003, collapsed = True

## Slow lineage (one cell, 200 PD)

| Arm | Immortal lock | Senesce PD | L_end (kb) | P_sen tail | dominant POV |
|-----|---------------|------------|------------|------------|--------------|
| FIB | False | 59 | 1.9887 | 1.0 | G2_checkpoint |
| PSC | True | None | 10.7243 | 0.0 | transplant_dock |
| PSC_TX | True | None | 11.0003 | 0.0 | immortal_lock |

## BioNeMo toolkit

- Hosted NIMs callable: `False` (NGC_API_KEY/NVIDIA_API_KEY not set in this process)
- Structure source: experimental PDB + UniProt sequences. No fabricated pLDDT.
- **ATP5F1B** UniProt P06576: 529 aa, PDB 1E79 Rg=44.584 Å, CA=3316
- **ATP5MC1** UniProt P05496: 136 aa, PDB 2XND Rg=57.076 Å, CA=3892
- **TERT** UniProt O14746: 1132 aa, PDB 7BG9 Rg=39.795 Å, CA=1085
- **SOD2** UniProt P04179: 222 aa, PDB 1N0J Rg=22.908 Å, CA=396

## DT#9

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-cell simulation. Not a clinical therapy, gene-therapy product, anti-aging treatment, or perpetual-motion device. Rotary catalysis requires a proton-motive force; the proton-motive force requires electron transport and a terminal acceptor. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.
