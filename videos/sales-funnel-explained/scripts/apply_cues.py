"""Write the VO timings from scripts/cues.json into index.html.

- data-start / data-duration of every scene <section> (windows derived from Scribe word starts)
- the full-length clips (root, ground, vignette, VO, music, sfx) and the subtitle track
- the CUES object the GSAP timeline reads (between /*CUES*/ and /*END CUES*/)

Run after scripts/build_vo.py, then rebuild audio with scripts/build_audio.py.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
cues = json.loads((ROOT / "scripts" / "cues.json").read_text())
w = lambda i: cues["words"][i][0]
we = lambda i: cues["words"][i][1]
END, DUR = cues["endcard"], cues["duration"]

# scene windows (each opens a little before its first word)
SCENES = {
    "s1": (0.0, w(9) - 0.25),            # hook: the ad nobody buys from
    "s1l": (0.0, we(8) + 0.5),           # logo watermark
    "s2": (w(9) - 0.25, w(17) - 0.3),    # stranger
    "s3": (w(17) - 0.3, w(34) - 0.35),   # term: Sales Funnel + the path
    "fn": (w(17) - 0.3, w(123) - 0.3),   # the funnel itself (persistent object, scenes 03-11)
    "cafe": (w(34) - 0.35, w(78) - 0.3), # the cafe street (persistent set, scenes 04-08)
    "s4": (w(34) - 0.35, w(39) - 0.3),   # cafe
    "s5": (w(39) - 0.3, w(48) - 0.3),    # awareness
    "s6": (w(48) - 0.3, w(60) - 0.3),    # consideration
    "s7": (w(60) - 0.3, w(68) - 0.05),   # decision
    "s8": (w(68) - 0.05, w(78) - 0.3),   # loyalty
    "s9": (w(78) - 0.3, w(90) - 0.4),    # the mistake
    "s10": (w(90) - 0.4, w(111) - 0.35), # the messages
    "s11": (w(111) - 0.35, w(123) - 0.3),  # drop-off
    "s12": (w(123) - 0.3, END),          # CTA
    "s13": (END, DUR),                   # end card
    "subs": (0.0, END),
}
FULL = ["root", "ground", "vig", "a-vo", "a-music", "a-sfx"]

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

data = {"duration": DUR, "endcard": END, "scenes": {k: [round(a, 3), round(b, 3)] for k, (a, b) in SCENES.items()},
        "words": cues["words"], "lines": cues["lines"]}
html, k = re.subn(r"/\*CUES\*/.*?/\*END CUES\*/",
                  lambda m: "/*CUES*/ const CUES = " + json.dumps(data, separators=(",", ":")) + "; /*END CUES*/", html, flags=re.S)
assert k == 1, "CUES markers not found"
HTML.write_text(html)
print("applied cues: duration", DUR, "end card", END)
for k, (a, b) in SCENES.items():
    print(f"  {k:5s} {a:7.3f} -> {b:7.3f}")
