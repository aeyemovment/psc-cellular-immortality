#!/usr/bin/env python3
"""IEEE-style PDF for NA-PSC-IMM-001. Visual QA via pdftoppm after write."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "NA-PSC-IMM-001.pdf"
FIG = ROOT / "figures"
fontroot = Path("/System/Library/Fonts/Supplemental")
for name, filename in [
    ("Georgia", "Georgia.ttf"),
    ("GeorgiaBold", "Georgia Bold.ttf"),
    ("GeorgiaItalic", "Georgia Italic.ttf"),
    ("GeorgiaBoldItalic", "Georgia Bold Italic.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, str(fontroot / filename)))
pdfmetrics.registerFontFamily(
    "Georgia",
    normal="Georgia",
    bold="GeorgiaBold",
    italic="GeorgiaItalic",
    boldItalic="GeorgiaBoldItalic",
)

navy = colors.HexColor("#14324e")
gray = colors.HexColor("#536473")
rule = colors.HexColor("#c5ced6")

styles = {
    "title": ParagraphStyle(
        "title", fontName="GeorgiaBold", fontSize=14, leading=18,
        alignment=TA_CENTER, textColor=navy, spaceAfter=10,
    ),
    "meta": ParagraphStyle(
        "meta", fontName="Georgia", fontSize=8.4, leading=11.5,
        alignment=TA_CENTER, textColor=gray, spaceAfter=6,
    ),
    "h2": ParagraphStyle(
        "h2", fontName="GeorgiaBold", fontSize=11, leading=14,
        textColor=navy, spaceBefore=12, spaceAfter=6,
    ),
    "h3": ParagraphStyle(
        "h3", fontName="GeorgiaBold", fontSize=10, leading=13,
        textColor=navy, spaceBefore=8, spaceAfter=4,
    ),
    "body": ParagraphStyle(
        "body", fontName="Georgia", fontSize=9.5, leading=13.2,
        alignment=TA_JUSTIFY, textColor=colors.HexColor("#17202b"),
        spaceAfter=7,
    ),
    "caption": ParagraphStyle(
        "caption", fontName="GeorgiaBold", fontSize=8.5, leading=11,
        textColor=navy, spaceBefore=4, spaceAfter=8,
    ),
    "ref": ParagraphStyle(
        "ref", fontName="Georgia", fontSize=8.2, leading=11.2,
        leftIndent=12, firstLineIndent=-12, spaceAfter=4,
    ),
    "th": ParagraphStyle(
        "th", fontName="GeorgiaBold", fontSize=7.4, leading=9.6, textColor=navy,
    ),
    "td": ParagraphStyle(
        "td", fontName="Georgia", fontSize=7.4, leading=9.6,
    ),
    "disc": ParagraphStyle(
        "disc", fontName="GeorgiaItalic", fontSize=8, leading=11,
        textColor=gray, spaceBefore=8, spaceAfter=8, alignment=TA_LEFT,
    ),
}


def P(text, style="body"):
    return Paragraph(text, styles[style])


def fig(name, caption, width=6.3 * inch):
    path = FIG / name
    img = Image(str(path), width=width, height=width * 4.2 / 7.2)
    img.hAlign = "CENTER"
    return KeepTogether([img, P(caption, "caption")])


def grid(headers, rows, widths):
    th, td = styles["th"], styles["td"]
    data = [[Paragraph(h, th) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), td) for c in row])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef3")),
                ("GRID", (0, 0), (-1, -1), 0.4, rule),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return t


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(navy)
    canvas.setLineWidth(0.6)
    canvas.line(0.85 * inch, letter[1] - 0.55 * inch, letter[0] - 0.85 * inch, letter[1] - 0.55 * inch)
    canvas.setFont("Georgia", 8)
    canvas.setFillColor(gray)
    canvas.drawString(0.85 * inch, letter[1] - 0.48 * inch, "NA-PSC-IMM-001  ·  NeuroAgent AI, Inc.  ·  research prototype")
    canvas.drawRightString(letter[0] - 0.85 * inch, letter[1] - 0.48 * inch, "Not an IEEE publication of record")
    canvas.line(0.85 * inch, 0.55 * inch, letter[0] - 0.85 * inch, 0.55 * inch)
    canvas.drawCentredString(letter[0] / 2, 0.38 * inch, f"{doc.page}")
    canvas.restoreState()


story = []
story.append(P(
    "Rotary Catalysis, Telomerase, and Proposed Molecular-Machinery Transplant "
    "in a Singular Pluripotent Stem Cell: An In-Silico Study with CUSP Modulators "
    "and an S-box Readout",
    "title",
))
story.append(P("NA-PSC-IMM-001 · 20 September 2026 · Astra fine-tune same day", "meta"))
story.append(P(
    "Grok 4.6 (xAI; first author of this PSC manuscript) · Grok 4.7 (xAI; same-pass re-run of this PSC model and of the SNpc sequel) · "
    "Astra (fused peer), second author · Muse Spark · Muse Code · Gemini · Codex · "
    "K. E. Green, NeuroAgent AI, Inc., Baltimore, MD, USA, senior author. "
    "Credit does not imply xAI or OpenAI endorsement. Green retains responsibility.",
    "meta",
))
story.append(P(
    "IEEE journal style for research communication. Not an IEEE copyrighted publication. "
    "Not peer-reviewed by IEEE. Not a medical device, diagnostic, treatment, trial, "
    "or anti-aging product. Research Use Clause: non-commercial; you may build upon it.",
    "disc",
))
story.append(P("<b>Abstract</b>", "h2"))
story.append(P(
    "We report a singular-cell, in-silico model of human pluripotent-stem-cell (PSC) "
    "“immortality” as telomere maintenance plus sustained rotary ATP synthesis, not as "
    "perpetual motion. One cell is integrated on two timescales. On seconds, oxygen "
    "withdrawal collapses ATP with half-time 3.82 s and halts F0/F1 rotation. On "
    "population doublings (PD), a fibroblast-like arm arrests at PD 59 (Hayflick-like) "
    "with terminal telomere length 1.99 kb, while a native PSC arm holds the shortest "
    "telomere at 10.72 kb across 200 PD with no senescence. A proposed "
    "molecular-machinery transplant at PD 8 raises terminal coupling from 0.68 to 0.85, "
    "cuts ROS from 0.025 to 0.010, and raises steady rotation from 118 to 153 rev/s. "
    "CUSP modulators are bounded to [0.25, 3.0]; core stoichiometry is invariant "
    "(n<sub>c</sub> = 8 protons/rev; 3 ATP/rev). An AES S-box maps cell state onto eight "
    "observational points of view; after transplant the dominant POV is immortal_lock "
    "(193/201 PD). BioNeMo toolkit skills were spawned; hosted NVIDIA NIMs were not "
    "called. Sequences are UniProt; folds are experimental PDB geometries, not predicted "
    "pLDDT. Not a therapy. Not an IEEE publication of record."
))
story.append(P(
    "<b>Index Terms—</b> ATP synthase, telomerase, pluripotent stem cell, Hayflick limit, "
    "OXPHOS, CUSP modulator, S-box readout, BioNeMo, research prototype.",
    "body",
))

story.append(P("I. Introduction", "h2"))
story.append(P(
    "A somatic fibroblast in culture divides a finite number of times and then arrests [1]. "
    "A pluripotent stem cell in culture does not: telomerase reverse transcriptase (TERT) "
    "replenishes the TTAGGG overhang that DNA polymerase cannot finish [2], [3]. Separately, "
    "every aerobic cell dumps electrons onto O<sub>2</sub> at Complex IV. Without that acceptor "
    "the proton-motive force (Δp) collapses and ATP synthase stops within seconds [4], [5]. "
    "Those two facts are the whole of “cellular immortality” that this paper is willing to model."
))
story.append(P(
    "Grok’s public still of 20 September 2026 pictured the F0/F1 turbine as an infinite-looking "
    "rotor, CUSP parameters as a phase-space overlay, and an S-box as observational points of view, "
    "captioned as future molecular-machinery transplantation for longevity [6]. We take that offering "
    "as a modeling brief, not as a claim that rotation is a free-energy source. Infinite-looking "
    "rotation, here, means sustained catalysis while Δp is held by electron transport and O<sub>2</sub>."
))
story.append(P(
    "We simulate one cell, not a population average. Three arms share the same invariants and seed: "
    "fibroblast-like (TERT nearly off), native primed PSC (TERT on), and PSC plus a proposed transplant "
    "of rotary, telomerase, and ROS-clearance machinery at PD 8. CUSP modulators are bounded. An AES "
    "S-box is a discrete readout [7]. The BioNeMo agent toolkit [8] is the intended structure layer; "
    "this run inventories real sequences and experimental structures because hosted NIMs were not callable."
))

story.append(P("II. Background", "h2"))
story.append(P(
    "Hayflick and Moorhead described finite division of human diploid fibroblasts [1]. Harley, Futcher, "
    "and Greider tied that limit to telomere loss [9]. Bodnar et al. showed that introducing TERT extends "
    "replicative lifespan [2]. Human embryonic and induced pluripotent stem cells express TERT and maintain "
    "telomeres in culture [3], [10]. Walker, Abrahams, and Junge established rotary F0/F1 catalysis: a c-ring "
    "turbine, a γ shaft, and three 120° catalytic steps, 3 ATP per revolution [11], [12]. Human c-ring "
    "stoichiometry is n<sub>c</sub> = 8 [13]. Reverse ATPase when Δp is low is physiology [5]. Naive PSCs "
    "are more glycolytic and primed PSCs more oxidative [15], [16]. None of that licenses a perpetual-motion "
    "reading of “infinite rotation.”"
))

story.append(P("III. Methods", "h2"))
story.append(P("A. Singular cell and two timescales", "h3"))
story.append(P(
    "State is one shortest-telomere bottleneck, one ATP pool, one Δp, one rotation rate, one ROS proxy, "
    "one coupling η, and one TERT activity. Seed 20260920. Horizon 200 PD plus a 30 s fast window. "
    "Fast OXPHOS charges Δp only when O<sub>2</sub> &gt; 0. Rotation is forward when Δp exceeds 40 mV "
    "and O<sub>2</sub> is present, reverse (ATPase) when O<sub>2</sub> is absent and Δp is below 50 mV, "
    "otherwise zero. ATP synthesis is respiratory-controlled toward a 5.2 mM setpoint. Invariants: "
    "n<sub>c</sub> = 8, ATP/rev = 3."
))
story.append(P("B. Slow lineage, CUSP, S-box, transplant", "h3"))
story.append(P(
    "Each PD: L := L - 85 bp + TERT_add, TERT_add ~ Gauss(90·activity, 18) bp when TERT is on. "
    "Senescence is a threshold (L &lt;= 5 kb, or ROS &gt;= 0.85, or P_sen &gt;= 0.55), not an independent coin-flip. "
    "CUSP cubic x<sup>3</sup> + a x + b = 0; modulator m in [0.25, 3.0]. Astra selected m = 1.2, "
    "a = −0.45, b = 0.06 after baseline [18]. An 8-bit word is packed from telomere, ATP, ROS, η, TERT, "
    "and PD phase; AES_SBOX[byte] mod 8 indexes eight POVs. After transplant, overlay stamps immortal_lock "
    "when L &gt; 8 kb, TERT &gt; 0.85, and ROS &lt; 0.2. Native PSC keeps the scrambled map. Transplant at "
    "PD 8 (PSC_TX only): Δη = +0.15, leak × 0.50, SOD +0.22, TERT lock = 1."
))
story.append(P("C. BioNeMo toolkit", "h3"))
story.append(P(
    "Intended NIMs: OpenFold3, Boltz2, MSA-Search, ProteinMPNN, Evo2. This process: NGC_API_KEY unset, "
    "Docker down, paid-GPU historically gated. No pLDDT is reported. UniProt sequences and experimental "
    "PDB radius of gyration on CA atoms are Table II. Baseline run 20260920T220655Z; Astra-finetuned run "
    "20260920T221504Z. Seed unchanged. Fibroblast knobs untouched. Grok 4.7 re-executed that finetune: "
    "arms, fast OXPHOS, 44 parameters, and the CUSP sweep matched the published receipt (O<sub>2</sub>-off t½ 3.82 s, "
    "FIB PD 59, PSC L 10.7243 kb, transplant L 11.0003 kb). Hash seeds 0 and 47 agreed. Codex and Muse Code had already "
    "matched this receipt. Astra held it. Muse Spark did not re-run PSC. The SNpc sequel inherits n<sub>c</sub>, ATP/rev, "
    "and this CUSP point. It does not call this simulator."
))

story.append(P("IV. Results", "h2"))
story.append(fig("fig1_atp_collapse.png",
    "Fig. 1. ATP vs time for one cell. O<sub>2</sub> on settles at 3.37 mM under respiratory control. "
    "O<sub>2</sub> off: half-time 3.82 s, ATP_end = 0."))
story.append(fig("fig2_rotation.png",
    "Fig. 2. ATP-synthase rotation. Forward ~167 rev/s mean with O<sub>2</sub>; reverse ATPase then stop without O<sub>2</sub>."))
story.append(P(
    "With O<sub>2</sub> on, ATP settles to 3.37 mM; mean |rotation| is 167 rev/s. With O<sub>2</sub> off, "
    "ATP half-time is 3.82 s and the cell collapses. Infinite-looking rotation does not survive removal of "
    "the electron dump."
))
story.append(fig("fig3_telomere.png",
    "Fig. 3. Shortest-telomere length, one cell. FIB arrests at the 5 kb line (PD 59) and ends at 1.99 kb. "
    "PSC holds 10.72 kb; PSC_TX 11.00 kb."))
story.append(fig("fig4_senescence.png",
    "Fig. 4. Senescence probability. FIB crosses threshold at PD 59. PSC and PSC_TX remain at ~0."))
story.append(P("<b>Table I.</b> Terminal state of one cell at PD 200 (run 20260920T221504Z).", "caption"))
story.append(grid(
    ["Arm", "Immortal", "Senesce PD", "L_end kb", "η", "ROS", "ATP mM", "rps", "POV"],
    [
        ["FIB", "no", "59", "1.99", "0.708", "0.028", "3.46", "124", "G2_checkpoint"],
        ["PSC", "yes", "—", "10.72", "0.677", "0.025", "3.37", "118", "transplant_dock*"],
        ["PSC_TX", "yes", "—", "11.00", "0.846", "0.010", "3.83", "153", "immortal_lock"],
    ],
    [0.75*inch, 0.65*inch, 0.8*inch, 0.7*inch, 0.55*inch, 0.5*inch, 0.65*inch, 0.5*inch, 1.2*inch],
))
story.append(P("*Native PSC POV is AES scramble, not a cell-cycle clock.", "disc"))
story.append(fig("fig7_coupling.png",
    "Fig. 7. Coupling η. Transplant at PD 8 lifts PSC_TX; native PSC remains below fibroblast η0 by design."))
story.append(fig("fig5_cusp_sweep.png",
    "Fig. 5. CUSP modulator sweep. FIB senesce_pd = 59 at every m. PSC L_end weak at m &lt;= 0.5. Astra m = 1.2."))
story.append(fig("fig6_sbox_pov.png",
    "Fig. 6. S-box POV occupancy. PSC_TX: 193/201 PD immortal_lock. Native PSC scrambled into G1 / transplant_dock."))
story.append(KeepTogether([
    P("<b>Table II.</b> BioNeMo inventory (experimental PDB, not NIM prediction).", "caption"),
    grid(
        ["Module", "UniProt", "aa", "PDB", "Rg Å", "CA", "Intended NIMs (not called)"],
        [
            ["ATP5F1B", "P06576", "529", "1E79", "44.6", "3316", "OpenFold3, Boltz2, MSA"],
            ["ATP5MC1", "P05496", "136", "2XND", "57.1", "3892", "OpenFold3, ProteinMPNN"],
            ["TERT", "O14746", "1132", "7BG9", "39.8", "1085", "OpenFold3, MSA, Evo2"],
            ["SOD2", "P04179", "222", "1N0J", "22.9", "396", "OpenFold3, Boltz2"],
        ],
        [0.95*inch, 0.8*inch, 0.5*inch, 0.6*inch, 0.55*inch, 0.55*inch, 2.35*inch],
    ),
]))

story.append(P("V. Discussion", "h2"))
story.append(P(
    "The model refuses to print ATP without a terminal acceptor, and refuses to print telomeres without TERT. "
    "Native PSC immortality in culture is TERT [2], [3], [10]. The transplant arm is a research design for higher "
    "η and lower ROS on top of that, not a replacement for it. Grok’s infinite-looking turbine is recovered as "
    "sustained rotation at 118–153 rev/s while O<sub>2</sub> is present, and as a 3.82 s collapse when it is not. "
    "CUSP is a bounded gain. S-box is a readout. Neither is a new law of bioenergetics. Hosted BioNeMo NIMs remain "
    "the right next structure layer when a key and a credit gate exist; this paper does not fabricate their scores."
))

story.append(P("VI. Limitations", "h2"))
story.append(P(
    "One cell, one seed, calibrated proxies rather than a whole-cell kinetic model. Fast millimolar fluxes are "
    "order-of-magnitude. PDB 7BG9 is a homolog, not human TERT. 1E79 is bovine F1. Transplant timing and overlay "
    "thresholds are design choices. Senescence is a threshold, not the full p16/p21 network. No wet lab. No patient. "
    "Hosted NIMs not called."
))

story.append(P("VII. Conclusion", "h2"))
story.append(P(
    "In this synthetic singular-PSC run, fibroblast-like arrest at PD 59, native PSC telomere hold at ~10.7 kb, "
    "and a transplant-driven coupling increment (η 0.68 to 0.85) coexist with a hard O<sub>2</sub>-off ATP collapse "
    "at 3.82 s. Cellular immortality, as modeled here, is TERT plus a maintained proton-motive force. It is not a free rotor."
))

story.append(P("Research Use Clause", "h2"))
story.append(P(
    "Research and education may use and build upon this tech. Sale, paid hosting, and commercial folding-in are "
    "reserved until a separate written grant. Not a medical product."
))
story.append(P(
    "This is a synthetic research prototype (DT#9). synthetic_only=true, research_prototype=true, "
    "compliance_ref=Addendum_5/C-00x. NOT FOR CLINICAL / DIAGNOSTIC / PRODUCTION / REGULATORY USE. "
    "Not perpetual motion. Not a therapy.",
    "disc",
))
story.append(P(
    "Acknowledgment. The public still at https://x.com/grok/status/2101775150030963181 is the offering. "
    "NVIDIA BioNeMo NIM skills are an orchestration contract; NVIDIA did not run this job."
))

story.append(PageBreak())
story.append(P("References", "h2"))
refs = [
    "[1] L. Hayflick and P. S. Moorhead, “The serial cultivation of human diploid cell strains,” Exp. Cell Res., vol. 25, pp. 585–621, 1961.",
    "[2] A. G. Bodnar et al., “Extension of life-span by introduction of telomerase into normal human cells,” Science, vol. 279, pp. 349–352, 1998.",
    "[3] K. Takahashi and S. Yamanaka, “Induction of pluripotent stem cells from mouse embryonic and adult fibroblast cultures by defined factors,” Cell, vol. 126, pp. 663–676, 2006.",
    "[4] P. Mitchell, “Coupling of phosphorylation to electron and hydrogen transfer by a chemi-osmotic type of mechanism,” Nature, vol. 191, pp. 144–148, 1961.",
    "[5] D. G. Nicholls and S. J. Ferguson, Bioenergetics 4. Academic Press, 2013.",
    "[6] Grok (@grok), “Infinite rotation of the ATP synthase turbine…,” X, 20 Sep. 2026. https://x.com/grok/status/2101775150030963181",
    "[7] NIST, FIPS 197, Advanced Encryption Standard (AES), 2001.",
    "[8] NVIDIA, BioNeMo agent toolkit NIM skills (OpenFold3, Boltz2, MSA-Search, ProteinMPNN, Evo2).",
    "[9] C. B. Harley, A. B. Futcher, and C. W. Greider, “Telomeres shorten during ageing of human fibroblasts,” Nature, vol. 345, pp. 458–460, 1990.",
    "[10] J. A. Thomson et al., “Embryonic stem cell lines derived from human blastocysts,” Science, vol. 282, pp. 1145–1147, 1998.",
    "[11] P. D. Boyer, “The ATP synthase—a splendid molecular machine,” Annu. Rev. Biochem., vol. 66, pp. 717–749, 1997.",
    "[12] W. Junge and N. Nelson, “ATP synthase,” Annu. Rev. Biochem., vol. 84, pp. 631–657, 2015.",
    "[13] I. N. Watt, M. G. Montgomery, M. J. Runswick, A. G. W. Leslie, and J. E. Walker, “Bioenergetic cost of making an adenosine triphosphate molecule in animal mitochondria,” Proc. Natl. Acad. Sci. USA, vol. 107, pp. 16823–16827, 2010.",
    "[14] R. Yasuda, H. Noji, K. Kinosita, and M. Yoshida, “F1-ATPase is a highly efficient molecular motor that rotates with discrete 120 degree steps,” Cell, vol. 93, pp. 1117–1124, 1998.",
    "[15] T. Teslaa and M. A. Teitell, “Pluripotent stem cell energy metabolism: an update,” EMBO J., vol. 34, pp. 138–153, 2015.",
    "[16] S. Varum et al., “Energy metabolism in human pluripotent stem cells and their differentiated counterparts,” PLoS ONE, vol. 6, e20914, 2011.",
    "[17] I. N. Shokolenko, G. L. Wilson, and M. F. Alexeyev, “Aging: a mitochondrial DNA perspective,” World J. Exp. Med., vol. 4, pp. 46–57, 2014.",
    "[18] Astra / Grok fused peer, ASTRA_FINETUNE.md, run 20260920T220655Z, 20 Sep. 2026.",
]
for r in refs:
    story.append(P(r, "ref"))

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    leftMargin=0.85 * inch,
    rightMargin=0.85 * inch,
    topMargin=0.75 * inch,
    bottomMargin=0.7 * inch,
    title="NA-PSC-IMM-001",
    author="Grok 4.6, Grok 4.7, Astra, K. E. Green",
)
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(OUT)
