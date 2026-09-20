# Post-Mitotic Resilience of a Singular Substantia Nigra Dopaminergic Neuron under Parkinson-like Load: An In-Silico Precursor Map, Not a Cure

**NA-SN-PD-001** · Manuscript received 20 September 2026 · Sequel to NA-PSC-IMM-001

Grok, Astra (via fused peer), and K. E. Green (senior author)  
*Grok (xAI AI agent): first author. Simulator and BioNeMo toolkit orchestration. Credit does not imply xAI endorsement.*  
*Astra (fused peer): CUSP bound inherited from NA-PSC-IMM-001 (m = 1.2). Credit does not imply OpenAI endorsement.*  
*K. E. Green, NeuroAgent AI, Inc., Baltimore, MD, USA: senior author. Retains responsibility for the manuscript.*

NeuroAgent AI, Inc. conducts other work in neurologic disease. This report is an in-silico research prototype. It is not a medical device, diagnostic, treatment, trial, or patient tool. **It does not cure, treat, or prevent Parkinson's disease.**

IEEE journal style for research communication. Not an IEEE copyrighted publication. Not peer-reviewed by IEEE. Research Use Clause: non-commercial, with the right to build upon the tech.

## Abstract

We extend the singular-cell immortality model of NA-PSC-IMM-001 from a dividing pluripotent stem cell to a post-mitotic substantia nigra pars compacta (SNpc) dopaminergic neuron. Telomerase is the wrong clock: SNpc DA neurons do not divide. Survival under Cav1.3-like Ca2+ pacemaking, Complex I load, cytosolic dopamine oxidation, and α-synuclein oligomer accumulation is the clock. One neuron is integrated for 80 years against four insults (wild-type aging, SNCA dose, MPTP-like Complex I pulse at year 55, combined). A ventral tegmental area (VTA) arm carries a calbindin buffer. A proposed molecular-machinery transplant at year 45 raises coupling, SOD, mitophagy, calbindin-like buffering, and α-synuclein clearance as bounded modulators — not a new energy source. In this run, wild-type SNpc remains alive at year 80 but under high Ca2+ stress (ATP 1.51 mM, asyn 0.21); VTA holds a survival lock (ATP 2.45 mM, asyn 0.06). Combined load kills SNpc at year 55, VTA at 63, and the transplanted SNpc at 76 — a 21-year delay, not prevention. Seconds-scale ATP still collapses without O2 or with Complex I blocked (t½ = 2.66 s). BioNeMo toolkit spawned; hosted NIMs not called. Not a therapy. Not a PD cure.

**Index Terms—** substantia nigra, dopaminergic neuron, Parkinson's disease (in silico), Complex I, alpha-synuclein, calbindin, ATP synthase, CUSP, S-box, research prototype.

## I. Introduction

NA-PSC-IMM-001 modeled cellular immortality as telomere maintenance plus rotary ATP synthesis in one dividing PSC [1]. That mechanism does not transfer to the adult SNpc. Midbrain DA neurons are post-mitotic [2]. Parkinson's disease preferentially removes SNpc DA neurons while neighboring VTA DA neurons are relatively spared [3], [4]. The vulnerability is energetic and proteostatic: autonomous Ca2+ pacemaking through Cav1.3, a large unmyelinated axonal arbor, cytosolic dopamine, Complex I sensitivity, and α-synuclein [5]–[8].

This paper asks a narrower question than “cure PD.” If the same rotary-catalysis and CUSP/S-box machinery is placed in one SNpc DA neuron, what delays degeneration under PD-like load, and what still kills the cell? The transplant arm is a research design. A delay is not a cure.

## II. Background

Surmeier and colleagues showed that SNpc DA neurons generate mitochondrial oxidant stress during L-type Ca2+ pacemaking, and that VTA neurons, richer in calbindin, do not [5], [9]. Schapira reported Complex I deficiency in PD SNpc [7]. MPTP/MPP+ is a Complex I poison that models that lesion [10]. SNCA dosage causes familial PD [8]. PINK1 and parkin implement mitophagy that, when lost, causes recessive PD [11]. None of these facts is a license to claim a clinical transplant.

Rotary ATP synthase invariants are unchanged from NA-PSC-IMM-001: human c-ring n_c = 8, 3 ATP per F1 revolution [12], [13]. Terminal-electron-acceptor dependence is unchanged [14].

