# Reel brief: A/B Testing, stop guessing which ad is better (شو يعني؟)

**Hand this whole file to Claude Code.** It is written so a fresh session can build the reel with no other context.

| | |
|---|---|
| Post date | Sat Oct 31, 2026, @reignitegroup |
| Series | **شو يعني؟** (What does it mean?). Same series as Incrementality, Vanity Metrics, SEO, Sales Funnel and Retargeting. |
| Length | ~48s of VO + 3s end card (v2, Oct 14: shorter script with a new hook) |
| Format | **1080×1920, 30fps**, MP4 H.264 (Instagram Reels) |
| Language | Lebanese Arabic, conversational. **Arabic subtitles** burned in; only key terms in English (Latin letters). |
| Tool | **hyperfr** repo (`groupreignite-debug/hyperfr`), **HyperFrames**. Start at `/hyperframes`, then use the `/faceless-explainer` workflow with the supplied VO, verbatim (do not rewrite or regenerate the script). Read the repo's `CLAUDE.md` first. |
| Reference build | The Incrementality reel: branch `ccr-65fff1ea-12hlnt`, folder `videos/incrementality-explained/`. **Copy its look, fonts, audio pipeline and logo handling.** Read its `BRIEF.md`, `SCRIPT.md` and `STORYBOARD.md` first. If other شو يعني؟ reels (`videos/sales-funnel-explained/`, `videos/retargeting-explained/`, `videos/seo-explained/`) exist by then, match them too. |
| New folder | `videos/ab-testing-explained/` on a new branch |

---

## 1. Goal

Teach one idea simply: **don't guess which ad works. Make two versions, change one thing, and let real people decide.**

The juice-shop flyer example makes the idea obvious. The viewer should leave knowing the two rules people break most:
- change only one thing at a time
- don't judge on day one

The CTA asks what they would test first. This also pays off the Sun Oct 18 "A or B?" image post.

It should teach, not sell.

**Honesty rules:**
- No statistics, uplift percentages, "X% more clicks" claims or results from any real test.
- The shop is a generic example: no real juice brand, logo or photo.
- The visit counters in scene 07 are **an illustration with no numbers**: two bars or two piles of flyers, one visibly taller. Don't show figures and don't add a `مثال` tag.
- No platform logos (Meta, Instagram, Google).

---

## 2. Voiceover

**Voice: ElevenLabs "Fadi - Lebanese Conversational Voice"** (`oJQlz7pz2yWd7MRmDUXm`, `eleven_multilingual_v2`), the same voice as the other episodes.
- **v2 script (Oct 14).** The new script below has been generated as **3 takes** on ElevenLabs flow `75QgovXYrXfkaqwk48P9`.
- They are saved as `/mnt/project-files/content/reel-09-vo/abtest-v2-take1.mp3` … `abtest-v2-take3.mp3` (47.9s, 48.7s, 48.2s). Salem picks the take.
- **Ignore the old `abtest-vo-take*.mp3` files.** They are the first, longer script.
- No speed-up needed. Don't trim the start: line 01 begins right at 0.0s, and the picture must start with it.

Put the chosen take at `videos/ab-testing-explained/audio/vo/vo_full.mp3`. Get word timings with ElevenLabs transcription (Scribe), as the Incrementality build did, then map scenes and subtitles to them (`scripts/apply_timemap.py` → `scripts/build_audio.py`). The timings below are targets. The real timings come from the audio.

**Pronunciation check:** `A/B Testing` should sound like "A B testing" in English, and `A` and `B` as English letters. If one is badly pronounced in the chosen take, tell Salem. Don't silently re-generate it.

### Script (spoken exactly like this)

