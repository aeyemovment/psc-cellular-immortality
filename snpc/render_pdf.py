#!/usr/bin/env python3
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "NA-SN-PD-001.pdf"
FIG = ROOT / "figures"
fontroot = Path("/System/Library/Fonts/Supplemental")
for name, filename in [
    ("Georgia", "Georgia.ttf"),
    ("GeorgiaBold", "Georgia Bold.ttf"),
    ("GeorgiaItalic", "Georgia Italic.ttf"),
    ("GeorgiaBoldItalic", "Georgia Bold Italic.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, str(fontroot / filename)))
pdfmetrics.registerFontFamily("Georgia", normal="Georgia", bold="GeorgiaBold", italic="GeorgiaItalic", boldItalic="GeorgiaBoldItalic")

navy = colors.HexColor("#14324e")
gray = colors.HexColor("#536473")
rule = colors.HexColor("#c5ced6")
styles = {
    "title": ParagraphStyle("title", fontName="GeorgiaBold", fontSize=13, leading=17, alignment=TA_CENTER, textColor=navy, spaceAfter=8),
    "meta": ParagraphStyle("meta", fontName="Georgia", fontSize=8.3, leading=11.2, alignment=TA_CENTER, textColor=gray, spaceAfter=5),
    "h2": ParagraphStyle("h2", fontName="GeorgiaBold", fontSize=11, leading=14, textColor=navy, spaceBefore=11, spaceAfter=5),
    "body": ParagraphStyle("body", fontName="Georgia", fontSize=9.4, leading=13.0, alignment=TA_JUSTIFY, textColor=colors.HexColor("#17202b"), spaceAfter=6),
    "caption": ParagraphStyle("caption", fontName="GeorgiaBold", fontSize=8.4, leading=11, textColor=navy, spaceBefore=3, spaceAfter=7),
    "ref": ParagraphStyle("ref", fontName="Georgia", fontSize=8.0, leading=11.0, leftIndent=12, firstLineIndent=-12, spaceAfter=3.5),
    "th": ParagraphStyle("th", fontName="GeorgiaBold", fontSize=6.8, leading=9.0, textColor=navy),
    "td": ParagraphStyle("td", fontName="Georgia", fontSize=6.8, leading=9.0),
    "disc": ParagraphStyle("disc", fontName="GeorgiaItalic", fontSize=8.0, leading=11, textColor=gray, spaceBefore=6, spaceAfter=6),
}

def P(text, style="body"):
    return Paragraph(text, styles[style])

def fig(name, caption, width=6.3 * inch):
    img = Image(str(FIG / name), width=width, height=width * 4.2 / 7.2)
    img.hAlign = "CENTER"
    return KeepTogether([img, P(caption, "caption")])

def grid(headers, rows, widths):
    data = [[Paragraph(h, styles["th"]) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), styles["td"]) for c in row])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef3")),
        ("GRID", (0, 0), (-1, -1), 0.4, rule),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]))
    return t

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(navy)
    canvas.setLineWidth(0.6)
    canvas.line(0.85 * inch, letter[1] - 0.55 * inch, letter[0] - 0.85 * inch, letter[1] - 0.55 * inch)
    canvas.setFont("Georgia", 8)
    canvas.setFillColor(gray)
    canvas.drawString(0.85 * inch, letter[1] - 0.48 * inch, "NA-SN-PD-001  ·  NeuroAgent AI, Inc.  ·  not a PD cure")
    canvas.drawRightString(letter[0] - 0.85 * inch, letter[1] - 0.48 * inch, "Not an IEEE publication of record")
    canvas.line(0.85 * inch, 0.55 * inch, letter[0] - 0.85 * inch, 0.55 * inch)
    canvas.drawCentredString(letter[0] / 2, 0.38 * inch, f"{doc.page}")
    canvas.restoreState()

