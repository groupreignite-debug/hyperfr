"""Speed-match the ElevenLabs VO lines and lay them on the timeline.

Input : audio/vo/src/vo_NN.bin  (ElevenLabs mp3, voice "Fadi - Lebanese Conversational")
Output: audio/vo/vo_NN.wav      (silence-trimmed, TEMPO x, 48 kHz mono)
        scripts/cues.json       (line starts/ends + word anchors, absolute seconds)
"""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VO = ROOT / "audio" / "vo"
TEMPO = 1.07
START = 0.45
# silence after line i before line i+1 (seconds, post-tempo)
GAPS = [1.25, 0.55, 0.45, 0.5, 0.55, 0.6, 0.35, 0.4, 0.65, 0.3, 0.65, 0.45, 0.65, 0.55, 0.7]
# word anchors measured with ElevenLabs Scribe on the raw takes (seconds from first word)
WORDS = {
    "01": {"jibt": 3.19, "thalatheen": 3.62},
    "03": {"miyye": 0.77, "arbaeen": 1.56},
    "04": {"khamse": 0.45, "hatta": 3.80},
    "08": {"addesh": 1.80},
    "09": {"addesh": 2.04},
    "10": {"shafet": 3.60, "mashafto": 5.38},
    "11": {"khamseen": 1.20, "tlatin": 2.73, "farq": 4.50, "khamstash": 5.07, "ziyade": 6.43},
    "12": {"roas": 1.82, "khamsex": 3.14},
    "13": {"taatheer": 0.91, "incr": 3.13},
    "14": {"kam": 2.31},
    "15": {"kam": 1.94, "makanet": 3.00},
}
TRIM = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,"
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse")


def dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


cues = {"tempo": TEMPO, "lines": {}}
t = START
srcs = sorted((VO / "src").glob("vo_*.bin"))
for i, src in enumerate(srcs):
    n = src.stem.split("_")[1]
    out = VO / f"vo_{n}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-af", f"{TRIM},atempo={TEMPO}",
                    "-ar", "48000", "-ac", "1", str(out)], check=True)
    d = dur(out)
    words = {k: round(t + v / TEMPO, 3) for k, v in WORDS.get(n, {}).items()}
    cues["lines"][n] = {"start": round(t, 3), "dur": round(d, 3), "end": round(t + d, 3), "words": words}
    if i < len(GAPS):
        t += d + GAPS[i]
print(json.dumps(cues, indent=1))
(ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, indent=1))
