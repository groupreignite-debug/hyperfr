"""Procedural score + SFX for the Reignite "Landing Page" reel (same bed as the earlier episodes).

Dark, minimal, tech-leaning bed: detuned D-minor drone, soft sub pulse, muted hats and a quiet
pluck arpeggio, pre-ducked ~-7 dB under every VO line, resolving under the end card.
Every cue time comes from scripts/cues.json (written by cues.py), so a new VO take only needs
`python3 scripts/cues.py --words …` then this script.

SFX (brief §6, subtle): tap + coin drop (01), a tick per counter increment (03), whoosh on the
page swap (06), a pop per highlight box (07), distant neighborhood ambience (09), door creak +
warm chime (10), three stamp thumps (11), the Reignite chime on the end card.

Outputs (48 kHz stereo, 16-bit): audio/music.wav, audio/sfx.wav
"""
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
ROOT = Path(__file__).resolve().parent.parent
CUES = json.loads((ROOT / "scripts" / "cues.json").read_text())
B = CUES["beats"]
LINES = CUES["lines"]
DUR = B["total"]
N = int(SR * DUR)
rng = np.random.default_rng(26)
T = np.arange(N) / SR


def lp(x, hz, order=2):
    return sosfilt(butter(order, hz, "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sosfilt(butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def env(points):
    pts = sorted(points)
    ts, vs = zip(*pts)
    return np.interp(T, ts, vs)


def place(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf) or i < 0:
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def stereo(s):
    return np.stack([s, s], 1)


# ---------------------------------------------------------------- music ---
def saw(freq):
    out = np.zeros(N)
    for k in range(1, 8):
        out += ((-1) ** (k + 1)) * np.sin(2 * np.pi * freq * k * T) / k
    return out


# section marks
S2, S6, S9, S11, S12, END = B["s2_phone"], B["s6_wipe"], B["s9_in"], B["s11_in"], B["s12_in"], B["end"]


def drone():
    notes = [36.71, 55.0, 73.42, 87.31, 110.0]  # D1 A1 D2 F2 A2
    l, r = np.zeros(N), np.zeros(N)
    for i, f in enumerate(notes):
        d = 0.1 + 0.05 * i
        g = 0.9 if i < 2 else 0.4
        l += saw(f - d) * g
        r += saw(f + d) * g
    cut = env([(0, 260), (S2, 520), (S6 - 0.2, 700), (S6 + 0.4, 420), (S9, 300), (S11, 700),
               (S12, 820), (END, 420), (DUR, 200)])
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
    gate = env([(0, 0), (0.3, 0.6), (S2 - 0.2, 0.7), (S2, 0.4), (S2 + 3, 0.65), (S6 - 0.1, 0.8), (S6 + 0.1, 0.2),
                (S6 + 1.5, 0.7), (S9 - 0.1, 0.7), (S9 + 0.1, 0), (S11 - 0.1, 0), (S11, 0.85), (END - 0.2, 0.85),
                (END, 0), (DUR, 0)])
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
    gate = env([(0, 0), (1.0, 0.5), (S2, 0.5), (S6 - 0.1, 0.7), (S6 + 0.1, 0), (S6 + 2.0, 0), (S6 + 2.2, 0.6),
                (S9 - 0.1, 0.6), (S9, 0), (S11, 0), (S11 + 0.2, 0.7), (END - 0.2, 0.7), (END, 0), (DUR, 0)])
    l = buf * gate
    r = np.roll(buf, int(0.011 * SR)) * gate
    return np.stack([l, r], 1) * 0.045


def plucks():
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
    gate = env([(0, 0), (S2, 0), (S2 + 0.6, 0.6), (S6, 0.65), (S6 + 0.3, 0.3), (S9 - 0.2, 0.55), (S9 + 0.3, 0.25),
                (S11 - 0.2, 0.3), (S11, 0), (S12, 0), (S12 + 0.4, 0.55), (END, 0.3), (DUR, 0)])
    return np.stack([lp(buf_l, 2800) * gate, lp(buf_r, 2800) * gate], 1) * 0.05


def air():
    n = rng.standard_normal((N, 2))
    n = np.stack([bp(n[:, 0], 1800, 5600), bp(n[:, 1], 1800, 5600)], 1)
    g = env([(0, 0.15), (S6, 0.3), (S9, 0.2), (S11, 0.35), (END, 0.45), (DUR, 0)])
    return n * g[:, None] * 0.012


def end_pad():
    freqs = [146.83, 220.0, 293.66, 369.99, 440.0]
    s = sum(np.sin(2 * np.pi * f * T + i) for i, f in enumerate(freqs)) / len(freqs)
    g = env([(0, 0), (END - 0.8, 0), (END + 0.2, 0.9), (DUR - 0.8, 0.7), (DUR, 0)])
    s = lp(s, 1500) * g
    return np.stack([s, np.roll(s, int(0.013 * SR))], 1) * 0.09


music = drone() + sub_pulse() + hats() + plucks() + air() + end_pad()
master = env([(0, 0), (0.25, 0.75), (S9 - 0.2, 0.85), (S9 + 0.3, 0.6), (S11 - 0.2, 0.6), (S11 + 0.2, 0.95),
              (END, 0.75), (DUR - 0.4, 0.25), (DUR, 0)])
music *= master[:, None]

duck = np.ones(N)
for ln in LINES:
    a, b = ln["start"] - 0.12, ln["end"] + 0.15
    duck = np.minimum(duck, env([(0, 1), (max(a - 0.15, 0.001), 1), (max(a, 0.002), 0.45), (b, 0.45), (b + 0.35, 1), (DUR, 1)]))
music *= duck[:, None]


# ------------------------------------------------------------------ sfx ---
def click():
    L = int(0.03 * SR)
    t = np.arange(L) / SR
    s = bp(rng.standard_normal(L), 2500, 7000) * np.exp(-t * 260) + np.sin(2 * np.pi * 1900 * t) * np.exp(-t * 420) * 0.4
    return stereo(s) * 0.5


def tap():
    L = int(0.08 * SR)
    t = np.arange(L) / SR
    s = np.sin(2 * np.pi * (520 + 300 * np.exp(-t * 60)) * t) * np.exp(-t * 70) + lp(rng.standard_normal(L), 2500) * np.exp(-t * 200) * 0.3
    return stereo(s) * 0.6


def tick():
    L = int(0.016 * SR)
    t = np.arange(L) / SR
    return stereo(np.sin(2 * np.pi * 3300 * t) * np.exp(-t * 520)) * 0.25


def pop():
    L = int(0.12 * SR)
    t = np.arange(L) / SR
    f = 380 + 900 * np.exp(-t * 45)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 38)
    return stereo(s) * 0.5


def whoosh(length=0.55):
    L = int(length * SR)
    t = np.arange(L) / SR
    shape = np.sin(np.pi * t / length) ** 2
    s = bp(rng.standard_normal(L), 300, 2600) * shape
    pan = np.linspace(-0.6, 0.6, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.6


def impact(deep=False):
    L = int((2.4 if deep else 1.3) * SR)
    t = np.arange(L) / SR
    f = (32 if deep else 44) + (70 if deep else 55) * np.exp(-t * (9 if deep else 14))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (1.8 if deep else 3.4))
    thump = lp(rng.standard_normal(L), 360) * np.exp(-t * 24) * 0.55
    return stereo(np.tanh((body + thump) * 1.3))


def stamp():
    L = int(0.5 * SR)
    t = np.arange(L) / SR
    f = 60 + 90 * np.exp(-t * 40)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 12)
    slap = bp(rng.standard_normal(L), 600, 3000) * np.exp(-t * 90) * 0.5
    return stereo(np.tanh((body + slap) * 1.6)) * 0.8


