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
    "s1": (0.0, w(11) - 0.25),             # hook: two ads, one fails, one does a bit better, why?
    "s1l": (0.0, we(10) + 0.45),           # logo watermark
    "s2": (w(11) - 0.25, w(16) - 0.3),     # guessing: the dart misses
    "s3": (w(16) - 0.3, w(32) - 0.35),     # term: A/B Testing, two versions, people decide
    "shop": (w(32) - 0.35, w(65) - 0.3),   # the juice shop (persistent set, scenes 04-07)
    "s4": (w(32) - 0.35, w(41) - 0.3),     # shop
    "s5": (w(41) - 0.3, w(52) - 0.3),      # the two flyers
    "s6": (w(52) - 0.3, w(59) - 0.25),     # split the crowd
    "s7": (w(59) - 0.25, w(65) - 0.3),     # count: two piles
    "s8": (w(65) - 0.3, w(73) - 0.3),      # numbers talk (subtitle hidden)
    "s9": (w(73) - 0.3, w(95) - 0.05),     # change one thing
    "s10": (w(95) - 0.05, w(108) - 0.35),  # give it time
    "pair": (w(108) - 0.35, w(129) - 0.3), # the two ad cards (persistent, scenes 11-12)
    "s11": (w(108) - 0.35, w(117) - 0.3),  # in ads
    "s12": (w(117) - 0.3, w(129) - 0.3),   # the winner
    "s13": (w(129) - 0.3, END),            # CTA
    "s14": (END, DUR),                     # end card
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
