"""Procedural score + SFX for the Reignite "A/B Testing" reel (series شو يعني؟).

Same dark, minimal bed as the earlier episodes: detuned D-minor drone, soft sub pulse, muted hats and
a quiet pluck arpeggio. It opens up on "the numbers are talking" (scene 08), thins out for the calm
"give it time" beat (scene 10), lifts on the winner (scene 12), then resolves under the end card.
The music is pre-ducked ~-7 dB under every VO line and sits low so a trending sound can still be added
inside Instagram.

SFX are subtle (brief section 5): a dull buzz for the ✗, a dart whoosh and a miss, paper flutter for the
flyers, a shop-door bell as the first people walk in, soft paper-stacking ticks as the piles grow, a
rubber-stamp thump for "1", calendar page flips, a soft positive chime when B wins, and the Reignite chime
on the end card. Very low street ambience sits under the juice-shop scenes.

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
SC = {"s2": W(11) - 0.25, "s3": W(16) - 0.3, "s4": W(32) - 0.35, "s5": W(41) - 0.3, "s6": W(52) - 0.3,
      "s7": W(59) - 0.25, "s8": W(65) - 0.3, "s9": W(73) - 0.3, "s10": W(95) - 0.05, "s11": W(108) - 0.35,
      "s12": W(117) - 0.3, "s13": W(129) - 0.3}
HIT = W(79)                                     # the "1" stamp (index.html: W(79))
WIN = W(128) - 0.05                             # B wins
C0, C1 = SC["s10"], SC["s11"]                   # the calm "give it time" beat


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
    cut = env([(0, 260), (SC["s3"], 520), (SC["s4"], 600), (SC["s6"], 680), (SC["s8"], 800), (SC["s9"], 700),
               (C0, 320), (C1, 650), (WIN, 850), (SC["s13"], 700), (END, 380), (DUR, 200)])
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
    gate = env([(0, 0), (0.3, 0.6), (SC["s3"], 0.6), (SC["s4"], 0.65), (SC["s6"], 0.7), (SC["s8"] - 0.05, 0.8),
                (SC["s9"], 0.75), (HIT - 0.05, 0.75), (HIT, 0), (HIT + 0.6, 0), (HIT + 0.9, 0.7), (C0 - 0.1, 0.5),
                (C0, 0), (C1, 0), (C1 + 0.1, 0.7), (END - 0.1, 0.2), (END, 0), (DUR, 0)])
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
    gate = env([(0, 0), (1.0, 0.5), (SC["s4"], 0.5), (SC["s6"], 0.7), (SC["s8"], 0.8), (HIT, 0), (HIT + 0.7, 0.7),
                (C0, 0), (C1, 0), (C1 + 0.1, 0.6), (END, 0), (DUR, 0)])
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
    gate = env([(0, 0), (SC["s3"], 0), (SC["s3"] + 0.6, 0.5), (SC["s5"], 0.6), (SC["s6"], 0.7), (SC["s9"], 0.65),
                (C0, 0.4), (C1 - 0.5, 0.3), (C1, 0.5), (WIN, 0.7), (END, 0), (DUR, 0)])
    return np.stack([lp(buf_l, 2800) * gate, lp(buf_r, 2800) * gate], 1) * 0.05


def air():
    n = rng.standard_normal((N, 2))
    n = np.stack([bp(n[:, 0], 1800, 5600), bp(n[:, 1], 1800, 5600)], 1)
    g = env([(0, 0.15), (SC["s4"], 0.25), (SC["s9"], 0.3), (C0, 0.45), (C1, 0.3), (END, 0.45), (DUR, 0)])
    return n * g[:, None] * 0.012


def end_pad():
    """Warm resolving chord under the end card (D maj9-ish, open)."""
    freqs = [146.83, 220.0, 293.66, 369.99, 440.0]
    s = sum(np.sin(2 * np.pi * f * T + i) for i, f in enumerate(freqs)) / len(freqs)
    g = env([(0, 0), (END - 0.8, 0), (END + 0.2, 0.9), (DUR - 0.8, 0.7), (DUR, 0)])
    s = lp(s, 1500) * g
    return np.stack([s, np.roll(s, int(0.013 * SR))], 1) * 0.09


music = drone() + sub_pulse() + hats() + plucks() + air() + end_pad()
# the "1" stamp dips the bed for a beat; "give it time" is calm
master = env([(0, 0), (0.25, 0.75), (SC["s4"], 0.8), (SC["s8"], 0.9), (HIT - 0.05, 0.9), (HIT + 0.05, 0.4),
              (HIT + 0.8, 0.85), (C0 - 0.1, 0.7), (C0 + 0.3, 0.45), (C1 - 0.1, 0.45), (C1 + 0.2, 0.85), (END, 0.7),
              (DUR - 0.4, 0.25), (DUR, 0)])
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


def chime():
    L = int(2.6 * SR)
    t = np.arange(L) / SR
    s = (np.sin(2 * np.pi * 587.33 * t) + 0.5 * np.sin(2 * np.pi * 880 * t) + 0.25 * np.sin(2 * np.pi * 1174.66 * t))
    s *= np.exp(-t * 2.2) * (1 - np.exp(-t * 60))
    return np.stack([s, np.roll(s, int(0.009 * SR))], 1) * 0.35


def pen(length=1.6):
    """Felt-pen line draw: band-limited scratch with a slow wobble."""
    L = int(length * SR)
    t = np.arange(L) / SR
    wob = 0.6 + 0.4 * np.sin(2 * np.pi * 7 * t + 1.3) * np.sin(2 * np.pi * 2.3 * t)
    s = bp(rng.standard_normal(L), 1800, 6500) * wob * np.minimum(1, t / 0.05) * np.minimum(1, (length - t) / 0.2)
    return stereo(s) * 0.35


def street(length):
    """Very low street ambience: distant traffic rumble + soft air, slow swells."""
    L = int(length * SR)
    t = np.arange(L) / SR
    rumble = lp(rng.standard_normal(L), 220) * (0.7 + 0.3 * np.sin(2 * np.pi * 0.13 * t))
    air_ = bp(rng.standard_normal(L), 600, 3000) * 0.25 * (0.6 + 0.4 * np.sin(2 * np.pi * 0.21 * t + 2))
    fade = np.minimum(1, t / 0.8) * np.minimum(1, (length - t) / 0.8)
    s = (rumble + air_) * fade
    return np.stack([s, np.roll(s, int(0.023 * SR))], 1) * 0.6


def fill():
    """Gentle rising fill tick: a soft sine sweep that settles on a note."""
    L = int(0.32 * SR)
    t = np.arange(L) / SR
    f = 520 + 360 * (1 - np.exp(-t * 18))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * (1 - np.exp(-t * 120)) * np.exp(-t * 9)
    return stereo(s) * 0.45


def cupset():
    """A ceramic cup set on a counter: short knock + small inharmonic ring."""
    L = int(0.45 * SR)
    t = np.arange(L) / SR
    knock = lp(rng.standard_normal(L), 900) * np.exp(-t * 60)
    ring_ = (np.sin(2 * np.pi * 2210 * t) + 0.6 * np.sin(2 * np.pi * 3470 * t) + 0.3 * np.sin(2 * np.pi * 5120 * t)) * np.exp(-t * 16)
    return stereo(knock * 0.8 + ring_ * 0.18) * 0.6


def thud():
    """Dull thud: the paper ad hitting the funnel (low, short, no tail)."""
    L = int(0.6 * SR)
    t = np.arange(L) / SR
    f = 52 + 70 * np.exp(-t * 22)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
    slap = lp(rng.standard_normal(L), 700) * np.exp(-t * 40) * 0.5
    return stereo(np.tanh((body + slap) * 1.4)) * 0.9


def buzz():
    """Dull 'wrong' buzz: a short low square-ish tone, softened."""
    L = int(0.32 * SR)
    t = np.arange(L) / SR
    s = np.tanh(3 * np.sin(2 * np.pi * 98 * t)) + 0.5 * np.tanh(3 * np.sin(2 * np.pi * 147 * t))
    s = lp(s, 900) * np.minimum(1, t / 0.01) * np.minimum(1, (0.32 - t) / 0.08)
    return stereo(s) * 0.35


def flutter(length=0.5):
    """Paper flutter: band-limited noise, amplitude-modulated like a sheet in the air."""
    L = int(length * SR)
    t = np.arange(L) / SR
    am = 0.5 + 0.5 * np.abs(np.sin(2 * np.pi * 13 * t + 2 * np.sin(2 * np.pi * 3 * t)))
    shape = np.sin(np.pi * t / length) ** 1.5
    s = bp(rng.standard_normal(L), 1200, 6000) * am * shape
    pan = np.linspace(0.5, -0.5, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.7


def flip():
    """Calendar page flip: a quick paper flick."""
    L = int(0.12 * SR)
    t = np.arange(L) / SR
    s = bp(rng.standard_normal(L), 1500, 7000) * np.exp(-t * 40) * (1 - np.exp(-t * 600))
    return stereo(s) * 0.6


def paper_tick():
    """A sheet landing on a pile: soft papery tick."""
    L = int(0.06 * SR)
    t = np.arange(L) / SR
    s = bp(rng.standard_normal(L), 800, 4500) * np.exp(-t * 90) + np.sin(2 * np.pi * 300 * t) * np.exp(-t * 120) * 0.3
    return stereo(s) * 0.5


def knock():
    """The dart missing the board: a light knock on the wall."""
    L = int(0.25 * SR)
    t = np.arange(L) / SR
    s = np.sin(2 * np.pi * 210 * t) * np.exp(-t * 30) + lp(rng.standard_normal(L), 1600) * np.exp(-t * 70) * 0.4
    return stereo(s) * 0.6


def stamp():
    """Rubber stamp: a dull thump plus a short rubbery slap."""
    L = int(0.45 * SR)
    t = np.arange(L) / SR
    f = 70 + 80 * np.exp(-t * 30)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14)
    slap = bp(rng.standard_normal(L), 300, 2400) * np.exp(-t * 55) * 0.6
    return stereo(np.tanh((body + slap) * 1.5)) * 0.8


def win_chime():
    """Soft positive chime: a rising major third, light and short."""
    L = int(1.4 * SR)
    t = np.arange(L) / SR
    def note(f, t0):
        tt = np.clip(t - t0, 0, None)
        return (t >= t0) * (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt)) * np.exp(-tt * 3.5) * (1 - np.exp(-tt * 200))
    s = note(880.0, 0) + note(1108.73, 0.12)
    return np.stack([s, np.roll(s, int(0.008 * SR))], 1) * 0.3


GEN = {"deep": lambda: impact(True), "click": click, "tap": tap, "tick": tick,
       "whoosh": lambda: whoosh(0.55), "whoosh_short": lambda: whoosh(0.35), "whoosh_long": lambda: whoosh(0.9),
       "pop": notif_pop, "bell": bell, "chime": chime, "pen": lambda: pen(1.6), "pen_long": lambda: pen(2.2),
       "fill": fill, "buzz": buzz, "flutter": lambda: flutter(0.55), "flutter_s": lambda: flutter(0.3),
       "flip": flip, "ptick": paper_tick, "knock": knock, "stamp": stamp, "win": win_chime}

# keep in step with the GSAP times in index.html
SFX = []
# 01 hook: dull buzz on the ✗, the second ad slides in, a light pop for ↗, the ؟ lands
SFX += [(0.1, "whoosh_short", 0.2), (W(3) - 0.05, "buzz", 0.6), (W(4) - 0.15, "whoosh", 0.3), (W(7) - 0.05, "pop", 0.3),
        (W(9) - 0.2, "whoosh_short", 0.2), (W(10) - 0.05, "click", 0.4)]
# 02 guessing: the board draws, the dart whooshes and misses (knock on the wall)
SFX += [(SC["s2"] + 0.05, "pen", 0.35), (W(13) - 0.05, "whoosh_short", 0.5), (W(13) + 0.37, "knock", 0.6), (W(15) - 0.1, "pop", 0.25)]
# 03 term: the word lands, the cards slide in, people drop in, the check
SFX += [(W(18) - 0.08, "whoosh", 0.25), (W(22) - 0.1, "whoosh", 0.25), (W(22) + 0.05, "whoosh", 0.2)]
SFX += [(W(27) - 0.05 + k * 0.08, "tick", 0.18) for k in range(9)] + [(W(31) - 0.05, "pop", 0.4)]
# 04 shop: the shop draws on, the flyer stack lands
SFX += [(SC["s4"] + 0.1, "pen_long", 0.45), (W(38) - 0.05, "ptick", 0.5)]
# 05 the flyers fly out of the stack (paper flutter)
SFX += [(W(42) - 0.2, "flutter", 0.6), (W(47) - 0.1, "flutter", 0.6)]
# 06 split: crowd walks in, the line splits it, mini flyers are handed out
SFX += [(SC["s6"], "whoosh", 0.15), (W(52) + 0.05, "whoosh_short", 0.15), (W(53) - 0.05, "flutter_s", 0.35), (W(56) - 0.05, "flutter_s", 0.35)]
# 07 count: shop-door bell on the first walk-in, paper stacking ticks as the piles grow
SFX += [(SC["s7"] + 0.4, "bell", 0.55)]
SFX += [(SC["s7"] + 0.35 + k * 0.17, "ptick", 0.4) for k in range(8)] + [(SC["s7"] + 0.6 + k * 0.4, "ptick", 0.3) for k in range(3)]
# 08 numbers talk: soft air under the words
SFX += [(W(70) - 0.1, "whoosh_long", 0.15)]
# 09 one thing: rubber-stamp thump for "1", the three parts, the blur-swap, check, ؟ ؟ ؟, reset, one swap
SFX += [(W(79) - 0.02, "stamp", 0.8), (W(81) - 0.25, "whoosh_short", 0.2)]
SFX += [(t - 0.1, "tick", 0.25) for t in (W(83), W(84), W(85))]
SFX += [(W(86) - 0.05, "whoosh_short", 0.45), (W(87) - 0.05, "pop", 0.35)]
SFX += [(W(88) - 0.1 + k * 0.12, "pop", 0.25) for k in range(3)]
SFX += [(W(92) - 0.1, "whoosh_short", 0.2), (W(92) + 0.2, "whoosh_short", 0.3), (W(92) + 0.25, "pop", 0.35)]
# 10 time: the stop hand, calendar page flips, the crowd grows
SFX += [(W(95) - 0.05, "pop", 0.35)] + [(W(99) + k * 0.3, "flip", 0.55) for k in range(4)]
SFX += [(t, "tick", 0.15) for t in (W(103) - 0.1, W(105) - 0.1, W(107) - 0.1)]
# 11 in ads: the flyers come in, morph to ads, chips
SFX += [(SC["s11"] + 0.05, "flutter", 0.45), (W(109) - 0.1, "whoosh", 0.3), (W(111) - 0.05, "pop", 0.25),
        (W(113) - 0.05, "pop", 0.25), (W(115) - 0.1, "whoosh_short", 0.15), (W(116) - 0.05, "pop", 0.25)]
# 12 the winner: heart pop, the bars rise, soft positive chime when B wins
SFX += [(W(121) - 0.1, "pop", 0.35), (W(125) - 0.1, "fill", 0.6), (WIN, "win", 0.6)]
# 13 CTA
SFX += [(SC["s13"] + 0.15, "pop", 0.45)] + [(t - 0.05, "tick", 0.25) for t in (W(137), W(138), W(140))]
# 14 end card: the Reignite chime
SFX += [(END - 0.5, "whoosh_long", 0.3), (END + 0.1, "chime", 0.55), (END + 0.1, "deep", 0.3)]

sfx = np.zeros((N, 2))
for t, kind, gain in SFX:
    place(sfx, GEN[kind](), t, gain)
# very low street ambience under the juice-shop scenes (04-07)
place(sfx, street(SC["s8"] - SC["s4"]), SC["s4"], 0.05)


# stem peaks are set so the VO stays the loudest element
def finish(x, peak_db):
    x = x - x.mean(0)
    pk = np.max(np.abs(x)) + 1e-9
    return x / pk * (10 ** (peak_db / 20))


sf.write(str(ROOT / "audio" / "music.wav"), finish(music, -11.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(ROOT / "audio" / "sfx.wav"), finish(sfx, -12.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote audio/music.wav, audio/sfx.wav", DUR, "s,", len(SFX), "sfx events")
