"""Write the VO timings from scripts/cues.json into index.html.

- the <audio> VO tags (between <!-- VO --> and <!-- /VO -->)
- data-start / data-duration of every scene <section> (windows derived from the line starts)
- the full-length clips (ground, vignette, music, sfx, subtitles)
- the CUES object the GSAP timeline reads (between /*CUES*/ and /*END CUES*/)

Run after scripts/build_vo.py, then rebuild audio with scripts/build_audio.py.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
cues = json.loads((ROOT / "scripts" / "cues.json").read_text())
L = cues["lines"]
s = lambda n: L[n]["start"]
END, DUR = cues["endcard"], cues["duration"]

# scene windows: each scene opens a little before its first line
SCENES = {
    "s1": (0.0, s("04") - 0.3),             # hook (frozen + dimmed behind the question)
    "s1l": (0.0, L["02"]["end"] + 0.8),     # logo watermark
    "s2": (L["02"]["end"] + 0.6, s("04") - 0.3),
    "s3": (s("04") - 0.3, s("06") - 0.45),
    "s4": (s("06") - 0.45, s("08") - 0.5),
    "s5": (s("08") - 0.5, s("11") - 0.45),
    "s6": (s("11") - 0.45, s("13") - 0.45),
    "s7": (s("13") - 0.45, s("15") - 0.5),
    "s8": (s("15") - 0.5, END),
    "s9": (END, DUR),
    "subs": (0.0, END),
}
FULL = ["root", "ground", "vig", "a-music", "a-sfx"]

html = HTML.read_text()


def set_window(html, el_id, start, dur):
    pat = re.compile(r'(<[a-z]+ id="%s"[^>]*?data-start=")[0-9.]+("[^>]*?data-duration=")[0-9.]+(")' % re.escape(el_id))
    html, k = pat.subn(lambda m: f"{m.group(1)}{round(start, 3)}{m.group(2)}{round(dur, 3)}{m.group(3)}", html)
    assert k == 1, f"#{el_id} not found"
    return html


for sid, (a, b) in SCENES.items():
    html = set_window(html, sid, a, b - a)
for fid in FULL:
    html = set_window(html, fid, 0.0, DUR)

tags = "\n".join(
    f'      <audio id="vo{n}" src="audio/vo/vo_{n}.wav" data-start="{v["start"]}" data-duration="{v["dur"]}" data-track-index="10"></audio>'
    for n, v in L.items())
html, k = re.subn(r"<!-- VO -->.*?<!-- /VO -->", lambda m: "<!-- VO -->\n" + tags + "\n      <!-- /VO -->", html, flags=re.S)
assert k == 1, "VO block markers not found"

data = {"duration": DUR, "endcard": END, "scenes": {k: [round(a, 3), round(b, 3)] for k, (a, b) in SCENES.items()},
        "lines": {n: {"s": v["start"], "e": v["end"], "p": v["pauses"]} for n, v in L.items()}}
html = re.sub(r"/\*CUES\*/.*?/\*END CUES\*/", lambda m: "/*CUES*/ const CUES = " + json.dumps(data, separators=(",", ":")) + "; /*END CUES*/",
              html, flags=re.S)
assert html.count('<audio id="vo') == len(L), "VO tags were not written"
HTML.write_text(html)
print("applied cues: duration", DUR, "end card", END)
