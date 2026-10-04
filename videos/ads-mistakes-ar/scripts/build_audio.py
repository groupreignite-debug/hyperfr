"""Procedural score + SFX for "3 أخطاء بتقتل إعلاناتك".

Modern, dark cinematic-electronic bed at 100 BPM: soft four-on-the-floor sub kick, filtered
claps, quiet 16th hats, a side-chained bass pulse and a minor pad (Dm - Bb - F - C).
Arrangement follows the cut: tight from frame 0 (no intro), lifts at each mistake, drops
to pad only while the weak-CTA ad "does nothing" (void), rebuilds for the ending, and lands
one deep hit on the payoff line. The bed is pre-ducked ~8 dB under every VO line so it
never fights the voice. SFX are restrained UI ticks, swipes, pops and whooshes.

Outputs (48 kHz stereo, PCM16): audio/music.wav, audio/sfx.wav
Cue sheet: scripts/cues.json (keep in sync with index.html).
"""
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
ROOT = Path(__file__).resolve().parent.parent
cues = json.loads((ROOT / "scripts" / "cues.json").read_text())
DUR = float(cues["duration"])
N = int(SR * DUR)
T = np.arange(N) / SR
S = cues["sections"]
rng = np.random.default_rng(11)
BPM = 100
BEAT = 60 / BPM


def flt(x, kind, hz, order=2):
    return sosfilt(butter(order, hz, kind, fs=SR, output="sos"), x)


def env(points):
    ts, vs = zip(*points)
    return np.interp(T, ts, vs)


def place(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf) or i < 0:
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def st(x):
    return np.stack([x, x], 1)


# ---------------------------------------------------------------- music ---
def kick():
    L = int(0.42 * SR); t = np.arange(L) / SR
    f = 48 + 90 * np.exp(-t * 38)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 8.5) + flt(rng.standard_normal(L), "low", 900) * np.exp(-t * 90) * 0.25


def clap():
    L = int(0.25 * SR); t = np.arange(L) / SR
    n = flt(rng.standard_normal(L), "band", [900, 3800])
    e = np.exp(-t * 26) + 0.6 * np.exp(-np.maximum(t - 0.012, 0) * 30) * (t > 0.012)
    return n * e * 0.5


def hat():
    L = int(0.045 * SR); t = np.arange(L) / SR
    return flt(rng.standard_normal(L), "high", 7000) * np.exp(-t * 110)


CHORDS = [  # Dm, Bb, F, C (one bar each)
    [36.71 * 2, 87.31 * 2, 110.0 * 2, 146.83 * 2],
    [58.27 * 2, 87.31 * 2, 116.54 * 2, 146.83 * 2],
    [43.65 * 2, 87.31 * 2, 130.81 * 2, 174.61 * 2],
    [65.41 * 2, 98.0 * 2, 130.81 * 2, 164.81 * 2],
]
BAR = BEAT * 4


def chord_at(t):
    return CHORDS[int(t // BAR) % 4]


def pad():
    out = np.zeros((N, 2))
    for b in range(int(DUR / BAR) + 1):
        t0 = b * BAR
        L = int(BAR * SR) + int(0.3 * SR)
        t = np.arange(L) / SR
        e = np.minimum(1, t / 0.25) * np.minimum(1, np.maximum(0, (BAR + 0.3 - t) / 0.3))
        for k, f in enumerate(chord_at(t0)):
            for dt, pan in ((-0.18, 0.25), (0.18, 0.75)):
                s = np.zeros(L)
                for h in range(1, 6):
                    s += np.sin(2 * np.pi * (f + dt) * h * t + k) / h
                place(out[:, 0], s * e * (1 - pan), t0)
                place(out[:, 1], s * e * pan, t0)
    out = np.stack([flt(out[:, 0], "low", 1400), flt(out[:, 1], "low", 1400)], 1)
    return out * 0.018


def bass():
    out = np.zeros(N)
    step = BEAT / 2
    L = int(step * SR); t = np.arange(L) / SR
    for i in range(int(DUR / step) + 1):
        t0 = i * step
        f = chord_at(t0)[0] / 2
        s = np.zeros(L)
        for h in range(1, 7):
            s += np.sin(2 * np.pi * f * h * t) / h * (-1) ** (h + 1)
        s *= np.minimum(1, t / 0.01) * np.exp(-t * 6)
        place(out, s, t0)
    return st(flt(out, "low", 420)) * 0.16


def pluck():
    """Sparse 8th-note arpeggio, top of the mix, for drive."""
    out = np.zeros((N, 2))
    step = BEAT / 2
    L = int(0.35 * SR); t = np.arange(L) / SR
    pat = [3, 1, 2, 1, 3, 2, 1, 2]
    for i in range(int(DUR / step) + 1):
        t0 = i * step
        f = chord_at(t0)[pat[i % 8]] * 2
        s = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2 * t)) * np.exp(-t * 16)
        pan = 0.3 if i % 2 else 0.7
        place(out[:, 0], s * (1 - pan), t0)
        place(out[:, 1], s * pan, t0)
    return out * 0.05


