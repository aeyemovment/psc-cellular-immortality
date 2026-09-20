#!/usr/bin/env python3
"""Singular substantia-nigra dopaminergic-neuron resilience simulator.

Post-mitotic sequel to the PSC immortality run (NA-PSC-IMM-001).
SNpc DA neurons do not divide. "Cellular immortality" here means
survival of one neuron under PD-like load, not telomere maintenance.

  1. Rotary ATP synthase + Complex I (terminal acceptor still required)
  2. Cav1.3-like Ca2+ pacemaking → mitochondrial oxidant stress
  3. Cytosolic dopamine oxidation
  4. α-synuclein oligomer load vs PINK1/Parkin mitophagy
  5. VTA vs SNpc (calbindin buffer)
  6. Proposed molecular-machinery transplant (research design, not a therapy)
  7. CUSP modulators bounded 0.25–3.0; n_c and ATP/rev invariant
  8. AES S-box observational POV map

This is a synthetic research prototype (DT#9).
NOT a Parkinson's cure, treatment, diagnostic, or clinical protocol.
In-silico precursor map of SNpc resilience mechanisms only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "snpc_da"
CUSP_DIR = Path.home() / "Library/Application Support/hazyeyes/cusp-agent-scheduler"

POLICY_ID = "CUSP-SNPC-DA-RESILIENCE-001"
THEORY_ID = "SNPC-DA-CI-ASYN-CA-TX-001"
WM_ID = "DT-SNPC-DA-RESILIENCE"
PRECURSOR_OF = "NA-PSC-IMM-001"
FUSION = (
    "Holo <> BioNeMo <> ATP-synthase-rotary <> Complex-I <> "
    "SNpc-DA <> Cav1.3-Ca <> SNCA <> PINK1-Parkin <> CALB1-VTA <> "
    "molecular-machinery-transplant <> CUSP* <> |S-box| POV"
)
COMPLIANCE_REF = "Addendum_5/C-00x"
DISCLAIMER = (
    "RESEARCH PROTOTYPE ONLY (DT#9). Synthetic single-neuron simulation. "
    "Not a Parkinson's disease cure, treatment, diagnostic, gene therapy, "
    "or clinical protocol. Not perpetual motion. SNpc DA neurons are "
    "post-mitotic: survival under PD-like load is not telomere immortality. "
    "Claims are bounded to this in-silico run. "
    "Not for clinical, diagnostic, production, or regulatory use."
)

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
    0: "pacemaker_ok",
    1: "high_ca_stress",
    2: "ci_deficit",
    3: "asyn_seed",
    4: "mitophagy",
    5: "transplant_dock",
    6: "degenerating",
    7: "survival_lock",
}

BIONEMO_MODULES = {
    "ATP5F1B": {
        "uniprot": "P06576", "role": "F1 catalytic beta — rotary ATP",
        "fasta": "ATP5F1B.fasta", "pdb": None, "pdb_id": "1E79",
        "nims": ["openfold3-nim", "boltz2-nim"],
    },
    "SOD2": {
        "uniprot": "P04179", "role": "mitochondrial MnSOD",
        "fasta": "SOD2.fasta", "pdb": None, "pdb_id": "1N0J",
        "nims": ["openfold3-nim"],
    },
    "SNCA": {
        "uniprot": "P37840", "role": "alpha-synuclein — PD protein",
        "fasta": "SNCA.fasta", "pdb": "1XQ8_SNCA.pdb", "pdb_id": "1XQ8",
        "nims": ["openfold3-nim", "boltz2-nim"],
    },
    "TH": {
        "uniprot": "P07101", "role": "tyrosine hydroxylase — DA synthesis",
        "fasta": "TH.fasta", "pdb": "2XSN_TH.pdb", "pdb_id": "2XSN",
        "nims": ["openfold3-nim"],
    },
    "NDUFS4": {
        "uniprot": "O43181", "role": "Complex I Fe-S subunit — PD-vulnerable",
        "fasta": "NDUFS4.fasta", "pdb": None, "pdb_id": None,
        "nims": ["openfold3-nim", "msa-search-nim"],
    },
    "PINK1": {
        "uniprot": "Q9BXM7", "role": "mitophagy kinase",
        "fasta": "PINK1.fasta", "pdb": "6EQI_PINK1.pdb", "pdb_id": "6EQI",
        "nims": ["openfold3-nim", "boltz2-nim"],
    },
    "PRKN": {
        "uniprot": "O60260", "role": "parkin E3 ligase — mitophagy",
        "fasta": "PRKN.fasta", "pdb": "5P33_PRKN.pdb", "pdb_id": "5P33",
        "nims": ["openfold3-nim"],
    },
    "CALB1": {
        "uniprot": "P05937", "role": "calbindin — VTA Ca2+ buffer / SNpc-sparing",
        "fasta": "CALB1.fasta", "pdb": "2F33_CALB1.pdb", "pdb_id": "2F33",
        "nims": ["openfold3-nim"],
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
    seed: int = 20260920
    n_c: int = 8
    atp_per_rev: int = 3
    rps_max: float = 250.0
    dp_max_mV: float = 180.0
    dp_threshold_mV: float = 40.0
    dp_reverse_mV: float = 50.0
    atp0_mM: float = 5.0
    atp_setpoint_mM: float = 5.2
    atp_use_per_s: float = 1.15  # peak SNpc pump load (seconds-scale only)
    k_syn_base: float = 2.2
    k_etc: float = 14.0
    k_leak: float = 0.28
    k_pmf_from_etc: float = 11.0
    k_pmf_from_synth: float = 0.032
    years_horizon: int = 80
    tx_year: int = 45
    mptp_year: int = 55
    mptp_years: int = 3
    mptp_ci_cut: float = 0.58
    o2_on: float = 1.0
    cusp_m: float = 1.2  # sequel default from PSC Astra peak
    cusp_a: float = -0.45
    cusp_b: float = 0.06
    # SNpc (vulnerable)
    eta0_sn: float = 0.74
    leak_sn: float = 0.022
    sod_sn: float = 0.62
    calb_sn: float = 0.18
    pace_sn: float = 0.85
    da_sn: float = 0.80
    asyn_prod_sn: float = 0.0045
    mito_sn: float = 0.70
    # VTA (more resistant)
    eta0_vta: float = 0.78
    leak_vta: float = 0.014
    sod_vta: float = 0.78
    calb_vta: float = 0.82
    pace_vta: float = 0.40
    da_vta: float = 0.55
    asyn_prod_vta: float = 0.0028
    mito_vta: float = 0.88
    # transplant (bounded; not a new energy source)
    tx_eta_boost: float = 0.12
    tx_leak_cut: float = 0.55
    tx_sod_boost: float = 0.22
    tx_calb_boost: float = 0.45
    tx_mito_boost: float = 0.20
    tx_asyn_clear: float = 0.35
    tx_ci_rescue: float = 0.18
    fast_t_end_s: float = 30.0
    fast_dt_s: float = 0.01
    atp_fail_mM: float = 1.05
    asyn_fail: float = 0.86
    ros_fail: float = 0.92
    ci_age_per_year: float = 0.0022


def load_fasta(path: Path) -> tuple[str, str]:
    header, seq = "", []
    if not path.exists():
        return "", ""
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
    if path is None or not path.exists():
        return {"exists": False}
    xs, ys, zs = [], [], []
    n_atom = 0
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
    x, y, z = np.array(xs), np.array(ys), np.array(zs)
    cx, cy, cz = float(x.mean()), float(y.mean()), float(z.mean())
    rg = float(np.sqrt(np.mean((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)))
    return {
        "exists": True, "n_atom": n_atom, "n_ca": len(xs),
        "rg_angstrom": round(rg, 3),
        "centroid": [round(cx, 2), round(cy, 2), round(cz, 2)],
    }


def probe_bionemo() -> dict[str, Any]:
    key = os.environ.get("NGC_API_KEY") or os.environ.get("NVIDIA_API_KEY")
    return {
        "toolkit_root": str(ROOT),
        "hosted_nims_callable": bool(key),
        "reason_if_not": None if key else "NGC_API_KEY/NVIDIA_API_KEY not set",
        "intended_nims": sorted({n for m in BIONEMO_MODULES.values() for n in m["nims"]}),
        "note": "Hosted NIMs not called. UniProt + experimental PDB. No fabricated pLDDT.",
        "paid_gpu_gate": "blocked_no_key",
        "precursor": PRECURSOR_OF,
    }


def cusp_order_parameter(a: float, b: float) -> float:
    disc = (b / 2.0) ** 2 + (a / 3.0) ** 3
    if disc >= 0:
        s = math.sqrt(disc)
        u = math.copysign(abs(-b / 2 + s) ** (1 / 3), -b / 2 + s)
        v = math.copysign(abs(-b / 2 - s) ** (1 / 3), -b / 2 - s)
        x = u + v
    else:
        r = math.sqrt(-a / 3.0)
        phi = math.acos(_clamp((-b / 2.0) / (r ** 3), -1.0, 1.0))
        roots = [2 * r * math.cos((phi + 2 * math.pi * k) / 3.0) for k in range(3)]
        x = max(roots, key=lambda z: abs(z))
    return _clamp(0.5 + 0.35 * math.tanh(x), 0.05, 0.98)


def cusp_modulator(m: float) -> float:
    m = _clamp(m, 0.25, 3.0)
    return _clamp(m / (1.0 + abs(m - 1.2) ** 1.4), 0.25, 2.2)


def pack_state_byte(atp: float, ros: float, asyn: float, ci: float, ca: float, alive: bool, tx: bool) -> int:
    b0 = 1 if atp > 2.5 else 0
    b1 = 1 if ros < 0.35 else 0
    b2 = 1 if asyn < 0.30 else 0
    b3 = 1 if ci > 0.55 else 0
    b4 = 1 if ca < 0.45 else 0
    b5 = 1 if alive else 0
    b6 = 1 if tx else 0
    b7 = 1 if alive and asyn < 0.25 and ci > 0.6 else 0
    return b0 | (b1 << 1) | (b2 << 2) | (b3 << 3) | (b4 << 4) | (b5 << 5) | (b6 << 6) | (b7 << 7)


def sbox_pov(byte: int) -> tuple[int, str, int]:
    s = AES_SBOX[byte & 0xFF]
    pov_id = s & 0x07
    return s, SBOX_POV[pov_id], pov_id


def fast_oxphos(p: Params, o2: float, eta: float, ci: float = 1.0) -> dict[str, Any]:
    """Seconds-scale ATP / Δp / rotation. CI scales ETC; thermodynamics enforced."""
    dt = p.fast_dt_s
    n = int(p.fast_t_end_s / dt)
    t = np.zeros(n)
    atp = np.zeros(n)
    dp = np.zeros(n)
    omega = np.zeros(n)
    atp[0] = p.atp0_mM
    dp[0] = 150.0
    k_syn_mM = p.k_syn_base * eta
    ci = _clamp(ci, 0.0, 1.0)
    for i in range(1, n):
        t[i] = i * dt
        o2_eff = max(o2, 0.0)
        etc = p.k_etc * o2_eff * ci * (1.0 - dp[i - 1] / p.dp_max_mV)
        leak = p.k_leak * (0.6 + 0.8 * (1.0 - eta)) * (dp[i - 1] / p.dp_max_mV)
        if dp[i - 1] >= p.dp_threshold_mV and o2_eff > 0.05 and ci > 0.08:
            frac = _clamp((dp[i - 1] - p.dp_threshold_mV) / (p.dp_max_mV - p.dp_threshold_mV), 0, 1)
            w = p.rps_max * eta * frac * (0.35 + 0.65 * ci)
            syn = 1.0
        elif dp[i - 1] < p.dp_reverse_mV and (o2_eff < 0.05 or ci < 0.08):
            w = -0.35 * p.rps_max * (1.0 - dp[i - 1] / p.dp_reverse_mV)
            syn = -0.55
        else:
            w = 0.0
            syn = 0.0
        drive = max(0.0, 1.0 - atp[i - 1] / max(p.atp_setpoint_mM * 1.25, 1e-6))
        d_atp = syn * k_syn_mM * (abs(w) / p.rps_max) * drive - p.atp_use_per_s * (atp[i - 1] / (atp[i - 1] + 0.8))
        d_dp = p.k_pmf_from_etc * etc - p.k_pmf_from_synth * abs(w) * max(syn, 0) - leak * p.dp_max_mV
        atp[i] = _clamp(atp[i - 1] + dt * d_atp, 0.0, 8.0)
        dp[i] = _clamp(dp[i - 1] + dt * d_dp, 0.0, p.dp_max_mV)
        omega[i] = w
        if (o2_eff < 0.05 or ci < 0.05) and atp[i] < 0.05 and dp[i] < 5:
            atp[i:] = atp[i]
            dp[i:] = dp[i]
            omega[i:] = 0.0
            t[i:] = t[i] + np.arange(n - i) * dt
            break
    t_half = None
    below = np.where(atp < 0.5 * p.atp0_mM)[0]
    if len(below):
        t_half = float(t[below[0]])
    return {
        "t_s": t, "atp_mM": atp, "dp_mV": dp, "rps": omega,
        "o2": o2, "eta": eta, "ci": ci,
        "t_half_atp_s": t_half,
        "atp_end_mM": float(atp[-1]),
        "rps_mean": float(np.mean(np.abs(omega))),
        "collapsed": bool(atp[-1] < 0.4),
    }


def arm_defaults(p: Params, arm: str) -> dict[str, float]:
    if arm in ("SNPC", "SNPC_TX"):
        return {
            "eta": p.eta0_sn, "leak": p.leak_sn, "sod": p.sod_sn, "calb": p.calb_sn,
            "pace": p.pace_sn, "da": p.da_sn, "asyn_prod": p.asyn_prod_sn, "mito": p.mito_sn,
        }
    if arm == "VTA":
        return {
            "eta": p.eta0_vta, "leak": p.leak_vta, "sod": p.sod_vta, "calb": p.calb_vta,
            "pace": p.pace_vta, "da": p.da_vta, "asyn_prod": p.asyn_prod_vta, "mito": p.mito_vta,
        }
    raise ValueError(arm)


def slow_neuron(p: Params, arm: str, insult: str, rng: random.Random) -> dict[str, Any]:
    """One post-mitotic DA neuron, one year per step, 0..80 years."""
    d = arm_defaults(p, arm)
    m = cusp_modulator(p.cusp_m)
    x_cusp = cusp_order_parameter(p.cusp_a, p.cusp_b)
    scale = (0.85 + 0.15 * x_cusp) * (0.7 + 0.3 * m)
    eta = _clamp(d["eta"] * scale, 0.15, 0.97)
    sod = _clamp(d["sod"] * (0.75 + 0.3 * m), 0.15, 1.2)
    mito = _clamp(d["mito"] * (0.8 + 0.2 * m), 0.2, 1.0)
    leak = d["leak"]
    calb = d["calb"]
    pace = d["pace"]
    da = d["da"]
    asyn_prod = d["asyn_prod"]
    if insult in ("SNCA", "COMBINED"):
        asyn_prod *= 2.4

    ci = 1.0
    ros = 0.08
    asyn = 0.04
    transplanted = False
    dead = False
    death_year = None

    rec = {k: [] for k in (
        "year", "atp", "eta", "ci", "ros", "asyn", "ca", "mito",
        "p_deg", "sbox", "pov", "alive", "transplanted"
    )}

    for year in range(p.years_horizon + 1):
        if arm == "SNPC_TX" and (not transplanted) and year >= p.tx_year:
            transplanted = True
            eta = _clamp(eta + p.tx_eta_boost, 0.15, 0.98)
            leak *= p.tx_leak_cut
            sod = _clamp(sod + p.tx_sod_boost, 0.15, 1.3)
            calb = _clamp(calb + p.tx_calb_boost, 0.0, 1.0)
            mito = _clamp(mito + p.tx_mito_boost, 0.2, 1.15)
            ci = _clamp(ci + p.tx_ci_rescue, 0.05, 1.0)

        toxin = 1.0
        if insult in ("MPTP", "COMBINED"):
            if year == p.mptp_year:
                toxin = p.mptp_ci_cut  # single pulse, not compounded yearly
            elif p.mptp_year < year < p.mptp_year + p.mptp_years:
                toxin = 0.97  # brief lingering, then aging-only

        ca = _clamp(pace * (1.0 - 0.75 * calb) * (0.85 + 0.15 * (year / 80.0)), 0.02, 1.0)
        da_cyto = _clamp(da * (0.7 + 0.35 * asyn), 0.05, 1.2)
        clear = mito * (0.55 + 0.45 * sod)
        if transplanted:
            clear = _clamp(clear + p.tx_asyn_clear, 0.0, 1.4)
        asyn = _clamp(
            asyn + asyn_prod * (1.0 + 1.1 * ros) - 0.11 * clear * asyn + rng.gauss(0, 0.002),
            0.0, 1.0,
        )
        ci *= (1.0 - p.ci_age_per_year) * (1.0 - 0.012 * asyn) * toxin
        ci = _clamp(ci, 0.08, 1.0)
        ros = _clamp(
            ros * (1.0 - 0.38 * sod)
            + 0.055 * ca
            + 0.045 * da_cyto
            + 0.06 * (1.0 - ci)
            + leak * 1.15,
            0.01, 1.4,
        )
        eta = _clamp(d["eta"] * (0.50 + 0.50 * ci) / (1.0 + 0.22 * ros) * (1.0 - 0.12 * ca) * scale, 0.12, 0.98)
        if transplanted:
            eta = _clamp(eta + 0.5 * p.tx_eta_boost, 0.15, 0.98)
        mito = _clamp(mito * (0.72 + 0.28 * ci) * (1.0 - 0.05 * asyn) + 0.015 * clear, 0.08, 1.15)

        # Yearly ATP is a quasi-steady snapshot, not a 30 s peak-pump integration.
        tax = 1.0 + 0.32 * ca + 0.22 * ros
        atp = _clamp(p.atp_setpoint_mM * eta * ci / tax, 0.0, 8.0)

        p_deg = 1.0 / (1.0 + math.exp(-(asyn - 0.62) / 0.10))
        p_deg = _clamp(p_deg + 0.25 * max(ros - 0.45, 0) + 0.35 * max(1.4 - atp, 0) / 1.4, 0.0, 1.0)
        if atp < p.atp_fail_mM or asyn >= p.asyn_fail or ros >= p.ros_fail or ci < 0.12:
            p_deg = 1.0

        byte = pack_state_byte(atp, ros, asyn, ci, ca, not dead, transplanted)
        s_val, pov, pov_id = sbox_pov(byte)
        if dead:
            pov, pov_id = "degenerating", 6
        elif transplanted and (not dead) and asyn < 0.28 and ci > 0.55 and atp > 2.2:
            pov, pov_id = "survival_lock", 7
        elif transplanted:
            pov, pov_id = "transplant_dock", 5
        elif (not dead) and calb > 0.6 and asyn < 0.25 and atp > 2.0:
            pov, pov_id = "pacemaker_ok", 0

        rec["year"].append(year)
        rec["atp"].append(atp)
        rec["eta"].append(eta)
        rec["ci"].append(ci)
        rec["ros"].append(ros)
        rec["asyn"].append(asyn)
        rec["ca"].append(ca)
        rec["mito"].append(mito)
        rec["p_deg"].append(p_deg)
        rec["sbox"].append(s_val)
        rec["pov"].append(pov)
        rec["alive"].append(not dead)
        rec["transplanted"].append(transplanted)

        if (not dead) and year > 34 and p_deg >= 0.80:
            dead = True
            death_year = year

        if dead:
            # post-death: ATP crash remainder, asyn locked high
            eta = _clamp(eta * 0.92, 0.05, 1)
            ci = _clamp(ci * 0.96, 0.05, 1)
            atp = _clamp(atp * 0.85, 0.0, 8)
            continue

    alive_end = not dead
    survival_lock = bool(alive_end and rec["asyn"][-1] < 0.40 and rec["atp"][-1] > 2.0 and rec["ci"][-1] > 0.35)
    pov_counts = {name: 0 for name in SBOX_POV.values()}
    for name in rec["pov"]:
        pov_counts[name] += 1
    return {
        "arm": arm, "insult": insult,
        "cusp_m": p.cusp_m, "cusp_order_x": round(x_cusp, 4),
        "cusp_modulator": round(m, 4),
        "records": rec,
        "dead": dead, "death_year": death_year,
        "alive_at_80": alive_end,
        "survival_lock": survival_lock,
        "asyn_end": round(float(rec["asyn"][-1]), 4),
        "ci_end": round(float(rec["ci"][-1]), 4),
        "ros_end": round(float(rec["ros"][-1]), 4),
        "eta_end": round(float(rec["eta"][-1]), 4),
        "atp_end": round(float(rec["atp"][-1]), 4),
        "pov_occupancy": pov_counts,
        "dominant_pov": max(pov_counts, key=pov_counts.get),
        "transplanted": bool(arm == "SNPC_TX" and transplanted),
        "n_c_invariant": p.n_c,
        "atp_per_rev_invariant": p.atp_per_rev,
        "post_mitotic": True,
        "not_a_pd_cure": True,
    }


def style_ax(ax: Any, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_title(title, color="#14324e", fontsize=11, pad=8)
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.grid(True, alpha=0.25, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def summarize(tr: dict[str, Any]) -> dict[str, Any]:
    return {
        "arm": tr["arm"], "insult": tr["insult"],
        "survival_lock": tr["survival_lock"],
        "alive_at_80": tr["alive_at_80"],
        "death_year": tr["death_year"],
        "asyn_end": tr["asyn_end"], "ci_end": tr["ci_end"],
        "ros_end": tr["ros_end"], "eta_end": tr["eta_end"],
        "atp_end": tr["atp_end"],
        "dominant_pov": tr["dominant_pov"],
        "pov_occupancy": tr["pov_occupancy"],
        "transplanted": tr["transplanted"],
    }


def make_figures(run_dir: Path, fast: dict, traces: dict[str, dict], sweep: list[dict]) -> list[str]:
    fig_dir = run_dir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    colors = {"SNPC": "#8a3b2c", "VTA": "#2b6cb0", "SNPC_TX": "#2f855a"}

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    ax.plot(fast["o2_on"]["t_s"], fast["o2_on"]["atp_mM"], color="#2f855a", lw=2, label="O2 on, CI intact")
    ax.plot(fast["o2_off"]["t_s"], fast["o2_off"]["atp_mM"], color="#c53030", lw=2, label="O2 off")
    ax.plot(fast["ci_block"]["t_s"], fast["ci_block"]["atp_mM"], color="#dd6b20", lw=2, label="O2 on, Complex I blocked")
    style_ax(ax, "Fig. 1. SNpc ATP collapse: no acceptor vs Complex I block", "time (s)", "ATP (mM)")
    ax.legend(frameon=False, fontsize=8)
    p1 = fig_dir / "fig1_atp_collapse.png"
    fig.tight_layout(); fig.savefig(p1); plt.close(fig); paths.append(str(p1))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for key, tr in traces.items():
        if tr["insult"] != "COMBINED":
            continue
        arm = tr["arm"]
        alive = np.array(tr["records"]["alive"], dtype=float)
        ax.step(tr["records"]["year"], alive, color=colors[arm], lw=2.0, where="post", label=arm)
    style_ax(ax, "Fig. 2. One-neuron survival under combined PD-like load", "age (years)", "alive")
    ax.set_ylim(-0.05, 1.15)
    ax.legend(frameon=False)
    p2 = fig_dir / "fig2_survival.png"
    fig.tight_layout(); fig.savefig(p2); plt.close(fig); paths.append(str(p2))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for key, tr in traces.items():
        if tr["insult"] != "COMBINED":
            continue
        arm = tr["arm"]
        ax.plot(tr["records"]["year"], tr["records"]["asyn"], color=colors[arm], lw=2.0, label=arm)
    ax.axhline(0.82, color="#c53030", ls=":", lw=1, label="asyn fail")
    style_ax(ax, "Fig. 3. Alpha-synuclein oligomer load (combined insult)", "age (years)", "asyn proxy")
    ax.legend(frameon=False, fontsize=8)
    p3 = fig_dir / "fig3_asyn.png"
    fig.tight_layout(); fig.savefig(p3); plt.close(fig); paths.append(str(p3))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for key, tr in traces.items():
        if tr["insult"] != "COMBINED":
            continue
        arm = tr["arm"]
        ax.plot(tr["records"]["year"], tr["records"]["ci"], color=colors[arm], lw=2.0, label=arm)
    style_ax(ax, "Fig. 4. Complex I activity (combined insult)", "age (years)", "CI")
    ax.legend(frameon=False)
    p4 = fig_dir / "fig4_complex_i.png"
    fig.tight_layout(); fig.savefig(p4); plt.close(fig); paths.append(str(p4))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    for key, tr in traces.items():
        if tr["insult"] != "WT":
            continue
        arm = tr["arm"]
        ax.plot(tr["records"]["year"], tr["records"]["ros"], color=colors[arm], lw=2.0, label=arm)
    style_ax(ax, "Fig. 5. ROS under wild-type aging (no toxin, no SNCA dose)", "age (years)", "ROS proxy")
    ax.legend(frameon=False)
    p5 = fig_dir / "fig5_ros_wt.png"
    fig.tight_layout(); fig.savefig(p5); plt.close(fig); paths.append(str(p5))

    fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=160)
    names = list(SBOX_POV.values())
    x = np.arange(len(names))
    w = 0.25
    combined = {a: traces[f"{a}|COMBINED"] for a in ("SNPC", "VTA", "SNPC_TX")}
    for i, arm in enumerate(("SNPC", "VTA", "SNPC_TX")):
        occ = [combined[arm]["pov_occupancy"][n] for n in names]
        ax.bar(x + (i - 1) * w, occ, w, color=colors[arm], label=arm)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=28, ha="right", fontsize=8)
    style_ax(ax, "Fig. 6. S-box POV occupancy (combined insult)", "POV class", "year counts")
    ax.legend(frameon=False)
    p6 = fig_dir / "fig6_sbox_pov.png"
    fig.tight_layout(); fig.savefig(p6); plt.close(fig); paths.append(str(p6))

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    ms = [s["cusp_m"] for s in sweep]
    for arm, col, mk in (("SNPC", "#8a3b2c", "o"), ("VTA", "#2b6cb0", "s"), ("SNPC_TX", "#2f855a", "D")):
        ys = []
        for s in sweep:
            dy = s["arms"][arm]["death_year"]
            ys.append(80 if dy is None else dy)
        ax.plot(ms, ys, color=col, marker=mk, lw=1.8, label=arm)
    ax.axhline(80, color="#718096", ls="--", lw=0.8)
    style_ax(ax, "Fig. 7. CUSP sweep — year of degeneration (combined insult)", "cusp_m (0.25-3.0)", "death year (80 = alive)")
    ax.legend(frameon=False)
    p7 = fig_dir / "fig7_cusp_sweep.png"
    fig.tight_layout(); fig.savefig(p7); plt.close(fig); paths.append(str(p7))

    fig, ax = plt.subplots(figsize=(7.4, 4.4), dpi=160)
    insults = ["WT", "SNCA", "MPTP", "COMBINED"]
    x = np.arange(len(insults))
    w = 0.25
    for i, arm in enumerate(("SNPC", "VTA", "SNPC_TX")):
        vals = []
        for ins in insults:
            tr = traces[f"{arm}|{ins}"]
            vals.append(80 if tr["death_year"] is None else tr["death_year"])
        ax.bar(x + (i - 1) * w, vals, w, color=colors[arm], label=arm)
    ax.set_xticks(x)
    ax.set_xticklabels(insults)
    ax.axhline(80, color="#718096", ls="--", lw=0.8)
    style_ax(ax, "Fig. 8. Year of degeneration by insult (80 = survived)", "insult", "death year")
    ax.legend(frameon=False)
    p8 = fig_dir / "fig8_insults.png"
    fig.tight_layout(); fig.savefig(p8); plt.close(fig); paths.append(str(p8))
    return paths


def inventory_structures() -> dict[str, Any]:
    inv = {}
    for name, spec in BIONEMO_MODULES.items():
        fa = DATA / spec["fasta"]
        header, seq = load_fasta(fa) if fa.exists() else ("", "")
        pdb_path = DATA / spec["pdb"] if spec.get("pdb") else None
        inv[name] = {
            **spec,
            "header": header,
            "sequence_metrics": sequence_metrics(seq) if seq else {},
            "pdb_geometry": pdb_ca_rg(pdb_path) if pdb_path else {"exists": False},
            "fold_source": "experimental_PDB_not_OpenFold3",
            "plddt": None,
            "synthetic_only": True,
        }
    return inv


def bind_cusp(payload: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {"bound": False}
    if not CUSP_DIR.exists():
        out["error"] = "cusp-agent-scheduler missing"
        return out
    state_path = CUSP_DIR / "data/state/cusp_snpc_da_resilience_latest.json"
    _write_json(state_path, payload)
    pol_path = CUSP_DIR / "data/governance/cusp_snpc_da_resilience_policy_2026-09-20.json"
    _write_json(
        pol_path,
        {
            "policy_id": POLICY_ID,
            "effective_date": "2026-09-20",
            "status": "active",
            "fusion": FUSION,
            "precursor": PRECURSOR_OF,
            "synthetic_only": True,
            "research_prototype": True,
            "not_a_pd_cure": True,
            "compliance_ref": COMPLIANCE_REF,
            "disclaimer": DISCLAIMER,
            "modulator_bounds": [0.25, 3.0],
            "invariant": ["n_c", "atp_per_rev"],
            "post_mitotic": True,
        },
    )
    out["bound"] = True
    out["state"] = str(state_path)
    out["policy"] = str(pol_path)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", default="")
    ap.add_argument("--finetune", default="")
    ap.add_argument("--tag", default="baseline")
    args = ap.parse_args()

    p = Params()
    finetune_meta: dict[str, Any] = {"applied": False}
    if args.finetune:
        ft = json.loads(Path(args.finetune).read_text(encoding="utf-8"))
        allowed = set(Params.__dataclass_fields__.keys())
        applied = {}
        for k, v in ft.items():
            if k in allowed:
                if k == "cusp_m":
                    v = _clamp(float(v), 0.25, 3.0)
                setattr(p, k, v)
                applied[k] = v
        p.n_c = 8
        p.atp_per_rev = 3
        finetune_meta = {"applied": True, "path": args.finetune, "fields": applied}

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = Path(args.run_dir) if args.run_dir else ROOT / "runs" / f"snpc_da_{args.tag}_{ts}"
    run_dir.mkdir(parents=True, exist_ok=True)

    rng = random.Random(p.seed)
    bionemo = probe_bionemo()
    structures = inventory_structures()

    eta_ref = _clamp(p.eta0_sn * cusp_modulator(p.cusp_m), 0.2, 0.97)
    fast = {
        "o2_on": fast_oxphos(p, o2=1.0, eta=eta_ref, ci=1.0),
        "o2_off": fast_oxphos(p, o2=0.0, eta=eta_ref, ci=1.0),
        "ci_block": fast_oxphos(p, o2=1.0, eta=eta_ref, ci=0.05),
    }

    traces: dict[str, dict] = {}
    for arm in ("SNPC", "VTA", "SNPC_TX"):
        for insult in ("WT", "SNCA", "MPTP", "COMBINED"):
            traces[f"{arm}|{insult}"] = slow_neuron(p, arm, insult, random.Random(p.seed + hash((arm, insult)) % 10000))

    sweep = []
    for m in (0.25, 0.5, 1.0, 1.2, 1.5, 2.0, 3.0):
        pp = Params(**{**asdict(p), "cusp_m": m, "seed": p.seed + int(m * 100)})
        sweep.append({
            "cusp_m": m,
            "modulator": round(cusp_modulator(m), 4),
            "arms": {
                a: summarize(slow_neuron(pp, a, "COMBINED", random.Random(pp.seed + hash(a) % 1000)))
                for a in ("SNPC", "VTA", "SNPC_TX")
            },
        })

    figs = make_figures(run_dir, fast, traces, sweep)
    summaries = {k: summarize(tr) for k, tr in traces.items()}

    for key, tr in traces.items():
        rec = tr["records"]
        safe = key.replace("|", "_")
        rows = ["year,atp,eta,ci,ros,asyn,ca,mito,p_deg,sbox,pov,alive,transplanted"]
        for i in range(len(rec["year"])):
            rows.append(",".join(str(rec[k][i]) for k in (
                "year", "atp", "eta", "ci", "ros", "asyn", "ca", "mito",
                "p_deg", "sbox", "pov", "alive", "transplanted",
            )))
        (run_dir / f"trace_{safe}.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")

    np.savez_compressed(
        run_dir / "fast_oxphos.npz",
        t=fast["o2_on"]["t_s"],
        atp_on=fast["o2_on"]["atp_mM"],
        atp_off=fast["o2_off"]["atp_mM"],
        atp_ci=fast["ci_block"]["atp_mM"],
    )

    receipt = {
        "synthetic_only": True, "research_prototype": True,
        "not_a_pd_cure": True, "post_mitotic": True,
        "compliance_ref": COMPLIANCE_REF,
        "risk_flags": [
            "no_clinical", "unvalidated", "not_perpetual_motion",
            "not_a_pd_cure", "hosted_nim_not_called",
            "experimental_PDB_not_predicted_fold",
        ],
        "version": "0.1.0", "disclaimer": DISCLAIMER,
        "policy_id": POLICY_ID, "theory_id": THEORY_ID, "wm_id": WM_ID,
        "precursor": PRECURSOR_OF, "fusion": FUSION,
        "created_at": utc_now(), "run_id": ts, "run_dir": str(run_dir),
        "tag": args.tag, "params": asdict(p), "finetune": finetune_meta,
        "bionemo": bionemo, "structures": structures,
        "fast_oxphos": {
            k: {kk: _py(vv) for kk, vv in v.items() if kk not in ("t_s", "atp_mM", "dp_mV", "rps")}
            for k, v in fast.items()
        },
        "arms": summaries, "cusp_sweep": sweep, "figures": figs,
        "thermodynamics": {
            "claim": "rotation is not free energy",
            "requires": ["proton_motive_force", "electron_transport", "terminal_acceptor", "complex_I"],
            "invariants": {"n_c": p.n_c, "atp_per_rev": p.atp_per_rev},
            "modulator_bounds": [0.25, 3.0],
        },
        "pd_research_frame": (
            "In-silico precursor map of SNpc DA-neuron resilience. "
            "Does not treat, prevent, or cure Parkinson's disease."
        ),
    }
    _write_json(run_dir / "receipt.json", _py(receipt))

    bind = bind_cusp({
        "bound_at": utc_now(), "policy_id": POLICY_ID, "run_dir": str(run_dir),
        "arms": summaries, "synthetic_only": True, "not_a_pd_cure": True,
        "disclaimer": DISCLAIMER,
    })
    _write_json(run_dir / "cusp_bind_result.json", bind)

    md = [
        "# Singular SNpc DA-neuron resilience (PD-research precursor)",
        "",
        f"**Run** `{ts}` · **tag** `{args.tag}` · **policy** `{POLICY_ID}` · precursor `{PRECURSOR_OF}`",
        "",
        DISCLAIMER,
        "",
        "## Why this is not PSC immortality",
        "",
        "SNpc DA neurons are post-mitotic. Telomerase / Hayflick is the wrong clock. "
        "Survival under Ca2+ pacemaking, Complex I load, cytosolic DA, and α-synuclein is the clock.",
        "",
        "## Fast OXPHOS",
        "",
        f"- O2 on, CI intact: ATP_end = {fast['o2_on']['atp_end_mM']:.3f} mM, collapsed = {fast['o2_on']['collapsed']}",
        f"- O2 off: ATP_end = {fast['o2_off']['atp_end_mM']:.3f} mM, t_half = {fast['o2_off']['t_half_atp_s']}, collapsed = {fast['o2_off']['collapsed']}",
        f"- CI blocked: ATP_end = {fast['ci_block']['atp_end_mM']:.3f} mM, t_half = {fast['ci_block']['t_half_atp_s']}, collapsed = {fast['ci_block']['collapsed']}",
        "",
        "## Slow neuron (one cell, 80 years)",
        "",
        "| Arm | Insult | Alive@80 | Survival lock | Death year | asyn_end | CI_end | POV |",
        "|-----|--------|----------|---------------|------------|----------|--------|-----|",
    ]
    for arm in ("SNPC", "VTA", "SNPC_TX"):
        for insult in ("WT", "SNCA", "MPTP", "COMBINED"):
            s = summaries[f"{arm}|{insult}"]
            md.append(
                f"| {arm} | {insult} | {s['alive_at_80']} | {s['survival_lock']} | "
                f"{s['death_year']} | {s['asyn_end']} | {s['ci_end']} | {s['dominant_pov']} |"
            )
    md += ["", "## BioNeMo toolkit", "",
           f"- Hosted NIMs callable: `{bionemo['hosted_nims_callable']}` ({bionemo['reason_if_not']})"]
    for name, spec in structures.items():
        sm = spec.get("sequence_metrics") or {}
        pg = spec.get("pdb_geometry") or {}
        md.append(
            f"- **{name}** UniProt {spec['uniprot']}: {sm.get('length_aa')} aa, "
            f"PDB {spec.get('pdb_id')} Rg={pg.get('rg_angstrom')} Å"
        )
    md += ["", "## DT#9", "", DISCLAIMER]
    (run_dir / "fusion_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({
        "run_dir": str(run_dir),
        "fast": {k: {"collapsed": v["collapsed"], "t_half": v["t_half_atp_s"], "atp_end": v["atp_end_mM"]} for k, v in fast.items()},
        "combined": {a: summaries[f"{a}|COMBINED"] for a in ("SNPC", "VTA", "SNPC_TX")},
        "wt": {a: summaries[f"{a}|WT"] for a in ("SNPC", "VTA", "SNPC_TX")},
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
