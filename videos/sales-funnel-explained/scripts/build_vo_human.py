"""Lay the client-recorded voiceover on the film and write the cue sheet (replaces build_vo.py's TTS take).

Input : audio/vo-human/src/vo_human_raw.m4a   (client recording AUD-20261013-WA0100, WhatsApp AAC 65 kb/s mono, 55.0s)
        scripts/vo_human_words.json            (ElevenLabs Scribe word timings of that file, raw seconds)
Output: audio/vo-human/vo_clean.wav            (whole take, cleaned and levelled; no cuts)
        audio/vo-human/vo_track.wav            (the take with 3 dead-air pauses tightened, film length, 48 kHz mono)
        scripts/cues.json                      (every word and every script line in film seconds, end card, duration)
Then run scripts/apply_cues.py (writes the timings into index.html) and scripts/build_audio.py.

The recording is NOT time-stretched and no words are cut. Only three silences are shortened (cuts land inside
silence, with short crossfades), so film = raw - (silence removed before that point).

Word indices: every animation and subtitle time in index.html is W(i) in the TTS take's Scribe indexing (132 words).
The recording has the same words in the same order except the TTS take's stray "أم" (TTS word 92, line 11), so a
zero-length placeholder is kept at index 92 and all W(i) keep their meaning.
"""
import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
VOH = ROOT / "audio" / "vo-human"
SR = 48000
TARGET_LUFS = -23.2   # same level as the TTS vo_track the music/SFX mix was balanced against
TAIL = 0.6            # after the last word, before the end card
END_CARD = 3.0
# silences to tighten, in raw seconds: (cut from, cut to). Each lies inside a detected silence.
CUTS = [
    (0.05, 0.71),     # lead-in: 1.06s of room tone before the first word -> 0.40s
    (36.10, 36.85),   # line 10 -> 11: 1.50s breath -> 0.75s
    (46.30, 46.80),   # line 12, mid-sentence hesitation "الناس … بيكمّلوا": 0.90s -> 0.40s
]
XF = 0.015            # crossfade at each cut
# first/last word index of each script line (TTS indexing, see above)
LINES = {"01": (0, 8), "02": (9, 16), "03": (17, 20), "04": (21, 33), "05": (34, 38), "06": (39, 47),
         "07": (48, 59), "08": (60, 67), "09": (68, 77), "10": (78, 89), "11": (90, 110), "12": (111, 117),
         "13": (118, 122), "14": (123, 131)}

raw = VOH / "src" / "vo_human_raw.m4a"
clean = VOH / "vo_clean.wav"
# 1) clean the whole take once (filters see continuous audio, so no edge artefacts at the cuts)
CHAIN = ",".join([
    "highpass=f=75:poles=2",                        # rumble / handling
    "equalizer=f=420:t=q:w=1.1:g=-2.0",             # phone-mic boxiness (+1.5 dB vs the TTS take at 150-1200 Hz)
    "equalizer=f=1900:t=q:w=1.2:g=2.0",             # fill the 1.2-2.5 kHz dip (intelligibility)
    "equalizer=f=4200:t=q:w=1.0:g=1.5",             # presence
    "highshelf=f=6500:g=4.0",                       # WhatsApp codec rolls the top off (-10..-17 dB above 5 kHz)
    "deesser=i=0.3:m=0.5:f=0.5",
    "acompressor=threshold=-26dB:ratio=2.5:attack=8:release=140:makeup=3:knee=5",
])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", CHAIN, "-ar", str(SR), "-ac", "1",
                "-c:a", "pcm_f32le", str(clean)], check=True)


def lufs(path):
    out = subprocess.run(["ffmpeg", "-nostats", "-i", str(path), "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return float(out.split("Integrated loudness:")[1].split("I:")[1].split("LUFS")[0])


x, sr = sf.read(str(clean))
assert sr == SR
x = x * 10 ** ((TARGET_LUFS - lufs(clean)) / 20)
x = np.clip(x, -0.89, 0.89)   # safety only; the take peaks well below this after levelling
sf.write(str(clean), x.astype(np.float32), SR, subtype="PCM_24")

# 2) words, with the placeholder for the TTS take's stray word
hw = [w for w in json.loads((ROOT / "scripts" / "vo_human_words.json").read_text())["words"] if w.get("type", "word") == "word"]
assert len(hw) == 131, len(hw)
for a, b in CUTS:   # no cut may touch a word
    assert all(w["end"] <= a or w["start"] >= b for w in hw), (a, b)
ph = {"text": "", "start": hw[91]["end"], "end": hw[91]["end"]}
words = hw[:92] + [ph] + hw[92:]


def film(t):
    return round(t - sum(min(max(t - a, 0), b - a) for a, b in CUTS), 3)


# 3) assemble: keep everything outside the cuts, crossfade at each join
keep, prev = [], 0.0
for a, b in CUTS:
    keep.append((prev, a))
    prev = b
keep.append((prev, len(x) / SR))
f = int(XF * SR)
out = np.zeros(0)
for s, e in keep:
    seg = x[int(s * SR):int(e * SR)].copy()
    if len(out) and f:
        ramp = np.linspace(0, 1, f)
        out[-f:] = out[-f:] * (1 - ramp) + seg[:f] * ramp
        seg = seg[f:]
    out = np.concatenate([out, seg])
# film(): each join overlaps by XF; that shifts later audio <= 45 ms, well under a frame-and-a-half, so the
# subtitle/animation map stays the simple silence-removed one. Correct it exactly anyway:
shift = lambda t: round(film(t) - XF * sum(1 for a, _ in CUTS if t >= a), 3)

W = [[shift(w["start"]), shift(w["end"])] for w in words]
end_card = round(W[-1][1] + TAIL, 3)
film_dur = round(end_card + END_CARD, 3)
n = int(round(film_dur * SR))
out = np.concatenate([out, np.zeros(max(0, n - len(out)))])[:n]
sf.write(str(VOH / "vo_track.wav"), out.astype(np.float32), SR, subtype="PCM_24")

cues = {
    "source": "client recording AUD-20261013-WA0100 (audio/vo-human)",
    "tempo": 1.0,
    "words": W,
    "text": [w["text"] for w in words],
    "lines": {k: {"s": W[a][0], "e": W[b][1], "w": [a, b]} for k, (a, b) in LINES.items()},
    "endcard": end_card,
    "duration": film_dur,
}
(ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, ensure_ascii=False, indent=0))
print("vo_track LUFS", round(lufs(VOH / "vo_track.wav"), 1), "| peak", round(float(np.abs(out).max()), 3))
for k, v in cues["lines"].items():
    print(k, v["s"], v["e"])
print("endcard", end_card, "duration", film_dur)
