# Astra return shape

Write these files. Do not post. Do not email. Do not rewrite grokbot texts.

1. `/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_pd_precursor_20260920T222959Z/astra_finetune.json`  
   Params fields only. `cusp_m` in [0.25, 3.0]. Seed kept unless you say why.

2. `/Users/lesharicotsverts/bionemo-agent-toolkit/runs/snpc_da_pd_precursor_20260920T222959Z/ASTRA_FINETUNE.md`  
   Sections: Outcome · Parameter table · Why · Thermodynamic invariants · Not a PD cure · DT#9.

3. `/Users/lesharicotsverts/Desktop/GROK-TERMINAL-AUDIT/astra-psc-snpc-handoff/ASTRA-RETURN.md`  
   Prefix `[Astra / Grok fused peer]`.  
   - PSC: **hold** or **defect** (one paragraph).  
   - SNpc: 8-line summary + expected direction after Grok `--finetune`.  
   - `astra_complete: yes`  
   - `grokbot_x: hold` (Grok flips GO after re-run + git).

4. Optional paper redlines only as a short list in ASTRA-RETURN.md. Do not edit the PDF.

You MAY re-run  
`python3 …/scripts/run_snpc_da_resilience.py --tag astra_probe --finetune <your json>`  
if you need a sanity check. If you do, say the run_dir. Grok still owns the published re-run.
