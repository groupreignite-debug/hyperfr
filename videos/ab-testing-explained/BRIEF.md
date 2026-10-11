# Reel brief: A/B Testing, stop guessing which ad is better (شو يعني؟)

**Hand this whole file to Claude Code.** It is written so a fresh session can build the reel with no other context.

| | |
|---|---|
| Post date | Sat Oct 31, 2026, @reignitegroup |
| Series | **شو يعني؟** (What does it mean?). Same series as Incrementality, Vanity Metrics, SEO, Sales Funnel and Retargeting. |
| Length | ~60s of VO (the raw takes are 64–66s; speed the chosen one up ~1.07× without changing pitch) + 3s end card |
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
- The full script below has already been generated as **3 takes** on ElevenLabs flow `zhPIN6mX7STxlNgjxbbw`.
- They are saved as `/mnt/project-files/content/reel-09-vo/abtest-vo-take1.mp3` … `take3.mp3`. Salem picks the take.
- The takes run 64–66s, so speed the chosen one up ~1.07× (no pitch change) to land near 60s.

Put the chosen take at `videos/ab-testing-explained/audio/vo/vo_full.mp3`. Get word timings with ElevenLabs transcription (Scribe), as the Incrementality build did, then map scenes and subtitles to them (`scripts/apply_timemap.py` → `scripts/build_audio.py`). The timings below are targets. The real timings come from the audio.

**Pronunciation check:** `A/B Testing` should sound like "A B testing" in English, and `A` and `B` as English letters. If one is badly pronounced in the chosen take, tell Salem. Don't silently re-generate it.

### Script (spoken exactly like this)

| # | ~start | Arabic (spoken = subtitle text) | English meaning (reference only, not on screen) |
|---|---|---|---|
| 01 | 0.0 | عملت إعلان، وما زبط. عملت غيرو، زبط شوي أحسن. بس ليش؟ | You made an ad, it didn't work. You made another, it worked a bit better. But why? |
| 02 | 4.5 | ما بتعرف. لأنك عم تخمّن. | You don't know. Because you're guessing. |
| 03 | 7.0 | الحل اسمو A/B Testing. | The fix is called A/B Testing. |
| 04 | 9.0 | يعني تعمل نسختين من نفس الشي، وتخلّي الناس هنّي يقرروا مين الأحسن. | You make two versions of the same thing and let people decide which is better. |
| 05 | 14.0 | تخيّل عندك محل عصير، وبدك توزّع أوراق إعلان بالشارع. | Imagine you have a juice shop and want to hand out flyers in the street. |
| 06 | 17.5 | ورقة A مكتوب عليها: "عصير طازة". وورقة B: "برتقال معصور قدّامك". | Flyer A says "Fresh juice". Flyer B says "Oranges squeezed in front of you". |
| 07 | 22.0 | بتعطي A لنص الناس، وB للنص التاني، وبتعدّ مين جاب أي ورقة عالمحل. | You give A to half the people and B to the other half, and count who brings which flyer to the shop. |
| 08 | 27.5 | هيك ما عم تخمّن. الأرقام عم تحكي. | That way you're not guessing. The numbers are talking. |
| 09 | 30.0 | بس في قاعدة مهمة: غيّر شي واحد بس. | But there's one important rule: change one thing only. |
| 10 | 32.5 | إذا غيّرت الصورة والعنوان والسعر سوا، وزبط، ما رح تعرف شو اللي زبّطو. | If you change the image, headline and price together and it works, you won't know what made it work. |
| 11 | 37.5 | وما تحكم من أول يوم. عطي التجربة وقت، وخلّي عدد كافي من الناس يشوفوها. | And don't judge on day one. Give the test time and let enough people see it. |
| 12 | 42.5 | وبالإعلانات؟ نفس الفكرة. نفس الإعلان، صورتين مختلفتين، ونفس الجمهور. | In ads? Same idea. Same ad, two different images, same audience. |
| 13 | 47.5 | الإعلان الربحان مش اللي عجبك إنت. هوي اللي الأرقام قالت إنو ربحان. | The winning ad isn't the one you liked. It's the one the numbers say won. |
| 14 | 52.5 | لو بدك تجرّب شي واحد بإعلانك، شو بتختار: الصورة، العنوان، ولا العرض؟ اكتبلنا بالكومنتات. | If you could test one thing in your ad, what would you pick: the image, the headline or the offer? Tell us in the comments. |

---

## 3. Look

Same visual system as the earlier episodes, so the series looks consistent:

- **Palette:** charcoal `#1A1A1A` dominant background, orange `#FF4D1A` for meaning, off-white `#F5F1EA` for text. Gold `#FFB000` appears at most twice; use it for the winner moment in scene 12. No other colors.
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
  - They are introduced in scene 05.
  - They are handed out in scene 06.
  - They are counted in scene 07.
  - They turn into two ad cards in scene 11, the same layout as a social ad but generic.
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
  - It appears as a small watermark at the top in scene 01 and full-size on the end card.

---

## 4. Storyboard

