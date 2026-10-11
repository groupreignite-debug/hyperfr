---
format: 1080x1920
fps: 30
duration: 65.1
music: dark minimal electronic bed (procedural, scripts/build_audio.py), same palette as the earlier episodes
captions: Arabic, burned in, one line at a time, key terms (A/B Testing, A, B) in orange Latin
---

# STORYBOARD: A/B Testing (شو يعني؟)

Same world as the earlier episodes: charcoal canvas, barely visible 72px grid drifting slowly, Alexandria 300–900,
orange for meaning, a progress hairline at the top. **The two versions** are told apart without new colours:
**A = off-white outline card, B = solid orange card**, A always on the right and B on the left (RTL reading order).
**One world:** the two flyers are the recurring objects: introduced on the counter (04), they fly out big (05), are
handed out as mini flyers (06), come back as two piles (07), and turn into two generic social ad cards (11–12).
The juice shop is a generic line drawing (awning, blank sign with an orange icon, counter, juicer, oranges, door) with
no name, logo or photo. Every scene window and reveal is keyed to a Scribe word time (`scripts/apply_cues.py`,
`W(i)` in `index.html`).

| # | window (s) | lines | scene | on-screen text |
|---|------------|-------|-------|----------------|
| 01 HOOK | 0–4.70 | 01 | A neutral ad card rises; a ✗ stamps on it (buzz). A second card replaces it while the first slides right and dims; a small ↗ pops on the new one. Both freeze side by side and a big orange `؟` lands between them. Logo watermark small at the top | `✗` · `↗` · `؟` (drawn icons) |
| 02 GUESSING | 4.70–6.64 | 02 | Line-drawn dartboard and a thrower whose head has an orange blindfold. A dart flies and misses the board (lands off it, wobbles) | target icon `تخمين` |
| 03 TERM | 6.64–13.82 | 03–04 | `A/B Testing` lands huge. A dashed line splits the screen; the `A` card slides in on the right, the `B` card on the left. Nine person icons drop into a crowd under them; a check mark pops above B | `A/B Testing` · `A` · `B` · people → ✓ chip |
| 04 SHOP | 13.82–17.55 | 05 | The juice shop draws itself on a street line; juicer and oranges on the counter; a stack of A/B flyers lands on it | orange icon |
| 05 THE FLYERS | 17.55–23.48 | 06 | Two flyers fly out of the stack (paper flutter) and land side by side, big. A (outline): `عصير طازة`. B (solid orange): small orange illustration and `برتقال معصور قدّامك` | `A` · `عصير طازة` · `B` · `برتقال معصور قدّامك` |
| 06 SPLIT | 23.48–26.13 | 07 (first half) | Ten identical person icons walk in on the street. An orange dashed line splits them; the right half receives A mini flyers, the left half B mini flyers | `½ A` · `½ B` |
| 07 COUNT | 26.13–28.11 | 07 (second half) | The shop again: people walk in through the door holding their flyers (door bell). Two piles grow on the counter (paper ticks); the B pile ends visibly taller. **No numbers** | `A` · `B` · chart icon |
| 08 NUMBERS TALK | 28.11–30.64 | 08 | The full line, big in the centre, word by word; the second sentence in orange (**subtitle hidden**) | `هيك ما عم تخمّن.` / `الأرقام عم تحكي.` |
| 09 ONE THING | 30.64–37.97 | 09–10 | The `1` rule card stamps in (thump), then moves up. An ad card with three parts (image, headline, price tag) appears, each labelled as spoken. All three swap at once with a fast blur, a check mark pops, then three `؟` pop over the parts. Reset: only the image swaps; the `صورة` label lights up with a check, the others dim | `1` · `صورة` · `عنوان` · `سعر` · `؟ ؟ ؟` → `✓ صورة` |
| 10 TIME | 37.97–42.46 | 11 | A calendar on day 1 (one dot) with a stop hand over it. The hand goes, pages flip forward (dots, no numbers, flip sounds) while three rows of person icons grow below | hand `يوم ١` · hourglass · three person icons |
| 11 IN ADS | 42.46–48.62 | 12 | The two flyers return and morph into two generic social ad cards: same layout and headline bars, different images (A: a cup, B: an orange). One audience group sits under both | `نفس الإعلان` · image icon `صورتين` · people icon `نفس الجمهور` |
| 12 THE WINNER | 48.62–53.87 | 13 | A heart badge (you liked it) sits on card A. Then bars rise under the cards: B's clearly taller, no numbers. B gets the **gold** outline and a gold check; the heart and A fade | heart `إنت` · chart `الأرقام` · `✓` |
| 13 CTA | 53.87–62.10 | 14 | A large orange comment bubble with three chips that light up as they're named; a bobbing down arrow | `الصورة` · `العنوان` · `العرض` · down arrow |
| 14 END CARD | 62.10–65.10 | — | The supplied logo fades in 0.97 → 1 with the Reignite chime. No text | (logo only) |

Notes
- **One text layer:** the bottom subtitles carry every spoken sentence; the centre shows only visuals and short labels.
  Scene 08 shows its full line big in the centre, so its subtitle is not shown. The flyer texts in scene 05 are props.
- Emoji (🎯 🍊 👥 📊 ✋ ⏳ ❤️ 👇) and ✗ ↗ ✓ ← are drawn as line icons in brand colours. Alexandria has none of them, and a
  fallback emoji font would look different from scene to scene (brief §4 allows this).
- Gold is used once: the winner moment in scene 12 (outline + check).
- The piles (07) and bars (12) are illustrations with no figures and no `مثال` tag, as the brief asks.
