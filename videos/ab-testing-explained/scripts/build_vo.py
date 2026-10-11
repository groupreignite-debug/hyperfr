"""Lay the chosen ElevenLabs take on the film and write the cue sheet.

Input : audio/vo/vo_full.mp3     (take 2, voice "Fadi - Lebanese Conversational", eleven_multilingual_v2,
                                  generated on ElevenLabs flow zhPIN6mX7STxlNgjxbbw; Salem's pick)
        scripts/vo_words.json    (ElevenLabs Scribe word timings of that file, raw take seconds;
                                  Scribe flow ezIgDHkMyfgVkxUDchRK)
Output: audio/vo/vo_track.wav    (1.07x tempo, pitch kept, +GAIN_DB, 48 kHz mono, starts at LEAD)
        scripts/cues.json        (every word and every script line in film seconds, end card, duration)
Then run scripts/apply_cues.py (writes the timings into index.html) and scripts/build_audio.py.

The take is one continuous file, so it is NOT cut or re-spaced: every timing is a straight linear map
film = LEAD + raw / TEMPO. The 14 script lines are word-index ranges into the Scribe word list.
"""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VO = ROOT / "audio" / "vo"
TEMPO = 1.07      # brief: the takes run 64-66s, speed up ~1.07x (atempo keeps the pitch)
LEAD = 0.3        # silence before the take (its first word sits ~0.08s in)
GAIN_DB = 7.0     # the take lands ~-30.3 LUFS at 1.07x; lift it so the VO sits on top of the mix (~-23 LUFS)
TAIL = 0.6        # after the last word, before the end card
END_CARD = 3.0
# first/last Scribe word index of each script line (brief section 2).
# Scribe hears an extra "ما" in line 08 (index 66: "هيك ما، ما عم تتخمّن"), so line 08 spans 65-72.
LINES = {"01": (0, 10), "02": (11, 15), "03": (16, 19), "04": (20, 31), "05": (32, 40), "06": (41, 51),
         "07": (52, 64), "08": (65, 72), "09": (73, 80), "10": (81, 93), "11": (94, 107), "12": (108, 116),
         "13": (117, 128), "14": (129, 143)}

words = [w for w in json.loads((ROOT / "scripts" / "vo_words.json").read_text())["words"] if w.get("type", "word") == "word"]
assert len(words) == 144, len(words)
f = lambda t: round(LEAD + t / TEMPO, 3)

W = [[f(w["start"]), f(max(w["end"], w["start"] + 0.08))] for w in words]
end_card = round(W[-1][1] + TAIL, 3)
film_dur = round(end_card + END_CARD, 3)
# the track runs the full film length (silence after the take) so its clip matches the root duration
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VO / "vo_full.mp3"), "-af",
                f"atempo={TEMPO},volume={GAIN_DB}dB,adelay={int(LEAD * 1000)},aresample=48000,apad",
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