def grid(sig, every, offset=0.0):
    out = np.zeros(N)
    t = offset
    while t < DUR:
        place(out, sig, t)
        t += every
    return out


K = grid(kick(), BEAT)
C = grid(clap(), BEAT * 2, BEAT)
H = grid(hat(), BEAT / 4)

# side-chain pump from the kick grid
phase = (T % BEAT) / BEAT
pump = 0.45 + 0.55 * np.minimum(1, phase / 0.35)

m1, m2, m3, vd, en, po = S["m1"], S["m2"], S["m3"], S["void"], S["end"], S["payoff"]
g_kick = env([(0, 0.75), (S["title"], 0.75), (S["title"] + 0.1, 0.0), (m1 - 0.05, 0.0), (m1, 1), (vd - 0.05, 1), (vd, 0), (en, 0), (en + 0.05, 0.8), (po - 0.7, 0.8), (po - 0.65, 0), (po, 0), (po + 0.05, 1), (DUR - 1.0, 1), (DUR, 0)])
g_clap = env([(0, 0), (m1 - 0.05, 0), (m1, 0.8), (vd - 0.05, 0.8), (vd, 0), (po, 0), (po + 0.05, 0.8), (DUR, 0.5)])
g_hat = env([(0, 0.5), (S["title"], 0.3), (m1, 0.6), (m2, 0.8), (m3, 0.9), (vd - 0.05, 0.9), (vd, 0), (en, 0), (en + 0.05, 0.6), (DUR, 0.4)])
g_bass = env([(0, 0.8), (S["title"], 0.5), (m1, 1), (vd - 0.05, 1), (vd, 0.0), (en, 0.0), (en + 0.05, 0.8), (po - 0.7, 0.8), (po - 0.65, 0), (po, 0), (po + 0.05, 1), (DUR, 0.6)])
g_pluck = env([(0, 0.0), (m1, 0.0), (m2, 0.7), (m3, 1.0), (vd - 0.05, 1.0), (vd, 0), (en, 0), (en + 1.0, 0.8), (DUR, 0.6)])
g_pad = env([(0, 0.8), (S["title"], 1.1), (m1, 0.8), (vd, 1.3), (en, 1.0), (DUR, 1.2)])

music = (
    st(K * g_kick) * 0.55
    + st(C * g_clap) * 0.22
    + np.stack([flt(H, "high", 6000), np.roll(flt(H, "high", 6000), 300)], 1) * g_hat[:, None] * 0.035
    + bass() * (g_bass * pump)[:, None]
    + pluck() * (g_pluck * pump)[:, None]
    + pad() * (g_pad * (0.6 + 0.4 * pump))[:, None]
)
music *= env([(0, 1.0), (DUR - 1.2, 1.0), (DUR, 0.0)])[:, None]

# Pre-baked voiceover carve: ~-8 dB under every line, smooth edges.
vo_lens = {k: sf.info(str(ROOT / "audio" / "vo" / f"vo_{k}.wav")).duration for k in cues["vo"]}
duck = np.ones(N)
for k, start in cues["vo"].items():
    a, b = start - 0.1, start + vo_lens[k] + 0.1
    duck = np.minimum(duck, env([(0, 1), (max(a - 0.15, 0), 1), (max(a, 0.001), 0.4), (b, 0.4), (b + 0.35, 1), (DUR, 1)]))
music *= duck[:, None]


