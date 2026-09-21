# Astra handoff — entire PSC + SNpc stack

**From:** Grok green (this lane)  
**To:** Astra (fused peer). **No send. No X. No email.**  
**Then back to:** Grok (re-run, paper numbers, git)  
**Then to:** grokbot @theNeuroagent (posts only after Grok sets `grokbot_x: go`)  
**Operator:** package the entire thing → Astra → Grok → grokbot; commit to git.

Public git (already live): https://github.com/aeyemovment/psc-cellular-immortality

This is a synthetic research prototype (DT#9). Not a medical product. **Not a Parkinson's cure.** Not an IEEE publication of record. Not perpetual motion.

## Order (do not skip)

1. Astra reads this packet + the two simulators + the two receipts. Fine-tunes **SNpc** (never got its own Astra pass). Reviews **PSC** (already Astra-finetuned; hold unless a real defect).
2. Astra writes the return files listed in `04-RETURN-SHAPE.md`. Stops.
3. Grok re-runs `run_snpc_da_resilience.py --finetune …`, updates NA-SN-PD-001 if numbers move, commits git, then flips grokbot GO.
4. Grokbot posts from `@theNeuroagent` only. Exact texts in `grokbot-psc-snpc/` after GO.

## Invariants (fail closed)

- `n_c = 8`, `atp_per_rev = 3`. Omit from JSON or they are forced.
- CUSP `cusp_m` ∈ **[0.25, 3.0]**.
- Rotation is not free energy. O2-off and CI-block must still collapse ATP on seconds.
- SNpc is **post-mitotic**. Do not put TERT/Hayflick back into the neuron model.
- Do not write “cure PD”, “treat PD”, “clinical”, “validated”, “gene therapy product”.
- kemar = operator = friend. Human gate: **Text Kemar**. Prefix: `[Astra / Grok fused peer]`.
