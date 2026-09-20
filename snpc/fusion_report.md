# Singular SNpc DA-neuron resilience (PD-research precursor)

**Run** `20260920T222959Z` · **tag** `pd_precursor` · **policy** `CUSP-SNPC-DA-RESILIENCE-001` · precursor `NA-PSC-IMM-001`

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-neuron simulation. Not a Parkinson's disease cure, treatment, diagnostic, gene therapy, or clinical protocol. Not perpetual motion. SNpc DA neurons are post-mitotic: survival under PD-like load is not telomere immortality. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.

## Why this is not PSC immortality

SNpc DA neurons are post-mitotic. Telomerase / Hayflick is the wrong clock. Survival under Ca2+ pacemaking, Complex I load, cytosolic DA, and α-synuclein is the clock.

## Fast OXPHOS

- O2 on, CI intact: ATP_end = 2.174 mM, collapsed = False
- O2 off: ATP_end = 0.000 mM, t_half = 2.66, collapsed = True
- CI blocked: ATP_end = 0.000 mM, t_half = 2.66, collapsed = True

## Slow neuron (one cell, 80 years)

| Arm | Insult | Alive@80 | Survival lock | Death year | asyn_end | CI_end | POV |
|-----|--------|----------|---------------|------------|----------|--------|-----|
| SNPC | WT | True | False | None | 0.2077 | 0.7522 | high_ca_stress |
| SNPC | SNCA | True | False | None | 0.6758 | 0.6156 | mitophagy |
| SNPC | MPTP | False | False | 55 | 0.2663 | 0.1458 | high_ca_stress |
| SNPC | COMBINED | False | False | 55 | 0.6916 | 0.1213 | high_ca_stress |
| VTA | WT | True | True | None | 0.0628 | 0.8087 | pacemaker_ok |
| VTA | SNCA | True | True | None | 0.2049 | 0.7566 | pacemaker_ok |
| VTA | MPTP | False | False | 73 | 0.1263 | 0.3255 | pacemaker_ok |
| VTA | COMBINED | False | False | 63 | 0.2757 | 0.204 | pacemaker_ok |
| SNPC_TX | WT | True | True | None | 0.0422 | 0.9022 | survival_lock |
| SNPC_TX | SNCA | True | True | None | 0.1518 | 0.8535 | survival_lock |
| SNPC_TX | MPTP | True | False | None | 0.0879 | 0.4882 | transplant_dock |
| SNPC_TX | COMBINED | False | False | 76 | 0.2424 | 0.3891 | high_ca_stress |

## BioNeMo toolkit

- Hosted NIMs callable: `False` (NGC_API_KEY/NVIDIA_API_KEY not set)
- **ATP5F1B** UniProt P06576: 529 aa, PDB 1E79 Rg=None Å
- **SOD2** UniProt P04179: 222 aa, PDB 1N0J Rg=None Å
- **SNCA** UniProt P37840: 140 aa, PDB 1XQ8 Rg=46.978 Å
- **TH** UniProt P07101: 528 aa, PDB 2XSN Rg=36.384 Å
- **NDUFS4** UniProt O43181: 175 aa, PDB None Rg=None Å
- **PINK1** UniProt Q9BXM7: 581 aa, PDB 6EQI Rg=25.712 Å
- **PRKN** UniProt O60260: 465 aa, PDB 5P33 Rg=19.633 Å
- **CALB1** UniProt P05937: 261 aa, PDB 2F33 Rg=18.525 Å

## DT#9

RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-neuron simulation. Not a Parkinson's disease cure, treatment, diagnostic, gene therapy, or clinical protocol. Not perpetual motion. SNpc DA neurons are post-mitotic: survival under PD-like load is not telomere immortality. Claims are bounded to this in-silico run. Not for clinical, diagnostic, production, or regulatory use.