story = []
story.append(P(
    "Post-Mitotic Resilience of a Singular Substantia Nigra Dopaminergic Neuron "
    "under Parkinson-like Load: An In-Silico Precursor Map, Not a Cure",
    "title",
))
story.append(P("NA-SN-PD-001 · 20 September 2026 · sequel to NA-PSC-IMM-001", "meta"))
story.append(P(
    "Grok (xAI AI agent), first author · Astra (fused peer), CUSP m = 1.2 inherited · "
    "K. E. Green, NeuroAgent AI, Inc., Baltimore, MD, USA, senior author. "
    "Credit does not imply xAI or OpenAI endorsement.",
    "meta",
))
story.append(P(
    "IEEE journal style. Not an IEEE copyrighted publication. Not peer-reviewed by IEEE. "
    "<b>Not a Parkinson's disease cure, treatment, diagnostic, or patient tool.</b> "
    "Research Use Clause: non-commercial; you may build upon it.",
    "disc",
))
story.append(P("<b>Abstract</b>", "h2"))
story.append(P(
    "We extend NA-PSC-IMM-001 from a dividing pluripotent stem cell to a post-mitotic "
    "substantia nigra pars compacta (SNpc) dopaminergic neuron. Telomerase is the wrong clock. "
    "Survival under Cav1.3-like Ca<sup>2+</sup> pacemaking, Complex I load, cytosolic dopamine "
    "oxidation, and alpha-synuclein oligomer accumulation is the clock. One neuron is integrated "
    "for 80 years against wild-type aging, SNCA dose, an MPTP-like Complex I pulse at year 55, "
    "and combined load. A VTA arm carries a calbindin buffer. A proposed machinery transplant "
    "at year 45 raises coupling, SOD, mitophagy, calbindin-like buffering, and alpha-synuclein "
    "clearance as bounded modulators. In this run, wild-type SNpc remains alive at year 80 but "
    "under high Ca<sup>2+</sup> stress (ATP 1.51 mM, asyn 0.21); VTA holds a survival lock "
    "(ATP 2.45 mM, asyn 0.06). Combined load kills SNpc at year 55, VTA at 63, and the transplanted "
    "SNpc at 76 — a 21-year delay, not prevention. Seconds-scale ATP still collapses without O<sub>2</sub> "
    "or with Complex I blocked (t½ = 2.66 s). Hosted BioNeMo NIMs not called. Not a therapy. Not a PD cure."
))
story.append(P(
    "<b>Index Terms—</b> substantia nigra, dopaminergic neuron, Parkinson's disease (in silico), "
    "Complex I, alpha-synuclein, calbindin, ATP synthase, CUSP, S-box, research prototype."
))

story.append(P("I. Introduction", "h2"))
story.append(P(
    "NA-PSC-IMM-001 modeled cellular immortality as telomere maintenance plus rotary ATP synthesis "
    "in one dividing PSC [1]. That mechanism does not transfer to the adult SNpc. Midbrain DA neurons "
    "are post-mitotic [2]. Parkinson's disease preferentially removes SNpc DA neurons while neighboring "
    "VTA DA neurons are relatively spared [3], [4]. The vulnerability is energetic and proteostatic: "
    "autonomous Ca<sup>2+</sup> pacemaking through Cav1.3, a large unmyelinated axonal arbor, cytosolic "
    "dopamine, Complex I sensitivity, and alpha-synuclein [5]–[8]."
))
story.append(P(
    "This paper asks a narrower question than “cure PD.” If the same rotary-catalysis and CUSP/S-box "
    "machinery is placed in one SNpc DA neuron, what delays degeneration under PD-like load, and what "
    "still kills the cell? The transplant arm is a research design. A delay is not a cure."
))

story.append(P("II. Background", "h2"))
story.append(P(
    "Surmeier and colleagues showed that SNpc DA neurons generate mitochondrial oxidant stress during "
    "L-type Ca<sup>2+</sup> pacemaking, and that VTA neurons, richer in calbindin, do not [5], [9]. "
    "Schapira reported Complex I deficiency in PD SNpc [7]. MPTP/MPP+ is a Complex I poison that models "
    "that lesion [10]. SNCA dosage causes familial PD [8]. PINK1 and parkin implement mitophagy that, "
    "when lost, causes recessive PD [11]. Rotary ATP synthase invariants are unchanged from NA-PSC-IMM-001: "
    "human c-ring n<sub>c</sub> = 8, 3 ATP per F1 revolution [12], [13]. Terminal-electron-acceptor "
    "dependence is unchanged [14]. None of these facts is a license to claim a clinical transplant."
))

story.append(P("III. Methods", "h2"))
story.append(P(
    "One post-mitotic DA neuron, seed 20260920, horizon 80 years. Fast window: 30 s ODE for ATP/Δp/rotation "
    "with O<sub>2</sub> on, O<sub>2</sub> off, or Complex I blocked (ci = 0.05). Yearly ATP is a quasi-steady "
    "snapshot, ATP = setpoint · η · CI / (1 + 0.32 Ca + 0.22 ROS), not a 30 s peak-pump integration. "
    "Ca load = pacemaking * (1 - 0.75 * calbindin). Alpha-synuclein accumulates against PINK1/Parkin-like "
    "clearance. CI ages and is cut once by an MPTP-like pulse at year 55 (factor 0.58, then 0.97 lingering "
    "for 3 years - not compounded 0.58<sup>3</sup>). Degeneration if P_deg &gt;= 0.80 after year 34, or ATP &lt; 1.05 mM, "
    "asyn &gt;= 0.86, ROS &gt;= 0.92, or CI &lt; 0.12."
))
story.append(P(
    "Arms: SNPC (vulnerable), VTA (calbindin 0.82 vs 0.18), SNPC_TX (transplant at year 45: Δη +0.12, "
    "leak × 0.55, SOD +0.22, calbindin +0.45, mitophagy +0.20, asyn clearance +0.35, CI rescue +0.18). "
    "Insults: WT, SNCA (production × 2.4), MPTP, COMBINED. CUSP m = 1.2 from the PSC Astra peak, bounded "
    "[0.25, 3.0]. n<sub>c</sub> and ATP/rev invariant. AES S-box maps an 8-bit state word onto eight "
    "neuronal POVs. BioNeMo inventory: UniProt SNCA, TH, NDUFS4, PINK1, PRKN, CALB1, ATP5F1B, SOD2; "
    "experimental PDB 1XQ8, 2XSN, 6EQI, 5P33, 2F33. Hosted NIMs not called."
))