def coin_drop():
    """Metallic clink, two bounces, then a short roll."""
    L = int(1.9 * SR)
    t = np.arange(L) / SR
    out = np.zeros(L)
    for k, (t0, g) in enumerate([(0.0, 1.0), (0.16, 0.55), (0.27, 0.3)]):
        tt = np.clip(t - t0, 0, None)
        on = (t >= t0).astype(float)
        ring = (np.sin(2 * np.pi * 3150 * tt) + 0.6 * np.sin(2 * np.pi * 4720 * tt) + 0.35 * np.sin(2 * np.pi * 6890 * tt))
        out += ring * np.exp(-tt * (22 + 8 * k)) * on * g
    roll_on = np.clip((t - 0.4) * 8, 0, 1) * np.exp(-np.clip(t - 0.4, 0, None) * 1.6)
    flutter = 0.6 + 0.4 * np.sin(2 * np.pi * 14 * t)
    out += bp(rng.standard_normal(L), 2200, 6000) * roll_on * flutter * 0.25
    return stereo(out) * 0.32


def creak(length=1.0):
    L = int(length * SR)
    t = np.arange(L) / SR
    f0 = 150 + 70 * np.sin(np.pi * t / length) + 18 * np.sin(2 * np.pi * 7 * t)
    ph = np.cumsum(f0) / SR
    pulses = (np.sin(2 * np.pi * ph) > 0.92).astype(float)  # stick-slip pulse train
    s = bp(pulses, 300, 2400) + 0.3 * bp(np.sin(2 * np.pi * ph * 2.02), 500, 1800)
    shape = np.sin(np.pi * t / length) ** 0.6
    return stereo(s * shape) * 0.5