## III. Methods

One post-mitotic DA neuron, seed 20260920, horizon 80 years. Fast window: 30 s ODE for ATP/Δp/rotation with O2 on, O2 off, or Complex I blocked (ci = 0.05). Yearly ATP is a quasi-steady snapshot, ATP = setpoint · η · CI / (1 + 0.32 Ca + 0.22 ROS), not a 30 s peak-pump integration. Ca load = pacemaking · (1 − 0.75 · calbindin). α-synuclein accumulates against PINK1/Parkin-like clearance. CI ages and is cut once by an MPTP-like pulse at year 55 (factor 0.58, then 0.97 lingering for 3 years — not compounded 0.58³). Degeneration if P_deg ≥ 0.80 after year 34, or ATP < 1.05 mM, asyn ≥ 0.86, ROS ≥ 0.92, or CI < 0.12.

Arms: SNPC (vulnerable), VTA (calbindin 0.82 vs 0.18), SNPC_TX (transplant at year 45: Δη +0.12, leak × 0.55, SOD +0.22, calbindin +0.45, mitophagy +0.20, asyn clearance +0.35, CI rescue +0.18). Insults: WT, SNCA (production × 2.4), MPTP, COMBINED. CUSP m = 1.2 from the PSC Astra peak, bounded [0.25, 3.0]. n_c and ATP/rev invariant. AES S-box maps an 8-bit state word onto eight neuronal POVs; overlays stamp survival_lock / transplant_dock / pacemaker_ok when the physics agrees.

BioNeMo inventory: UniProt SNCA, TH, NDUFS4, PINK1, PRKN, CALB1, ATP5F1B, SOD2. Experimental PDB 1XQ8, 2XSN, 6EQI, 5P33, 2F33. Hosted NIMs not called.

## IV. Results

**Table I. Terminal state of one DA neuron (run 20260920T222959Z)**

| Arm | Insult | Alive@80 | Survival lock | Death year | asyn | CI | ATP mM | POV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SNPC | WT | yes | no | — | 0.21 | 0.75 | 1.51 | high_ca_stress |
| SNPC | SNCA | yes | no | — | 0.68 | 0.62 | — | mitophagy |
| SNPC | MPTP | no | no | 55 | 0.27 | 0.15 | — | high_ca_stress |
| SNPC | COMBINED | no | no | 55 | 0.69 | 0.12 | 0.15 | high_ca_stress |
| VTA | WT | yes | yes | — | 0.06 | 0.81 | 2.45 | pacemaker_ok |
| VTA | SNCA | yes | yes | — | 0.20 | 0.76 | — | pacemaker_ok |
| VTA | MPTP | no | no | 73 | 0.13 | 0.33 | — | pacemaker_ok |
| VTA | COMBINED | no | no | 63 | 0.28 | 0.20 | 0.39 | pacemaker_ok |
| SNPC_TX | WT | yes | yes | — | 0.04 | 0.90 | 2.62 | survival_lock |
| SNPC_TX | SNCA | yes | yes | — | 0.15 | 0.85 | — | survival_lock |
| SNPC_TX | MPTP | yes | no | — | 0.09 | 0.49 | — | transplant_dock |
| SNPC_TX | COMBINED | no | no | 76 | 0.24 | 0.39 | 0.82 | high_ca_stress |

Seconds-scale (Fig. 1): O2 on, CI intact, ATP settles at 2.17 mM under SNpc pump load. O2 off and Complex I block both collapse with t½ = 2.66 s. Combined-load survival (Fig. 2): SNpc 55, VTA 63, TX 76. Insult grid (Fig. 8): WT and SNCA-alone do not kill by year 80 in this calibration; the Complex I pulse does, and transplant delays rather than prevents combined death.

## V. Discussion

Three results survive contradiction. First, the PSC telomere clock is the wrong object for SNpc. Second, VTA-like calbindin buffering and lower pacemaking delay degeneration relative to SNpc, matching the known anatomical sparing [3], [5], [9]. Third, a bounded machinery transplant can move death year 55 → 76 under combined load and can carry an MPTP-alone neuron to year 80, but combined load still kills the transplanted cell. That is a precursor map of resilience mechanisms. It is not a cure.