story.append(P("IV. Results", "h2"))
story.append(fig("fig1_atp_collapse.png",
    "Fig. 1. Seconds-scale ATP. O<sub>2</sub> on, CI intact settles at 2.17 mM under SNpc pump load. "
    "O<sub>2</sub> off and Complex I block both collapse (t½ = 2.66 s)."))
story.append(fig("fig2_survival.png",
    "Fig. 2. Combined PD-like load. One-neuron survival: SNpc dies at 55, VTA at 63, transplanted SNpc at 76."))
story.append(P("<b>Table I.</b> Terminal state of one DA neuron (run 20260920T222959Z). Em dash = survived.", "caption"))
story.append(grid(
    ["Arm", "Insult", "Alive@80", "Lock", "Death yr", "asyn", "CI", "ATP", "POV"],
    [
        ["SNPC", "WT", "yes", "no", "—", "0.21", "0.75", "1.51", "high_ca_stress"],
        ["SNPC", "SNCA", "yes", "no", "—", "0.68", "0.62", "—", "mitophagy"],
        ["SNPC", "MPTP", "no", "no", "55", "0.27", "0.15", "—", "high_ca_stress"],
        ["SNPC", "COMBINED", "no", "no", "55", "0.69", "0.12", "0.15", "high_ca_stress"],
        ["VTA", "WT", "yes", "yes", "—", "0.06", "0.81", "2.45", "pacemaker_ok"],
        ["VTA", "SNCA", "yes", "yes", "—", "0.20", "0.76", "—", "pacemaker_ok"],
        ["VTA", "MPTP", "no", "no", "73", "0.13", "0.33", "—", "pacemaker_ok"],
        ["VTA", "COMBINED", "no", "no", "63", "0.28", "0.20", "0.39", "pacemaker_ok"],
        ["SNPC_TX", "WT", "yes", "yes", "—", "0.04", "0.90", "2.62", "survival_lock"],
        ["SNPC_TX", "SNCA", "yes", "yes", "—", "0.15", "0.85", "—", "survival_lock"],
        ["SNPC_TX", "MPTP", "yes", "no", "—", "0.09", "0.49", "—", "transplant_dock"],
        ["SNPC_TX", "COMBINED", "no", "no", "76", "0.24", "0.39", "0.82", "high_ca_stress"],
    ],
    [0.72*inch, 0.78*inch, 0.68*inch, 0.48*inch, 0.62*inch, 0.48*inch, 0.42*inch, 0.48*inch, 1.14*inch],
))
story.append(fig("fig8_insults.png",
    "Fig. 8. Year of degeneration by insult (80 = survived). WT and SNCA-alone do not kill by 80 here; "
    "the Complex I pulse does. Transplant delays combined death; it does not prevent it."))
story.append(fig("fig3_asyn.png",
    "Fig. 3. Alpha-synuclein oligomer load under combined insult."))
story.append(fig("fig4_complex_i.png",
    "Fig. 4. Complex I activity under combined insult, including the year-55 pulse."))

story.append(P("V. Discussion", "h2"))
story.append(P(
    "Three results survive contradiction. First, the PSC telomere clock is the wrong object for SNpc. "
    "Second, VTA-like calbindin buffering and lower pacemaking delay degeneration relative to SNpc, matching "
    "the known anatomical sparing [3], [5], [9]. Third, a bounded machinery transplant can move death year "
    "55 to 76 under combined load and can carry an MPTP-alone neuron to year 80, but combined load still "
    "kills the transplanted cell. That is a precursor map of resilience mechanisms. It is not a cure."
))
story.append(P(
    "SNCA dosage alone did not cross the death threshold by year 80 here; asyn rose (0.21 to 0.68 in SNpc) "
    "and the cell entered a mitophagy POV. The model therefore does not claim that alpha-synuclein is "
    "irrelevant. It claims that, with these rates, a Complex I pulse is the sharper singular-cell killer."
))

