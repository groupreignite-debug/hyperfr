"""Lay the chosen ElevenLabs take on the film and write the cue sheet.

Input : audio/vo/vo_full.m4a     (v2 script, take 1, voice "Fadi - Lebanese Conversational", eleven_multilingual_v2,
                                  generated on ElevenLabs flow 75QgovXYrXfkaqwk48P9; supplied as abtest-v2-take1.mp4,
                                  an audio-only AAC file, kept byte-for-byte as .m4a so it isn't re-encoded)
        scripts/vo_words.json    (ElevenLabs Scribe word timings of that file, raw take seconds;
                                  Scribe flow ezIgDHkMyfgVkxUDchRK)
Output: audio/vo/vo_track.wav    (no tempo change, +GAIN_DB, 48 kHz mono, line 01 at frame 0)
        scripts/cues.json        (every word and every script line in film seconds, end card, duration)
Then run scripts/apply_cues.py (writes the timings into index.html) and scripts/build_audio.py.

The take is one continuous file, so it is NOT cut or re-spaced: every timing is a straight linear map
film = LEAD + raw / TEMPO. The 11 script lines are word-index ranges into the Scribe word list.
"""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VO = ROOT / "audio" / "vo"
TEMPO = 1.0       # v2 brief: no speed-up
LEAD = 0.0        # v2 brief: don't trim or delay the start, line 01 begins at frame 0 (first word ~0.1s in)
GAIN_DB = 9.7     # the take lands ~-33.0 LUFS; lift it so the VO sits on top of the mix (~-23 LUFS)
TAIL = 0.6        # after the last word, before the end card
END_CARD = 3.0
# first/last Scribe word index of each script line (brief section 2, v2).
# Scribe hears "A شرطة مقلة B testing" in line 03 (indices 18-22) and an extra "بتجيب" in line 05 (index 42).
LINES = {"01": (0, 8), "02": (9, 15), "03": (16, 28), "04": (29, 35), "05": (36, 45), "06": (46, 58),
         "07": (59, 65), "08": (66, 79), "09": (80, 87), "10": (88, 99), "11": (100, 111)}

words = [w for w in json.loads((ROOT / "scripts" / "vo_words.json").read_text())["words"] if w.get("type", "word") == "word"]
assert len(words) == 112, len(words)
f = lambda t: round(LEAD + t / TEMPO, 3)

W = [[f(w["start"]), f(max(w["end"], w["start"] + 0.08))] for w in words]
end_card = round(W[-1][1] + TAIL, 3)
film_dur = round(end_card + END_CARD, 3)
# the track runs the full film length (silence after the take) so its clip matches the root duration
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VO / "vo_full.m4a"), "-af",
                f"volume={GAIN_DB}dB,aresample=48000,apad",
                "-t", str(film_dur), "-ac", "1", "-c:a", "pcm_s24le", str(VO / "vo_track.wav")], check=True)

cues = {
    "tempo": TEMPO,
    "words": W,
    "text": [w["text"] for w in words],
    "lines": {n: {"s": W[a][0], "e": W[b][1], "w": [a, b]} for n, (a, b) in LINES.items()},
}
cues["endcard"] = end_card
cues["duration"] = film_dur
(ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, ensure_ascii=False, indent=0))
for n, v in cues["lines"].items():
    print(n, v["s"], v["e"], " ".join(cues["text"][v["w"][0]:v["w"][1] + 1]))
print("endcard", cues["endcard"], "duration", cues["duration"])
