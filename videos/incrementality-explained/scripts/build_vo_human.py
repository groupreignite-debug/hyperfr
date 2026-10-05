"""Lay the client-recorded voiceover onto the film and derive the retime map.

Input : audio/vo-human/src/vo_human_raw.m4a   (client recording, WhatsApp AAC 64 kb/s mono)
        scripts/vo_human_words.json            (ElevenLabs Scribe word timings of that file)
        scripts/cues.json                      (the original TTS cue sheet the animation was authored to)
Output: audio/vo-human/vo_clean.wav            (whole take, cleaned: HPF, mud cut, presence, de-ess, comp)
        audio/vo-human/vo_track.wav            (the 16 lines cut at word boundaries, re-spaced; outtake dropped)
        scripts/cues_human.json                (new line starts/ends)
        scripts/timemap.json                   (old→new time anchors; drives index.html + build_audio.py)
"""
import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
VOH = ROOT / "audio" / "vo-human"
SR = 48000
OLD_TEMPO = 1.07
OLD_END = 75.4

words = json.loads((ROOT / "scripts" / "vo_human_words.json").read_text())
old = json.loads((ROOT / "scripts" / "cues.json").read_text())["lines"]

# word-index ranges of the 16 script lines in the recording (142+ is an outtake: "نسيتها، هاه؟ ...")
LINES = [(0, 10), (11, 17), (18, 23), (24, 35), (36, 43), (44, 48), (49, 55), (56, 62), (63, 72),
         (73, 86), (87, 100), (101, 109), (110, 121), (122, 129), (130, 137), (138, 141)]
# silence after line i (seconds) — sized to the visual beats (3X hit, freeze, scene turns)
GAPS = [1.2, 0.55, 0.45, 0.5, 0.55, 0.55, 0.35, 0.45, 0.6, 0.35, 0.6, 0.45, 0.6, 0.5, 0.75]
START = 0.45
# (TTS-take word time [s, raw], human word index) pairs that the animation keys on
PAIRS = {
    0: [(3.19, 6), (3.62, 7)],
    2: [(0.77, 20), (1.56, 22)],
    3: [(0.45, 25), (3.80, 31)],
    7: [(0.197, 56), (1.80, 58)],
    8: [(0.372, 64), (2.043, 66)],
    9: [(3.599, 81), (4.063, 82), (5.375, 84)],
    10: [(1.196, 90), (2.206, 92), (2.728, 93), (4.505, 94), (5.074, 95), (6.432, 97)],
    11: [(1.823, 106), (3.135, 108)],
    12: [(0.906, 113), (3.135, 117), (4.493, 119)],
    13: [(2.31, 126)],
    14: [(1.939, 132), (3.007, 134)],
}
# absolute old-time anchors (visual key) paired to a human word: INCREMENTALITY letters in the memory beat
ABS_PAIRS = {15: [(69.55, 141)]}

# 1) clean the whole take once (filters see continuous audio — no per-cut edge artefacts)
raw = VOH / "src" / "vo_human_raw.m4a"
clean = VOH / "vo_clean.wav"
CHAIN = ",".join([
    "highpass=f=80:poles=2",                       # rumble / plosive thumps (heavy < 120 Hz)
    "equalizer=f=220:t=q:w=1.0:g=-2.5",            # boxy low-mids from the phone mic
    "equalizer=f=3200:t=q:w=1.2:g=2.0",            # presence / intelligibility
    "equalizer=f=10500:t=q:w=0.8:g=1.5",           # air (AAC rolls off ~16 kHz)
    "deesser=i=0.35:m=0.5:f=0.5",
    "acompressor=threshold=-24dB:ratio=3:attack=6:release=120:makeup=5:knee=4",
    "alimiter=limit=0.89:attack=3:release=60:level=false",
])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", CHAIN, "-ar", str(SR), "-ac", "1", str(clean)], check=True)
x, sr = sf.read(str(clean))
assert sr == SR


def silence_edges():
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(clean), "-af", "silencedetect=noise=-45dB:d=0.12",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    s, e = [], []
    for ln in out.splitlines():
        if "silence_start:" in ln:
            s.append(float(ln.split("silence_start:")[1].split()[0]))
        if "silence_end:" in ln:
            e.append(float(ln.split("silence_end:")[1].split()[0]))
    return s, e


sil_start, sil_end = silence_edges()


def snap(t, cands, win):
    best = min(cands, key=lambda c: abs(c - t)) if cands else t
    return best if abs(best - t) <= win else t


# 2) cut each line at refined word edges, re-space, assemble
track = []
new_lines, anchors = [], [(0.0, 0.0)]
cursor = START
for i, (a, b) in enumerate(LINES):
    ws = snap(words[a]["start"], sil_end, 0.2)
    we = snap(words[b]["end"], sil_start, 0.2)
    prev_end = words[LINES[i - 1][1]]["end"] if i else 0.0
    next_start = words[LINES[i + 1][0]]["start"] if i + 1 < len(LINES) else we + 0.4
    cs = max(ws - 0.08, (prev_end + ws) / 2)
    ce = min(we + 0.16, (we + next_start) / 2)
    seg = x[int(cs * SR):int(ce * SR)].copy()
    f = int(0.012 * SR)
    seg[:f] *= np.linspace(0, 1, f)
    seg[-f:] *= np.linspace(1, 0, f)
    new_ws = cursor
    track.append((new_ws - (ws - cs), seg))
    new_we = new_ws + (we - ws)
    k = f"{i + 1:02d}"
    o = old[k]
    new_lines.append({"line": k, "start": round(new_ws, 3), "end": round(new_we, 3),
                      "src": [round(ws, 3), round(we, 3)]})
    pts = [(o["start"], new_ws)]
    for raw_t, wi in PAIRS.get(i, []):
        pts.append((o["start"] + raw_t / OLD_TEMPO, new_ws + words[wi]["start"] - ws))
    for old_abs, wi in ABS_PAIRS.get(i, []):
        pts.append((old_abs, new_ws + words[wi]["start"] - ws))
    pts.append((o["end"], new_we))
    anchors += sorted(pts)
    cursor = new_we + (GAPS[i] if i < len(GAPS) else 0)

last_old_end = old["16"]["end"]
new_dur = round(new_lines[-1]["end"] + (OLD_END - last_old_end), 2)
anchors.append((OLD_END, new_dur))

# sanity: strictly increasing, report local stretch per span
for (o0, n0), (o1, n1) in zip(anchors, anchors[1:]):
    assert o1 > o0 and n1 > n0, ((o0, n0), (o1, n1))
ratios = [round((n1 - n0) / (o1 - o0), 2) for (o0, n0), (o1, n1) in zip(anchors, anchors[1:])]

N = int(new_dur * SR) + SR
out = np.zeros(N)
for t0, seg in track:
    i0 = int(round(t0 * SR))
    out[i0:i0 + len(seg)] += seg
out = out[:int(new_dur * SR)]
sf.write(str(VOH / "vo_track.wav"), out.astype(np.float32), SR, subtype="PCM_24")

(ROOT / "scripts" / "cues_human.json").write_text(json.dumps({"lines": new_lines}, ensure_ascii=False, indent=1))
(ROOT / "scripts" / "timemap.json").write_text(json.dumps(
    {"duration": new_dur, "anchors": [[round(a, 3), round(b, 3)] for a, b in anchors]}, indent=0))
print("new duration", new_dur, "| anchors", len(anchors))
print("stretch min/max", min(ratios), max(ratios))
for ln in new_lines:
    print(ln)
