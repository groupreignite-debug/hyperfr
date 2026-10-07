"""Speed-match the ElevenLabs VO lines and lay them on the timeline.

Input : audio/vo/src/vo_NN.bin  (ElevenLabs mp3, voice "Fadi - Lebanese Conversational", eleven_multilingual_v2)
Output: audio/vo/vo_NN.wav      (silence-trimmed, TEMPO x, +GAIN_DB, 48 kHz mono)
        scripts/cues.json       (line start/end + internal pauses, absolute seconds)
Then run scripts/apply_cues.py to write the timings into index.html.
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VO = ROOT / "audio" / "vo"
TEMPO = 1.07
START = 0.4
# silence after line i before line i+1 (seconds, post-tempo)
GAPS = [0.45, 1.1, 0.8, 0.6, 0.95, 0.7, 1.25, 0.6, 0.8, 1.2, 0.5, 1.2, 0.5, 1.3]
TAIL = 1.0   # after the last line, before the end card
END_CARD = 3.0
GAIN_DB = 6.0  # ElevenLabs takes land ~-26 LUFS; lift so the VO sits on top of the mix (peaks stay < -1.5 dBFS)
TRIM = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,"
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse")


def dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


def pauses(p):
    """Internal pauses (>=120 ms under -38 dB before the gain lift) -> list of [start, end] seconds from the line start."""
    err = subprocess.run(["ffmpeg", "-v", "info", "-i", str(p), "-af", f"silencedetect=n={-38 + GAIN_DB}dB:d=0.12", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    s = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    e = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    return [[round(a, 3), round(b, 3)] for a, b in zip(s, e)]


cues = {"tempo": TEMPO, "lines": {}}
t = START
srcs = sorted((VO / "src").glob("vo_*.bin"))
for i, src in enumerate(srcs):
    n = src.stem.split("_")[1]
    out = VO / f"vo_{n}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-af", f"{TRIM},atempo={TEMPO},volume={GAIN_DB}dB",
                    "-ar", "48000", "-ac", "1", str(out)], check=True)
    d = dur(out)
    cues["lines"][n] = {"start": round(t, 3), "dur": round(d, 3), "end": round(t + d, 3),
                        "pauses": [[round(t + a, 3), round(t + b, 3)] for a, b in pauses(out)]}
    t += d + (GAPS[i] if i < len(GAPS) else 0)
cues["endcard"] = round(t + TAIL, 3)
cues["duration"] = round(t + TAIL + END_CARD, 3)
(ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, indent=1))
print(json.dumps({k: (v["start"], v["end"], v["pauses"]) for k, v in cues["lines"].items()}, indent=0))
print("endcard", cues["endcard"], "duration", cues["duration"])