| # | ~start | Arabic (spoken = subtitle text) | English meaning (reference only, not on screen) |
|---|---|---|---|
| 01 | 0.0 | واحد من هالإعلانين عم يضيّعلك مصاري… أيّا واحد؟ | One of these two ads is wasting your money… which one? |
| 02 | 2.6 | إذا جاوبت بس من شعورك، عم تخمّن. | If you answered from your gut, you're guessing. |
| 03 | 5.0 | الحل اسمو A/B Testing: نسختين من نفس الإعلان، والناس بيقرروا. | The fix is called A/B Testing: two versions of the same ad, and people decide. |
| 04 | 10.0 | تخيّل محل عصير عم يوزّع أوراق إعلان. | Imagine a juice shop handing out flyers. |
| 05 | 12.5 | ورقة A: "عصير طازة". ورقة B: "برتقال معصور قدّامك". | Flyer A: "Fresh juice". Flyer B: "Oranges squeezed in front of you". |
| 06 | 16.5 | نص الناس بياخدو A، والنص التاني B… وبتعدّ مين جاب أي ورقة عالمحل. | Half the people get A, the other half B… and you count who brings which flyer to the shop. |
| 07 | 22.0 | هيك ما عم تخمّن. الأرقام عم تحكي. | That way you're not guessing. The numbers are talking. |
| 08 | 24.5 | بس في قاعدتين: غيّر شي واحد بس، وإلّا ما رح تعرف شو اللي زبّط. | But there are two rules: change one thing only, or you won't know what worked. |
| 09 | 29.5 | وما تحكم من أول يوم. عطي التجربة وقت. | And don't judge on day one. Give the test time. |
| 10 | 32.5 | الإعلان الربحان مش اللي عجبك إنت. هوّي اللي الأرقام قالت إنو ربحان. | The winning ad isn't the one you liked. It's the one the numbers say won. |
| 11 | 37.5 | لو بدك تجرّب شي واحد: الصورة، العنوان، ولا العرض؟ اكتبلنا بالكومنتات. | If you could test one thing: the image, the headline or the offer? Tell us in the comments. |

---

## 3. Look

Same visual system as the earlier episodes, so the series looks consistent:

- **Palette:** charcoal `#1A1A1A` dominant background, orange `#FF4D1A` for meaning, off-white `#F5F1EA` for text. Gold `#FFB000` appears at most twice; use it for the winner moment in scene 10. No other colors.
- **A and B colors:** the two versions must be told apart without new colors.
  - **A** is an off-white outline card.
  - **B** is a solid orange card.
  - Keep that pairing the same in every scene.
- **Type:** Alexandria (Arabic + Latin, weights 300–900), already in `assets/fonts/` of the reference build.
  - Arabic must be shaped correctly in RTL.
  - Wrap English terms so the word order doesn't flip.
  - Never animate Arabic letter by letter, because it breaks the joins. Animate whole words or lines.
- **Background:** the same barely visible 72px grid with slow drift.
- **Motion:** soft masked rises, line draws, slides and side-by-side splits (`power3.out` / `expo.out`). No glitch, fire FX, flashy transitions, stock footage, real people, real screenshots or AI imagery.
- **One world:** the **two flyers, A and B**, are the recurring objects.
  - They first appear as two ad cards in the hook (scene 01), the same layout as a social ad but generic.
  - They become flyers in scene 05, are handed out and counted in scene 06.
  - They turn back into ad cards in scene 10.
  - The screen splits vertically for every A-vs-B moment: A on the right and B on the left, which is natural reading order in RTL.
- **One text layer rule (Salem, Oct 11): never show the same sentence twice.**
  - The bottom subtitles carry every spoken sentence.
  - The center graphics never repeat that sentence. They show visuals plus short labels only: a letter, a term, 1–3 words.
  - When a scene shows a full spoken line big in the center (marked "subtitle hidden" below), **hide the bottom subtitle for that line**, so the text appears only once.
  - The flyer texts in scene 05 are props inside the picture, not a repeated sentence, so the subtitle stays on there.
- **Subtitles: Arabic**, exactly the spoken line.
  - RTL, in the bottom safe area, off-white on a subtle charcoal pill.
  - One line at a time, synced to the VO.
  - **Only these key terms are written in English (Latin letters) and highlighted in orange:** `A/B Testing`, `A`, `B`. Everything else stays Arabic.
  - No English translation track.
  - Keep subtitles clear of the Instagram UI: above the bottom ~300px and away from the right-edge icons.
