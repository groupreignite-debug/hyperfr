"""Procedural score + SFX for "ليش أشهر الشعارات بسيطة؟" (Reignite Group).

Minimal, modern, premium bed in A minor at 100 BPM:
  - warm detuned pad on a 4-bar loop (Am9 - Fmaj7 - C(add9) - G6)
  - soft pluck arpeggio that enters with the setup and thickens with the principles
  - sub pulse + muted hats under the principle sections
  - drops to pad-only for the final statement, one bass hit on "الصح", resolves on the end card
The bed is ducked under every voiceover line (VO starts/durations mirror index.html).

SFX are restrained: filtered whooshes on scene cuts, soft clicks on text lands,
UI ticks on scale steps, one riser into the Reignite logo, one bass hit.

Outputs (48 kHz stereo WAV): audio/music.wav, audio/sfx.wav
"""
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
DUR = 106.5
N = int(SR * DUR)
T = np.arange(N) / SR
ROOT = Path(__file__).resolve().parent.parent
rng = np.random.default_rng(11)

BPM = 100
BEAT = 60 / BPM
BAR = 4 * BEAT

# ---- timeline (keep in sync with index.html) -------------------------------
VO = [(0.2, 8.78), (9.4, 6.11), (15.95, 9.09), (25.5, 6.58), (32.5, 9.51), (42.45, 10.21),
      (53.1, 12.36), (65.95, 10.76), (77.4, 11.78), (89.7, 6.03), (96.4, 5.25)]
CUTS = [9.2, 15.75, 25.3, 32.3, 42.25, 52.9, 65.75, 77.1, 89.45, 96.1, 102.2]


def lp(x, hz, order=2):
    return sosfilt(butter(order, hz, "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sosfilt(butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def env_points(points):
    ts, vs = zip(*points)
    return np.interp(T, ts, vs)


def place(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf) or i < 0:
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)


# ---------------------------------------------------------------- music ---
CHORDS = [  # pad voicings (midi)
    [45, 52, 59, 60, 64, 71],   # Am9
    [41, 48, 57, 60, 64, 69],   # Fmaj7
    [48, 55, 62, 64, 67, 74],   # C(add9)
    [43, 50, 59, 62, 64, 71],   # G6
]
ARPS = [
    [69, 72, 76, 79, 76, 72, 71, 72],
    [69, 72, 77, 76, 72, 69, 67, 69],
    [67, 72, 74, 76, 79, 76, 74, 72],
    [67, 71, 74, 76, 74, 71, 69, 71],
]


def pad():
    out = np.zeros((N, 2))
    n_bars = int(DUR / BAR) + 2
    seg = int(BAR * SR)
    tt = np.arange(seg + int(0.8 * SR)) / SR
    a = np.minimum(1, tt / 0.6) * np.exp(-np.maximum(0, tt - BAR) / 0.35)
    for b in range(n_bars):
        notes = CHORDS[b % 4]
        sig_l = np.zeros_like(tt)
        sig_r = np.zeros_like(tt)
        for k, m in enumerate(notes):
            f = midi(m)
            g = 0.9 if k == 0 else 0.42
            for d, side in ((-0.18, 0), (0.18, 1)):
                s = np.sin(2 * np.pi * (f + d) * tt) + 0.22 * np.sin(2 * np.pi * 2 * (f + d) * tt)
                if side == 0:
                    sig_l += s * g
                else:
                    sig_r += s * g
        st = int(b * BAR * SR)
        for ch, s in ((0, sig_l), (1, sig_r)):
            e = min(N, st + len(s))
            if st < N:
                out[st:e, ch] += (s * a)[: e - st]
    out[:, 0] = lp(out[:, 0], 2400)
    out[:, 1] = lp(out[:, 1], 2400)
    return out * 0.028


def pluck_arp():
    buf = np.zeros(N)
    step = BEAT / 2
    ln = int(0.5 * SR)
    tt = np.arange(ln) / SR
    t, k = 0.0, 0
    while t < DUR:
        bar = int(t / BAR)
        m = ARPS[bar % 4][k % 8]
        f = midi(m)
        tone = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt)) * np.exp(-tt * 9)
        place(buf, tone, t, 1.0 if k % 2 == 0 else 0.7)
        t += step
        k += 1
    # stereo ping-pong echo
    d = int(BEAT * 0.75 * SR)
    l = buf + 0.35 * np.roll(buf, d)
    r = 0.6 * buf + 0.45 * np.roll(buf, d // 2 * 3)
    gate = env_points([(0, 0), (9.2, 0), (9.6, 0.35), (15.75, 0.5), (32.3, 0.7), (52.9, 0.8),
                       (65.6, 0.85), (65.9, 0.35), (75.6, 0.4), (77.1, 0.75), (88.8, 0.9),
                       (89.4, 0.25), (95.9, 0.3), (96.15, 0.0), (106.5, 0)])
    return np.stack([l * gate, r * gate], 1) * 0.05


def sub_pulse():
    buf = np.zeros(N)
    kl = int(0.4 * SR)
    kt = np.arange(kl) / SR
    freq = 44 + 70 * np.exp(-kt * 32)
    kick = np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-kt * 8)
    t = 0.0
    while t < DUR:
        place(buf, kick, t)
        t += BEAT
    gate = env_points([(0, 0), (15.7, 0), (15.8, 0.45), (32.3, 0.65), (52.9, 0.8), (65.6, 0.85),
                       (65.8, 0), (75.6, 0), (75.7, 0.5), (77.1, 0.7), (89.3, 0.8), (89.45, 0),
                       (106.5, 0)])
    return np.stack([buf * gate] * 2, 1) * 0.32


