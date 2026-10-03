"""Procedural score + SFX for the Reignite branding reel.

Dark, minimal editorial electronic bed: a low drone that grows as the
figures escalate, drops out almost completely at WHY?, then rebuilds
under the strategic explanation. SFX are restrained: low impacts, soft
UI ticks, filtered whooshes, one riser, a deep hit on $100M.

Outputs (48 kHz stereo WAV):
  audio/music.wav  - bed, pre-ducked under the voiceover
  audio/sfx.wav    - impacts / clicks / whooshes

Timings mirror the cue sheet in index.html (TIMING block). Keep in sync.
"""
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
DUR = 65.0
N = int(SR * DUR)
ROOT = Path(__file__).resolve().parent.parent
rng = np.random.default_rng(7)

cues = json.loads((ROOT / "scripts" / "cues.json").read_text())
VO = cues["vo"]          # {id: start}
SFX = cues["sfx"]        # list of [time, kind, gain]
T = np.arange(N) / SR


def lp(x, hz, order=2):
    return sosfilt(butter(order, hz, "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sosfilt(butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def env_points(points):
    """Piecewise-linear envelope from [(t, value), ...]."""
    ts, vs = zip(*points)
    return np.interp(T, ts, vs)


def place(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


# ---------------------------------------------------------------- music ---
def saw(freq, t):
    # band-limited-ish saw via a few harmonics, keeps it soft and dark
    out = np.zeros_like(t)
    for k in range(1, 9):
        out += ((-1) ** (k + 1)) * np.sin(2 * np.pi * freq * k * t) / k
    return out


def drone():
    # D minor colour: D1 / A1 / D2 / F2 / C3 (m7 adds unresolved tension)
    notes = [36.71, 55.0, 73.42, 87.31, 130.81]
    left = np.zeros(N)
    right = np.zeros(N)
    for i, f in enumerate(notes):
        detune = 0.12 + 0.05 * i
        l = saw(f - detune, T) * (0.9 if i < 2 else 0.45)
        r = saw(f + detune, T) * (0.9 if i < 2 else 0.45)
        left += l
        right += r
    # slow filter movement that opens as tension builds
    cutoff_env = env_points([(0, 180), (27, 900), (29.2, 220), (31, 220), (49, 700), (61, 1100), (65, 400)])
    # time-varying LP: process in blocks
    out = []
    for ch in (left, right):
        y = np.zeros(N)
        blk = 2400
        zi_sos = None
        for s in range(0, N, blk):
            c = float(cutoff_env[min(s + blk // 2, N - 1)])
            sos = butter(2, c, "low", fs=SR, output="sos")
            if zi_sos is None:
                zi_sos = np.zeros((sos.shape[0], 2))
            y[s : s + blk], zi_sos = sosfilt(sos, ch[s : s + blk], zi=zi_sos)
        out.append(y)
    return np.stack(out, 1) * 0.11


def sub_pulse(bpm=92):
    """Soft sub kick on quarter notes, only where the arrangement asks."""
    beat = 60 / bpm
    buf = np.zeros(N)
    kick_len = int(0.45 * SR)
    kt = np.arange(kick_len) / SR
    freq = 46 + 60 * np.exp(-kt * 30)
    phase = 2 * np.pi * np.cumsum(freq) / SR
    kick = np.sin(phase) * np.exp(-kt * 7)
    t = 0.0
    while t < DUR:
        place(buf, kick, t)
        t += beat
    gate = env_points([(0, 0), (3.6, 0), (3.8, 0.55), (19.9, 0.7), (20.0, 0.9), (28.9, 1.0), (29.1, 0),
                       (34.4, 0), (34.6, 0.55), (49.5, 0.7), (49.6, 0.9), (55.6, 1.0), (55.8, 0.35),
                       (62.0, 0.35), (62.1, 0), (65, 0)])
    return np.stack([buf * gate] * 2, 1) * 0.5


def ticks(bpm=92):
    """Muted filtered hats on 8ths - quiet clockwork under the numbers."""
    step = 60 / bpm / 2
    buf = np.zeros(N)
    hl = int(0.05 * SR)
    hat = hp(rng.standard_normal(hl), 6000) * np.exp(-np.arange(hl) / SR * 90)
    t, k = 0.0, 0
    while t < DUR:
        place(buf, hat, t, 0.6 if k % 2 else 0.25)
        t += step
        k += 1
    gate = env_points([(0, 0), (9.6, 0), (9.8, 0.6), (28.9, 1.0), (29.1, 0), (41.0, 0), (41.2, 0.5),
                       (55.6, 0.8), (55.8, 0), (65, 0)])
    l = buf * gate
    r = np.roll(buf, int(0.011 * SR)) * gate
    return np.stack([l, r], 1) * 0.05


def pad_air():
    """High airy noise shimmer for the strategic sections."""
    n = rng.standard_normal((N, 2))
    n = np.stack([bp(n[:, 0], 1800, 5200), bp(n[:, 1], 1800, 5200)], 1)
    g = env_points([(0, 0.15), (27, 0.5), (29.1, 0), (30.5, 0), (34.5, 0.25), (55.6, 0.6), (62, 0.2), (65, 0)])
    return n * g[:, None] * 0.012


music = drone() + sub_pulse() + ticks() + pad_air()

# Master shape: build with the numbers, near-silence at WHY?, rebuild.
master = env_points([
    (0.0, 0.0), (0.4, 0.55), (3.8, 0.7), (9.8, 0.8), (19.9, 0.9), (27.3, 1.0), (29.05, 1.0),
    (29.15, 0.04), (31.0, 0.05), (34.5, 0.6), (41.2, 0.75), (49.6, 0.85), (55.6, 0.9),
    (55.9, 0.45), (61.9, 0.6), (62.1, 0.7), (64.2, 0.55), (65.0, 0.0),
])
music *= master[:, None]

# Pre-baked voiceover carve: ~-6 dB under every line, smooth edges.
vo_lens = {k: sf.info(str(ROOT / "audio" / "vo" / f"vo_{k}.wav")).duration for k in VO}
duck = np.ones(N)
for k, start in VO.items():
    a, b = start - 0.15, start + vo_lens[k] + 0.2
    duck = np.minimum(duck, env_points([(0, 1), (max(a - 0.12, 0), 1), (a, 0.5), (b, 0.5), (b + 0.3, 1), (DUR, 1)]))
music *= duck[:, None]

# ------------------------------------------------------------------ sfx ---
def impact(deep=False):
    L = int((2.6 if deep else 1.4) * SR)
    t = np.arange(L) / SR
    f = (30 if deep else 42) + (70 if deep else 55) * np.exp(-t * (9 if deep else 14))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (1.6 if deep else 3.2))
    thump = lp(rng.standard_normal(L), 380) * np.exp(-t * 22) * 0.6
    tail = lp(rng.standard_normal(L), 1400) * np.exp(-t * 4.5) * 0.05
    s = np.tanh((body + thump + tail) * 1.4)
    return np.stack([s, s], 1)


def click():
    L = int(0.03 * SR)
    t = np.arange(L) / SR
    s = bp(rng.standard_normal(L), 2500, 7000) * np.exp(-t * 260) + np.sin(2 * np.pi * 1900 * t) * np.exp(-t * 400) * 0.4
    return np.stack([s, s], 1) * 0.5


def whoosh(length=0.6):
    L = int(length * SR)
    t = np.arange(L) / SR
    shape = np.sin(np.pi * t / length) ** 2
    n = rng.standard_normal(L)
    s = bp(n, 300, 2600) * shape
    pan = np.linspace(-0.6, 0.6, L)
    return np.stack([s * (1 - pan) / 2, s * (1 + pan) / 2], 1) * 0.6


def riser(length):
    L = int(length * SR)
    t = np.arange(L) / SR
    out = np.zeros(L)
    blk = 1200
    n = rng.standard_normal(L)
    for s in range(0, L, blk):
        c = 300 + 3500 * (s / L) ** 2
        out[s : s + blk] = bp(n[s : s + blk], c * 0.6, c * 1.4)
    tone = np.sin(2 * np.pi * np.cumsum(55 + 55 * (t / length) ** 2) / SR) * 0.4
    g = (t / length) ** 2.2
    s = (out * 0.5 + tone) * g
    return np.stack([s, s], 1) * 0.35


def tick_ui():
    L = int(0.018 * SR)
    t = np.arange(L) / SR
    s = np.sin(2 * np.pi * 3200 * t) * np.exp(-t * 500)
    return np.stack([s, s], 1) * 0.25


GEN = {
    "impact": lambda: impact(False),
    "deep": lambda: impact(True),
    "click": click,
    "tick": tick_ui,
    "whoosh": lambda: whoosh(0.55),
    "whoosh_long": lambda: whoosh(0.9),
}

sfx = np.zeros((N, 2))
for t, kind, gain in SFX:
    if kind.startswith("riser:"):
        length = float(kind.split(":")[1])
        place(sfx, riser(length), t - length, gain)
    else:
        place(sfx, GEN[kind](), t, gain)


def finish(x, peak_db):
    x = x - x.mean(0)
    pk = np.max(np.abs(x)) + 1e-9
    return x / pk * (10 ** (peak_db / 20))


out_dir = ROOT / "audio"
sf.write(str(out_dir / "music.wav"), finish(music, -4.0).astype(np.float32), SR, subtype="PCM_16")
sf.write(str(out_dir / "sfx.wav"), finish(sfx, -3.0).astype(np.float32), SR, subtype="PCM_16")
print("wrote music.wav, sfx.wav", DUR, "s")
