"""Procedural score + SFX for the Reignite "Vanity Metrics" reel (series شو يعني؟ #2, v2 script).

Dark, minimal, tech-leaning bed: detuned D-minor drone, soft sub pulse, muted hats and a
quiet pluck arpeggio (same palette as the Incrementality reel). It is already playing at frame 0 (no fade-in),
hushes around the strike-through before the real question, and resolves under the end card. The music is
pre-ducked ~-7 dB under the VO phrases. All times come from scripts/cues.json (build_vo.py), so another take
only needs build_vo.py -> apply_cues.py -> this script.

SFX are subtle and only mark visual state changes: fast like-pops under the hearts from frame 0, a low thud
when 0 زبون lands, a stamp on the rent bill, balloon pops, counter ticks, a whoosh as the 10 dots enter the
shop, a short scratch on the strike-through, and the Reignite chime on the end card.

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
PH = CUES["phrases"]
AN = CUES["anchors"]
DUR = CUES["duration"]
END = CUES["endcard"]
N = int(SR * DUR)
rng = np.random.default_rng(11)
T = np.arange(N) / SR


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


# ------------------------------------------------------------------ cues ---
def PS(k):
    return PH[k][0]


def PE(k):
    return PH[k][1]


SC = {  # scene starts — keep in step with scripts/apply_cues.py
    "term": PS("02a") - 0.25, "balloons": PS("03a") - 0.35, "shop": PS("05") - 0.35,
    "split": PS("08a") - 0.35, "realq": PS("09a") - 0.3, "viewer": PS("10a") - 0.3,
}
Q0, Q1 = PE("09a"), PS("09c")            # hush around the strike-through, back in on "قدّيش رسالة إجت"


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
    cut = env([(0, 520), (SC["term"], 380), (SC["balloons"], 600), (SC["shop"], 480), (SC["split"], 760),
               (SC["realq"], 850), (Q0, 180), (Q1, 700), (SC["viewer"], 500), (END, 380), (DUR, 200)])
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
    gate = env([(0, 0.7), (SC["term"], 0.6), (SC["balloons"], 0.65), (SC["shop"], 0.7), (SC["realq"], 0.8),
                (Q0 - 0.1, 0.3), (Q0, 0), (Q1, 0), (Q1 + 0.1, 0.85), (SC["viewer"], 0.5), (END - 0.1, 0.2),
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
    gate = env([(0, 0.6), (SC["balloons"], 0.6), (SC["shop"], 0.6), (SC["split"], 0.75), (SC["realq"], 0.8),
                (Q0, 0), (Q1, 0), (Q1 + 0.1, 0.7), (SC["viewer"], 0.4), (END, 0), (DUR, 0)])
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
    gate = env([(0, 0), (SC["term"], 0), (SC["term"] + 0.6, 0.5), (SC["balloons"], 0.6), (SC["shop"], 0.65),
                (SC["split"], 0.7), (SC["realq"], 0.6), (Q0 - 0.2, 0.5), (Q0, 0), (SC["viewer"], 0),
                (SC["viewer"] + 0.5, 0.4), (END, 0), (DUR, 0)])
    return np.stack([lp(buf_l, 2800) * gate, lp(buf_r, 2800) * gate], 1) * 0.05


def air():
    n = rng.standard_normal((N, 2))
    n = np.stack([bp(n[:, 0], 1800, 5600), bp(n[:, 1], 1800, 5600)], 1)
    g = env([(0, 0.15), (SC["balloons"], 0.3), (SC["realq"], 0.3), (Q0, 0.55), (Q1, 0.35), (END, 0.45), (DUR, 0)])
    return n * g[:, None] * 0.012


def end_pad():
    """Warm resolving chord under the end card (D maj9-ish, open)."""
    freqs = [146.83, 220.0, 293.66, 369.99, 440.0]
    s = sum(np.sin(2 * np.pi * f * T + i) for i, f in enumerate(freqs)) / len(freqs)
    g = env([(0, 0), (END - 0.8, 0), (END + 0.2, 0.9), (DUR - 0.8, 0.7), (DUR, 0)])
    s = lp(s, 1500) * g
    return np.stack([s, np.roll(s, int(0.013 * SR))], 1) * 0.09


music = drone() + sub_pulse() + hats() + plucks() + air() + end_pad()
master = env([(0, 0.8), (SC["term"], 0.8), (SC["balloons"], 0.8), (SC["split"], 0.85), (SC["realq"], 0.9),
              (Q0 - 0.1, 0.5), (Q0 + 0.2, 0.12), (Q1 - 0.1, 0.15), (Q1 + 0.1, 0.95), (SC["viewer"], 0.6),
              (END, 0.7), (DUR - 0.4, 0.25), (DUR, 0)])
music *= master[:, None]

duck = np.ones(N)
for ps, pe in PH.values():
    a, b = ps - 0.12, pe + 0.15
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




def pop():
    """Balloon pop: a short bright noise burst with a tiny low thump."""
    L = int(0.18 * SR)
    t = np.arange(L) / SR
    burst = bp(rng.standard_normal(L), 900, 6500) * np.exp(-t * 70)
    thump = np.sin(2 * np.pi * (180 * np.exp(-t * 30) + 60) * t) * np.exp(-t * 40) * 0.6
    return stereo(np.tanh((burst + thump) * 1.6)) * 0.55


def scratch():
    """Marker strike: filtered noise with a rough sawtooth amplitude, ~0.45s."""
    L = int(0.45 * SR)
    t = np.arange(L) / SR
    rough = 0.55 + 0.45 * np.abs(np.sin(2 * np.pi * 26 * t))
    s = bp(rng.standard_normal(L), 1400, 5200) * rough * np.sin(np.pi * t / 0.45) ** 0.6
    pan = np.linspace(0.4, -0.4, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.7


def likepop():
    """Tiny bright tap — the 'like' counter firing."""
    L = int(0.05 * SR)
    t = np.arange(L) / SR
    s = np.sin(2 * np.pi * (1500 + 900 * np.exp(-t * 60)) * t) * np.exp(-t * 110)
    return stereo(s) * 0.4


def stamp():
    """Rubber stamp: a dull thump plus a short paper slap."""
    L = int(0.35 * SR)
    t = np.arange(L) / SR
    thump = np.sin(2 * np.pi * (70 + 90 * np.exp(-t * 40)) * t) * np.exp(-t * 18)
    slap = bp(rng.standard_normal(L), 600, 3500) * np.exp(-t * 45) * 0.7
    return stereo(np.tanh((thump + slap) * 1.8)) * 0.6


GEN = {"impact": lambda: impact(False), "deep": lambda: impact(True), "click": click, "tick": tick,
       "whoosh": lambda: whoosh(0.55), "whoosh_long": lambda: whoosh(0.9), "chime": chime, "pop": pop,
       "scratch": scratch, "likepop": likepop, "stamp": stamp}

SFX = []


def ticks(t0, t1, every, gain=0.35):
    t = t0
    while t <= t1 + 1e-6:
        SFX.append((t, "tick", gain))
        t += every


# keep in step with the GSAP times in index.html
tz = AN["zboun"]
# 01 hook: like-pops under the hearts from frame 0, a low thud when 0 زبون lands
lp_r = np.random.default_rng(5)
t = 0.0
while t < tz - 0.05:
    SFX.append((t, "likepop", 0.22 + 0.18 * lp_r.random()))
    t += 0.07 + 0.06 * lp_r.random()
SFX += [(tz, "deep", 0.85), (tz, "click", 0.4)]
# 02 term + rent-bill stamp
SFX += [(SC["term"] + 0.05, "whoosh", 0.3)]
ticks(AN["vanity"] - 0.25, AN["vanity"] - 0.25 + 12 * 0.035, 0.035, 0.28)
SFX += [(PE("02a") - 0.1, "click", 0.3), (AN["rent"] - 0.4, "whoosh", 0.2), (AN["rent"] + 0.2, "stamp", 0.8)]
# 03 balloons
for k in ("likes", "views", "followers"):
    SFX.append((AN[k] - 0.1, "whoosh", 0.22))
    ticks(AN[k] - 0.05, AN[k] + 0.75, 0.08, 0.22)
tPop = AN["pop"]
SFX += [(tPop - 0.35, "click", 0.3)]
SFX += [(tPop + 0.195 + i * 0.375, "pop", 0.7) for i in range(3)]
SFX += [(AN["zboun2"] - 0.15, "impact", 0.5)]
# 04 shop
SFX += [(SC["shop"], "whoosh", 0.35)]
ticks(AN["alf"] - 0.25, AN["alf"] + 0.75, 0.07, 0.28)
SFX += [(AN["ten"] + 0.05, "whoosh_long", 0.5), (AN["ten"] + 0.25, "click", 0.35)]
SFX += [(AN["two"], "click", 0.5), (AN["two"] + 0.12, "click", 0.45), (AN["two"] + 0.1, "impact", 0.45)]
SFX += [(AN["reach"] - 0.2, "click", 0.35), (AN["biz"] - 0.1, "impact", 0.6)]
# 05 split
SFX += [(SC["split"], "whoosh", 0.35), (AN["actionable"] - 0.1, "click", 0.45)]
SFX += [(AN[k] - 0.05, "click", 0.35) for k in ("item1", "item2", "item3", "item4")]
# 06 the real question
SFX += [(SC["realq"], "whoosh", 0.3), (AN["likesq"] - 0.35, "click", 0.3), (PE("09a") + 0.05, "scratch", 0.6),
        (AN["msg"] - 0.1, "click", 0.35), (AN["msg"] + 0.55, "whoosh", 0.3), (AN["sale"] - 0.12, "impact", 0.6)]
# 07 question to the viewer
SFX += [(SC["viewer"], "whoosh", 0.3), (SC["viewer"] + 0.15, "click", 0.35), (AN["comments"] - 0.1, "click", 0.3)]
# 08 end card
SFX += [(END - 0.5, "whoosh_long", 0.3), (END + 0.1, "chime", 0.55), (END + 0.1, "deep", 0.3)]

sfx = np.zeros((N, 2))
for t, kind, gain in SFX:
    if kind.startswith("riser:"):
        length = float(kind.split(":")[1])
        place(sfx, riser(length), t - length, gain)
    else:
        place(sfx, GEN[kind](), t, gain)


# stem peaks are set so the VO stays the loudest element (VO lines peak around -1.7 dBFS)
def finish(x, peak_db):
    x = x - x.mean(0)
    pk = np.max(np.abs(x)) + 1e-9
    return x / pk * (10 ** (peak_db / 20))


sf.write(str(ROOT / "audio" / "music.wav"), finish(music, -9.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(ROOT / "audio" / "sfx.wav"), finish(sfx, -12.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote audio/music.wav, audio/sfx.wav", DUR, "s,", len(SFX), "sfx events")
