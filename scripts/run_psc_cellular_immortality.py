#!/usr/bin/env python3
"""Singular pluripotent-stem-cell cellular-immortality simulator.

Orchestrates the BioNeMo agent toolkit around a single-cell model of:

  1. Rotary ATP synthase (F0/F1) under a proton-motive force
  2. Terminal-electron-acceptor dependence (O2 as the dump for electrons)
  3. Telomerase (TERT) vs the end-replication problem
  4. Proposed molecular-machinery transplant (research design, not a therapy)
  5. CUSP catastrophe modulators (bounded 0.25–3.0; core stoichiometry invariant)
  6. AES S-box as an 8-bit observational POV map (readout, not cryptography)

This is a synthetic research prototype (DT#9).
synthetic_only=true  research_prototype=true
NOT FOR CLINICAL / DIAGNOSTIC / PRODUCTION / REGULATORY USE.
Not perpetual motion. Rotation continues only while Δp is maintained by ETC + acceptor.
Hosted NVIDIA NIM calls are attempted only when NGC_API_KEY/NVIDIA_API_KEY is set.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "psc_immortality"
CUSP_DIR = Path.home() / "Library/Application Support/hazyeyes/cusp-agent-scheduler"

POLICY_ID = "CUSP-PSC-IMMORTALITY-001"
THEORY_ID = "PSC-ATP-TERT-TX-CUSP-SBOX-001"
WM_ID = "DT-PSC-CELLULAR-IMMORTALITY"
FUSION = (
    "Holo <> BioNeMo <> ATP-synthase-rotary <> TERT <> "
    "molecular-machinery-transplant <> CUSP* <> |S-box| POV <> "
    "singular-PSC"
)
COMPLIANCE_REF = "Addendum_5/C-00x"
DISCLAIMER = (
    "RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-cell simulation. "
    "Not a clinical therapy, gene-therapy product, anti-aging treatment, "
    "or perpetual-motion device. Rotary catalysis requires a proton-motive "
    "force; the proton-motive force requires electron transport and a terminal "
    "acceptor. Claims are bounded to this in-silico run. "
    "Not for clinical, diagnostic, production, or regulatory use."
)

# Kyte–Doolittle hydropathy (sequence GRAVY).
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
AA_MASS = {
    "A": 89.1, "R": 174.2, "N": 132.1, "D": 133.1, "C": 121.2, "Q": 146.2,
    "E": 147.1, "G": 75.1, "H": 155.2, "I": 131.2, "L": 131.2, "K": 146.2,
    "M": 149.2, "F": 165.2, "P": 115.1, "S": 105.1, "T": 119.1, "W": 204.2,
    "Y": 181.2, "V": 117.1,
}

# Standard AES S-box (FIPS-197). Used only as a discrete POV map.
AES_SBOX = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
]

SBOX_POV = {
    0: "G1_pluripotent",
    1: "S_replication",
    2: "G2_checkpoint",
    3: "M_division",
    4: "repair_DDR",
    5: "oxphos_lock",
    6: "transplant_dock",
    7: "immortal_lock",
}

BIONEMO_MODULES = {
    "ATP5F1B": {
        "uniprot": "P06576",
        "role": "F1 catalytic beta — 120° rotary ATP synthesis",
        "fasta": "ATP5F1B.fasta",
        "pdb": "1E79_F1_ATPsynthase.pdb",
        "pdb_id": "1E79",
        "pdb_note": "bovine mitochondrial F1-ATPase (experimental); human sequence used for composition",
        "nims": ["openfold3-nim", "boltz2-nim", "msa-search-nim"],
    },
    "ATP5MC1": {
        "uniprot": "P05496",
        "role": "F0 c-subunit — proton turbine of the c-ring",
        "fasta": "ATP5MC1.fasta",
        "pdb": "2XND_c_ring.pdb",
        "pdb_id": "2XND",
        "pdb_note": "c-ring experimental structure; human ATP5MC1 sequence for composition",
        "nims": ["openfold3-nim", "proteinmpnn-nim"],
    },
    "TERT": {
        "uniprot": "O14746",
        "role": "telomerase reverse transcriptase — telomere maintenance",
        "fasta": "TERT.fasta",
        "pdb": "7BG9_TERT.pdb",
        "pdb_id": "7BG9",
        "pdb_note": "Tetrahymena telomerase holoenzyme (experimental homolog); human TERT sequence",
        "nims": ["openfold3-nim", "msa-search-nim", "evo2-nim"],
    },
    "SOD2": {
        "uniprot": "P04179",
        "role": "mitochondrial MnSOD — superoxide clearance",
        "fasta": "SOD2.fasta",
        "pdb": "1N0J_SOD2.pdb",
        "pdb_id": "1N0J",
        "pdb_note": "human MnSOD experimental structure",
        "nims": ["openfold3-nim", "boltz2-nim"],
    },
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _py(x: Any) -> Any:
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, dict):
        return {k: _py(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_py(v) for v in x]
    return x


@dataclass
class Params:
    """Single-cell parameters. Core stoichiometry is invariant; modulators bounded."""

    seed: int = 20260920
    n_c: int = 8  # human c-ring protons per revolution (Watt 2010)
    atp_per_rev: int = 3  # F1 120° steps
    rps_max: float = 250.0  # in-vivo order (Yasuda / Ueno)
    dp_max_mV: float = 180.0
    dp_threshold_mV: float = 40.0
    dp_reverse_mV: float = 50.0
    atp0_mM: float = 5.0
    atp_setpoint_mM: float = 5.2  # respiratory-control setpoint; not a free-energy source
    atp_use_per_s: float = 0.8  # basal PSC demand (mM/s scale proxy)
    k_syn_base: float = 2.2  # mM/s at full rotation, eta=1, ATP near 0
    k_etc: float = 14.0
    k_leak: float = 0.28
    k_pmf_from_etc: float = 11.0
    k_pmf_from_synth: float = 0.032
    n_mito: int = 220
    n_synthase_per_mito: int = 4500
    l0_psc_kb: float = 10.0
    l0_fib_kb: float = 10.0
    delta_bp_per_pd: float = 85.0
    tert_add_bp: float = 90.0
    crisis_kb: float = 3.0
    senescence_kb: float = 5.0
    pd_horizon: int = 200
    tx_pd: int = 8
    o2_on: float = 1.0
    # CUSP modulators — bounded. Do not touch n_c / atp_per_rev.
    cusp_m: float = 1.0
    cusp_a: float = -0.55
    cusp_b: float = 0.12
    cusp_p: float = 3.0
    eta0_psc: float = 0.72
    eta0_fib: float = 0.80
    leak_frac_psc: float = 0.018
    leak_frac_fib: float = 0.012
    tert_on_psc: float = 0.92
    tert_on_fib: float = 0.02
    sod_psc: float = 0.70
    sod_fib: float = 0.55
    tx_eta_boost: float = 0.18
    tx_leak_cut: float = 0.55
    tx_tert_lock: float = 1.0
    tx_sod_boost: float = 0.25
    fast_t_end_s: float = 30.0
    fast_dt_s: float = 0.01


def load_fasta(path: Path) -> tuple[str, str]:
    header = ""
    seq: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(">"):
            header = line[1:].strip()
        else:
            seq.append(line.strip())
    return header, "".join(seq)


def sequence_metrics(seq: str) -> dict[str, Any]:
    seq = "".join(c for c in seq.upper() if c in KD)
    n = max(len(seq), 1)
    gravy = sum(KD[c] for c in seq) / n
    mass = sum(AA_MASS[c] for c in seq) - 18.015 * (n - 1)
    charge = seq.count("K") + seq.count("R") - seq.count("D") - seq.count("E")
    return {
        "length_aa": n,
        "gravy": round(gravy, 4),
        "mass_da_proxy": round(mass, 1),
        "net_charge_pH7_proxy": charge,
        "sha256_16": _sha(seq)[:16],
    }


def pdb_ca_rg(path: Path) -> dict[str, Any]:
    xs, ys, zs = [], [], []
    n_atom = 0
    if not path.exists():
        return {"exists": False}
    for line in path.open(encoding="utf-8", errors="ignore"):
        if line.startswith("ATOM"):
            n_atom += 1
            if line[12:16].strip() == "CA":
                try:
                    xs.append(float(line[30:38]))
                    ys.append(float(line[38:46]))
                    zs.append(float(line[46:54]))
                except ValueError:
                    continue
    if not xs:
        return {"exists": True, "n_atom": n_atom, "n_ca": 0}
    x = np.array(xs)
    y = np.array(ys)
    z = np.array(zs)
    cx, cy, cz = x.mean(), y.mean(), z.mean()
    rg = float(np.sqrt(np.mean((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)))
    return {
        "exists": True,
        "n_atom": n_atom,
        "n_ca": len(xs),
        "rg_angstrom": round(rg, 3),
        "centroid": [round(float(cx), 2), round(float(cy), 2), round(float(cz), 2)],
    }


def probe_bionemo() -> dict[str, Any]:
    key = os.environ.get("NGC_API_KEY") or os.environ.get("NVIDIA_API_KEY")
    hosted = bool(key)
    return {
        "toolkit_root": str(ROOT),
        "hosted_nims_callable": hosted,
        "reason_if_not": None if hosted else "NGC_API_KEY/NVIDIA_API_KEY not set in this process",
        "docker": "not_probed_here",
        "intended_nims": sorted({n for m in BIONEMO_MODULES.values() for n in m["nims"]}),
        "note": (
            "Hosted OpenFold3/Boltz2/MSA/Evo2 were not called. "
            "Structures are experimental PDB files; sequences are UniProt. "
            "No fabricated pLDDT."
        ),
        "paid_gpu_gate": "blocked_no_key",
    }


def cusp_order_parameter(a: float, b: float) -> float:
    """Real root of x^3 + a x + b = 0 (cusp catastrophe), mapped to (0, 1)."""
    # Cardano for depressed cubic.
    disc = (b / 2.0) ** 2 + (a / 3.0) ** 3
    if disc >= 0:
        s = math.sqrt(disc)
        u = math.copysign(abs(-b / 2 + s) ** (1 / 3), -b / 2 + s)
        v = math.copysign(abs(-b / 2 - s) ** (1 / 3), -b / 2 - s)
        x = u + v
    else:
        r = math.sqrt(-a / 3.0)
        phi = math.acos(_clamp((-b / 2.0) / (r ** 3), -1.0, 1.0))
        # Pick the most stable (largest |x|) real root.
        roots = [2 * r * math.cos((phi + 2 * math.pi * k) / 3.0) for k in range(3)]
        x = max(roots, key=lambda z: abs(z))
    return _clamp(0.5 + 0.35 * math.tanh(x), 0.05, 0.98)


def cusp_modulator(m: float) -> float:
    m = _clamp(m, 0.25, 3.0)
    # Smooth, peaked near 1.2, never a free-energy source.
    return _clamp(m / (1.0 + abs(m - 1.2) ** 1.4), 0.25, 2.2)


def pack_state_byte(L_kb: float, atp: float, ros: float, eta: float, tert: float, pd: int) -> int:
    b0 = 1 if L_kb > 8 else 0
    b1 = 1 if L_kb > 5 else 0
    b2 = 1 if atp > 2.5 else 0
    b3 = 1 if ros < 0.35 else 0
    b4 = 1 if eta > 0.6 else 0
    b5 = 1 if tert > 0.5 else 0
    b6 = 1 if (pd % 4) < 2 else 0
    b7 = 1 if L_kb > 4 and tert > 0.8 and ros < 0.4 else 0
    return b0 | (b1 << 1) | (b2 << 2) | (b3 << 3) | (b4 << 4) | (b5 << 5) | (b6 << 6) | (b7 << 7)


def sbox_pov(byte: int) -> tuple[int, str, int]:
    s = AES_SBOX[byte & 0xFF]
    pov_id = s & 0x07
    return s, SBOX_POV[pov_id], pov_id


def fast_oxphos(p: Params, o2: float, eta: float, n_steps: int | None = None) -> dict[str, Any]:
    """Seconds-scale ATP / Δp / rotation. Thermodynamics enforced."""
    dt = p.fast_dt_s
    t_end = p.fast_t_end_s
    n = n_steps or int(t_end / dt)
    t = np.zeros(n)
    atp = np.zeros(n)
    dp = np.zeros(n)
    omega = np.zeros(n)  # rev/s
    atp[0] = p.atp0_mM
    dp[0] = 150.0 if o2 > 0.5 else 150.0
    n_syn = p.n_mito * p.n_synthase_per_mito
    # Scale single-enzyme ATP rate into mM/s for one cell volume proxy.
    # 1 synthase @ 250 rps * 3 ATP ≈ 750 ATP/s. 1e6 synthases ≈ 7.5e8 ATP/s.
    # Cell volume ~ 2000 µm^3 → ~2 pL → 7.5e8 / (2e-12 * 6e23) * 1e3 mM/s is tiny;
    # we use a calibrated millimolar flux so collapse-in-seconds matches physiology
    # (Nicholls): basal use ~0.5–2 mM/s, synthesis matches when OXPHOS is on.
    k_syn_mM = p.k_syn_base * eta  # mM/s at full rotation
    for i in range(1, n):
        t[i] = i * dt
        o2_eff = max(o2, 0.0)
        etc = p.k_etc * o2_eff * (1.0 - dp[i - 1] / p.dp_max_mV)
        leak = p.k_leak * (0.6 + 0.8 * (1.0 - eta)) * (dp[i - 1] / p.dp_max_mV)
        if dp[i - 1] >= p.dp_threshold_mV and o2_eff > 0.05:
            frac = _clamp((dp[i - 1] - p.dp_threshold_mV) / (p.dp_max_mV - p.dp_threshold_mV), 0, 1)
            w = p.rps_max * eta * frac
            syn = 1.0
        elif dp[i - 1] < p.dp_reverse_mV and o2_eff < 0.05:
            # Reverse ATPase: hydrolyze ATP to rebuild Δp (brief, then crash).
            w = -0.35 * p.rps_max * (1.0 - dp[i - 1] / p.dp_reverse_mV)
            syn = -0.55
        else:
            w = 0.0
            syn = 0.0
        # Respiratory control: synthesis falls as ATP approaches the setpoint.
        drive = max(0.0, 1.0 - atp[i - 1] / max(p.atp_setpoint_mM * 1.25, 1e-6))
        d_atp = syn * k_syn_mM * (abs(w) / p.rps_max) * drive - p.atp_use_per_s * (atp[i - 1] / (atp[i - 1] + 0.8))
        d_dp = p.k_pmf_from_etc * etc - p.k_pmf_from_synth * abs(w) * max(syn, 0) - leak * p.dp_max_mV
        atp[i] = _clamp(atp[i - 1] + dt * d_atp, 0.0, 8.0)
        dp[i] = _clamp(dp[i - 1] + dt * d_dp, 0.0, p.dp_max_mV)
        omega[i] = w
        if o2_eff < 0.05 and atp[i] < 0.05 and dp[i] < 5:
            # Dead: fill the rest as collapsed.
            atp[i:] = atp[i]
            dp[i:] = dp[i]
            omega[i:] = 0.0
            t[i:] = t[i] + np.arange(n - i) * dt
            break
    t_half = None
    if o2 < 0.5:
        below = np.where(atp < 0.5 * p.atp0_mM)[0]
        if len(below):
            t_half = float(t[below[0]])
    return {
        "t_s": t,
        "atp_mM": atp,
        "dp_mV": dp,
        "rps": omega,
        "o2": o2,
        "eta": eta,
        "n_synthase_proxy": n_syn,
        "t_half_atp_s": t_half,
        "atp_end_mM": float(atp[-1]),
        "rps_mean": float(np.mean(np.abs(omega))),
        "collapsed": bool(atp[-1] < 0.4),
    }


def slow_lineage(p: Params, arm: str, rng: random.Random) -> dict[str, Any]:
    """One cell, one shortest-telomere bottleneck, PD = 0..horizon."""
    if arm == "FIB":
        L = p.l0_fib_kb
        eta = p.eta0_fib
        tert = p.tert_on_fib
        sod = p.sod_fib
        leak = p.leak_frac_fib
        tx = False
    elif arm == "PSC":
        L = p.l0_psc_kb
        eta = p.eta0_psc
        tert = p.tert_on_psc
        sod = p.sod_psc
        leak = p.leak_frac_psc
        tx = False
    elif arm == "PSC_TX":
        L = p.l0_psc_kb
        eta = p.eta0_psc
        tert = p.tert_on_psc
        sod = p.sod_psc
        leak = p.leak_frac_psc
        tx = True
    else:
        raise ValueError(arm)

    m = cusp_modulator(p.cusp_m)
    x_cusp = cusp_order_parameter(p.cusp_a, p.cusp_b)
    # Modulators scale rates; stoichiometry n_c, ATP/rev stay pure.
    eta *= (0.85 + 0.15 * x_cusp) * (0.7 + 0.3 * m)
    eta = _clamp(eta, 0.15, 0.97)
    tert = _clamp(tert * (0.8 + 0.25 * m), 0.0, 1.0)
    sod = _clamp(sod * (0.75 + 0.3 * m), 0.15, 1.2)

    n = p.pd_horizon + 1
    rec = {
        "pd": [],
        "L_kb": [],
        "eta": [],
        "tert": [],
        "ros": [],
        "p_sen": [],
        "atp_ss_mM": [],
        "rps_ss": [],
        "sbox": [],
        "pov": [],
        "pov_id": [],
        "transplanted": [],
    }
    ros = 0.08
    transplanted = False
    senescent = False
    senesce_pd = None

    for pd in range(n):
        if tx and (not transplanted) and pd >= p.tx_pd:
            transplanted = True
            eta = _clamp(eta + p.tx_eta_boost, 0.15, 0.98)
            leak *= p.tx_leak_cut
            tert = p.tx_tert_lock
            sod = _clamp(sod + p.tx_sod_boost, 0.15, 1.3)

        # Steady ATP/rotation snapshot (fast model, O2 on, short).
        snap = fast_oxphos(p, o2=p.o2_on, eta=eta, n_steps=400)
        atp_ss = float(snap["atp_mM"][-1])
        rps_ss = float(np.mean(np.abs(snap["rps"][-80:])))

        leak_eff = leak * (1.4 - eta)
        ros = _clamp(ros * (1.0 - 0.35 * sod) + leak_eff * (0.6 + 0.4 * (1.0 - eta)), 0.01, 1.5)
        eta = _clamp(eta * (1.0 - 0.012 * ros), 0.12, 0.98)

        p_sen = 1.0 / (1.0 + math.exp(-(p.senescence_kb - L) / 0.45))
        p_sen = _clamp(p_sen + 0.25 * max(ros - 0.25, 0.0) ** 1.4, 0.0, 1.0)
        if L <= p.crisis_kb:
            p_sen = 1.0

        byte = pack_state_byte(L, atp_ss, ros, eta, tert, pd)
        s_val, pov, pov_id = sbox_pov(byte)
        # Biology overlay: S-box remains the scrambled readout, but an
        # immortal-lock / transplant bit is reported when the physics agrees.
        if transplanted and L > 8.0 and tert > 0.85 and ros < 0.2:
            pov, pov_id = "immortal_lock", 7
        elif transplanted:
            pov, pov_id = "transplant_dock", 6

        rec["pd"].append(pd)
        rec["L_kb"].append(L)
        rec["eta"].append(eta)
        rec["tert"].append(tert)
        rec["ros"].append(ros)
        rec["p_sen"].append(p_sen)
        rec["atp_ss_mM"].append(atp_ss)
        rec["rps_ss"].append(rps_ss)
        rec["sbox"].append(s_val)
        rec["pov"].append(pov)
        rec["pov_id"].append(pov_id)
        rec["transplanted"].append(transplanted)

        # Threshold senescence (Hayflick), not a tiny independent coin-flip
        # each PD — that would force eventual arrest even at high L.
        if (not senescent) and pd > 6 and (L <= p.senescence_kb or ros >= 0.85 or p_sen >= 0.55):
            senescent = True
            senesce_pd = pd
            tert = 0.0

        if senescent:
            L = max(L - (p.delta_bp_per_pd * 0.25) / 1000.0, 0.5)
            continue

        loss_kb = p.delta_bp_per_pd / 1000.0
        # Stochastic TERT addition (Poisson, mean tert_add * activity).
        add_bp = rng.gauss(p.tert_add_bp * tert, 18.0) if tert > 0.05 else 0.0
        add_bp = max(add_bp, 0.0)
        L = _clamp(L - loss_kb + add_bp / 1000.0, 0.4, 16.0)

    L_arr = np.array(rec["L_kb"])
    psen_arr = np.array(rec["p_sen"])
    immortal = bool(
        L_arr[-1] > 4.0
        and float(np.mean(psen_arr[-20:])) < 0.08
        and not senescent
        and rec["atp_ss_mM"][-1] > 1.8
    )
    pov_counts = {name: 0 for name in SBOX_POV.values()}
    for name in rec["pov"]:
        pov_counts[name] += 1

    return {
        "arm": arm,
        "cusp_m": p.cusp_m,
        "cusp_order_x": round(x_cusp, 4),
        "cusp_modulator": round(m, 4),
        "records": rec,
        "senescent": senescent,
        "senesce_pd": senesce_pd,
        "L_end_kb": round(float(L_arr[-1]), 4),
        "L_min_kb": round(float(L_arr.min()), 4),
        "p_sen_tail": round(float(np.mean(psen_arr[-20:])), 4),
        "immortal_lock": immortal,
        "pov_occupancy": pov_counts,
        "transplanted": bool(tx and transplanted),
        "n_c_invariant": p.n_c,
        "atp_per_rev_invariant": p.atp_per_rev,
    }


def style_ax(ax: Any, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_title(title, color="#14324e", fontsize=11, pad=8)
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.grid(True, alpha=0.25, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def make_figures(run_dir: Path, fast_on: dict, fast_off: dict, arms: dict[str, dict], sweep: list[dict]) -> list[str]:
    fig_dir = run_dir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    colors = {"FIB": "#8a3b2c", "PSC": "#2b6cb0", "PSC_TX": "#2f855a"}

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    ax.plot(fast_on["t_s"], fast_on["atp_mM"], color="#2f855a", lw=2.0, label="O2 on")
    ax.plot(fast_off["t_s"], fast_off["atp_mM"], color="#c53030", lw=2.0, label="O2 off (no terminal acceptor)")
    style_ax(ax, "Fig. 1. ATP collapse without a terminal electron acceptor", "time (s)", "ATP (mM)")
    ax.legend(frameon=False)
    p1 = fig_dir / "fig1_atp_collapse.png"
    fig.tight_layout()
    fig.savefig(p1)
    plt.close(fig)
    paths.append(str(p1))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    ax.plot(fast_on["t_s"], fast_on["rps"], color="#6b46c1", lw=1.6, label="rotation O2 on")
    ax.plot(fast_off["t_s"], fast_off["rps"], color="#dd6b20", lw=1.6, label="rotation O2 off")
    style_ax(ax, "Fig. 2. ATP-synthase rotation (rev/s)", "time (s)", "rps")
    ax.legend(frameon=False)
    p2 = fig_dir / "fig2_rotation.png"
    fig.tight_layout()
    fig.savefig(p2)
    plt.close(fig)
    paths.append(str(p2))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for arm, tr in arms.items():
        ax.plot(tr["records"]["pd"], tr["records"]["L_kb"], color=colors[arm], lw=2.0, label=arm)
    ax.axhline(5.0, color="#718096", ls="--", lw=1, label="senescence threshold")
    ax.axhline(3.0, color="#c53030", ls=":", lw=1, label="crisis")
    style_ax(ax, "Fig. 3. Shortest-telomere length, one cell", "population doubling", "telomere (kb)")
    ax.legend(frameon=False, fontsize=8)
    p3 = fig_dir / "fig3_telomere.png"
    fig.tight_layout()
    fig.savefig(p3)
    plt.close(fig)
    paths.append(str(p3))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for arm, tr in arms.items():
        ax.plot(tr["records"]["pd"], tr["records"]["p_sen"], color=colors[arm], lw=2.0, label=arm)
    style_ax(ax, "Fig. 4. Senescence probability", "population doubling", "P(senescence)")
    ax.legend(frameon=False)
    p4 = fig_dir / "fig4_senescence.png"
    fig.tight_layout()
    fig.savefig(p4)
    plt.close(fig)
    paths.append(str(p4))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    ms = [s["cusp_m"] for s in sweep]
    for arm, col, mk in (("FIB", "#8a3b2c", "o"), ("PSC", "#2b6cb0", "s"), ("PSC_TX", "#2f855a", "D")):
        ax.plot(ms, [s["arms"][arm]["L_end_kb"] for s in sweep], color=col, marker=mk, lw=1.8, label=arm)
    style_ax(ax, "Fig. 5. CUSP modulator sweep — terminal telomere length", "cusp_m (0.25–3.0)", "L_end (kb)")
    ax.legend(frameon=False)
    p5 = fig_dir / "fig5_cusp_sweep.png"
    fig.tight_layout()
    fig.savefig(p5)
    plt.close(fig)
    paths.append(str(p5))

    fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=160)
    names = list(SBOX_POV.values())
    x = np.arange(len(names))
    w = 0.25
    for i, arm in enumerate(("FIB", "PSC", "PSC_TX")):
        occ = [arms[arm]["pov_occupancy"][n] for n in names]
        ax.bar(x + (i - 1) * w, occ, w, color=colors[arm], label=arm)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=30, ha="right", fontsize=8)
    style_ax(ax, "Fig. 6. S-box POV occupancy (AES S-box readout)", "POV class", "PD counts")
    ax.legend(frameon=False)
    p6 = fig_dir / "fig6_sbox_pov.png"
    fig.tight_layout()
    fig.savefig(p6)
    plt.close(fig)
    paths.append(str(p6))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for arm, tr in arms.items():
        ax.plot(tr["records"]["pd"], tr["records"]["eta"], color=colors[arm], lw=2.0, label=arm)
    style_ax(ax, "Fig. 7. OXPHOS coupling efficiency η", "population doubling", "η")
    ax.legend(frameon=False)
    p7 = fig_dir / "fig7_coupling.png"
    fig.tight_layout()
    fig.savefig(p7)
    plt.close(fig)
    paths.append(str(p7))
    return paths


def bind_cusp(payload: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {"bound": False}
    if not CUSP_DIR.exists():
        out["error"] = "cusp-agent-scheduler missing"
        return out
    state_path = CUSP_DIR / "data/state/cusp_psc_cellular_immortality_latest.json"
    _write_json(state_path, payload)
    pol_path = CUSP_DIR / "data/governance/cusp_psc_cellular_immortality_policy_2026-09-20.json"
    _write_json(
        pol_path,
        {
            "policy_id": POLICY_ID,
            "effective_date": "2026-09-20",
            "status": "active",
            "fusion": FUSION,
            "synthetic_only": True,
            "research_prototype": True,
            "compliance_ref": COMPLIANCE_REF,
            "disclaimer": DISCLAIMER,
            "modulator_bounds": [0.25, 3.0],
            "invariant": ["n_c", "atp_per_rev"],
        },
    )
    out["bound"] = True
    out["state"] = str(state_path)
    out["policy"] = str(pol_path)
    return out


def inventory_structures() -> dict[str, Any]:
    inv = {}
    for name, spec in BIONEMO_MODULES.items():
        fa = DATA / spec["fasta"]
        header, seq = load_fasta(fa) if fa.exists() else ("", "")
        metrics = sequence_metrics(seq) if seq else {}
        pdb = pdb_ca_rg(DATA / spec["pdb"])
        inv[name] = {
            **spec,
            "header": header,
            "sequence_metrics": metrics,
            "pdb_geometry": pdb,
            "fold_source": "experimental_PDB_not_OpenFold3",
            "plddt": None,
            "synthetic_only": True,
        }
    return inv


def summarize_arm(tr: dict[str, Any]) -> dict[str, Any]:
    rec = tr["records"]
    return {
        "arm": tr["arm"],
        "immortal_lock": tr["immortal_lock"],
        "senescent": tr["senescent"],
        "senesce_pd": tr["senesce_pd"],
        "L_end_kb": tr["L_end_kb"],
        "L_min_kb": tr["L_min_kb"],
        "p_sen_tail": tr["p_sen_tail"],
        "eta_end": round(float(rec["eta"][-1]), 4),
        "ros_end": round(float(rec["ros"][-1]), 4),
        "atp_ss_end_mM": round(float(rec["atp_ss_mM"][-1]), 4),
        "rps_ss_end": round(float(rec["rps_ss"][-1]), 3),
        "pov_occupancy": tr["pov_occupancy"],
        "transplanted": tr["transplanted"],
        "dominant_pov": max(tr["pov_occupancy"], key=tr["pov_occupancy"].get),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", default="")
    ap.add_argument("--finetune", default="", help="optional Astra JSON overriding Params fields")
    ap.add_argument("--tag", default="baseline")
    args = ap.parse_args()

    p = Params()
    finetune_meta: dict[str, Any] = {"applied": False}
    if args.finetune:
        ft_path = Path(args.finetune)
        ft = json.loads(ft_path.read_text(encoding="utf-8"))
        allowed = set(Params.__dataclass_fields__.keys())
        applied = {}
        for k, v in ft.items():
            if k in allowed:
                if k == "cusp_m":
                    v = _clamp(float(v), 0.25, 3.0)
                setattr(p, k, v)
                applied[k] = v
        # Never let a finetune change stoichiometry.
        p.n_c = 8
        p.atp_per_rev = 3
        finetune_meta = {"applied": True, "path": str(ft_path), "fields": applied}

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = Path(args.run_dir) if args.run_dir else ROOT / "runs" / f"psc_immortality_{args.tag}_{ts}"
    run_dir.mkdir(parents=True, exist_ok=True)

    rng = random.Random(p.seed)
    bionemo = probe_bionemo()
    structures = inventory_structures()

    eta_ref = _clamp(p.eta0_psc * cusp_modulator(p.cusp_m), 0.2, 0.97)
    fast_on = fast_oxphos(p, o2=1.0, eta=eta_ref)
    fast_off = fast_oxphos(p, o2=0.0, eta=eta_ref)

    arms = {}
    for arm in ("FIB", "PSC", "PSC_TX"):
        arms[arm] = slow_lineage(p, arm, rng)

    sweep = []
    for m in (0.25, 0.5, 1.0, 1.2, 1.5, 2.0, 3.0):
        pp = Params(**{**asdict(p), "cusp_m": m, "seed": p.seed + int(m * 100)})
        rng_m = random.Random(pp.seed)
        sweep.append(
            {
                "cusp_m": m,
                "modulator": round(cusp_modulator(m), 4),
                "order_x": round(cusp_order_parameter(pp.cusp_a, pp.cusp_b), 4),
                "arms": {a: summarize_arm(slow_lineage(pp, a, rng_m)) for a in ("FIB", "PSC", "PSC_TX")},
            }
        )

    figs = make_figures(run_dir, fast_on, fast_off, arms, sweep)
    summaries = {a: summarize_arm(tr) for a, tr in arms.items()}

    # Drop bulky arrays from the JSON receipt; keep CSV traces.
    for arm, tr in arms.items():
        rec = tr["records"]
        rows = ["pd,L_kb,eta,tert,ros,p_sen,atp_ss_mM,rps_ss,sbox,pov,transplanted"]
        for i in range(len(rec["pd"])):
            rows.append(
                ",".join(
                    str(rec[k][i])
                    for k in (
                        "pd",
                        "L_kb",
                        "eta",
                        "tert",
                        "ros",
                        "p_sen",
                        "atp_ss_mM",
                        "rps_ss",
                        "sbox",
                        "pov",
                        "transplanted",
                    )
                )
            )
        (run_dir / f"trace_{arm}.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")

    np.savez_compressed(
        run_dir / "fast_oxphos.npz",
        t_on=fast_on["t_s"],
        atp_on=fast_on["atp_mM"],
        dp_on=fast_on["dp_mV"],
        rps_on=fast_on["rps"],
        t_off=fast_off["t_s"],
        atp_off=fast_off["atp_mM"],
        dp_off=fast_off["dp_mV"],
        rps_off=fast_off["rps"],
    )

    receipt = {
        "synthetic_only": True,
        "research_prototype": True,
        "compliance_ref": COMPLIANCE_REF,
        "risk_flags": [
            "no_clinical",
            "unvalidated",
            "not_perpetual_motion",
            "hosted_nim_not_called",
            "experimental_PDB_not_predicted_fold",
        ],
        "version": "0.1.0",
        "disclaimer": DISCLAIMER,
        "policy_id": POLICY_ID,
        "theory_id": THEORY_ID,
        "wm_id": WM_ID,
        "fusion": FUSION,
        "created_at": utc_now(),
        "run_id": ts,
        "run_dir": str(run_dir),
        "tag": args.tag,
        "params": asdict(p),
        "finetune": finetune_meta,
        "bionemo": bionemo,
        "structures": structures,
        "fast_oxphos": {
            "o2_on": {k: _py(v) for k, v in fast_on.items() if k not in ("t_s", "atp_mM", "dp_mV", "rps")},
            "o2_off": {k: _py(v) for k, v in fast_off.items() if k not in ("t_s", "atp_mM", "dp_mV", "rps")},
        },
        "arms": summaries,
        "cusp_sweep": sweep,
        "figures": figs,
        "source_post": "https://x.com/grok/status/2101775150030963181",
        "thermodynamics": {
            "claim": "rotation is not free energy",
            "requires": ["proton_motive_force", "electron_transport", "terminal_acceptor"],
            "o2_off_collapses_seconds": True,
            "invariants": {"n_c": p.n_c, "atp_per_rev": p.atp_per_rev},
            "modulator_bounds": [0.25, 3.0],
        },
    }
    _write_json(run_dir / "receipt.json", _py(receipt))
    _write_json(run_dir / "astra_finetune_input.json", _py({"params": asdict(p), "arms": summaries, "sweep": sweep, "fast": receipt["fast_oxphos"]}))

    bind = bind_cusp(
        {
            "bound_at": utc_now(),
            "policy_id": POLICY_ID,
            "run_dir": str(run_dir),
            "arms": summaries,
            "synthetic_only": True,
            "research_prototype": True,
            "disclaimer": DISCLAIMER,
        }
    )
    _write_json(run_dir / "cusp_bind_result.json", bind)

    md = []
    md.append("# Singular PSC cellular-immortality simulation")
    md.append("")
    md.append(f"**Run** `{ts}` · **tag** `{args.tag}` · **policy** `{POLICY_ID}`")
    md.append("")
    md.append(DISCLAIMER)
    md.append("")
    md.append("## Equation (research model)")
    md.append("")
    md.append("```")
    md.append("e− → CI–CIV → O2 (terminal acceptor) → Δp")
    md.append("Δp → ATP synthase (n_c protons/rev, 3 ATP/rev) → ATP")
    md.append("L_{n+1} = L_n − δ + TERT_add · activity")
    md.append("CUSP: x^3 + a x + b = 0  (modulates η, TERT, SOD in [0.25, 3.0])")
    md.append("S-box: AES_SBOX[state_byte] → POV class")
    md.append("```")
    md.append("")
    md.append("## Fast OXPHOS (one cell, seconds)")
    md.append("")
    md.append(f"- O2 on: ATP_end = {fast_on['atp_end_mM']:.3f} mM, mean |rps| = {fast_on['rps_mean']:.1f}, collapsed = {fast_on['collapsed']}")
    md.append(f"- O2 off: ATP_end = {fast_off['atp_end_mM']:.3f} mM, t_half = {fast_off['t_half_atp_s']}, collapsed = {fast_off['collapsed']}")
    md.append("")
    md.append("## Slow lineage (one cell, 200 PD)")
    md.append("")
    md.append("| Arm | Immortal lock | Senesce PD | L_end (kb) | P_sen tail | dominant POV |")
    md.append("|-----|---------------|------------|------------|------------|--------------|")
    for a in ("FIB", "PSC", "PSC_TX"):
        s = summaries[a]
        md.append(
            f"| {a} | {s['immortal_lock']} | {s['senesce_pd']} | {s['L_end_kb']} | {s['p_sen_tail']} | {s['dominant_pov']} |"
        )
    md.append("")
    md.append("## BioNeMo toolkit")
    md.append("")
    md.append(f"- Hosted NIMs callable: `{bionemo['hosted_nims_callable']}` ({bionemo['reason_if_not']})")
    md.append("- Structure source: experimental PDB + UniProt sequences. No fabricated pLDDT.")
    for name, spec in structures.items():
        sm = spec.get("sequence_metrics") or {}
        pg = spec.get("pdb_geometry") or {}
        md.append(
            f"- **{name}** UniProt {spec['uniprot']}: {sm.get('length_aa')} aa, "
            f"PDB {spec['pdb_id']} Rg={pg.get('rg_angstrom')} Å, CA={pg.get('n_ca')}"
        )
    md.append("")
    md.append("## DT#9")
    md.append("")
    md.append(DISCLAIMER)
    (run_dir / "fusion_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({"run_dir": str(run_dir), "arms": summaries, "fast_off_collapsed": fast_off["collapsed"], "t_half_s": fast_off["t_half_atp_s"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