def hats():
    step = BEAT / 2
    buf = np.zeros(N)
    hl = int(0.045 * SR)
    hat = hp(rng.standard_normal(hl), 7000) * np.exp(-np.arange(hl) / SR * 95)
    t, k = 0.0, 0
    while t < DUR:
        place(buf, hat, t, 0.7 if k % 2 else 0.25)
        t += step
        k += 1
    gate = env_points([(0, 0), (32.2, 0), (32.4, 0.6), (52.9, 0.9), (65.6, 1.0), (65.8, 0),
                       (77.0, 0), (77.2, 0.7), (89.3, 0.9), (89.45, 0), (106.5, 0)])
    return np.stack([buf * gate, np.roll(buf, int(0.009 * SR)) * gate], 1) * 0.045


def bass():
    """Soft sustained root notes following the pad, from the Nike section on."""
    out = np.zeros(N)
    roots = [33, 29, 36, 31]
    seg = int(BAR * SR)
    tt = np.arange(seg) / SR
    a = np.minimum(1, tt / 0.04) * np.exp(-tt * 0.9)
    for b in range(int(DUR / BAR) + 1):
        f = midi(roots[b % 4])
        s = np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(2 * np.pi * 2 * f * tt)
        place(out, s * a, b * BAR)
    gate = env_points([(0, 0), (15.7, 0), (16.0, 0.6), (52.9, 0.85), (65.6, 0.9), (65.8, 0.4),
                       (77.1, 0.8), (89.3, 0.9), (89.45, 0.5), (95.9, 0.5), (96.1, 0), (106.5, 0)])
    return np.stack([out * gate] * 2, 1) * 0.06


music = pad() + pluck_arp() + sub_pulse() + hats() + bass()

master = env_points([(0, 0.0), (0.3, 0.7), (9.2, 0.8), (32.3, 0.9), (65.6, 1.0), (65.9, 0.75),
                     (77.1, 0.95), (89.3, 1.0), (89.6, 0.8), (96.0, 0.75), (96.3, 0.55),
                     (101.0, 0.7), (102.2, 0.85), (105.2, 0.6), (106.5, 0.0)])
music *= master[:, None]

# duck under the voice (-7 dB), smoothed
duck = np.ones(N)
for s, d in VO:
    i, j = int((s - 0.08) * SR), int((s + d + 0.15) * SR)
    duck[max(0, i):min(N, j)] = 0.45
duck = lp(np.concatenate([np.ones(SR), duck]), 3, order=1)[SR:]
music *= duck[:, None]

# ------------------------------------------------------------------ sfx ---
sfx = np.zeros((N, 2))


def whoosh(length=0.55, lo=300, hi=5000, gain=0.12):
    n = int(length * SR)
    x = rng.standard_normal(n)
    tt = np.arange(n) / SR
    e = np.sin(np.pi * np.minimum(1, tt / length)) ** 2
    y = bp(x, lo, hi) * e
    return np.stack([y, np.roll(y, 120)], 1) * gain


def click(f=2400, gain=0.08):
    n = int(0.03 * SR)
    tt = np.arange(n) / SR
    y = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 260) + 0.4 * hp(rng.standard_normal(n), 4000) * np.exp(-tt * 400)
    return np.stack([y, y], 1) * gain


def tick(f=1500, gain=0.09):
    n = int(0.06 * SR)
    tt = np.arange(n) / SR
    y = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 70)
    return np.stack([y, y], 1) * gain


