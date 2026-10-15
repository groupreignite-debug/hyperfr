"""Sound for the 1.4s signature intro (scene 00): "Retargeting" ignites, holds, burns away.

Clean and minimal, matching the visual: a soft airy ignite swell with a warm low body, a few
ember crackles, a quiet glow during the hold, and a short burn-off hiss that is fully faded
before 1.4s, where the film (and its own music/SFX/VO tracks) starts unchanged.

Output (48 kHz stereo, 16-bit): audio/intro.wav  — placed at 0s by <audio id="a-intro">.
The film's audio/music.wav, audio/sfx.wav and VO are not touched by this script.
"""
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
INTRO = 1.4
IGN = (0.0, 0.4)
BURN = (INTRO - 0.44, INTRO - 0.04)
ROOT = Path(__file__).resolve().parent.parent
N = int(SR * INTRO)
T = np.arange(N) / SR
rng = np.random.default_rng(2026)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)


def lp(x, hz):
    return sosfilt(butter(2, hz, "low", fs=SR, output="sos"), x)


def env(points):
    ts, vs = zip(*points)
    return np.interp(T, ts, vs)


# ignite: airy noise swell + a warm low "whump" body
air = bp(rng.standard_normal(N), 500, 4200) * env([(0, 0.0), (0.08, 0.55), (0.3, 0.35), (0.5, 0.0), (INTRO, 0)])
f = 55 + 40 * np.exp(-T * 6)
body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env([(0, 0), (0.04, 0.9), (0.4, 0.35), (0.85, 0.12), (BURN[0], 0.1), (BURN[1], 0), (INTRO, 0)])

# hold: a quiet ember glow (low filtered noise)
glow = lp(rng.standard_normal(N), 260) * env([(0, 0), (0.35, 0.25), (BURN[0], 0.3), (BURN[1] - 0.1, 0), (INTRO, 0)]) * 3

# burn-off: a soft hiss sweep that rises in pitch with the front, gone before 2.0s
hiss = np.zeros(N)
blk = 1200
noise = rng.standard_normal(N)
for s in range(0, N, blk):
    t = s / SR
    c = 1500 + 3500 * np.clip((t - BURN[0]) / (BURN[1] - BURN[0]), 0, 1)
    hiss[s:s + blk] = bp(noise[s:s + blk], c * 0.6, min(c * 1.5, 20000))
hiss *= env([(0, 0), (BURN[0] - 0.04, 0), (BURN[0] + 0.1, 0.45), (BURN[1] - 0.1, 0.35), (BURN[1], 0), (INTRO, 0)])

# ember crackles: tiny clicks, denser on the two fronts
crack = np.zeros(N)
L = int(0.012 * SR)
ct = np.arange(L) / SR
times = list(np.linspace(0.03, 0.38, 6)) + [0.6, 0.8] + list(np.linspace(BURN[0] + 0.02, BURN[1] - 0.06, 10))
for t0 in times:
    i = int((t0 + (rng.random() - 0.5) * 0.04) * SR)
    c = bp(rng.standard_normal(L), 2500, 9000) * np.exp(-ct * 450) * (0.4 + 0.6 * rng.random())
    crack[i:i + L] += c[: max(0, min(L, N - i))]

mono = air * 0.5 + body * 0.35 + glow * 0.4 + hiss * 0.5 + crack * 0.9
pan = 0.5 + 0.3 * np.sin(2 * np.pi * 0.7 * T)
st = np.stack([mono * (1.2 - pan), mono * (0.2 + pan)], 1)
st *= env([(0, 1), (INTRO - 0.03, 1), (INTRO, 0)])[:, None]  # hard-safe edge: silent at the film's first frame
st = st / (np.max(np.abs(st)) + 1e-9) * (10 ** (-12 / 20))
sf.write(str(ROOT / "audio" / "intro.wav"), st.astype(np.float32), SR, subtype="PCM_16")
print("wrote audio/intro.wav", INTRO, "s")
