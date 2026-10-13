"""Voiceover: audio/vo/vo_full.mp3 (the chosen Fadi landing-v2 take) → audio/vo/vo_track.wav.

  python3 scripts/build_vo.py              # process the chosen take
  python3 scripts/build_vo.py --silent     # timing-preview only: silent track of the cue length

Light polish for an ElevenLabs take (80 Hz HPF, gentle presence, de-ess, -16 LUFS speech level, soft limiter). If the
take runs over 60 s it is sped up without changing pitch (ffmpeg atempo) to land at ~60 s.
The final mix is normalised to -14 LUFS on the render (README).

After a new take: get Scribe word timings into scripts/vo_words.json (on vo_track.wav), then
  python3 scripts/cues.py --words scripts/vo_words.json && python3 scripts/build_audio.py
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "audio" / "vo" / "vo_full.mp3"
OUT = ROOT / "audio" / "vo" / "vo_track.wav"
MAX = 60.0


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


if "--silent" in sys.argv:
    total = json.loads((ROOT / "scripts" / "cues.json").read_text())["beats"]["total"]
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(total),
                    "-c:a", "pcm_s16le", str(OUT)], check=True)
    print("wrote silent", OUT.name, total, "s (timing preview — no VO yet)")
    sys.exit()

d = dur(SRC)
tempo = max(1.0, d / MAX)
chain = [
    "highpass=f=80",
    "equalizer=f=3200:t=q:w=1.2:g=1.5",
    "deesser=i=0.35",
    f"atempo={tempo:.4f}",
    "loudnorm=I=-16:TP=-1.5:LRA=7",  # takes arrive at very different levels (landing-v2 take 1: -33.6 dB mean)
    "alimiter=limit=0.89:level=false",
]
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(SRC), "-af", ",".join(chain), "-ar", "48000", "-ac", "2",
                "-c:a", "pcm_s16le", str(OUT)], check=True)
print(f"wrote {OUT.name}: take {d:.2f}s, tempo x{tempo:.3f} → {dur(OUT):.2f}s")