def blip(gain=0.09):
    n = int(0.22 * SR)
    tt = np.arange(n) / SR
    y = (np.sin(2 * np.pi * 1320 * tt) * (tt < 0.08) + np.sin(2 * np.pi * 1760 * tt) * (tt >= 0.08)) * np.exp(-tt * 18)
    return np.stack([y, y], 1) * gain


def impact(gain=0.35, f0=58):
    n = int(1.2 * SR)
    tt = np.arange(n) / SR
    freq = f0 + 90 * np.exp(-tt * 25)
    y = np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-tt * 3.2)
    y += 0.25 * lp(rng.standard_normal(n), 900) * np.exp(-tt * 14)
    return np.stack([y, y], 1) * gain


def riser(length=1.4, gain=0.1):
    n = int(length * SR)
    tt = np.arange(n) / SR
    x = rng.standard_normal(n)
    y = np.zeros(n)
    blk = 2400
    for s in range(0, n, blk):
        c = 400 + 5200 * (s / n) ** 2
        y[s:s + blk] = bp(x[s:s + blk], c * 0.6, min(c * 1.6, 20000))
    y *= (tt / length) ** 2
    return np.stack([y, np.roll(y, 200)], 1) * gain


def chime(gain=0.06):
    n = int(2.5 * SR)
    tt = np.arange(n) / SR
    y = sum(np.sin(2 * np.pi * midi(m) * tt) * g for m, g in ((81, 1), (88, 0.5), (93, 0.3))) * np.exp(-tt * 1.6)
    return np.stack([y, np.roll(y, 300)], 1) * gain


def put(sig, t, gain=1.0):
    i = int(t * SR)
    if i >= N:
        return
    j = min(N, i + len(sig))
    sfx[i:j] += sig[: j - i] * gain


for c in CUTS:
    put(whoosh(), c - 0.28)

clicks = [
    0.2, 0.49, 0.83, 1.33, 2.57, 3.01, 3.83, 8.05,            # hook
    9.4, 11.34, 12.15, 14.2,                                  # setup
    16.97, 18.02, 19.66, 21.56,                               # nike
    25.5, 26.84, 30.71,                                       # apple
    34.2, 40.38,                                              # recognition
    45.77, 46.58,                                             # scale
    53.1, 54.82, 55.97, 57.29, 59.3, 60.65, 61.73,            # mcdonald's
    66.33, 68.43, 69.82,                                      # lesson
    80.82, 82.72, 83.02, 85.3, 85.98, 87.81,                  # process
    89.7, 94.7,                                               # reignite
    96.4, 97.74,                                              # statement
]
for t in clicks:
    put(click(), t)

# strikes / removals
for t in (5.05, 5.17, 5.29, 13.02, 28.3, 79.7, 81.3):
    put(whoosh(0.3, 1500, 7000, 0.05), t)
# subtractive "pops" as the emblem empties (setup)
for i in range(12):
    put(tick(900 + 40 * i, 0.04), 13.45 + i * 0.1)
# scale ladder + environment steps
for t in (42.4, 43.0, 43.55, 44.1):
    put(tick(1500), t)
for t in (47.33, 48.56, 49.7, 51.02):
    put(tick(1100, 0.08), t)
    put(whoosh(0.35, 800, 6000, 0.05), t - 0.12)
# glance flashes + shrink + check (recognition)
for t in (36.12, 36.42):
    put(tick(2100, 0.06), t)
put(whoosh(0.9, 200, 3000, 0.07), 37.45)
put(blip(), 39.35)
# mark draws (nike swoosh, arches, logo)
put(whoosh(1.0, 400, 4000, 0.06), 16.3)
put(whoosh(1.1, 150, 1800, 0.06), 53.0)
# the two "big lesson" landings
put(impact(0.22, 64), 8.05)
put(impact(0.26, 60), 75.69)
# into the Reignite logo
put(riser(1.4, 0.09), 88.15)
put(impact(0.16, 70), 89.62)
# final statement: soft land, then the bass hit on "الصح"
put(impact(0.18, 66), 98.82)
put(impact(0.42, 46), 100.85)
# end card
put(chime(), 102.4)

sfx = np.tanh(sfx * 1.1) / 1.1


def norm(x, peak):
    m = np.max(np.abs(x))
    return x if m == 0 else x * (peak / m)


out = ROOT / "audio"
sf.write(out / "music.wav", norm(music, 0.5).astype(np.float32), SR, subtype="PCM_16")
sf.write(out / "sfx.wav", norm(sfx, 0.6).astype(np.float32), SR, subtype="PCM_16")
print("wrote", out / "music.wav", out / "sfx.wav")
