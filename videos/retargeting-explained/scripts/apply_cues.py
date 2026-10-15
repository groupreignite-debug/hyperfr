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
INTRO = 1.4  # signature intro (scene 00) in front of the film; everything below is offset by it

# scene windows (each opens a little before its first word)
SCENES = {
    "s1": (0.0, w(8) - 0.25),            # hook: twist teaser, rewind, shop page, tap, the jacket left behind
    "s2": (w(8) - 0.25, w(21) - 0.3),    # follow (dimmed behind the freeze)
    "s3": (w(19) - 0.15, w(21) - 0.3),   # freeze
    "s4": (w(21) - 0.3, w(34) - 0.15),   # term
    "s5": (w(34) - 0.15, w(56) - 0.4),   # shop
    "s6": (w(56) - 0.4, w(71) - 0.35),   # pixel
    "s7": (w(71) - 0.35, w(84) - 0.35),  # warm
    "s8": (w(84) - 0.35, w(94) - 0.35),  # don't repeat
    "s9": (w(94) - 0.35, w(113) - 0.4),  # the rules
    "s10": (w(113) - 0.4, w(129) - 0.35),  # the line
    "s11": (w(129) - 0.35, END),         # CTA
    "s12": (END, DUR),                   # end card
    "subs": (0.0, END),
}
FULL = ["root", "ground", "vig"]          # span intro + film
FILM_AUDIO = ["a-vo", "a-music", "a-sfx"]  # the film's own tracks: start after the intro, same length as before

html = HTML.read_text()


def set_window(html, el_id, start, dur):
    pat = re.compile(r'(<[a-z]+ id="%s"[^>]*?data-start=")[0-9.]+("[^>]*?data-duration=")[0-9.]+(")' % re.escape(el_id))
    html, k = pat.subn(lambda m: f"{m.group(1)}{round(start, 3)}{m.group(2)}{round(dur, 3)}{m.group(3)}", html)
    assert k == 1, f"#{el_id} not found"
    return html


for sid, (a, b) in SCENES.items():
    html = set_window(html, sid, a + INTRO, b - a)
for fid in FULL:
    html = set_window(html, fid, 0.0, DUR + INTRO)
for fid in FILM_AUDIO:
    html = set_window(html, fid, INTRO, DUR)
html = set_window(html, "s0", 0.0, INTRO)
html = set_window(html, "a-intro", 0.0, INTRO)

data = {"intro": INTRO, "duration": DUR, "endcard": END, "scenes": {k: [round(a, 3), round(b, 3)] for k, (a, b) in SCENES.items()},
        "words": cues["words"], "lines": cues["lines"]}
html, k = re.subn(r"/\*CUES\*/.*?/\*END CUES\*/",
                  lambda m: "/*CUES*/ const CUES = " + json.dumps(data, separators=(",", ":")) + "; /*END CUES*/", html, flags=re.S)
assert k == 1, "CUES markers not found"
HTML.write_text(html)
print("applied cues: intro", INTRO, "+ film", DUR, "=", round(INTRO + DUR, 3), "| end card at", round(INTRO + END, 3))
for k, (a, b) in SCENES.items():
    print(f"  {k:5s} {a:7.3f} -> {b:7.3f}")
