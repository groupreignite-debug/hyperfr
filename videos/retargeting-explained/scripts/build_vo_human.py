"""Lay the client-recorded voiceover on the film and write the cue sheet.

Input : audio/vo-human/src/vo_human_raw.m4a   (client recording, WhatsApp AAC 64 kb/s mono, 59.2s)
        scripts/vo_human_words.json            (ElevenLabs Scribe word timings of that file)
        scripts/vo_words.json                  (Scribe words of the earlier TTS take = the word-index space
                                                the animation is keyed to: W(i) in index.html)
Output: audio/vo-human/vo_clean.wav            (whole take, cleaned: HPF, mud cut, presence, air, de-ess, comp)
        audio/vo-human/vo_track.wav            (cleaned take, first word at LEAD, padded to the film length)
        scripts/cues.json                      (139 word slots + 14 lines in film seconds, end card, duration)
Then run scripts/apply_cues.py and scripts/build_audio.py.

The recording is played as one continuous take at its own pace (no cuts, no tempo change). Its words are
aligned to the TTS word slots with difflib, so every scene, subtitle and SFX cue follows the human timing.
Slots for words that were not spoken (e.g. "إياه", "لنا") collapse to a zero-length point at the next word.
"""
import difflib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOH = ROOT / "audio" / "vo-human"
LEAD = 0.12       # first spoken word lands here (brief, Oct 15: within ~0.15s of the start)
TAIL = 0.6        # after the last word, before the end card
END_CARD = 3.0
# first/last word slot of each script line (same as build_vo.py)
LINES = {"01": (0, 7), "02": (8, 18), "03": (19, 20), "04": (21, 23), "05": (24, 33), "06": (34, 43),
         "07": (44, 55), "08": (56, 70), "09": (71, 83), "10": (84, 93), "11": (94, 107), "12": (108, 112),
         "13": (113, 128), "14": (129, 138)}

ws = lambda p: [w for w in json.loads((ROOT / "scripts" / p).read_text())["words"] if w.get("type", "word") == "word"]
old, new = ws("vo_words.json"), ws("vo_human_words.json")
assert len(old) == 139, len(old)

# ---- align the recording's words onto the 139 animation slots
norm = lambda s: re.sub(r"[^\w]", "", s.lower()).replace("ـ", "")
sm = difflib.SequenceMatcher(None, [norm(w["text"]) for w in old], [norm(w["text"]) for w in new], autojunk=False)
slot = [None] * len(old)
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op == "insert":
        continue
    if op == "delete":  # not spoken: a point at the start of the next spoken word
        t = new[b1]["start"] if b1 < len(new) else new[-1]["end"]
        for a in range(a1, a2):
            slot[a] = [t, t]
        continue
    na, nb = a2 - a1, b2 - b1
    for k in range(na):  # equal / replace: spread the old slots over the new words proportionally
        s0, s1 = b1 + (k * nb) // na, b1 + ((k + 1) * nb - 1) // na
        slot[a1 + k] = [new[s0]["start"], new[s1]["end"]]
assert all(slot)

shift = LEAD - new[0]["start"]
W = [[round(a + shift, 3), round(b + shift, 3)] for a, b in slot]
end_card = round(new[-1]["end"] + shift + TAIL, 3)
film_dur = round(end_card + END_CARD, 3)

# ---- clean the whole take once (filters see continuous audio), then place it
raw = VOH / "src" / "vo_human_raw.m4a"
CHAIN = ",".join([
    "highpass=f=80:poles=2",                       # rumble / plosive thumps
    "equalizer=f=220:t=q:w=1.0:g=-2.5",            # boxy low-mids from the phone mic
    "equalizer=f=3200:t=q:w=1.2:g=2.0",            # presence / intelligibility
    "equalizer=f=10500:t=q:w=0.8:g=1.5",           # air (AAC rolls off ~16 kHz)
    "deesser=i=0.35:m=0.5:f=0.5",
    "acompressor=threshold=-24dB:ratio=3:attack=6:release=120:makeup=5:knee=4",
    "alimiter=limit=0.89:attack=3:release=60:level=false",
])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", CHAIN, "-ar", "48000", "-ac", "1",
                str(VOH / "vo_clean.wav")], check=True)
cut = round(-shift, 3)  # drop the silence before the first word (positive: trim, negative: pad)
place = f"atrim=start={cut},asetpts=PTS-STARTPTS" if cut >= 0 else f"adelay={int(-cut * 1000)}"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VOH / "vo_clean.wav"), "-af", f"{place},apad",
                "-t", str(film_dur), "-ac", "1", "-c:a", "pcm_s24le", str(VOH / "vo_track.wav")], check=True)

cues = {
    "source": "vo-human",
    "words": W,
    "text": [" ".join(w["text"] for w in new if slot[i][0] <= w["start"] < slot[i][1] + 1e-6) for i in range(len(old))],
    "lines": {n: {"s": W[a][0], "e": W[b][1], "w": [a, b]} for n, (a, b) in LINES.items()},
    "endcard": end_card,
    "duration": film_dur,
}
(ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, ensure_ascii=False, indent=0))
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op != "equal":
        print(f"  {op:7s} script {[w['text'] for w in old[a1:a2]]} -> spoken {[w['text'] for w in new[b1:b2]]}")
for n, v in cues["lines"].items():
    print(n, v["s"], v["e"])
print("endcard", end_card, "duration", film_dur)