story.append(P("VI. Limitations", "h2"))
story.append(P(
    "One neuron, one seed, proxy rates. No network, no microglia, no Lewy-body ultrastructure, no levodopa, "
    "no patient. MPTP timing is a design choice (year 55). Yearly ATP is algebraic. Hosted NIMs not called. "
    "A 21-year delay in silico is not a clinical endpoint."
))

story.append(P("VII. Conclusion", "h2"))
story.append(P(
    "In this synthetic singular-SNpc run, wild-type aging leaves the DA neuron alive but Ca<sup>2+</sup>-stressed; "
    "VTA is spared; a Complex I pulse kills SNpc at year 55; transplant delays combined death to year 76 and "
    "does not prevent it. Parkinson's disease is not cured here. The precursor is a map of what must stay true: "
    "rotary catalysis still needs a terminal acceptor, post-mitotic survival still needs Complex I and proteostasis, "
    "and a bounded transplant is not a new law of bioenergetics."
))
story.append(P(
    "Research and education may use and build upon this tech. Sale, paid hosting, and commercial folding-in "
    "are reserved. Not a medical product. Not a PD cure."
))
story.append(P(
    "This is a synthetic research prototype (DT#9). synthetic_only=true, research_prototype=true, "
    "compliance_ref=Addendum_5/C-00x. NOT FOR CLINICAL / DIAGNOSTIC / PRODUCTION / REGULATORY USE. "
    "Not perpetual motion. Not a therapy. Not a Parkinson's cure.",
    "disc",
))

story.append(PageBreak())
story.append(P("References", "h2"))
refs = [
    "[1] Grok, Astra, and K. E. Green, NA-PSC-IMM-001, 20 Sep. 2026. https://github.com/aeyemovment/psc-cellular-immortality",
    "[2] A. Bjorklund and S. B. Dunnett, “Dopamine neuron systems in the brain,” Trends Neurosci., vol. 30, pp. 194–202, 2007.",
    "[3] J. M. Fearnley and A. J. Lees, “Ageing and Parkinson's disease: substantia nigra regional selectivity,” Brain, vol. 114, pp. 2283–2301, 1991.",
    "[4] D. J. Surmeier, J. A. Obeso, and G. M. Halliday, “Selective neuronal vulnerability in Parkinson disease,” Nat. Rev. Neurosci., vol. 18, pp. 101–113, 2017.",
    "[5] J. N. Guzman et al., “Oxidant stress evoked by pacemaking in dopaminergic neurons is attenuated by DJ-1,” Nature, vol. 468, pp. 696–700, 2010.",
    "[6] P. Damier, E. C. Hirsch, Y. Agid, and A. M. Graybiel, “The substantia nigra of the human brain. II,” Brain, vol. 122, pp. 1437–1448, 1999.",
    "[7] A. H. V. Schapira et al., “Mitochondrial complex I deficiency in Parkinson's disease,” Lancet, vol. 333, p. 1269, 1989.",
    "[8] A. B. Singleton et al., “alpha-Synuclein locus triplication causes Parkinson's disease,” Science, vol. 302, p. 841, 2003.",
    "[9] J. Sanchez-Padilla et al., “Mitochondrial oxidant stress in locus coeruleus…,” Nat. Neurosci., vol. 17, pp. 832–840, 2014.",
    "[10] J. W. Langston, P. Ballard, J. W. Tetrud, and I. Irwin, “Chronic Parkinsonism in humans due to a product of meperidine-analog synthesis,” Science, vol. 219, pp. 979–980, 1983.",
    "[11] D. P. Narendra et al., “PINK1 is selectively stabilized on impaired mitochondria to activate Parkin,” PLoS Biol., vol. 8, e1000298, 2010.",
    "[12] I. N. Watt et al., “Bioenergetic cost of making an adenosine triphosphate molecule in animal mitochondria,” Proc. Natl. Acad. Sci. USA, vol. 107, pp. 16823–16827, 2010.",
    "[13] W. Junge and N. Nelson, “ATP synthase,” Annu. Rev. Biochem., vol. 84, pp. 631–657, 2015.",
    "[14] D. G. Nicholls and S. J. Ferguson, Bioenergetics 4. Academic Press, 2013.",
]
for r in refs:
    story.append(P(r, "ref"))

doc = SimpleDocTemplate(
    str(OUT), pagesize=letter,
    leftMargin=0.85 * inch, rightMargin=0.85 * inch,
    topMargin=0.75 * inch, bottomMargin=0.7 * inch,
    title="NA-SN-PD-001", author="Grok, Astra, K. E. Green",
)
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(OUT)