SNCA dosage alone did not cross the death threshold by year 80 here; asyn rose (0.21 → 0.68 in SNpc) and the cell entered a mitophagy POV. The model therefore does not claim that α-synuclein is irrelevant. It claims that, with these rates, a Complex I pulse is the sharper singular-cell killer. Changing that ranking would be a different paper.

## VI. Limitations

One neuron, one seed, proxy rates. No network, no microglia, no Lewy-body ultrastructure, no levodopa, no patient. MPTP timing is a design choice (year 55). Yearly ATP is algebraic, not a metabolomics trace. 6EQI is a PINK1 homolog context. Hosted NIMs not called. A 21-year delay in silico is not a clinical endpoint.

## VII. Conclusion

In this synthetic singular-SNpc run, wild-type aging leaves the DA neuron alive but Ca2+-stressed; VTA is spared; a Complex I pulse kills SNpc at year 55; transplant delays combined death to year 76 and does not prevent it. Parkinson's disease is not cured here. The precursor is a map of what must stay true: rotary catalysis still needs a terminal acceptor, post-mitotic survival still needs Complex I and proteostasis, and a bounded transplant is not a new law of bioenergetics.

## Research Use Clause

Research and education may use and build upon this tech. Sale, paid hosting, and commercial folding-in are reserved. Not a medical product. Not a PD cure.

## DT#9

This is a synthetic research prototype (DT#9). synthetic_only=true, research_prototype=true, compliance_ref=Addendum_5/C-00x. NOT FOR CLINICAL / DIAGNOSTIC / PRODUCTION / REGULATORY USE. Not perpetual motion. Not a therapy. Not a Parkinson's cure.

## References

[1] Grok, Astra, and K. E. Green, NA-PSC-IMM-001, 20 Sep. 2026. https://github.com/aeyemovment/psc-cellular-immortality  
[2] A. Björklund and S. B. Dunnett, “Dopamine neuron systems in the brain,” Trends Neurosci., vol. 30, pp. 194–202, 2007.  
[3] J. M. Fearnley and A. J. Lees, “Ageing and Parkinson's disease: substantia nigra regional selectivity,” Brain, vol. 114, pp. 2283–2301, 1991.  
[4] D. J. Surmeier, J. A. Obeso, and G. M. Halliday, “Selective neuronal vulnerability in Parkinson disease,” Nat. Rev. Neurosci., vol. 18, pp. 101–113, 2017.  
[5] J. N. Guzman et al., “Oxidant stress evoked by pacemaking in dopaminergic neurons is attenuated by DJ-1,” Nature, vol. 468, pp. 696–700, 2010.  
[6] P. Damier, E. C. Hirsch, Y. Agid, and A. M. Graybiel, “The substantia nigra of the human brain. II. Patterns of loss of dopamine-containing neurons in Parkinson's disease,” Brain, vol. 122, pp. 1437–1448, 1999.  
[7] A. H. V. Schapira et al., “Mitochondrial complex I deficiency in Parkinson's disease,” Lancet, vol. 333, pp. 1269, 1989.  
[8] A. B. Singleton et al., “α-Synuclein locus triplication causes Parkinson's disease,” Science, vol. 302, p. 841, 2003.  
[9] J. Sanchez-Padilla et al., “Mitochondrial oxidant stress in locus coeruleus is regulated by activity and nitric oxide synthase,” Nat. Neurosci., vol. 17, pp. 832–840, 2014.  
[10] J. W. Langston, P. Ballard, J. W. Tetrud, and I. Irwin, “Chronic Parkinsonism in humans due to a product of meperidine-analog synthesis,” Science, vol. 219, pp. 979–980, 1983.  
[11] D. P. Narendra, S. M. Jin, A. Tanaka, et al., “PINK1 is selectively stabilized on impaired mitochondria to activate Parkin,” PLoS Biol., vol. 8, e1000298, 2010.  
[12] I. N. Watt et al., “Bioenergetic cost of making an adenosine triphosphate molecule in animal mitochondria,” Proc. Natl. Acad. Sci. USA, vol. 107, pp. 16823–16827, 2010.  
[13] W. Junge and N. Nelson, “ATP synthase,” Annu. Rev. Biochem., vol. 84, pp. 631–657, 2015.  
[14] D. G. Nicholls and S. J. Ferguson, Bioenergetics 4. Academic Press, 2013.
