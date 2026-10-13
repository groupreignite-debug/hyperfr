"""Fallback word timings when Scribe isn't reachable: align the known script to the take's pauses.

ElevenLabs reads pause at punctuation, so the take's silences mark phrase edges reliably. A
dynamic program maps every detected pause to a word boundary in the script (punctuation
boundaries are cheap, plain word boundaries cost more, a skipped punctuation boundary costs a
little), scoring each speech run by how well its length matches its letter count at the take's
average speaking rate. Words inside a run are spread by letter count.

  python3 scripts/align_pauses.py            # audio/vo/vo_track.wav → scripts/vo_words.json

Output has Scribe's shape ([{text, start, end, type}]), so cues.py --words reads either.
Prefer real Scribe timings when available.
"""
import importlib.util
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("cues", ROOT / "scripts" / "cues.py")
cues = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cues)

x, sr = sf.read(str(ROOT / "audio" / "vo" / "vo_track.wav"))
if x.ndim > 1:
    x = x.mean(1)
hop = int(sr * 0.01)
rms = np.sqrt(np.convolve(x ** 2, np.ones(hop * 2) / (hop * 2), mode="same"))[::hop] + 1e-9
db = 20 * np.log10(rms)
voiced = db > -38
t = np.arange(len(db)) * 0.01

on = np.flatnonzero(voiced)
v0, v1 = t[on[0]], t[on[-1]] + 0.01
# pauses ≥ 120 ms below -38 dB (ffmpeg silencedetect: ignores the short dips of stop consonants)
log = subprocess.run(["ffmpeg", "-v", "info", "-i", str(ROOT / "audio" / "vo" / "vo_track.wav"), "-af",
                      "silencedetect=noise=-38dB:d=0.12", "-f", "null", "-"], capture_output=True, text=True).stderr
ss = [float(m) for m in re.findall(r"silence_start: ([0-9.]+)", log)]
se = [float(m) for m in re.findall(r"silence_end: ([0-9.]+)", log)]
pauses = [(a, b) for a, b in zip(ss, se) if a > v0 + 0.05 and b < v1 - 0.05]
# a "speech" run under 120 ms between two pauses is a click or a dip, not a word: fold it into the silence
merged = []
for a, b in pauses:
    if merged and a - merged[-1][1] < 0.12:
        merged[-1] = (merged[-1][0], b)
    else:
        merged.append((a, b))
pauses = merged

words = [w for ln in cues.SCRIPT for w in ln.split()]
line_end = set(np.cumsum([len(ln.split()) for ln in cues.SCRIPT]) - 1)
weight = [len(re.sub(r"[^\w]", "", w)) + 1.5 for w in words]
punct = [bool(re.search(r"[،:.؟…]$", w)) or k in line_end for k, w in enumerate(words)]
cw = np.concatenate([[0], np.cumsum(weight)])
speech = (v1 - v0) - sum(b - a for a, b in pauses)
rate = speech / cw[-1]  # seconds per weight unit

# DP: anchors are pauses; state = (pause index p, boundary k = last word before the pause)
P, W = len(pauses), len(words)
starts = [v0] + [b for a, b in pauses]
ends = [a for a, b in pauses] + [v1]
INF = 1e18


def seg_cost(p, k0, k1):
    """Speech run p covers words k0..k1 inclusive."""
    if k1 < k0:
        return INF
    dur = ends[p] - starts[p]
    exp = (cw[k1 + 1] - cw[k0]) * rate
    c = abs(math.log(max(dur, 0.05) / exp)) * 2.0
    c += 0.35 * sum(punct[k] for k in range(k0, k1))  # punctuation read without a pause
    return c


best = {(-1, -1): (0.0, None)}
prev_layer = {-1: 0.0}
back = [dict() for _ in range(P + 1)]
for p in range(P + 1):
    layer = {}
    for k_prev, c_prev in prev_layer.items():
        k0 = k_prev + 1
        lo, hi = k0, min(W - 1, k0 + 30)
        if p == P:
            lo = hi = W - 1
        for k1 in range(lo, hi + 1):
            c = c_prev + seg_cost(p, k0, k1)
            if p < P:
                c += 0.0 if punct[k1] else 0.6  # a pause mid-phrase is possible but rarer
            if c < layer.get(k1, INF):
                layer[k1] = c
                back[p][k1] = k_prev
    prev_layer = layer

k = W - 1
bounds = []
for p in range(P, -1, -1):
    kp = back[p][k]
    bounds.append((p, kp + 1, k))
    k = kp
bounds.reverse()

out = []
for p, k0, k1 in bounds:
    s, e = starts[p], ends[p]
    tot = cw[k1 + 1] - cw[k0]
    for kk in range(k0, k1 + 1):
        a = s + (e - s) * (cw[kk] - cw[k0]) / tot
        b = s + (e - s) * (cw[kk + 1] - cw[k0]) / tot
        out.append({"text": words[kk], "start": round(a, 3), "end": round(b - (0.0 if kk == k1 else 0.02), 3), "type": "word"})

(ROOT / "scripts" / "vo_words.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
print(f"{len(pauses)} pauses, {W} words, rate {rate:.4f}s/unit, speech {v0:.2f}–{v1:.2f}s")
for p, k0, k1 in bounds:
    print(f"{starts[p]:6.2f}–{ends[p]:6.2f}  {' '.join(words[k0:k1 + 1])}")
