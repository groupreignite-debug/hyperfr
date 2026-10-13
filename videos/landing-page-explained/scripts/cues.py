"""Cue sheet for the "Landing Page" reel: line + word timings → scripts/cues.json → index.html.

The animation, the subtitles and the SFX all read one cue sheet, so a new voiceover take only
needs this script re-run (then build_audio.py).

  python3 scripts/cues.py --placeholder          # brief's target timings (no audio yet)
  python3 scripts/cues.py --words scripts/vo_words.json   # ElevenLabs Scribe word timings

vo_words.json is Scribe's word list: [{"text": "...", "start": s, "end": s}, ...] (spacing
entries are ignored). Scribe's tokens are aligned to the script's tokens with difflib on a
normalised form; any script token Scribe split or merged differently is interpolated from its
neighbours. Writes scripts/cues.json and injects CUES + BEATS into index.html.
"""
import argparse
import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Spoken = subtitle text (brief §3). Tokens split on spaces; keep this in sync with SCRIPT.md.
SCRIPT = [
    "عم تدفع عالإعلان… وتبعت الناس عالصفحة الرئيسية؟",
    "هون عم تضيّع مصاري.",
    "خلّيني فرجيك مثال: محل أحذية أونلاين.",
    "هيدي الـ Homepage تبعو. فيها قائمة، وأقسام كتير، وكبسات بكل مكان.",
    "وهيدا طبيعي. الـ Homepage معمولة لكل الناس: اللي بدو رجالي، اللي بدو نسائي، واللي بدو العروض.",
    "بس هوّي عامل إعلان على حذاء رياضي واحد. لوين لازم يبعت الناس؟",
    "على Landing Page.",
    "ما في قائمة. صورة الحذاء، عنوان واحد، وكبسة وحدة: اطلب هلّق.",
    "ليش؟ لأن الزائر جايي لسبب واحد، والصفحة لازم تحكي عن هيدا السبب بس.",
    "تخيّل تعزم حدا على العشا، وتقلّو: تعا عالحي، ودوّر عالبيت لحالك.",
    "الـ Landing Page هيي إنك تفتحلو الباب، والطاولة جاهزة.",
    "القاعدة بسيطة: إعلان واحد، صفحة وحدة، هدف واحد.",
    "إعلاناتك لوين عم تبعت الناس؟ اكتبلنا بالكومنتات.",
]
# Brief §3 target starts (seconds) — used only for the placeholder sheet.
TARGET = [0.0, 3.5, 5.5, 8.5, 14.5, 22.0, 27.0, 29.0, 35.0, 41.0, 46.5, 51.0, 55.5]
TARGET_END = 59.0

END_GAP = 0.5   # VO end → end card
END_CARD = 3.0  # end card length (brief: ~3s)

# Homepage mockup: buttons per section, in page order (must match the .btn elements built in
# index.html → HOME_SECTIONS). Used for the counter ticks.
HOME_BUTTONS = [1, 0, 1, 7, 1, 1, 1, 0]


def norm(s):
    s = re.sub(r"[ً-ْـ]", "", s)  # harakat + tatweel
    s = re.sub(r"[^\w]", "", s.lower())
    return s.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ة", "ه").replace("ى", "ي")


def tokens():
    return [ln.split() for ln in SCRIPT]


def placeholder():
    out = []
    for i, toks in enumerate(tokens()):
        s = TARGET[i]
        e = (TARGET[i + 1] - 0.45) if i + 1 < len(TARGET) else TARGET_END
        w = [len(t) + 2 for t in toks]
        tot = sum(w)
        t, words = s, []
        for tok, wi in zip(toks, w):
            d = (e - s) * wi / tot
            words.append({"t": tok, "s": round(t, 3), "e": round(t + d * 0.9, 3)})
            t += d
        out.append(words)
    return out


def from_scribe(path):
    raw = json.loads(Path(path).read_text())
    if isinstance(raw, dict):
        raw = raw.get("words", raw)
    sw = [w for w in raw if w.get("type", "word") == "word" and norm(w["text"])]
    flat = [(li, tok) for li, toks in enumerate(tokens()) for tok in toks]
    a = [norm(t) for _, t in flat]
    b = [norm(w["text"]) for w in sw]
    times = [None] * len(flat)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                times[i1 + k] = (sw[j1 + k]["start"], sw[j1 + k]["end"])
        elif tag == "replace":
            # spread the Scribe span over the script tokens (handles split / merged words)
            s, e = sw[j1]["start"], sw[j2 - 1]["end"]
            n = i2 - i1
            for k in range(n):
                times[i1 + k] = (s + (e - s) * k / n, s + (e - s) * (k + 1) / n)
    # interpolate anything still missing
    for i in range(len(times)):
        if times[i] is None:
            p = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), 0.0)
            n = next((times[j][0] for j in range(i + 1, len(times)) if times[j]), p + 0.3)
            times[i] = (p, max(p + 0.05, n))
    out = [[] for _ in SCRIPT]
    for (li, tok), (s, e) in zip(flat, times):
        out[li].append({"t": tok, "s": round(s, 3), "e": round(e, 3)})
    return out


