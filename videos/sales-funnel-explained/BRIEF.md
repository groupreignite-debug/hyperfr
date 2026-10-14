# Reel brief: Sales Funnel, why nobody buys the first time (شو يعني؟)

**Hand this whole file to Claude Code.** It is written so a fresh session can build the reel with no other context.

| | |
|---|---|
| Post date | Sat Oct 17, 2026, @reignitegroup |
| Series | **شو يعني؟** (What does it mean?). Same series as Incrementality, Vanity Metrics, SEO and Retargeting. |
| Length | ~55–60s of VO + 3s end card |
| Format | **1080×1920, 30fps**, MP4 H.264 (Instagram Reels) |
| Language | Lebanese Arabic, conversational. **Arabic subtitles** burned in; only key terms in English (Latin letters). |
| Tool | **hyperfr** repo (`groupreignite-debug/hyperfr`), **HyperFrames**. Start at `/hyperframes`, then use the `/faceless-explainer` workflow with the supplied VO, verbatim (do not rewrite or regenerate the script). Read the repo's `CLAUDE.md` first. |
| Reference build | The Incrementality reel: branch `ccr-65fff1ea-12hlnt`, folder `videos/incrementality-explained/`. **Copy its look, fonts, audio pipeline and logo handling.** Read its `BRIEF.md`, `SCRIPT.md` and `STORYBOARD.md` first. If other شو يعني؟ reels (`videos/vanity-metrics/`, `videos/seo-explained/`, `videos/retargeting-explained/`) exist by then, match them too. |
| New folder | `videos/sales-funnel-explained/` on a new branch |

---

## 1. Goal

Teach one idea simply: **people don't buy from someone they don't know yet. They walk a path, and each step needs a different message.** The café example makes the four stages feel obvious. The viewer should leave knowing the classic mistake (asking for the sale on the first contact) and asking themselves which stage they lose people at. That question is the comment CTA.

It should teach, not sell. This episode also sets up the Retargeting episode on Nov 7 (bringing back people who dropped out of the funnel), so keep the funnel shape and colors reusable.

**Honesty rules:**
- No statistics, conversion rates, percentages or "most businesses…" claims.
- The café is a generic example: no real café name, logo, cup branding or photo.
- The funnel shows **no numbers**. Its narrowing is a shape, not data.

---

## 2. Voiceover

**Voice: ElevenLabs "Fadi - Lebanese Conversational Voice"** (`oJQlz7pz2yWd7MRmDUXm`, `eleven_multilingual_v2`), the same as the SEO and Retargeting reels. The full script below has already been generated as **3 takes** on ElevenLabs flow `b2xrMxWciA7lUhILktXK`, saved as `/mnt/project-files/content/reel-08-vo/funnel-vo-take1.mp3` … `take3.mp3`. Salem picks the take. If it feels slow, speed it up slightly (~1.05×) without changing pitch.

Put the chosen take at `videos/sales-funnel-explained/audio/vo/vo_full.mp3`. Get word timings with ElevenLabs transcription (Scribe), as the Incrementality build did, and map scenes and subtitles to them (`scripts/apply_timemap.py` → `scripts/build_audio.py`). Timings below are targets. The real timings come from the audio.

**Pronunciation check:** `Sales Funnel`, `Awareness`, `Consideration`, `Decision` and `Loyalty` should sound English. If one is badly pronounced in the chosen take, tell Salem. Don't silently re-generate it.

### Script (spoken exactly like this)

