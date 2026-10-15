---
format: 1080x1920
fps: 30
duration: 61.64  # 1.4s intro + 60.24s film
music: dark minimal electronic bed (procedural, scripts/build_audio.py), same palette as the earlier episodes
captions: Arabic, burned in, one line at a time, key terms in orange Latin
---

# STORYBOARD: Retargeting (شو يعني؟)

Same world as the earlier episodes: charcoal canvas, barely visible 72px grid drifting slowly, Alexandria 300–900,
orange for meaning, a progress hairline at the top. **Hook (Oct 14/15):** frame 0 is already full, the twist is on screen by
~0.9s before the voice reaches it, and there is no logo before the end card. **One text layer:** the centre shows
visuals and short labels; where it shows a full spoken line, the bottom subtitle is hidden. **One world:** the off-white **jacket card** (line-drawn jacket,
tiny orange zip pull) is the item left behind, the card that follows across feeds, the piece on the shop rail, the
product the Pixel remembers and the ad that repeats. The **Pixel** is one small glowing orange dot. Every scene window
and reveal is keyed to a Scribe word time (`scripts/apply_cues.py`, `W(i)` in `index.html`).

| # | window (s) | lines | scene | on-screen text |
|---|------------|-------|-------|----------------|
| 00 INTRO | master 0–1.4 | — | Signature intro, purely additive. `Retargeting` (off-white, Alexandria 900) ignites left→right: a gold-orange ember edge, a soft orange glow, a light heat shimmer and a few embers; holds crisp ~0.55s; burns away left→right the same way; every ember is out before 1.4s. Its own soft ember sound. **All windows below are film time; add 1.4s for master time.** | `Retargeting` |
| 01 HOOK | 0–3.07 | 01 | **0–1.2s, twist teaser (frame 0 already full):** the jacket card is big in the centre with three empty feed phones under it; inside 0.3s the same card pops into each feed (notification pops). At 0.8s the card lunges at the camera, the feeds dim and `لاحقك؟` stamps in big orange with a short shake (whoosh-thud). **1.2s, rewind:** `⏪` appears (tape-rewind zip), the feeds fly back the way they came, the card settles and a phone with an abstract shop page appears around it. As line 01 is spoken a cursor taps the jacket, the phone slides down, and the jacket is left floating. **No logo** | `لاحقك؟` · `⏪` (drawn icon) · `شفت` (eye icon) · `فلّيت` (hand icon) |
| 02 FOLLOW | 3.07–8.54 | 02 | The floating card hops on "الجاكيت", then three feed phones slide in from the right (RTL order). The card flies into the first feed; the same card pops into the second and third; on the third it drifts toward the viewer | `Instagram` · `YouTube` · `بكل مكان` |
| 03 FREEZE | 6.89–8.54 | 03 | The feeds dim and blur; the question rises; `لأ.` stamps in orange. The music stops dead on "لأ" | `صدفة؟` · `لأ.` (bottom subtitle hidden) |
| 04 TERM | 8.54–13.99 | 04–05 | Caret, then `Retargeting` lands letter by letter. A person icon and a small jacket card: a dotted arc goes out to the shop, an orange arc draws back to the same person with an arrowhead. The definition rises word by word | `Retargeting` · icons only: eye ← ✗ ← loop (orange) |
| 05 SHOP | 13.99–22.80 | 06–07 | Line-drawn shop (awning, window with a rail, door) draws on; the jacket hangs on the rail. A person walks in (door bell), tries the jacket in the window, walks out. Chips land as spoken. An orange salesperson appears in the doorway; the person passes by again and a speech bubble pops from the shop; the jacket glows | `فات ✓` · `جرّب ✓` · `اشترى ✗` · bubble: wave (hand) icon, the line itself stays in the subtitle |
| 06 PIXEL | 22.80–29.21 | 08 | A browser window rises. The orange salesperson shrinks into the Pixel dot in the page corner. A cursor taps the product page (dot pulses + blip), a dashed orange line drops to the memory panel, then the cursor taps the cart button and the page switches to the cart (dot pulses) | `PIXEL = البيّاع` · list: `فات ✓` · `صفحة الجاكيت ✓` |
| 07 WARM | 29.21–34.29 | 09 | Two small shops. Left: grey stranger with a long dotted path. Right: orange person with a short path | `ما بيعرفك` · `بيعرفك` · `مش من الصفر` |
| 08 DON'T REPEAT | 34.29–38.29 | 10 | The same jacket ad is dealt five times like a deck (card flicks), each one more faded. The sleepy face appears on "بيزهق" and the deck slides away | `×5 = 😴` (sleepy face drawn as a line icon) |
| 09 THE RULES | 38.29–46.48 | 11–12 | Three rows build down, icon on the right (RTL), mini ad thumbnail on the left. Eye → "show it again" (thumbnail flashes). Cart → "remind" (Pixel dot on the thumbnail). Check → on "وقّف" the row turns **gold** and the thumbnail fades out (positive click) | `👁 شاف ← 🔁` · `🛒 بالسلة ← 🔔` · `✓ اشترى ← ⛔` (labels + line icons; ⛔ drawn as a circle with a bar) |
| 10 LINE | 46.48–52.07 | 13 | Calm type beat, whole words rising, slow push-in, music thins out. `فات وفلّ.` lands in orange | `مش كل إعلان لازم يحكي مع ناس جداد.` · `أقرب زبون… هوي اللي فات وفلّ.` (bottom subtitle hidden) |
| 11 CTA | 52.07–57.24 | 14 | Large orange comment bubble with `PIXEL` and the Pixel dot pulsing beside it; the prompt, a bobbing down arrow, then the promise | `اكتب PIXEL 👇` (arrow drawn as a line icon) · `ومنقلّك كيف تتأكد` (subtitle shows only `موقعك فيه Pixel؟`, then hides) |
| 12 END CARD | 57.24–60.24 | — | The supplied logo fades in 0.97 → 1 with the Reignite chime. No text | (logo only) |

Notes
- Emoji (👀 👋 ✓ ✗ 🛒 👁 😴 👇 ←) are drawn as line icons in brand colours. Alexandria has no emoji, and a fallback
  emoji font would look different from scene to scene (brief §4 allows this).
- Gold appears once: the "bought" row in scene 09.
- Muted grey `#6E6A64` (the stranger in scene 07) is the same neutral the earlier episodes use for "inactive".
- `Instagram` / `YouTube` appear only as plain words in Alexandria: no logos, icons or platform colours.
- Multi-line layouts: the scene 04 definition, the scene 09 rules (condition on line one, `←` + action on line two)
  and the scene 10 lines are broken across rows to fit 1080px. The strings themselves match the brief.
