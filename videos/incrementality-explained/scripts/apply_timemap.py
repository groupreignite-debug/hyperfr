"""Write scripts/timemap.json into index.html (idempotent).

Clip windows are listed here in AUTHORED time (the original cue sheet); they are mapped
through the time map and written as data-start / data-duration. The TIMEMAP constant in the
script block and every full-length clip/audio duration are refreshed too.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tm = json.loads((ROOT / "scripts" / "timemap.json").read_text())
A, DUR = tm["anchors"], tm["duration"]
AUTHORED = {  # id: (start, end) in authored time
    "s1": (0, 9.4), "s1l": (0, 6.8), "s2": (6.2, 9.4), "s3": (9.4, 21.15), "s4": (21.15, 35.75),
    "s5": (35.75, 50.1), "s6": (50.1, 59.95), "s7": (59.95, 68.4), "s8": (68.4, 72.4), "s9": (72.4, 75.4),
}
FULL = ["root", "ground", "vig", "a-music", "a-vo", "a-sfx"]


def M(t):
    for (o0, n0), (o1, n1) in zip(A, A[1:]):
        if o0 <= t <= o1:
            return n0 + (t - o0) * (n1 - n0) / (o1 - o0)
    return A[-1][1] + (t - A[-1][0])


p = ROOT / "index.html"
s = p.read_text()
for el, (a, b) in AUTHORED.items():
    s, n = re.subn(rf'(id="{el}"[^>]*?)data-start="[\d.]+" data-duration="[\d.]+"',
                   rf'\g<1>data-start="{M(a):.3f}" data-duration="{M(b) - M(a):.3f}"', s)
    assert n == 1, el
for el in FULL:
    s, n = re.subn(rf'(id="{el}"[^>]*?)data-start="[\d.]+" data-duration="[\d.]+"',
                   rf'\g<1>data-start="0" data-duration="{DUR}"', s)
    assert n == 1, el
s, n = re.subn(r"const TIMEMAP = \[.*?\];", f"const TIMEMAP = {json.dumps(A)};", s)
assert n == 1
p.write_text(s)
print("applied timemap, duration", DUR)