| # | ~start | Arabic (spoken = subtitle text) | English meaning (reference only, not on screen) |
|---|---|---|---|
| 01 | 0.0 | ليش ما حدا بيشتري منك من أول مرة بيشوفك؟ | Why does nobody buy from you the first time they see you? |
| 02 | 3.0 | لأن الناس ما بيشتروا من حدا ما بيعرفوه. | Because people don't buy from someone they don't know. |
| 03 | 6.0 | هيدا اسمو Sales Funnel. | This is called a Sales Funnel. |
| 04 | 8.0 | يعني الطريق اللي بيمشيه الزبون، من أول مرة بيسمع فيك، لحد ما يشتري. | It's the path a customer walks, from the first time they hear of you until they buy. |
| 05 | 13.0 | تخيّل في قهوة جديدة بحيّك. | Imagine there's a new café in your neighborhood. |
| 06 | 15.5 | أول مرة بتمرق قدّامها، بس بتلاحظها. هيدي الـ Awareness. | The first time you pass by, you just notice it. That's Awareness. |
| 07 | 20.0 | بعدين بتشمّ الريحة، بتشوف الناس قاعدين، بتقرا الريفيوز. هيدا الـ Consideration. | Then you smell the coffee, see people sitting there, read the reviews. That's Consideration. |
| 08 | 26.0 | وبيوم، بتفوت وبتطلب أول فنجان. هيدا الـ Decision. | One day you walk in and order your first cup. That's Decision. |
| 09 | 30.0 | وإذا عجبتك؟ بترجع كل يوم، وبتخبّر رفقاتك. هيدي الـ Loyalty. | And if you liked it? You come back every day and tell your friends. That's Loyalty. |
| 10 | 35.0 | الغلطة؟ إنك تطلب من حدا يشتري، وهوي بعدو أول مرة عم يشوفك. | The mistake? Asking someone to buy when it's the first time they've seen you. |
| 11 | 40.0 | كل مرحلة إلها رسالة. للي ما بيعرفك، علّمو شي. للي عم يفكّر، فرجيه ليش إنت. وللي جاهز، سهّلّو يشتري. | Each stage has its message. To someone who doesn't know you, teach them something. To someone considering, show them why you. To someone ready, make buying easy. |
| 12 | 48.5 | ومش كل الناس بيكمّلوا الطريق، وهيدا طبيعي. | Not everyone finishes the path, and that's normal. |
| 13 | 51.5 | المهم تعرف وين عم تخسرهن. | What matters is knowing where you lose them. |
| 14 | 54.0 | بأي مرحلة عم تخسر زباينك؟ اكتبلنا بالكومنتات. | At which stage are you losing customers? Tell us in the comments. |

---

## 3. Look

Same visual system as the earlier episodes, so the series looks consistent:

- **Palette:** charcoal `#1A1A1A` dominant background, orange `#FF4D1A` for meaning, off-white `#F5F1EA` for text, gold `#FFB000` at most twice (use it for the Loyalty stage). No other colors.
- **Type:** Alexandria (Arabic + Latin, weights 300–900), already in `assets/fonts/` of the reference build. Arabic shaped correctly in RTL; wrap English terms so word order doesn't flip. Never animate Arabic letter by letter (it breaks the joins). Animate whole words or lines.
- **Background:** the same barely visible 72px grid with slow drift.
- **Motion:** soft masked rises, line draws, slides (`power3.out` / `expo.out`). No glitch, fire FX, flashy transitions, stock footage, real people, real screenshots or AI imagery.
- **One world:** the **funnel** is the recurring object. It's a clean line-drawn funnel with 4 bands, top to bottom: Awareness, Consideration, Decision, Loyalty. It builds band by band as each stage is named. A small **person icon** (the customer) moves down through it, and a simple line-drawn **café** (awning, door, one cup) supplies the example for each band.
- **One text layer rule (Salem, Oct 11): never show the same sentence twice.**
  - The bottom subtitles carry every spoken sentence.
  - The center graphics never repeat that sentence. They show visuals plus short labels only: the term, a stage name, or 1–3 words.
  - When a scene shows a full spoken line big in the center (marked "subtitle hidden" below), **hide the bottom subtitle for that line**, so the text appears only once.
- **Subtitles: Arabic**, exactly the spoken line, RTL, bottom safe area, off-white on a subtle charcoal pill, one line at a time, synced to the VO.
  - **Only these key terms are written in English (Latin letters) and highlighted in orange:** `Sales Funnel`, `Awareness`, `Consideration`, `Decision`, `Loyalty`. Everything else stays Arabic.
  - There is no English translation track.
  - Keep subtitles clear of the Instagram UI: above the bottom ~300px and away from the right-edge icons.