def beats(L):
    """Every timed beat in the film, derived from the cue sheet (shared by JS + audio)."""
    W = lambda n, k: L[n - 1]["words"][k]["s"]
    WE = lambda n, k: L[n - 1]["words"][k]["e"]
    LS = lambda n: L[n - 1]["start"]
    LE = lambda n: L[n - 1]["end"]
    b = {}
    # 01 hook
    b["s1_ad"] = max(0.15, W(1, 0))
    b["s1_tap"] = W(1, 2) + 0.15
    b["s1_arrow"] = W(1, 3)
    b["s1_house"] = W(1, 3) + 0.45
    b["s1_push"] = W(1, 6)
    b["s1_lost"] = W(1, 6) + 0.35
    b["s1_coin"] = W(2, 3)
    b["s1_out"] = LS(3) - 0.35
    # 02 example
    b["s2_phone"] = LS(3) - 0.15
    b["s2_mark"] = W(3, 4)
    # 03 homepage
    b["s3_menu"] = W(4, 5)
    b["s3_menu_close"] = W(4, 6) - 0.1
    s0 = W(4, 6) + 0.05
    s1 = max(s0 + 2.6, min(LE(4) + 0.6, W(5, 2) - 0.35))
    b["s3_steps"] = [round(s0 + (s1 - s0) * k / len(HOME_BUTTONS), 3) for k in range(len(HOME_BUTTONS))]
    b["s3_end"] = s1
    # 04 for everyone
    b["s4_shrink"] = W(5, 2) - 0.1
    b["s4_p"] = [W(5, 9), W(5, 12), W(5, 15)]
    # 05 the ad
    b["s5_ad"] = W(6, 2)
    b["s5_shoe"] = W(6, 5)
    b["s5_arrow"] = W(6, 8)
    b["s5_q"] = W(6, 11)
    # 06 term
    b["s6_wipe"] = LS(7) - 0.1
    b["s6_term"] = W(7, 1)
    # 07 one of each
    b["s7_k"] = [W(8, 0), W(8, 3), W(8, 5), W(8, 7)]
    b["s7_tap"] = W(8, 9)
    # 08 side by side
    b["s8_split"] = LS(9) - 0.1
    b["s8_lab_a"] = W(9, 1)
    b["s8_ad"] = W(9, 2)
    b["s8_line"] = W(9, 4)
    b["s8_lab_b"] = W(9, 6)
    # 09 dinner
    b["s9_in"] = LS(10) - 0.15
    b["s9_guest"] = W(10, 1)
    b["s9_wander"] = W(10, 6)
    # 10 door open
    b["s10_light"] = W(11, 1)
    b["s10_door"] = W(11, 5)
    b["s10_table"] = W(11, 7)
    b["s10_walk"] = WE(11, 7)
    # 11 the rule
    b["s11_in"] = LS(12) - 0.1
    b["s11_stamp"] = [W(12, 2), W(12, 4), W(12, 6)]
    # 12 cta
    b["s12_in"] = LS(13) - 0.1
    b["s12_chips"] = [W(13, 1), W(13, 3)]
    b["s12_arrow"] = W(13, 5)
    # 13 end
    b["end"] = round(LE(13) + END_GAP, 3)
    b["total"] = round(b["end"] + END_CARD, 3)
    return {k: (round(v, 3) if isinstance(v, float) else v) for k, v in b.items()}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--placeholder", action="store_true")
    g.add_argument("--words")
    args = ap.parse_args()
    words = placeholder() if args.placeholder else from_scribe(args.words)
    lines = [{"n": i + 1, "text": SCRIPT[i], "start": w[0]["s"], "end": w[-1]["e"], "words": w}
             for i, w in enumerate(words)]
    cues = {"source": "placeholder" if args.placeholder else Path(args.words).name, "lines": lines}
    cues["beats"] = beats(lines)
    cues["home_buttons"] = HOME_BUTTONS
    (ROOT / "scripts" / "cues.json").write_text(json.dumps(cues, ensure_ascii=False, indent=1))

    # inject into index.html
    idx = ROOT / "index.html"
    html = idx.read_text()
    blob = json.dumps({"lines": [{"n": l["n"], "start": l["start"], "end": l["end"],
                                  "words": [[w["t"], w["s"], w["e"]] for w in l["words"]]} for l in lines],
                       "beats": cues["beats"]}, ensure_ascii=False, separators=(",", ":"))
    html = re.sub(r"/\*CUES\*/.*?/\*END-CUES\*/", lambda m: "/*CUES*/" + blob + "/*END-CUES*/", html, flags=re.S)
    total = cues["beats"]["total"]
    html = re.sub(r'(data-full[^>]*?data-duration=")[0-9.]+"', lambda m: m.group(1) + f'{total}"', html)
    idx.write_text(html)
    print(f"cues: {cues['source']}  VO {lines[0]['start']:.2f}–{lines[-1]['end']:.2f}s  total {total}s")


if __name__ == "__main__":
    main()
