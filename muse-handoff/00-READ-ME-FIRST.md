# Muse Spark handoff — own sim for the immortality / SNpc papers

**From:** Grok green (commander)  
**To:** Muse Spark  
**After:** Astra's own sim (probe `snpc_da_astra_probe_20260921T130059Z`)  
**Then back to:** Grok (merge both sims into NA-PSC-IMM-001 / NA-SN-PD-001, then grokbot)  
**Do not:** send, post, email, iMessage, DT ritual, grokbot GO.

Public git: https://github.com/aeyemovment/psc-cellular-immortality

DT#9 research prototype. **Not a PD cure.** Not a medical product. Not an IEEE publication of record.

## Why you

Astra already fine-tuned Grok's SNpc knobs and ran **their own probe sim**. Operator: Muse does **the same** — an independent sim to include in the paper — then results return to Grok. You are not replacing Astra. You are a second independent run.

## What to run

Use the existing simulators (do not rewrite physics invariants):

- SNpc (primary): `/Users/lesharicotsverts/bionemo-agent-toolkit/scripts/run_snpc_da_resilience.py`
- Optional PSC check only: `/Users/lesharicotsverts/bionemo-agent-toolkit/scripts/run_psc_cellular_immortality.py`

**Your own sim means:**

1. Write `muse_finetune.json` (Params fields only). You MAY change seed (recommend `20260921` so it is visibly Muse, not Astra's `20260920`). You MAY apply a light CUSP-HOLO / S-box POV overlay in the **note**, but do not break `n_c=8` / `atp_per_rev=3`. `cusp_m` ∈ [0.25, 3.0].
2. Run:  
   `python3 …/run_snpc_da_resilience.py --tag muse_own --finetune <your json>`
3. Keep ranking: SNpc more vulnerable than VTA; transplant delays combined death, does not prevent it. O2-off and CI-block must still collapse.
4. No TERT/Hayflick in the neuron. No “cure PD”.

Astra probe (do not overwrite):  
`/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_astra_probe_20260921T130059Z/`  
Grok published re-run:  
`/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_astra_finetune_20260921T130321Z/`

## Return files

1. `/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_pd_precursor_20260920T222959Z/muse_finetune.json`
2. `/Users/lesharicotsverts/bionemo-agent-toolkit/runs/<your muse_own run dir>/` (script creates this)
3. `/Users/lesharicotsverts/Desktop/GROK-TERMINAL-AUDIT/muse-psc-snpc-handoff/MUSE-RETURN.md`  
   Prefix not required as Astra's; say **Muse Spark**. Include run_dir, combined deaths, WT ATP, SNCA death year, t½ O2-off, `muse_complete: yes`, `grokbot_x: hold`.
4. Short `MUSE_SIM.md` in your run dir (Outcome · table vs Astra probe vs Grok published · DT#9 · not a PD cure).

Do not edit the PDF. Do not flip grokbot. Hand back to Grok.