# ------------------------------------------------------------------ sfx ---
def impact(deep=False):
    L = int((2.4 if deep else 1.2) * SR); t = np.arange(L) / SR
    f = (32 if deep else 44) + (80 if deep else 60) * np.exp(-t * (8 if deep else 14))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (1.8 if deep else 3.4))
    thump = flt(rng.standard_normal(L), "low", 420) * np.exp(-t * 22) * 0.6
    tail = flt(rng.standard_normal(L), "low", 2000) * np.exp(-t * 4) * 0.06
    return st(np.tanh((body + thump + tail) * 1.4))


def tick():
    L = int(0.02 * SR); t = np.arange(L) / SR
    return st(np.sin(2 * np.pi * 3400 * t) * np.exp(-t * 480)) * 0.3


def click():
    L = int(0.035 * SR); t = np.arange(L) / SR
    s = flt(rng.standard_normal(L), "band", [2500, 7000]) * np.exp(-t * 240) + np.sin(2 * np.pi * 1800 * t) * np.exp(-t * 380) * 0.5
    return st(s) * 0.5


def whoosh(length):
    L = int(length * SR); t = np.arange(L) / SR
    shape = np.sin(np.pi * t / length) ** 2
    s = flt(rng.standard_normal(L), "band", [350, 3000]) * shape
    pan = np.linspace(-0.7, 0.7, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.7


def swipe():
    L = int(0.32 * SR); t = np.arange(L) / SR
    shape = (t / 0.32) ** 1.5 * np.exp(-np.maximum(t - 0.24, 0) * 40)
    s = flt(rng.standard_normal(L), "band", [1200, 6500]) * shape
    pan = np.linspace(0.6, -0.6, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.9


def blip(f0, f1, length=0.14):
    L = int(length * SR); t = np.arange(L) / SR
    f = np.linspace(f0, f1, L)
    return st(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 18) * np.minimum(1, t / 0.004)) * 0.35


def chime():
    L = int(1.2 * SR); t = np.arange(L) / SR
    s = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * d) * a for f, d, a in ((1318.5, 3.5, 0.5), (1975.5, 4.5, 0.3), (2637, 6, 0.15)))
    return st(s) * 0.35


def glitch():
    L = int(0.22 * SR)
    s = np.sign(np.sin(2 * np.pi * 180 * np.arange(L) / SR)) * (rng.random(L) > 0.4)
    s = flt(s.astype(float), "band", [400, 4000]) * np.repeat(rng.random(L // 480 + 1) > 0.3, 480)[:L]
    return st(s) * 0.25


def thud():
    L = int(0.6 * SR); t = np.arange(L) / SR
    return st(np.sin(2 * np.pi * np.cumsum(70 * np.exp(-t * 3)) / SR) * np.exp(-t * 7)) * 0.8


def riser(length):
    L = int(length * SR); t = np.arange(L) / SR
    n = rng.standard_normal(L); out = np.zeros(L); blk = 1200
    for s0 in range(0, L, blk):
        c = 300 + 4000 * (s0 / L) ** 2
        out[s0 : s0 + blk] = flt(n[s0 : s0 + blk], "band", [c * 0.6, c * 1.4])
    tone = np.sin(2 * np.pi * np.cumsum(60 + 80 * (t / length) ** 2) / SR) * 0.4
    return st((out * 0.5 + tone) * (t / length) ** 2.2) * 0.4


GEN = {
    "impact": lambda: impact(False), "deep": lambda: impact(True), "tick": tick, "click": click,
    "whoosh": lambda: whoosh(0.5), "whoosh_long": lambda: whoosh(0.85), "swipe": swipe,
    "pop": lambda: blip(600, 1400, 0.12), "blip_up": lambda: blip(500, 1600, 0.22),
    "blip_down": lambda: blip(900, 260, 0.3), "chime": chime, "glitch": glitch, "thud": thud,
}

sfx = np.zeros((N, 2))
for t, kind, gain in cues["sfx"]:
    if kind.startswith("riser:"):
        length = float(kind.split(":")[1])
        place(sfx, riser(length), t - length + 0.8, gain)
    else:
        place(sfx, GEN[kind](), t, gain)
# SFX also sit under the voice, but less than the music
sfx *= (0.55 + 0.45 * duck)[:, None]


def finish(x, peak_db):
    x = x - x.mean(0)
    return x / (np.max(np.abs(x)) + 1e-9) * (10 ** (peak_db / 20))


sf.write(str(ROOT / "audio" / "music.wav"), finish(music, -9.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(ROOT / "audio" / "sfx.wav"), finish(sfx, -6.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote music.wav, sfx.wav", DUR, "s")
