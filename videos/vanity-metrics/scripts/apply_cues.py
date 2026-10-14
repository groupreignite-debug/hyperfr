"""Write the VO timings from scripts/cues.json into index.html.

- the single VO <audio> tag (between <!-- VO --> and <!-- /VO -->)
- data-start / data-duration of every scene <section> (windows derived from the phrase starts)
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
P = cues["phrases"]
s = lambda k: P[k][0]
END, DUR = cues["endcard"], cues["duration"]

# scene windows (v2 storyboard); the hook is on screen from frame 0 and shrinks to the top under the term
SCENES = {
    "s1": (0.0, s("03a") - 0.35),          # 01 HOOK
    "s2": (s("02a") - 0.25, s("03a") - 0.35),  # 02 TERM
    "s3": (s("03a") - 0.35, s("05") - 0.35),   # 03 BALLOONS
    "s4": (s("05") - 0.35, s("08a") - 0.35),   # 04 SHOP
    "s5": (s("08a") - 0.35, s("09a") - 0.3),   # 05 SPLIT
    "s6": (s("09a") - 0.3, s("10a") - 0.3),    # 06 THE REAL QUESTION
    "s7": (s("10a") - 0.3, END),               # 07 QUESTION TO VIEWER
    "s8": (END, DUR),                          # 08 END CARD
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

vo = cues["vo"]
tag = f'      <audio id="vo" src="{vo["src"]}" data-start="0" data-duration="{vo["dur"]}" data-track-index="10"></audio>'
html, k = re.subn(r"<!-- VO -->.*?<!-- /VO -->", lambda m: "<!-- VO -->\n" + tag + "\n      <!-- /VO -->", html, flags=re.S)
assert k == 1, "VO block markers not found"

data = {"duration": DUR, "endcard": END, "phrases": P, "anchors": cues["anchors"],
        "scenes": {sid: [round(a, 3), round(b, 3)] for sid, (a, b) in SCENES.items()}}
html, k = re.subn(r"/\*CUES\*/.*?/\*END CUES\*/",
                  lambda m: "/*CUES*/ const CUES = " + json.dumps(data, separators=(",", ":")) + "; /*END CUES*/", html, flags=re.S)
assert k == 1, "CUES markers not found"
assert html.count('<audio id="vo"') == 1, "VO tag was not written"
HTML.write_text(html)
print("applied cues: duration", DUR, "end card", END)