| # | Lines | Scene | On-screen text (exact) |
|---|---|---|---|
| 01 HOOK | 01 | An ad card appears with a ✗. A second ad card replaces it with a small ↗. Then both freeze, and a big question mark lands between them. The logo watermark sits small at the top. | `✗` · `↗` · `؟` |
| 02 GUESSING | 02 | A blindfolded dartboard idea, line-drawn only: a dart flies and misses the board. | `🎯 تخمين` |
| 03 TERM | 03–04 | `A/B Testing` lands huge. The screen splits: an `A` card slides in on the right and a `B` card on the left. Small person icons drop into a crowd under them, and a check mark appears above one card. | `A/B Testing` · `A` · `B` · `👥 ← ✓` |
| 04 SHOP | 05 | A line-drawn juice shop front (awning, a juicer, oranges) draws itself on a street line. A stack of flyers sits on the counter. | `🍊` |
| 05 THE FLYERS | 06 | Two flyers fly out of the stack and land side by side, big. Flyer A (off-white outline) says `عصير طازة`. Flyer B (solid orange) says `برتقال معصور قدّامك` with a small orange illustration. | `A` · `عصير طازة` · `B` · `برتقال معصور قدّامك` |
| 06 SPLIT | 07 (first half) | A crowd of identical person icons walks down the street. A line splits the crowd in half. The right half receives A flyers and the left half receives B flyers. | `½ A` · `½ B` |
| 07 COUNT | 07 (second half) | Person icons walk into the shop holding their flyers. Behind the counter two piles grow: an A pile and a B pile. The B pile grows visibly taller. **No numbers.** | `A` · `B` · `📊` |
| 08 NUMBERS TALK | 08 | **Full spoken line shown big in the center; the bottom subtitle is hidden.** The second half `الأرقام عم تحكي` is in orange. | `هيك ما عم تخمّن. الأرقام عم تحكي.` (subtitle hidden) |
| 09 ONE THING | 09–10 | The rule card stamps in: `1`. Then an ad card shows three parts labeled image, headline and price. All three swap at once (fast blur), a check mark appears, and three question marks pop over the three parts. Then the card resets and only the image swaps, and a single clear arrow points at it. | `1` · `صورة` · `عنوان` · `سعر` · `؟ ؟ ؟` → `✓ صورة` |
| 10 TIME | 11 | A calendar shows day 1 with a small "stop" hand ✋ over it. The pages flip forward a few days while the crowd of person icons grows behind it. | `✋ يوم ١` · `⏳` · `👥👥👥` |
| 11 IN ADS | 12 | The two flyers morph into two generic social ad cards with the same headline and different images (both simple illustrations: one a cup, one an orange). The same audience icon group sits under both. | `نفس الإعلان` · `صورتين` · `نفس الجمهور` |
| 12 THE WINNER | 13 | A small heart icon (you liked it) sits over card A. Then a bar rises under card B and B gets a **gold** outline and a crown/check mark. The heart fades. | `❤️ إنت` · `📊 الأرقام` · `✓` |
| 13 CTA | 14 | A large comment bubble with three chips to pick from. | `الصورة` · `العنوان` · `العرض` · `👇` |
| 14 END CARD | none | The logo fades in with a 0.97→1 scale on charcoal, with the Reignite chime. About 3s. No extra text. | (logo only) |

If an emoji doesn't render in the brand font, replace it with a simple line icon in the same style. Don't use a fallback emoji font that looks different from scene to scene.

---

## 5. Audio

- **VO:** the chosen Fadi take is the loudest element. Normalize the full mix to about −14 LUFS integrated.
- **Music:** the same dark minimal electronic bed as the earlier episodes, ducked well under the VO.
- **SFX (keep them subtle):**
  - a dull buzz for the ✗ (scene 01)
  - a dart whoosh and a miss (scene 02)
  - paper flutter for the flyers (scenes 05–06)
  - a shop door bell when the first icons walk in (scene 07)
  - soft paper stacking ticks as the piles grow (scene 07)
  - a rubber-stamp thump for `1` (scene 09)
  - calendar page flips (scene 10)
  - a soft positive chime when B wins (scene 12)
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
عملت إعلان وما زبط؟ ولا بتعرف ليش التاني زبط؟ 🤔

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

- [ ] Chosen Fadi take in place; timings mapped from the audio (Scribe)
- [ ] Composition is **1080×1920 at 30fps**
- [ ] Every on-screen string matches section 4 exactly, with Arabic shaped correctly in RTL
- [ ] Arabic subtitles synced, only the listed key terms in English and orange, inside the safe area
- [ ] No sentence appears twice on screen (subtitle hidden in scene 08; elsewhere the center shows labels only)
- [ ] A = off-white outline, B = solid orange, consistent in every scene
- [ ] Only brand colors; no numbers on the counters; no real brands, platform logos, people or screenshots; logo untouched
- [ ] `npm run check` passes in the composition folder
- [ ] Rendered `ab-testing-explained.mp4` (1080×1920, 30fps) + `cover.png`
- [ ] Committed to a new branch in hyperfr; ask Salem before opening a PR