- **Logo:** the official Reignite Group logo, used exactly as supplied: no redraw, recolor, crop or a different flame. Copy it from `videos/incrementality-explained/assets/reignite/reignite-group-logo.png` (branch `ccr-65fff1ea-12hlnt`). Show it only full-size on the end card. No watermark in the opening.

### Hook rules (first 2 seconds, Salem, Oct 14)

Instagram retention on our reels drops 50-65% in the first 3 seconds, then stays flat. So:
- **Frame 0 is already full.** The hook visual is on screen at the first frame, with movement inside the first 0.3s. Nothing builds up from empty, and there's no fade-in from black.
- **The twist is on screen inside 1.5 seconds, before the voice gets to it.** A big 1-3 word label in the center shows the payoff early, while the bottom subtitle carries the spoken line (the one-text-layer rule still holds). The VO stays as recorded.
- **No logo in the opening.** The logo appears only on the end card. That keeps the first seconds from reading as an ad.

---

## 4. Storyboard

| # | Lines | Scene | On-screen text (exact) |
|---|---|---|---|
| 01 HOOK | 01 | **Frame 0 (no build-up, no fade-in):** a phone fills the center with an ad card reading "اشتري هلق", and a thumb is already swiping it away. Three fast swipes in about 1.5s: each new "اشتري هلق" card gets swiped off, and a small orange `✗` stamps where it was. At about 1.5s, while Fadi is still asking the question, `0 🛒` lands big in orange in the center with a short shake. It stays until line 02 starts. The bottom subtitle shows line 01 as usual. No logo. | `اشتري هلق` (on the ad cards) · `✗` · `0 🛒` |
| 02 STRANGER | 02 | Two person icons. The left one has a question mark over its head, labeled as a stranger. An arrow from the ad bounces off it. | `؟` · `ما بيعرفك` |
| 03 TERM | 03–04 | `Sales Funnel` lands huge. Then an empty funnel outline draws itself under it, and a dotted path runs from the top of the funnel to a small cart icon at the bottom. | `Sales Funnel` · `🧍 ← … ← 🛒` |
| 04 CAFÉ | 05 | The funnel slides to one side (the left in RTL) and stays small. On the other side, a line-drawn café front draws itself on a street line. | `☕` |
| 05 AWARENESS | 06 | The person icon walks past the café and glances at it (a small eye icon pops). The **top band** of the funnel fills in orange and gets its label. | `Awareness` · `👀 لاحظ` |
| 06 CONSIDERATION | 07 | Three quick beats around the café: steam lines rise from a cup, two small seated person icons appear inside, and three stars appear on a small review card (outline stars, no rating number). The **second band** fills. | `Consideration` · `👃 · 👥 · ⭐` |
| 07 DECISION | 08 | The person icon walks through the door. A cup slides across a counter toward it. The **third band** fills. | `Decision` · `☕ أول فنجان` |
| 08 LOYALTY | 09 | A quick loop: the person icon comes back again and again (a 3-day calendar flips), then two friend icons join it. The **bottom band** fills in **gold**. | `Loyalty` · `🔁` · `+👥` |
| 09 THE MISTAKE | 10 | The full funnel is back in the center. A big "اشتري هلق" ad card jumps straight at the top band, hits it and breaks, and an orange ✗ stamps over it. | `✗` · `أول مرة؟` |
| 10 THE MESSAGES | 11 | The strongest beat. Next to each of the top 3 bands, a short message tag slides in as it's spoken: a book icon for teaching, a star for "why you", a cart for "easy to buy". | `📖 علّمو` · `⭐ ليش إنت` · `🛒 سهّلّو` |
| 11 DROP-OFF | 12–13 | A few person icons fall out from the funnel's sides at different bands. That's calm, not dramatic. Then a magnifier glides over the bands and stops, pulsing, on one of them. | `🔍 وين؟` |
| 12 CTA | 14 | A large comment bubble. Inside it are the four stage names as tappable-looking chips. | `Awareness` · `Consideration` · `Decision` · `Loyalty` · `👇` |
| 13 END CARD | none | The logo fades in with a 0.97→1 scale on charcoal, with the Reignite chime. About 3s. No extra text. | (logo only) |

