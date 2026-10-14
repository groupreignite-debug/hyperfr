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

# scene windows (each opens a little before its first word). Keep in step with scripts/build_audio.py (SC).
SCENES = {
    "cards": (0.0, w(29) - 0.3),           # the two ad cards (persistent, scenes 01-03); on screen at frame 0
    "s1": (0.0, w(9) - 0.25),              # hook: coins pouring, which one?
    "s2": (w(9) - 0.25, w(16) - 0.3),      # gut: heart points at A, the dart misses
    "s3": (w(16) - 0.3, w(29) - 0.3),      # term: A/B Testing, people decide
    "shop": (w(29) - 0.3, w(59) - 0.3),    # the juice shop (persistent set, scenes 04-06)
    "s4": (w(29) - 0.3, w(36) - 0.3),      # shop
    "s5": (w(36) - 0.3, w(46) - 0.3),      # the two flyers
    "s6": (w(46) - 0.3, w(53) - 0.2),      # split the crowd
    "s6b": (w(53) - 0.2, w(59) - 0.3),     # count: two piles
    "s7": (w(59) - 0.3, w(66) - 0.3),      # numbers talk (subtitle hidden)
    "s8": (w(66) - 0.3, w(81) - 0.05),     # change one thing
    "s9": (w(81) - 0.05, w(88) - 0.3),     # give it time
    "s10": (w(88) - 0.3, w(100) - 0.3),    # the winner (cards again)
    "s11": (w(100) - 0.3, END),            # CTA
    "s12": (END, DUR),                     # end card
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
