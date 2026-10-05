"""Procedural score + SFX for the Reignite "Incrementality" reel.

Dark, minimal, tech-leaning bed: detuned D-minor drone, soft sub pulse, muted hats and a
quiet pluck arpeggio. It drops to near-silence at the FREEZE (6.2s) and again before the
real question (63.5s), then resolves under the end card. The music is pre-ducked ~-7 dB
under every VO line (starts come from scripts/cues.json, written by build_vo.py).

SFX are restrained and only mark visual state changes: counter ticks, UI clicks,
soft whooshes, low impacts on the key numbers, one riser, and a soft chime on the logo.

Outputs (48 kHz stereo, 16-bit): audio/music.wav, audio/sfx.wav
"""
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
ROOT = Path(__file__).resolve().parent.parent
# Cue times below are authored on the original cue sheet; TIMEMAP re-times them onto the
# client voiceover (scripts/timemap.json, written by build_vo_human.py).
_tm = json.loads((ROOT / "scripts" / "timemap.json").read_text())
TIMEMAP = _tm["anchors"]
DUR = _tm["duration"]
N = int(SR * DUR)
rng = np.random.default_rng(11)
T = np.arange(N) / SR
LINES = {ln["line"]: ln for ln in json.loads((ROOT / "scripts" / "cues_human.json").read_text())["lines"]}


def M(t):
    for (o0, n0), (o1, n1) in zip(TIMEMAP, TIMEMAP[1:]):
        if o0 <= t <= o1:
            return n0 + (t - o0) * (n1 - n0) / (o1 - o0)
    return TIMEMAP[-1][1] + (t - TIMEMAP[-1][0])


