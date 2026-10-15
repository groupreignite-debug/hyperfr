"""Procedural score + SFX for the Reignite "Retargeting" reel (series شو يعني؟).

Same dark, minimal bed as the earlier episodes: detuned D-minor drone, soft sub pulse, muted hats and
a quiet pluck arpeggio. It drops out at the FREEZE (صدفة؟) and goes fully silent on "لأ." (the stop beat),
thins out for the calm line in scene 10, then resolves under the end card. The music is pre-ducked
~-7 dB under every VO line and sits low so a trending sound can still be added inside Instagram.

SFX are subtle and only mark visual state changes: a tap on the jacket, three feed pops, a door bell,
digital blips when the Pixel pulses, card flicks for the repeated ad, a soft positive click when the
rule turns gold, and the Reignite chime on the end card.

All times come from scripts/cues.json (build_vo.py: Scribe word timings in film seconds), so a new VO
only needs build_vo.py -> apply_cues.py -> this script.
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
WORDS = CUES["words"]
LINES = CUES["lines"]
DUR = CUES["duration"]
END = CUES["endcard"]
N = int(SR * DUR)
rng = np.random.default_rng(11)
T = np.arange(N) / SR


def W(i):
    return WORDS[i][0]


def We(i):
    return WORDS[i][1]


# scene starts — keep in step with scripts/apply_cues.py
SC = {"s2": W(8) - 0.25, "s3": W(19) - 0.15, "s4": W(21) - 0.3, "s5": W(34) - 0.15, "s6": W(56) - 0.4,
      "s7": W(71) - 0.35, "s8": W(84) - 0.35, "s9": W(94) - 0.35, "s10": W(113) - 0.4, "s11": W(129) - 0.35}
F0, NO, F1 = SC["s3"], W(20), SC["s4"]          # freeze: صدفة؟ … لأ. (stop) … back in on Retargeting
C0, C1 = SC["s10"], SC["s11"]                   # the calm line


def lp(x, hz, order=2):
    return sosfilt(butter(order, hz, "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sosfilt(butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def env(points):
    ts, vs = zip(*points)
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
    cut = env([(0, 260), (F0 - 0.5, 700), (F0, 160), (F1, 300), (SC["s5"], 600), (SC["s6"], 700), (SC["s8"], 760),
               (SC["s9"], 850), (C0, 300), (C1, 650), (END, 380), (DUR, 200)])
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
    gate = env([(0, 0.6), (F0 - 0.1, 0.8), (F0, 0), (F1, 0), (F1 + 0.2, 0.6), (SC["s5"], 0.65),
                (SC["s6"], 0.7), (SC["s9"], 0.8), (C0 - 0.1, 0.5), (C0, 0), (C1, 0), (C1 + 0.1, 0.7),
                (END - 0.1, 0.2), (END, 0), (DUR, 0)])
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
    gate = env([(0, 0.5), (F0 - 0.1, 0.6), (F0, 0), (F1, 0), (F1 + 0.2, 0.6), (SC["s6"], 0.7),
                (SC["s9"], 0.8), (C0, 0), (C1, 0), (C1 + 0.1, 0.6), (END, 0), (DUR, 0)])
    l = buf * gate
    r = np.roll(buf, int(0.011 * SR)) * gate
    return np.stack([l, r], 1) * 0.045


def plucks():
    """Quiet D-minor-pentatonic arpeggio on 8ths."""
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
    gate = env([(0, 0), (F1, 0), (F1 + 0.6, 0.5), (SC["s5"], 0.6), (SC["s6"], 0.7), (SC["s9"], 0.65),
                (C0, 0.4), (C1 - 0.5, 0.3), (C1, 0), (END, 0), (DUR, 0)])
    return np.stack([lp(buf_l, 2800) * gate, lp(buf_r, 2800) * gate], 1) * 0.05


def air():
    n = rng.standard_normal((N, 2))
    n = np.stack([bp(n[:, 0], 1800, 5600), bp(n[:, 1], 1800, 5600)], 1)
    g = env([(0, 0.15), (F0, 0.25), (NO, 0.05), (F1, 0.1), (SC["s5"], 0.3), (C0, 0.45), (C1, 0.3),
             (END, 0.45), (DUR, 0)])
    return n * g[:, None] * 0.012


def end_pad():
    """Warm resolving chord under the end card (D maj9-ish, open)."""
    freqs = [146.83, 220.0, 293.66, 369.99, 440.0]
    s = sum(np.sin(2 * np.pi * f * T + i) for i, f in enumerate(freqs)) / len(freqs)
    g = env([(0, 0), (END - 0.8, 0), (END + 0.2, 0.9), (DUR - 0.8, 0.7), (DUR, 0)])
    s = lp(s, 1500) * g
    return np.stack([s, np.roll(s, int(0.013 * SR))], 1) * 0.09


music = drone() + sub_pulse() + hats() + plucks() + air() + end_pad()
# starts at frame 0 with no fade-in (brief, Oct 14). FREEZE dims the bed; "لأ." is a hard stop (silence) until Retargeting lands
master = env([(0, 0.75), (F0 - 0.1, 0.85), (F0 + 0.05, 0.2), (NO - 0.05, 0.2), (NO, 0.0),
              (F1 - 0.05, 0.0), (F1 + 0.3, 0.75), (SC["s6"], 0.8), (SC["s9"], 0.9), (C0 - 0.1, 0.7),
              (C0 + 0.3, 0.45), (C1 - 0.1, 0.45), (C1 + 0.2, 0.85), (END, 0.7), (DUR - 0.4, 0.25), (DUR, 0)])
music *= master[:, None]

duck = np.ones(N)
for ln in LINES.values():
    a, b = ln["s"] - 0.12, ln["e"] + 0.15
    duck = np.minimum(duck, env([(0, 1), (max(a - 0.15, 0), 1), (a, 0.45), (b, 0.45), (b + 0.35, 1), (DUR, 1)]))
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


def tap():
    """Soft finger tap on glass: a damped low-mid knock plus a tiny click."""
    L = int(0.08 * SR)
    t = np.arange(L) / SR
    knock = np.sin(2 * np.pi * 420 * t) * np.exp(-t * 70)
    s = knock + bp(rng.standard_normal(L), 2000, 6000) * np.exp(-t * 300) * 0.3
    return stereo(s) * 0.6


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


def notif_pop():
    """Light notification pop: quick rising bubble tone."""
    L = int(0.14 * SR)
    t = np.arange(L) / SR
    f = 700 + 900 * (1 - np.exp(-t * 40))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 28) * (1 - np.exp(-t * 900))
    return stereo(s) * 0.5


def bell():
    """Shop-door bell: two quick inharmonic strikes."""
    L = int(1.6 * SR)
    t = np.arange(L) / SR
    def strike(t0):
        tt = np.clip(t - t0, 0, None)
        on = (t >= t0).astype(float)
        return on * (np.sin(2 * np.pi * 1568 * tt) + 0.6 * np.sin(2 * np.pi * 2349 * tt) + 0.3 * np.sin(2 * np.pi * 4180 * tt)) * np.exp(-tt * 4.5)
    s = strike(0.0) + 0.7 * strike(0.11)
    return np.stack([s, np.roll(s, int(0.007 * SR))], 1) * 0.22


def blip():
    """Tiny digital blip for the Pixel pulse."""
    L = int(0.07 * SR)
    t = np.arange(L) / SR
    s = np.sign(np.sin(2 * np.pi * 1760 * t)) * 0.35 + np.sin(2 * np.pi * 2640 * t) * 0.5
    s = lp(s * np.exp(-t * 55) * (1 - np.exp(-t * 2000)), 6000)
    return stereo(s) * 0.4


def flick():
    """Card flick: a short airy slap."""
    L = int(0.09 * SR)
    t = np.arange(L) / SR
    s = bp(rng.standard_normal(L), 1200, 5500) * np.exp(-t * 60) * (1 - np.exp(-t * 3000))
    return stereo(s) * 0.7


def positive():
    """Soft positive click: two short rising notes."""
    L = int(0.5 * SR)
    t = np.arange(L) / SR
    a = np.sin(2 * np.pi * 880 * t) * np.exp(-t * 18)
    tb = np.clip(t - 0.09, 0, None)
    b = (t >= 0.09) * np.sin(2 * np.pi * 1318.5 * tb) * np.exp(-tb * 10)
    return stereo((a * 0.6 + b) * (1 - np.exp(-t * 800))) * 0.35


def rewind():
    """Tape-rewind zip: a fast falling squeal over scrubby noise, ~0.38s."""
    L = int(0.38 * SR)
    t = np.arange(L) / SR
    f = 2600 * np.exp(-t * 4.5) + 300
    squeal = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.35
    scrub = bp(rng.standard_normal(L), 1500, 6000) * (0.6 + 0.4 * np.sin(2 * np.pi * 38 * t))
    s = (squeal + scrub * 0.5) * np.sin(np.pi * t / 0.38) ** 0.7
    return stereo(s) * 0.55


def chime():
    L = int(2.6 * SR)
    t = np.arange(L) / SR
    s = (np.sin(2 * np.pi * 587.33 * t) + 0.5 * np.sin(2 * np.pi * 880 * t) + 0.25 * np.sin(2 * np.pi * 1174.66 * t))
    s *= np.exp(-t * 2.2) * (1 - np.exp(-t * 60))
    return np.stack([s, np.roll(s, int(0.009 * SR))], 1) * 0.35


GEN = {"impact": lambda: impact(False), "deep": lambda: impact(True), "click": click, "tap": tap, "tick": tick,
       "whoosh": lambda: whoosh(0.55), "whoosh_long": lambda: whoosh(0.9), "pop": notif_pop, "bell": bell,
       "blip": blip, "flick": flick, "positive": positive, "rewind": rewind, "chime": chime}

# keep in step with the GSAP times in index.html
SFX = []
# 01 hook: three notification pops from frame 0, whoosh-thud on لاحقك؟, tape-rewind zip on ⏪,
# then the tap on the jacket and the page closing
TAP = max(W(5), 1.9)
SFX += [(0.05, "pop", 0.6), (0.17, "pop", 0.6), (0.29, "pop", 0.65), (0.68, "whoosh", 0.35), (0.82, "impact", 0.6),
        (1.18, "rewind", 0.6), (TAP, "tap", 0.7), (W(7) - 0.1, "whoosh", 0.3)]
# 02 follow: three feed pops
SFX += [(W(13) - 0.25, "whoosh", 0.2), (W(14) + 0.42, "pop", 0.6), (W(16) + 0.02, "pop", 0.6), (W(17) + 0.07, "pop", 0.65)]
# 03 freeze: the stop on "لأ."
SFX += [(F0, "whoosh_long", 0.3), (NO - 0.02, "impact", 0.45)]
# 04 term
SFX += [(W(23) - 0.05 + i * 0.035, "tick", 0.25) for i in range(11)]
SFX += [(W(25) + 0.78, "click", 0.35)]
# 05 shop: the door bell when he walks in; the bubble
SFX += [(W(38) - 0.08, "bell", 0.7), (W(39), "click", 0.3), (W(43) - 0.1, "click", 0.3), (W(53) - 0.08, "pop", 0.45)]
# 06 pixel: a blip on every pulse, clicks on the visits
SFX += [(SC["s6"] + 1.0, "blip", 0.5)] + [(t, "blip", 0.55) for t in (W(62), W(65), W(68) + 0.15)]
SFX += [(W(64), "tap", 0.5), (W(68) - 0.05, "tap", 0.5)]
# 07 warm
SFX += [(W(72), "click", 0.25), (W(77) - 0.15, "click", 0.3), (W(82) - 0.15, "whoosh", 0.2)]
# 08 don't repeat: card flicks, then the stack slides away
SFX += [(t, "flick", 0.6) for t in (SC["s8"] + 0.25, W(87), W(88), W(90), W(91))]
SFX += [(We(93) + 0.05, "whoosh", 0.35)]
# 09 rules: a click per row, the gold row gets the positive click
SFX += [(W(94) - 0.05, "click", 0.35), (W(101) - 0.05, "click", 0.35), (W(104) + 0.1, "blip", 0.35),
        (W(108) - 0.05, "click", 0.35), (W(110) + 0.15, "positive", 0.7)]
# 10 the line: quiet
SFX += [(W(127) - 0.05, "whoosh", 0.18)]
# 11 CTA
SFX += [(SC["s11"] + 0.2, "pop", 0.45), (W(131) - 0.1, "blip", 0.4), (W(132) - 0.05, "click", 0.3)]
# 12 end card
SFX += [(END - 0.5, "whoosh_long", 0.3), (END + 0.1, "chime", 0.55), (END + 0.1, "deep", 0.3)]

sfx = np.zeros((N, 2))
for t, kind, gain in SFX:
    place(sfx, GEN[kind](), t, gain)


# stem peaks are set so the VO stays the loudest element
def finish(x, peak_db):
    x = x - x.mean(0)
    pk = np.max(np.abs(x)) + 1e-9
    return x / pk * (10 ** (peak_db / 20))


sf.write(str(ROOT / "audio" / "music.wav"), finish(music, -11.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(ROOT / "audio" / "sfx.wav"), finish(sfx, -12.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote audio/music.wav, audio/sfx.wav", DUR, "s,", len(SFX), "sfx events")
