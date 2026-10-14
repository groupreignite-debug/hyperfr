---
format: 1080x1920
fps: 30
duration: 50.9
music: dark minimal electronic bed (procedural, scripts/build_audio.py), same palette as the earlier episodes; starts at frame 0
captions: Arabic, burned in, one line at a time, key terms (A/B Testing, A, B) in orange Latin
---

# STORYBOARD: A/B Testing v2 (شو يعني؟)

Same world as the earlier episodes: charcoal canvas, barely visible 72px grid drifting slowly, Alexandria 300–900,
orange for meaning, a progress hairline at the top. **The two versions** are told apart without new colours:
**A = off-white outline card, B = solid orange card**, A always on the right and B on the left (RTL reading order).
**One world:** the two versions open as two generic ad cards (01–03), become flyers in the juice shop (04–06), and turn
back into the ad cards for the winner (10). The juice shop is a generic line drawing (awning, blank sign with an orange
icon, counter, juicer, oranges, door) with no name, logo or photo. Every scene window and reveal is keyed to a Scribe
word time (`scripts/apply_cues.py`, `W(i)` in `index.html`).

**Hook rules (Oct 14):** frame 0 already shows both cards, the coin stream and the first subtitle (no build-up, no fade
from black, no logo); the cards wobble inside the first 0.3s; `؟` is on screen at 1.0s. Music and coin clinks start at
frame 0. The logo appears only on the end card.

| # | window (s) | lines | scene | on-screen text |
|---|------------|-------|-------|----------------|
| 01 HOOK | 0–3.49 | 01 | Frame 0: two generic ad cards fill the frame (B left, A right, big letters). Coins already pour down from under them and out of the frame, from both sides, so you can't tell which card loses them; a small banknote chip sits where they start. The cards wobble in the first 0.3s. At 0.95s a big `؟` lands between them with a dry thud and a short shake; the letters pulse, and again on "أيّا واحد؟" | `A` · `B` · banknote icon (💸) · `؟` |
| 02 GUT | 3.49–5.90 | 02 | Coins stop. A heart badge (your gut) bobs over card A. A dart flies at A and misses, landing just off its top-right corner | heart `شعورك` · target `تخمين` |
| 03 TERM | 5.90–11.58 | 03 | The cards step back; `A/B Testing` lands huge above them. Nine person icons drop into a crowd under both, a people chip, and a check mark pops on B. The cards fly off | `A/B Testing` · people icon · `✓` |
| 04 SHOP | 11.58–14.30 | 04 | The juice shop draws itself on a street line; juicer and oranges on the counter; a stack of A/B flyers lands on it | orange icon |
| 05 THE FLYERS | 14.30–19.56 | 05 | Two flyers fly out of the stack (paper flutter) and land side by side, big. A (outline): `عصير طازة`. B (solid orange): small orange illustration and `برتقال معصور قدّامك` | `A` · `عصير طازة` · `B` · `برتقال معصور قدّامك` |
| 06 SPLIT & COUNT | 19.56–25.64 | 06 | Ten identical person icons walk in; an orange dashed line splits them; the right half gets A mini flyers, the left half B. Then the shop again: people walk in through the door holding flyers (door bell) and two piles grow on the counter (paper ticks); B's pile ends visibly taller. **No numbers** | `½ A` · `½ B` · chart icon |
| 07 NUMBERS TALK | 25.64–28.36 | 07 | The full line, big in the centre, word by word; the second sentence in orange (**subtitle hidden**) | `هيك ما عم تخمّن.` / `الأرقام عم تحكي.` |
| 08 ONE THING | 28.36–33.53 | 08 | The `1` rule card stamps in (thump), then moves up. An ad card with three labelled parts (image, headline, price tag). All three swap at once with a fast blur and three `؟` pop. Reset: only the image swaps and one clear check lands on it; the `صورة` label lights up, the others dim | `1` · `صورة` · `عنوان` · `سعر` · `؟ ؟ ؟` → `✓ صورة` |
| 09 TIME | 33.53–36.20 | 09 | A calendar on day 1 (one dot) with a stop hand over it. The hand goes, pages flip forward (dots, no numbers) while three rows of person icons grow | hand `يوم ١` · hourglass · three person icons |
| 10 THE WINNER | 36.20–41.68 | 10 | The flyers come back and turn into the two ad cards (same layout, different images: A a cup, B an orange). A heart badge sits on A. Bars rise under the cards, B's clearly taller, no numbers. B gets the **gold** outline and a gold check; the heart and A fade | heart `إنت` · chart `الأرقام` · `✓` |
| 11 CTA | 41.68–47.88 | 11 | A large orange comment bubble with three chips that light up as they're named; a bobbing down arrow | `الصورة` · `العنوان` · `العرض` · down arrow |
| 12 END CARD | 47.88–50.88 | — | The supplied logo fades in 0.97 → 1 with the Reignite chime. No text | (logo only) |

Notes
- **One text layer:** the bottom subtitles carry every spoken sentence; the centre shows only visuals and short labels.
  Scene 07 shows its full line big in the centre, so its subtitle is not shown. The flyer texts in scene 05 are props.
- Emoji (💸 ❤️ 🎯 👥 🍊 📊 ✋ ⏳ 👇) and ✓ are drawn as line icons in brand colours. Alexandria has none of them, and a
  fallback emoji font would look different from scene to scene (brief §4 allows this).
- Gold is used once: the winner moment in scene 10 (outline + check).
- The coins, piles and bars are illustrations with no figures and no `مثال` tag.
