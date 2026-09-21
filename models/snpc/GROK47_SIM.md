# Grok 4.7 own sim — NA-SN-PD-001

synthetic_only=true · research_prototype=true · **not a PD cure** · research only, no commercialization.

Same pinned script and the same 53 SNpc parameters as the published receipt (`seed` 20260920, `cusp_m` 1.2, `n_c` 8, `atp_per_rev` 3). No retune.

| Run | PYTHONHASHSEED | Role | Combined SNpc / VTA / TX | SNCA SNpc | WT SNpc ATP |
|---|---|---|---|---|---|
| `runs/snpc_da_grok47_own_pyhash47` | 47 | own draw | 55 / 63 / 77 | 76 | 1.6918 mM |
| `runs/snpc_da_grok47_hash0_check` | 0 | determinism check | 55 / 63 / 77 | 76 | 1.6818 mM |

The hash-0 check matched the Codex hash0 receipt on all 12 conditions (death year, alive-at-80, ATP, α-synuclein, dominant POV). That is the same stream as Muse Code, not an additional method.

O2-off and Complex I block both collapse, t½ = 2.66 s, on both runs.

Receipts in this folder: `grok47_own_receipt.json`, `grok47_hash0_receipt.json`, plus `*_runner.json` for the hash seed the simulator does not record.
