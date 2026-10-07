---
format: 1080x1920
fps: 30
duration: 56.07
music: dark minimal electronic bed (procedural, scripts/build_audio.py), same palette as Incrementality
captions: Arabic, burned in, one line at a time, key terms in orange Latin
---

# STORYBOARD: Vanity Metrics

Same world as episode 1: charcoal canvas, barely visible 72px grid drifting slowly, Alexandria 300–900,
orange for meaning, a progress hairline at the top. All scene windows are derived from the VO line starts
(`scripts/apply_cues.py`), so they move with the voice.

| # | window (s) | lines | scene | on-screen text |
|---|------------|-------|-------|----------------|
| 01 HOOK | 0–7.1 | 01–02 | Heart card counts 0 → `10,000` (off-white) as "عشر آلاف لايك" is said, small hearts float up. Second card lands `0 زبون` in orange. Logo watermark at top | `10,000 ❤` · `0 زبون` |
| 02 FREEZE | 5.65–7.1 | 03 | Hook dims and blurs; the question rises | `شو صار؟` |
| 03 TERM | 7.1–12.6 | 04–05 | Caret blinks, `VANITY METRICS` lands letter by letter, gloss slides in, then the line types in word by word with `الإيجار` in orange | `VANITY METRICS` · `أرقام الغرور` · `بتبيّن حلوة… بس ما بتدفع الإيجار` |
| 04 BALLOONS | 12.6–22.1 | 06–07 | `LIKES 10,000`, `VIEWS 50,000`, `FOLLOWERS 2,500` puff up (elastic) on each spoken word and bob. On line 07 a thin orange line sweeps down and pops them one by one into small dots. The question rises | `LIKES` `VIEWS` `FOLLOWERS` · `قدّيش واحد صار زبون؟` |
| 05 SHOP | 22.1–33.2 | 08–10 | A line-drawn shop front draws on; a dense crowd of dots streams past (`1,000 مرقوا` counts up). 10 dots peel into the door (`10 فاتوا`), 2 turn orange and glow (`2 اشتروا`). `REACH` brackets the crowd; the shop sign lights `BUSINESS` in orange | `1,000 مرقوا` · `10 فاتوا` · `2 اشتروا` · `REACH` / `BUSINESS` |
| 06 SPLIT | 33.2–41.2 | 11–12 | Divider draws. Left (dim): `VANITY` — LIKES · VIEWS · FOLLOWERS. Right: orange `ACTIONABLE`, items appear as spoken | `VANITY` / `ACTIONABLE` · `رسائل` `طلبات أسعار` `مبيعات` `زبون رجع` |
| 07 THE REAL QUESTION | 41.2–48.4 | 13–14 | `قدّيش لايك جبنا؟` is struck through in orange and greys out; the two real questions land, `بيعة` in orange, slow push-in | ~~`قدّيش لايك جبنا؟`~~ · `قدّيش رسالة إجت؟` · `قدّيش منها صار بيعة؟` |
| 08 QUESTION TO VIEWER | 48.4–53.1 | 15 | Calm. Large comment bubble (typing dots), the question, then the comments prompt with a bobbing arrow | `شو أول رقم بتتطلّع عليه؟` · `قلّي بالكومنتات` ↓ |
| 09 END CARD | 53.1–56.1 | — | Logo fades in 0.97 → 1 with the chime. No text | (logo only) |

Notes
- `❤` and `👇` are drawn as brand-colour SVG icons (off-white heart, orange down-arrow) instead of colour emoji,
  which would bring in non-brand yellow/red and render inconsistently across fonts.
- The metric values (10,000 / 50,000 / 2,500 / 1,000 → 10 → 2) are hypothetical, framed by "تخيّل".
