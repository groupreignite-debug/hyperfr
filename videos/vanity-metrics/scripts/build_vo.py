"""Map the chosen v2 VO take onto the script and write the timing cues.

Input : audio/vo/vo_full.m4a   (ElevenLabs "Fadi - Lebanese Conversational", v2 take 1, one continuous take)
Output: audio/vo/vo_full.wav   (48 kHz mono, +GAIN_DB, untrimmed: line 01 starts at 0.0s with the picture)
        scripts/cues.json      (phrase windows, word anchors, end card, duration)
Then run scripts/apply_cues.py (index.html) and scripts/build_audio.py (music + SFX).

The speaker's own pauses split the take into phrases. PHRASES names them in script order (line number + part);
the build stops if the detected phrase count changes, so a different take cannot silently mis-map.
Word anchors inside a phrase are offsets from its start, measured on this take (finer silence dips).
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VO = ROOT / "audio" / "vo"
SRC, OUT = VO / "vo_full.m4a", VO / "vo_full.wav"
GAIN_DB = 10.0      # the take lands ~-31 LUFS; lift so the VO sits on top of the mix (peaks stay < -2 dBFS)
TAIL = 0.5          # after the last word, before the end card
END_CARD = 3.0

# one entry per detected phrase, in order. "_" = a breath blip, folded into the next phrase.
PHRASES = ["01", "02a", "02b", "02c", "03a", "03b", "04a", "04b", "05", "06a", "06b", "07a", "_", "07b",
           "08a", "08b", "08c", "08d", "09a", "09b", "09c", "10a", "10b", "10c"]
# word onsets: name -> (phrase, seconds from phrase start)
ANCHORS = {
    "zboun": ("01", 1.35),        # "وولا زبون" — 0 زبون slams in
    "vanity": ("02a", 0.70),      # "Vanity Metrics"
    "rent": ("02c", 0.50),        # "الإيجار" — bill stamp
    "likes": ("03a", 0.02), "views": ("03a", 0.66), "followers": ("03a", 1.31),
    "pop": ("04a", 0.25),         # needle starts popping on line 04
    "zboun2": ("04b", 1.20),      # "زبون؟"
    "alf": ("05", 1.50),          # "ألف شخص"
    "ten": ("06a", 0.00), "two": ("06b", 0.05),
    "reach": ("07a", 0.60), "biz": ("07b", 0.60),
    "actionable": ("08a", 1.55),
    "item1": ("08b", 0.00), "item2": ("08b", 0.67), "item3": ("08c", 0.00), "item4": ("08d", 0.03),
    "likesq": ("09a", 0.90),      # "قدّيش لايك جبنا"
    "msg": ("09c", 0.15), "sale": ("09c", 1.50),
    "comments": ("10c", 0.00),
}


def phrases(path):
    err = subprocess.run(["ffmpeg", "-v", "info", "-i", str(path), "-af", "silencedetect=n=-40dB:d=0.12", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    s = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    e = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    out, t = [], 0.0
    for a, b in zip(s, e):
        if a > t + 0.02:
            out.append([round(t, 3), round(a, 3)])
        t = b
    return out


det = phrases(SRC)
assert len(det) == len(PHRASES), f"take has {len(det)} phrases, script map expects {len(PHRASES)}"
P = {}
blip = None
for key, (a, b) in zip(PHRASES, det):
    if key == "_":
        blip = a
        continue
    P[key] = [blip if blip is not None else a, b]
    blip = None

subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(SRC), "-af", f"volume={GAIN_DB}dB", "-ar", "48000", "-ac", "1",
                str(OUT)], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(OUT)],
                           capture_output=True, text=True, check=True).stdout)
end = round(P["10c"][1] + TAIL, 3)
cues = {"vo": {"src": "audio/vo/vo_full.wav", "dur": round(dur, 3)}, "phrases": P,
        "anchors": {k: round(P[p][0] + o, 3) for k, (p, o) in ANCHORS.items()},
        "endcard": end, "duration": round(end + END_CARD, 3)}
(ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, indent=1))
for k, v in P.items():
    print(k, v)
print("endcard", cues["endcard"], "duration", cues["duration"])
