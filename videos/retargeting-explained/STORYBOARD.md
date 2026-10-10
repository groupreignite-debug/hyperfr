---
format: 1080x1920
fps: 30
duration: 61.58
music: dark minimal electronic bed (procedural, scripts/build_audio.py), same palette as the earlier episodes
captions: Arabic, burned in, one line at a time, key terms in orange Latin
---

# STORYBOARD: Retargeting (شو يعني؟)

Same world as the earlier episodes: charcoal canvas, barely visible 72px grid drifting slowly, Alexandria 300–900,
orange for meaning, a progress hairline at the top. **One world:** the off-white **jacket card** (line-drawn jacket,
tiny orange zip pull) is the item left behind, the card that follows across feeds, the piece on the shop rail, the
product the Pixel remembers and the ad that repeats. The **Pixel** is one small glowing orange dot. Every scene window
and reveal is keyed to a Scribe word time (`scripts/apply_cues.py`, `W(i)` in `index.html`).

| # | window (s) | lines | scene | on-screen text |
|---|------------|-------|-------|----------------|
| 01 HOOK | 0–4.15 | 01 | Phone frame with an abstract shop page (no brand). A cursor glides in and taps the jacket card (ring + tap). The phone slides down and fades; the jacket card is left floating. Logo watermark at the top | `شفت` (eye icon) · `فلّيت` (hand icon) |
| 02 FOLLOW | 4.15–10.82 | 02 | The floating card hops on "الجاكيت", then three feed phones slide in from the right (RTL order). The card flies into the first feed; the same card pops into the second and third; on the third it drifts toward the viewer | `Instagram` · `YouTube` · `بكل مكان` |
| 03 FREEZE | 9.16–10.82 | 03 | The feeds dim and blur; the question rises; `لأ.` stamps in orange. The music stops dead on "لأ" | `صدفة؟` · `لأ.` |
| 04 TERM | 10.82–15.25 | 04–05 | Caret, then `Retargeting` lands letter by letter. A person icon and a small jacket card: a dotted arc goes out to the shop, an orange arc draws back to the same person with an arrowhead. The definition rises word by word | `Retargeting` · `توصل مرة تانية للي شافوك…` / `وما اشتروا` |
| 05 SHOP | 15.25–24.17 | 06–07 | Line-drawn shop (awning, window with a rail, door) draws on; the jacket hangs on the rail. A person walks in (door bell), tries the jacket in the window, walks out. Chips land as spoken. An orange salesperson appears in the doorway; the person passes by again and a speech bubble pops from the shop; the jacket glows | `فات ✓` · `جرّب ✓` · `اشترى ✗` · bubble: `بعدها القطعة ناطرتك` |
| 06 PIXEL | 24.17–30.37 | 08 | A browser window rises. The orange salesperson shrinks into the Pixel dot in the page corner. A cursor taps the product page (dot pulses + blip), a dashed orange line drops to the memory panel, then the cursor taps the cart button and the page switches to the cart (dot pulses) | `PIXEL = البيّاع` · list: `فات ✓` · `صفحة الجاكيت ✓` |
| 07 WARM | 30.37–35.13 | 09 | Two small shops. Left: grey stranger with a long dotted path. Right: orange person with a short path | `ما بيعرفك` · `بيعرفك` · `مش من الصفر` |
| 08 DON'T REPEAT | 35.13–39.07 | 10 | The same jacket ad is dealt five times like a deck (card flicks), each one more faded. The sleepy face appears on "بيزهق" and the deck slides away | `نفس الإعلان كل يوم = 😴` (sleepy face drawn as a line icon) |
| 09 THE RULES | 39.07–47.08 | 11–12 | Three rows build down, icon on the right (RTL), mini ad thumbnail on the left. Eye → "show it again" (thumbnail flashes). Cart → "remind" (Pixel dot on the thumbnail). Check → on "وقّف" the row turns **gold** and the thumbnail fades out (positive click) | `شاف المنتج ← فرجيه ياه مرة تانية` · `حطّو بالسلة ← ذكّرو` · `اشترى ← وقّف الإعلان` |
| 10 LINE | 47.08–53.28 | 13 | Calm type beat, whole words rising, slow push-in, music thins out. `فات وفلّ.` lands in orange | `مش كل إعلان لازم يحكي مع ناس جداد.` · `أقرب زبون… هوي اللي فات وفلّ.` |
| 11 CTA | 53.28–58.58 | 14 | Large orange comment bubble with `PIXEL` and the Pixel dot pulsing beside it; the prompt, a bobbing down arrow, then the promise | `اكتب PIXEL 👇` (arrow drawn as a line icon) · `ومنقلّك كيف تتأكد` |
| 12 END CARD | 58.58–61.58 | — | The supplied logo fades in 0.97 → 1 with the Reignite chime. No text | (logo only) |

Notes
- Emoji (👀 👋 ✓ ✗ 🛒 👁 😴 👇 ←) are drawn as line icons in brand colours. Alexandria has no emoji, and a fallback
  emoji font would look different from scene to scene (brief §4 allows this).
- Gold appears once: the "bought" row in scene 09.
- Muted grey `#6E6A64` (the stranger in scene 07) is the same neutral the earlier episodes use for "inactive".
- `Instagram` / `YouTube` appear only as plain words in Alexandria: no logos, icons or platform colours.
- Multi-line layouts: the scene 04 definition, the scene 09 rules (condition on line one, `←` + action on line two)
  and the scene 10 lines are broken across rows to fit 1080px. The strings themselves match the brief.