If an emoji doesn't render in the brand font, replace it with a simple line icon in the same style. Don't use a fallback emoji font that looks different from scene to scene.

---

## 5. Audio

- **VO:** the chosen Fadi take, the loudest element. Normalize the full mix to about −14 LUFS integrated.
- **Music:** the same dark minimal electronic bed as the earlier episodes, ducked well under the VO.
- **SFX (subtle):**
  - three quick swipes, one per ad card, with a dry tick on each `✗`, then a low thud when `0 🛒` lands (scene 01). The first swipe sounds at frame 0
  - a light pen-draw sound as the funnel outline draws (scene 03)
  - soft street ambience under the café scenes (05–08), very low
  - a shop door bell on Decision (scene 07)
  - a cup set on the counter (scene 07)
  - a gentle rising "fill" tick each time a funnel band fills
  - a dull thud when the ad hits the funnel (scene 09)
  - three soft pops for the message tags (scene 10)
  - the Reignite chime on the end card
- Salem may add a trending sound inside Instagram, so keep the music low enough that this still works.

---

## 6. Cover (thumbnail frame)

Same template every episode:
- charcoal background
- small `شو يعني؟` at the top in orange
- `Sales Funnel` huge in off-white
- `ليش ما حدا بيشتري من أول مرة؟` beneath it
- the 4-band funnel small beside it
- the logo small at the bottom

Keep all text inside the center 1080×1350 so it survives the grid crop. Export as `cover.png`.

---

## 7. Instagram caption

```
ليش ما حدا بيشتري منك من أول مرة بيشوفك؟ ☕

لأن الزبون بيمشي طريق، وهيدا اسمو Sales Funnel:
١. Awareness: بيلاحظك
٢. Consideration: بيفكّر ويقارن
٣. Decision: بيشتري أول مرة
٤. Loyalty: بيرجع وبيخبّر غيرو

كل مرحلة إلها رسالة. ما تطلب البيعة من حدا بعدو أول مرة عم يشوفك.

شو يعني؟ | الحلقات اللي قبل 👈 عالبروفايل

بأي مرحلة عم تخسر زباينك؟ اكتبلنا بالكومنتات 👇

#تسويق #تسويق_رقمي #مبيعات #بزنس #ريادة_الأعمال #مشاريع_صغيرة #لبنان #دبي #الإمارات #DigitalMarketing #SalesFunnel #MarketingTips #SmallBusiness #ReigniteGroup
```

**For the comments:** reply to each stage answer with one practical tip for that stage, the same tips the reel gives: teach, show why you, make buying easy. Don't pitch services in the replies.

---

## 8. Done checklist for Claude Code

- [ ] Chosen Fadi take in place; timings mapped from the audio (Scribe)
- [ ] Composition is **1080×1920 at 30fps**
- [ ] Every on-screen string matches section 4 exactly, with Arabic shaped correctly in RTL
- [ ] Arabic subtitles synced, only the listed key terms in English and orange, inside the safe area
- [ ] No sentence appears twice on screen (the center shows visuals and short labels only; the subtitles carry the speech)
- [ ] Hook: frame 0 already shows the phone and ad mid-swipe (no empty or black first frame); `0 🛒` is on screen by about 1.5s; no logo before the end card
- [ ] Only brand colors; no real café branding, people or screenshots; no numbers on the funnel; logo untouched
- [ ] `npm run check` passes in the composition folder
- [ ] Rendered `sales-funnel-explained.mp4` (1080×1920, 30fps) + `cover.png`
- [ ] Committed to a new branch in hyperfr; ask Salem before opening a PR