- **Logo:** the official Reignite Group logo, used exactly as supplied: no redraw, recolor, crop or a different flame.
  - Copy it from `videos/incrementality-explained/assets/reignite/reignite-group-logo.png` (branch `ccr-65fff1ea-12hlnt`).
  - It appears only full-size on the end card. No watermark in the opening.

### Hook rules (first 2 seconds, Salem, Oct 14)

Instagram retention on our reels drops 50-65% in the first 3 seconds, then stays flat. So:
- **Frame 0 is already full.** The hook visual is on screen at the first frame, with movement inside the first 0.3s. Nothing builds up from empty, and there's no fade-in from black.
- **The twist is on screen inside 1.5 seconds.** A big 1-3 word label in the center, while the bottom subtitle carries the spoken line (the one-text-layer rule still holds).
- **No logo in the opening.** The logo appears only on the end card. That keeps the first seconds from reading as an ad.

---

## 4. Storyboard

| # | Lines | Scene | On-screen text (exact) |
|---|---|---|---|
| 01 HOOK | 01 | **Frame 0 (no build-up, no fade-in):** two generic ad cards are already on screen side by side, filling the frame: A (off-white outline) on the right, B (solid orange) on the left. Coins are already pouring down out of the frame from under them, and you can't tell which card they come from. In the first 0.3s both cards wobble. At about 1s `؟` lands big between them with a short shake, and the two letters pulse. | `A` · `B` · `💸` · `؟` |
| 02 GUT | 02 | A heart icon (your gut) points at card A. A dart flies at A and misses, landing beside it. | `❤️ شعورك` · `🎯 تخمين` |
| 03 TERM | 03 | `A/B Testing` lands huge above the two cards. Small person icons drop into a crowd under both, and a check mark appears above one card. | `A/B Testing` · `👥` · `✓` |
| 04 SHOP | 04 | The cards fly off. A line-drawn juice shop front (awning, a juicer, oranges) draws itself on a street line. A stack of flyers sits on the counter. | `🍊` |
| 05 THE FLYERS | 05 | Two flyers fly out of the stack and land side by side, big. Flyer A (off-white outline) says `عصير طازة`. Flyer B (solid orange) says `برتقال معصور قدّامك` with a small orange illustration. | `A` · `عصير طازة` · `B` · `برتقال معصور قدّامك` |
| 06 SPLIT & COUNT | 06 | A crowd of identical person icons walks down the street; a line splits it in half, the right half gets A flyers and the left half B. Then icons walk into the shop holding their flyers, and two piles grow behind the counter. The B pile grows visibly taller. **No numbers.** | `½ A` · `½ B` · `📊` |
| 07 NUMBERS TALK | 07 | **Full spoken line shown big in the center; the bottom subtitle is hidden.** The second half `الأرقام عم تحكي` is in orange. | `هيك ما عم تخمّن. الأرقام عم تحكي.` (subtitle hidden) |
| 08 ONE THING | 08 | The rule card stamps in: `1`. An ad card shows three parts labeled image, headline and price. All three swap at once (fast blur) and three question marks pop. Then the card resets, only the image swaps, and one clear check lands on it. | `1` · `صورة` · `عنوان` · `سعر` · `؟ ؟ ؟` → `✓ صورة` |
| 09 TIME | 09 | A calendar on day 1 with a "stop" hand over it. The pages flip forward a few days while the crowd behind it grows. | `✋ يوم ١` · `⏳` · `👥👥👥` |
| 10 THE WINNER | 10 | The flyers turn back into the two ad cards. A small heart (you liked it) sits over A. Then a bar rises under B and B gets a **gold** outline and a check mark. The heart fades. | `❤️ إنت` · `📊 الأرقام` · `✓` |
| 11 CTA | 11 | A large comment bubble with three chips to pick from. | `الصورة` · `العنوان` · `العرض` · `👇` |
| 12 END CARD | none | The logo fades in with a 0.97→1 scale on charcoal, with the Reignite chime. About 3s. No extra text. | (logo only) |