def lp(x, hz, order=2):
    return sosfilt(butter(order, hz, "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sosfilt(butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def env(points, remap=True):
    ts, vs = zip(*points)
    if remap:
        ts = [M(t) for t in ts]
    return np.interp(T, ts, vs)


def place(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf) or i < 0:
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


# ---------------------------------------------------------------- music ---
def saw(freq):
    out = np.zeros(N)
    for k in range(1, 8):
        out += ((-1) ** (k + 1)) * np.sin(2 * np.pi * freq * k * T) / k
    return out


def drone():
    notes = [36.71, 55.0, 73.42, 87.31, 110.0]  # D1 A1 D2 F2 A2
    l, r = np.zeros(N), np.zeros(N)
    for i, f in enumerate(notes):
        d = 0.1 + 0.05 * i
        g = 0.9 if i < 2 else 0.4
        l += saw(f - d) * g
        r += saw(f + d) * g
    cut = env([(0, 260), (5.5, 700), (6.2, 160), (9.4, 300), (21, 650), (24, 450), (50, 800),
               (60, 900), (63.5, 180), (65.8, 700), (68.4, 500), (72.4, 380), (75.4, 200)])
    outs = []
    for ch in (l, r):
        y = np.zeros(N)
        zi = None
        blk = 2400
        for s in range(0, N, blk):
            sos = butter(2, float(cut[min(s + blk // 2, N - 1)]), "low", fs=SR, output="sos")
            if zi is None:
                zi = np.zeros((sos.shape[0], 2))
            y[s:s + blk], zi = sosfilt(sos, ch[s:s + blk], zi=zi)
        outs.append(y)
    return np.stack(outs, 1) * 0.1


BPM = 100
BEAT = 60 / BPM


def sub_pulse():
    buf = np.zeros(N)
    L = int(0.42 * SR)
    kt = np.arange(L) / SR
    f = 44 + 58 * np.exp(-kt * 30)
    kick = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-kt * 8)
    t = 0.0
    while t < DUR:
        place(buf, kick, t)
        t += BEAT
    gate = env([(0, 0), (0.3, 0.6), (6.1, 0.8), (6.2, 0), (9.4, 0), (9.6, 0.6), (21.0, 0.7), (21.2, 0.3),
                (24.3, 0.5), (36, 0.65), (50, 0.75), (59.9, 0.8), (60.1, 0.3), (63.4, 0.3), (63.6, 0),
                (65.8, 0), (65.9, 0.85), (68.3, 0.85), (68.5, 0.3), (72.3, 0.2), (72.5, 0), (75.4, 0)])
    return np.stack([buf * gate] * 2, 1) * 0.45


def hats():
    step = BEAT / 2
    buf = np.zeros(N)
    L = int(0.05 * SR)
    hat = hp(rng.standard_normal(L), 6500) * np.exp(-np.arange(L) / SR * 95)
    t, k = 0.0, 0
    while t < DUR:
        place(buf, hat, t, 0.6 if k % 2 else 0.22)
        t += step
        k += 1
    gate = env([(0, 0), (1.0, 0.5), (6.1, 0.6), (6.2, 0), (11.0, 0), (11.2, 0.6), (21.0, 0.6), (21.2, 0),
                (27.0, 0), (27.2, 0.6), (49.9, 0.8), (50.1, 0.5), (59.9, 0.8), (60.0, 0), (65.8, 0),
                (65.9, 0.7), (68.3, 0.7), (68.4, 0), (75.4, 0)])
    l = buf * gate
    r = np.roll(buf, int(0.011 * SR)) * gate
    return np.stack([l, r], 1) * 0.045


def plucks():
    """Quiet D-minor-pentatonic arpeggio on 8ths — the 'data' texture."""
    scale = [293.66, 349.23, 392.0, 440.0, 523.25, 587.33]
    pattern = [0, 2, 4, 3, 1, 4, 2, 5]
    L = int(0.5 * SR)
    pt = np.arange(L) / SR
    buf_l, buf_r = np.zeros(N), np.zeros(N)
    t, k = 0.0, 0
    while t < DUR:
        f = scale[pattern[k % len(pattern)]]
        s = (np.sin(2 * np.pi * f * pt) + 0.3 * np.sin(2 * np.pi * 2 * f * pt)) * np.exp(-pt * 9)
        pan = 0.5 + 0.35 * np.sin(k * 0.9)
        place(buf_l, s * (1 - pan), t)
        place(buf_r, s * pan, t)
        t += BEAT / 2
        k += 1
    gate = env([(0, 0), (9.4, 0), (10.0, 0.6), (20.8, 0.7), (21.2, 0), (27.0, 0), (28.0, 0.45),
                (35.5, 0.5), (36.5, 0.6), (49.8, 0.7), (50.3, 0.5), (59.8, 0.6), (60.0, 0), (75.4, 0)])
    return np.stack([lp(buf_l, 2800) * gate, lp(buf_r, 2800) * gate], 1) * 0.05


def air():
    n = rng.standard_normal((N, 2))
    n = np.stack([bp(n[:, 0], 1800, 5600), bp(n[:, 1], 1800, 5600)], 1)
    g = env([(0, 0.15), (6.2, 0.25), (9.4, 0.1), (21.2, 0.45), (24.3, 0.2), (59.9, 0.3), (63.5, 0.55),
             (65.8, 0.35), (72.4, 0.45), (75.4, 0)])
    return n * g[:, None] * 0.012


def end_pad():
    """Warm resolving chord under the end card (D maj9-ish, open)."""
    freqs = [146.83, 220.0, 293.66, 369.99, 440.0]
    s = sum(np.sin(2 * np.pi * f * T + i) for i, f in enumerate(freqs)) / len(freqs)
    g = env([(0, 0), (71.6, 0), (72.6, 0.9), (74.6, 0.7), (75.4, 0)])
    s = lp(s, 1500) * g
    return np.stack([s, np.roll(s, int(0.013 * SR))], 1) * 0.09


music = drone() + sub_pulse() + hats() + plucks() + air() + end_pad()
master = env([(0, 0), (0.25, 0.75), (6.1, 0.85), (6.25, 0.18), (9.3, 0.2), (9.6, 0.75), (21, 0.8),
              (24.3, 0.85), (50, 0.9), (59.9, 0.9), (60.2, 0.55), (63.4, 0.5), (63.7, 0.12),
              (65.7, 0.15), (65.9, 0.95), (68.3, 0.9), (68.6, 0.6), (72.4, 0.7), (75.0, 0.25), (75.4, 0)])
music *= master[:, None]

duck = np.ones(N)
for ln in LINES.values():
    a, b = ln["start"] - 0.12, ln["end"] + 0.15
    duck = np.minimum(duck, env([(0, 1), (max(a - 0.15, 0), 1), (a, 0.45), (b, 0.45), (b + 0.35, 1), (DUR, 1)], remap=False))
music *= duck[:, None]


# ------------------------------------------------------------------ sfx ---
def stereo(s):
    return np.stack([s, s], 1)


def impact(deep=False):
    L = int((2.4 if deep else 1.3) * SR)
    t = np.arange(L) / SR
    f = (32 if deep else 44) + (70 if deep else 55) * np.exp(-t * (9 if deep else 14))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (1.8 if deep else 3.4))
    thump = lp(rng.standard_normal(L), 360) * np.exp(-t * 24) * 0.55
    tail = lp(rng.standard_normal(L), 1300) * np.exp(-t * 5) * 0.05
    return stereo(np.tanh((body + thump + tail) * 1.3))


def click():
    L = int(0.03 * SR)
    t = np.arange(L) / SR
    s = bp(rng.standard_normal(L), 2500, 7000) * np.exp(-t * 260) + np.sin(2 * np.pi * 1900 * t) * np.exp(-t * 420) * 0.4
    return stereo(s) * 0.5


def tick():
    L = int(0.016 * SR)
    t = np.arange(L) / SR
    return stereo(np.sin(2 * np.pi * 3300 * t) * np.exp(-t * 520)) * 0.25


def whoosh(length=0.55):
    L = int(length * SR)
    t = np.arange(L) / SR
    shape = np.sin(np.pi * t / length) ** 2
    s = bp(rng.standard_normal(L), 300, 2600) * shape
    pan = np.linspace(-0.6, 0.6, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.6


def riser(length):
    L = int(length * SR)
    t = np.arange(L) / SR
    n = rng.standard_normal(L)
    out = np.zeros(L)
    blk = 1200
    for s in range(0, L, blk):
        c = 300 + 3200 * (s / L) ** 2
        out[s:s + blk] = bp(n[s:s + blk], c * 0.6, c * 1.4)
    tone = np.sin(2 * np.pi * np.cumsum(55 + 55 * (t / length) ** 2) / SR) * 0.4
    return stereo((out * 0.5 + tone) * (t / length) ** 2.2) * 0.35


def chime():
    L = int(2.6 * SR)
    t = np.arange(L) / SR
    s = (np.sin(2 * np.pi * 587.33 * t) + 0.5 * np.sin(2 * np.pi * 880 * t) + 0.25 * np.sin(2 * np.pi * 1174.66 * t))
    s *= np.exp(-t * 2.2) * (1 - np.exp(-t * 60))
    return np.stack([s, np.roll(s, int(0.009 * SR))], 1) * 0.35


GEN = {"impact": lambda: impact(False), "deep": lambda: impact(True), "click": click, "tick": tick,
       "whoosh": lambda: whoosh(0.55), "whoosh_long": lambda: whoosh(0.9), "chime": chime}

SFX = []


def ticks(t0, t1, every, gain=0.35):
    # spacing is kept in real seconds; the span itself is re-timed
    t, end = M(t0), M(t1)
    while t <= end + 1e-6:
        SFX.append((t, "tick", gain, True))
        t += every


# 01 hook
SFX += [(0.28, "whoosh", 0.3)]
ticks(0.55, 1.75, 0.07)
SFX += [(2.95, "click", 0.5), (3.2, "whoosh", 0.25)]
ticks(3.43, 4.5, 0.07)
SFX += [(4.85, "click", 0.45), (5.15, "impact", 0.8)]
# freeze
SFX += [(6.2, "whoosh_long", 0.35), (6.2, "click", 0.35)]
# 03 dots
SFX += [(9.55, "whoosh", 0.35)]
ticks(9.65, 10.55, 0.06, 0.28)
SFX += [(11.13, "click", 0.6), (13.05, "click", 0.5), (16.1, "click", 0.3), (17.8, "whoosh", 0.3), (19.05, "impact", 0.6)]
# 04 term + split
SFX += [(20.8, "whoosh", 0.3), (21.3, "click", 0.4)]
ticks(22.7, 23.22, 0.04, 0.3)
SFX += [(24.45, "whoosh", 0.35), (25.2, "click", 0.4), (25.95, "whoosh", 0.45)]
ticks(29.9, 30.35, 0.05, 0.22)
ticks(34.3, 34.75, 0.05, 0.22)
SFX += [(34.95, "click", 0.45), (35.4, "whoosh", 0.3)]
# 05 control group
SFX += [(36.0, "whoosh", 0.4)]
ticks(39.45, 40.75, 0.078, 0.3)
ticks(41.15, 42.0, 0.078, 0.3)
SFX += [(43.45, "click", 0.4), (44.9, "click", 0.4), (46.5, "whoosh", 0.3), (46.75, "click", 0.5), (47.15, "impact", 0.7)]
# 06 dashboard
SFX += [(49.75, "whoosh", 0.3), (50.3, "whoosh", 0.4)]
ticks(52.05, 53.25, 0.08, 0.3)
SFX += [(53.25, "click", 0.4), (54.55, "whoosh_long", 0.4), (55.3, "click", 0.35)]
ticks(57.4, 58.3, 0.08, 0.3)
SFX += [(58.4, "impact", 0.6)]
# 07 real question
SFX += [(59.6, "whoosh", 0.3), (60.95, "click", 0.3), (62.35, "click", 0.35), (63.55, "whoosh", 0.3),
        (65.8, "riser:1.7", 0.45), (65.8, "deep", 0.75)]
# 08 memory
SFX += [(68.05, "whoosh", 0.3), (68.75, "click", 0.3)]
ticks(69.55, 70.04, 0.035, 0.28)
SFX += [(71.95, "whoosh_long", 0.3)]
# 09 end card
SFX += [(72.55, "chime", 0.55), (72.55, "deep", 0.3)]

sfx = np.zeros((N, 2))
for ev in SFX:
    t, kind, gain = ev[0], ev[1], ev[2]
    if len(ev) < 4:
        t = M(t)
    if kind.startswith("riser:"):
        length = float(kind.split(":")[1])
        place(sfx, riser(length), t - length, gain)
    else:
        place(sfx, GEN[kind](), t, gain)


def finish(x, peak_db):
    x = x - x.mean(0)
    pk = np.max(np.abs(x)) + 1e-9
    return x / pk * (10 ** (peak_db / 20))


sf.write(str(ROOT / "audio" / "music.wav"), finish(music, -5.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(ROOT / "audio" / "sfx.wav"), finish(sfx, -4.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote audio/music.wav, audio/sfx.wav", DUR, "s,", len(SFX), "sfx events")