def chime(base=587.33):
    L = int(2.6 * SR)
    t = np.arange(L) / SR
    s = (np.sin(2 * np.pi * base * t) + 0.5 * np.sin(2 * np.pi * base * 1.5 * t) + 0.25 * np.sin(2 * np.pi * base * 2 * t))
    s *= np.exp(-t * 2.2) * (1 - np.exp(-t * 60))
    return np.stack([s, np.roll(s, int(0.009 * SR))], 1) * 0.35


def ambience(t0, t1):
    """Distant neighborhood: low wash, faint far-off chirps."""
    L = int((t1 - t0) * SR)
    t = np.arange(L) / SR
    wash = lp(rng.standard_normal((L, 2)).T, 700).T * 0.5
    sig = wash.copy()
    for k in range(int((t1 - t0) / 0.9)):
        c0 = 0.4 + k * 0.9 + (k % 3) * 0.17
        cl = 0.12
        i0 = int(c0 * SR)
        n = int(cl * SR)
        if i0 + n >= L:
            break
        ct = np.arange(n) / SR
        chirp = np.sin(2 * np.pi * (3400 + 900 * np.sin(np.pi * ct / cl)) * ct) * np.sin(np.pi * ct / cl) ** 2
        sig[i0:i0 + n, k % 2] += chirp * 0.12
    fade = np.minimum(1, np.minimum(t / 0.8, (t[-1] - t) / 0.8))
    return sig * fade[:, None] * 0.35


SFX = []  # (time, sound, gain)
# 01 hook
SFX += [(B["s1_ad"], whoosh(0.45), 0.25), (B["s1_tap"], tap(), 0.7), (B["s1_arrow"], whoosh(0.5), 0.3),
        (B["s1_house"], click(), 0.35), (B["s1_push"], whoosh(0.9), 0.3), (B["s1_coin"] - 0.02, coin_drop(), 0.9)]
# 02 example
SFX += [(B["s2_phone"], whoosh(0.9), 0.35), (B["s2_mark"], click(), 0.3)]
# 03 homepage: menu, then one tick per counter increment
SFX += [(B["s3_menu"], click(), 0.45), (B["s3_menu"] + 0.45, pop(), 0.35)]
for k, t in enumerate(B["s3_steps"]):
    SFX.append((t, tick(), 0.55))
    for j in range(CUES["home_buttons"][k]):
        SFX.append((t + 0.06 + j * 0.05, tick(), 0.4))
# 04 for everyone
SFX += [(B["s4_shrink"], whoosh(0.8), 0.3)] + [(t, click(), 0.3) for t in B["s4_p"]]
# 05 the ad
SFX += [(B["s5_ad"], pop(), 0.4), (B["s5_arrow"], whoosh(0.5), 0.2), (B["s5_q"], pop(), 0.35)]
# 06 page swap
SFX += [(B["s6_wipe"] + 0.1, whoosh(0.6), 0.6), (B["s6_term"], impact(), 0.45)]
# 07 a soft pop per highlight box
SFX += [(t, pop(), 0.5) for t in B["s7_k"]] + [(B["s7_tap"], tap(), 0.6)]
# 08 side by side
SFX += [(B["s8_split"], whoosh(0.8), 0.35), (B["s8_ad"], pop(), 0.3), (B["s8_line"], whoosh(0.45), 0.25)]
# 09 distant neighborhood ambience (mixed in below), 10 door creak + warm chime
SFX += [(B["s10_light"], impact(True), 0.25), (B["s10_door"], creak(0.9), 0.55), (B["s10_table"], chime(440.0), 0.4)]
# 11 three stamp thumps
SFX += [(t + 0.55, stamp(), 0.7) for t in B["s11_stamp"]]
# 12 cta
SFX += [(B["s12_in"], pop(), 0.3)] + [(t, click(), 0.3) for t in B["s12_chips"]]
# 13 the Reignite chime on the end card
SFX += [(B["end"], chime(), 0.55), (B["end"], impact(True), 0.25)]

sfx = np.zeros((N, 2))
for t, sig, gain in SFX:
    place(sfx, sig, t, gain)
amb = ambience(B["s9_in"], B["s11_in"])
place(sfx, amb, B["s9_in"], 1.0)


def finish(x, peak_db):
    x = x - x.mean(0)
    pk = np.max(np.abs(x)) + 1e-9
    return x / pk * (10 ** (peak_db / 20))


sf.write(str(ROOT / "audio" / "music.wav"), finish(music, -5.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(ROOT / "audio" / "sfx.wav"), finish(sfx, -4.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote audio/music.wav, audio/sfx.wav", DUR, "s,", len(SFX), "sfx events")