If an emoji doesn't render in the brand font, replace it with a simple line icon in the same style. Don't use a fallback emoji font that looks different from scene to scene.

---

## 5. Audio

- **VO:** the chosen Fadi take is the loudest element. Normalize the full mix to about −14 LUFS integrated.
- **Music:** the same dark minimal electronic bed as the earlier episodes, ducked well under the VO. It starts at frame 0, with no fade-in.
- **SFX (keep them subtle):**
  - coins clinking from frame 0 and a dry thud when `؟` lands (scene 01). The first sound is at frame 0
  - a dart whoosh and a miss (scene 02)
  - paper flutter for the flyers (scenes 05–06)
  - a shop door bell when the first icons walk in, and soft paper stacking ticks as the piles grow (scene 06)
  - a rubber-stamp thump for `1` (scene 08)
  - calendar page flips (scene 09)
  - a soft positive chime when B wins (scene 10)
  - the Reignite chime on the end card
- Salem may add a trending sound inside Instagram, so keep the music low enough that this still works.

---

## 6. Cover (thumbnail frame)

Use the same template as every episode:
- charcoal background
- small `شو يعني؟` at the top in orange
- `A/B Testing` huge in off-white
- `إعلانين… مين الأحسن؟` beneath it
- a small A card and B card beside the text
- the logo small at the bottom

Keep all text inside the center 1080×1350 so it survives the grid crop. Export as `cover.png`.

---

## 7. Instagram caption

```
واحد من إعلاناتك عم يضيّعلك مصاري… بتعرف أيّا واحد؟ 🤔

ما تخمّن. هيدا اسمو A/B Testing:
نسختين من نفس الإعلان، والناس بيقرروا مين الأحسن.

قاعدتين:
١. غيّر شي واحد بس
٢. ما تحكم من أول يوم

الإعلان الربحان مش اللي عجبك إنت، هوي اللي الأرقام قالت إنو ربحان.

شو يعني؟ | الحلقات اللي قبل 👈 عالبروفايل

لو بدك تجرّب شي واحد بإعلانك: الصورة، العنوان، ولا العرض؟ اكتبلنا 👇

#تسويق #تسويق_رقمي #إعلانات #إعلانات_ممولة #بزنس #ريادة_الأعمال #لبنان #دبي #الإمارات #DigitalMarketing #ABTesting #MarketingTips #SmallBusiness #ReigniteGroup
```

**For the comments:** reply to each pick with one concrete idea for testing it.
- Image: a product photo vs a photo of the product being used.
- Headline: the benefit vs the problem.
- Offer: a discount vs a free extra.

Don't pitch services in the replies.

---

## 8. Done checklist for Claude Code

- [ ] Chosen **v2** Fadi take (`abtest-v2-take*.mp3`) in place; timings mapped from the audio (Scribe)
- [ ] Composition is **1080×1920 at 30fps**
- [ ] Every on-screen string matches section 4 exactly, with Arabic shaped correctly in RTL
- [ ] Arabic subtitles synced, only the listed key terms in English and orange, inside the safe area
- [ ] No sentence appears twice on screen (subtitle hidden in scene 07; elsewhere the center shows labels only)
- [ ] Hook: frame 0 already shows both ad cards and the falling coins (no empty or black first frame); `؟` on screen by about 1s; no logo before the end card
- [ ] A = off-white outline, B = solid orange, consistent in every scene
- [ ] Only brand colors; no numbers on the counters; no real brands, platform logos, people or screenshots; logo untouched
- [ ] `npm run check` passes in the composition folder
- [ ] Rendered `ab-testing-explained.mp4` (1080×1920, 30fps) + `cover.png`
- [ ] Committed to a new branch in hyperfr; ask Salem before opening a PR
