# Reel brief: Landing page vs Homepage (شو يعني؟)

**Hand this whole file to Claude Code.** It is written so a fresh session can build the reel end to end with no other context and no footage.

| | |
|---|---|
| Post date | Mon Oct 26, 2026, @reignitegroup |
| Series | **شو يعني؟** (What does it mean?) |
| Approach | **Fully animated, no real website footage** (Salem, Oct 13). The example is a **fictional online shoe store** drawn as clean UI mockups. No real brand, page or logo appears. |
| Length | ~60s of VO + 3s end card |
| Format | **1080×1920, 30fps**, MP4 H.264 (Instagram Reels) |
| Language | Lebanese Arabic, conversational. **Arabic subtitles** burned in; only key terms in English (Latin letters). |
| Tool | **hyperfr** repo (`groupreignite-debug/hyperfr`), **HyperFrames**. Read the repo's `CLAUDE.md`, start at `/hyperframes`, then use the `/faceless-explainer` workflow with the supplied VO used verbatim. |
| Reference build | The Incrementality reel: branch `ccr-65fff1ea-12hlnt`, folder `videos/incrementality-explained/`. **Copy its look, fonts, audio pipeline and logo handling.** |
| New folder | `videos/landing-page-explained/` on a new branch |

---

## 1. Goal

Teach one idea: **a homepage is built for everyone, while a landing page is built for one visitor with one goal.** Sending ad traffic to a homepage makes the visitor search for what the ad promised.

**Honesty rules:**
- The shoe store is made up. Don't give it a name that could be a real brand; use a neutral wordmark like `SHOES` drawn in plain type.
- No statistics, conversion rates or results on screen.
- No AI-generated images. The shoe is a simple flat vector drawing in brand colors.

---

## 2. The two mockups (build these in HTML/CSS)

Both pages sit inside the same minimal **phone frame**, drawn in off-white lines on charcoal, centered in the upper-middle of the canvas (about 620px wide). Mobile makes sense because the ad is clicked on Instagram. Leave room above for labels and below for subtitles.

**Mockup A: the Homepage (busy on purpose, but still tidy)**
- Top bar: wordmark `SHOES`, a hamburger menu icon, a search icon, a cart icon.
- Menu that drops down when "opened": `رجالي` · `نسائي` · `أطفال` · `العروض` · `من نحن` · `تواصل معنا` (6 items).
- A hero banner with a generic slogan, then a scrolling page of about 8 sections: category tiles, a product grid of 6 shoes, a "best sellers" row, an offers strip, a blog teaser, a newsletter box, and a long footer of links.
- Buttons and links everywhere: `تسوّق الآن`, `شوف الكل`, `اشترك`, and so on.
- It should look like a normal, decent store homepage. Don't make it ugly; the point is that it serves everyone.

**Mockup B: the Landing Page (one goal)**
- No menu, no search, no footer links. Just the small wordmark.
- One large shoe illustration (the sporty shoe from the ad).
- One headline: `الحذاء الرياضي الجديد` with a short sub-line.
- Three tiny benefit ticks.
- One big orange button: `اطلب هلّق`, repeated once at the bottom.

**The ad:** an Instagram-style ad card showing the same sporty shoe and a `اطلب هلّق` button. It appears in scene 01 and again in scene 05 so the viewer connects the ad to the right page.

The on-screen counters can only count what the mockups actually contain. If you change the mockups, update the counts.

---

## 3. Voiceover

**Voice: ElevenLabs "Fadi - Lebanese Conversational Voice"** (`oJQlz7pz2yWd7MRmDUXm`, `eleven_multilingual_v2`).
- The new script below has been generated as **3 takes** on ElevenLabs flow `SaUIRP89lUAMdXMYARly`.
- The takes are saved as `/mnt/project-files/content/reel-05-vo/landing-v2-take1.mp3` … `take3.mp3`.
- The older `landing-vo-take*.mp3` files talk about Shopify. **Don't use them.**
- Salem picks the take. If it runs over ~60s, speed it up slightly without changing pitch.

Put the chosen take at `videos/landing-page-explained/audio/vo/vo_full.mp3`. Get word timings with ElevenLabs Scribe and map scenes and subtitles to them, as the Incrementality build did. The timings below are targets.

**Pronunciation check:** `Homepage` and `Landing Page` should sound English. Tell Salem if one is wrong. Don't silently re-generate.

### Script (spoken exactly like this)

| # | ~start | Arabic (spoken = subtitle text) | English meaning (reference only) |
|---|---|---|---|
| 01 | 0.0 | عم تدفع عالإعلان… وتبعت الناس عالصفحة الرئيسية؟ | You pay for the ad… and send people to your homepage? |
| 02 | 3.5 | هون عم تضيّع مصاري. | That's where you're losing money. |
| 03 | 5.5 | خلّيني فرجيك مثال: محل أحذية أونلاين. | Let me show you an example: an online shoe store. |
| 04 | 8.5 | هيدي الـ Homepage تبعو. فيها قائمة، وأقسام كتير، وكبسات بكل مكان. | This is its Homepage. A menu, lots of sections, buttons everywhere. |
| 05 | 14.5 | وهيدا طبيعي. الـ Homepage معمولة لكل الناس: اللي بدو رجالي، اللي بدو نسائي، واللي بدو العروض. | And that's normal. A homepage is for everyone: men's, women's, people after the offers. |
| 06 | 22.0 | بس هوّي عامل إعلان على حذاء رياضي واحد. لوين لازم يبعت الناس؟ | But his ad is for one sports shoe. Where should he send people? |
| 07 | 27.0 | على Landing Page. | To a Landing Page. |
| 08 | 29.0 | ما في قائمة. صورة الحذاء، عنوان واحد، وكبسة وحدة: اطلب هلّق. | No menu. The shoe photo, one headline, one button: order now. |
| 09 | 35.0 | ليش؟ لأن الزائر جايي لسبب واحد، والصفحة لازم تحكي عن هيدا السبب بس. | Why? The visitor came for one reason, and the page should only talk about that. |
| 10 | 41.0 | تخيّل تعزم حدا على العشا، وتقلّو: تعا عالحي، ودوّر عالبيت لحالك. | Imagine inviting someone to dinner and saying: come to the neighborhood and find the house yourself. |
| 11 | 46.5 | الـ Landing Page هيي إنك تفتحلو الباب، والطاولة جاهزة. | A Landing Page is opening the door, with the table ready. |
| 12 | 51.0 | القاعدة بسيطة: إعلان واحد، صفحة وحدة، هدف واحد. | The rule is simple: one ad, one page, one goal. |
| 13 | 55.5 | إعلاناتك لوين عم تبعت الناس؟ اكتبلنا بالكومنتات. | Where do your ads send people? Tell us in the comments. |

---

## 4. Look

- **Palette:** charcoal `#1A1A1A` background, orange `#FF4D1A` for meaning, off-white `#F5F1EA` for text. Use gold `#FFB000` at most twice, for the `1 · 1 · 1` rule in scene 11. Don't introduce any new colors. The mockups use the same palette.
- **Motion (this is the "pro" part):**
  - **Highlight boxes:** orange rounded rectangles draw around the elements being described, such as the menu, the shoe, the headline and the button.
  - **Counters:** small orange count badges tick up as the homepage scrolls. They count only what the mockup contains.
  - **Dimming:** everything except the highlighted area dims to ~40% when a single element is being pointed out.
  - **Smooth camera:** push-ins and pans on the phone, using `power3.inOut`, synced to the VO.
  - Mockups scroll like real pages (seek-safe GSAP, no `Date.now()`), so they feel alive.
  - Use these sparingly, so the screen stays clean.
- **Type:** Alexandria (Arabic + Latin, 300–900), from the reference build. Arabic must be correctly shaped in RTL. Never animate Arabic letter by letter.
- **Background:** the same faint 72px grid with slow drift, around the phone frame.
- **One text layer rule (Salem, Oct 11): never show the same sentence twice.**
  - The bottom subtitles carry every spoken sentence.
  - The center graphics show only visuals and 1–3 word labels.
  - On beats marked "subtitle hidden", the line appears big in the center and the bottom subtitle is hidden for that line.
- **Subtitles:** Arabic, exactly the spoken line, RTL, off-white on a subtle charcoal pill, one line at a time, synced. **Only these key terms are written in English and highlighted in orange:** `Homepage`, `Landing Page`. Keep subtitles above the bottom ~300px and away from the right-edge icons.
- **Logo:** the official Reignite Group logo, used exactly as supplied, from `videos/incrementality-explained/assets/reignite/reignite-group-logo.png` (branch `ccr-65fff1ea-12hlnt`). Use it as a small watermark at the top in scene 01 and full-size on the end card.

---

## 5. Storyboard

| # | Lines | Scene | On-screen text (exact) |
|---|---|---|---|
| 01 HOOK | 01–02 | The ad card is tapped, and an arrow flies from it to a **house icon labeled Homepage**. Inside, a person icon looks around, lost: question marks pop, and a coin drops and rolls away. Logo watermark at the top. | `Homepage` · `؟ ؟` · `💸` |
| 02 EXAMPLE | 03 | The phone frame slides up with Mockup A at the top. The `SHOES` wordmark settles in. | `مثال` |
| 03 HOMEPAGE | 04 | The menu opens and gets an orange box with a badge `٦`. Then the page scrolls smoothly while a section counter ticks up and small orange dots mark each button that passes. Counts must match Mockup A. | `قائمة ٦` · `أقسام` · `كبسات` (counts from the mockup) |
| 04 FOR EVERYONE | 05 | The phone shrinks to the right (RTL). Three person icons appear on the left, each with a tiny label, and each draws a line to a different part of the homepage. | `رجالي` · `نسائي` · `العروض` |
| 05 THE AD | 06 | The sporty-shoe ad card pops in beside the phone. A dashed arrow from the ad hesitates over the homepage, with a question mark. | `؟` |
| 06 TERM | 07 | A quick wipe swaps the phone to Mockup B. `Landing Page` lands big above the frame in orange. | `Landing Page` |
| 07 ONE OF EACH | 08 | Highlights one by one, synced to the VO: (1) an empty dashed box where the menu used to be, with `✗`, (2) the shoe image gets a box, (3) the headline gets `١`, (4) the button gets `١`. Everything else dims to ~40%. | `قائمة ✗` · `صورة` · `عنوان ١` · `كبسة ١` |
| 08 SIDE BY SIDE | 09 | Split screen with two phones. The Homepage on the right with all its boxes and badges back, looking busy. The Landing Page on the left with one clean box. The ad card connects only to the left phone with a solid orange line. | `Homepage = للكل` · `Landing Page = لهدف واحد` |
| 09 DINNER | 10 | A line-drawn neighborhood with many identical houses. A guest icon wanders between them with a question mark. | `🏘️` · `؟` |
| 10 DOOR OPEN | 11 | One house lights up orange, its door swings open, and a set table appears inside. The guest walks straight in. | `🚪 ← 🍽️` |
| 11 THE RULE | 12 | **The full spoken line is shown big in the center, and the bottom subtitle is hidden.** Three gold `١` badges stamp in, one per phrase. | `إعلان واحد · صفحة وحدة · هدف واحد` (subtitle hidden) |
| 12 CTA | 13 | A large comment bubble with two chips to pick from. | `Homepage` · `Landing Page` · `👇` |
| 13 END CARD | none | The logo fades in with a 0.97→1 scale on charcoal, with the Reignite chime. About 3s. | (logo only) |

---

## 6. Audio

- **VO:** the chosen Fadi take, as the loudest element. Mix to about −14 LUFS integrated.
- **Music:** the same dark minimal electronic bed as the earlier episodes, ducked under the VO.
- **SFX (subtle):**
  - a soft tap for the ad and a coin drop (scene 01)
  - a light "tick" for every counter increment (scene 03)
  - a quick whoosh for the page swap (scene 06)
  - a soft "pop" for each highlight box (scene 07)
  - distant neighborhood ambience (scene 09)
  - a door creak and a warm chime (scene 10)
  - three stamp thumps (scene 11)
  - the Reignite chime on the end card

---

## 7. Cover

Use the same template as every episode:
- charcoal background
- small `شو يعني؟` at the top in orange
- `Landing Page` huge in off-white
- `لوين عم تبعت إعلاناتك؟` beneath it
- a small still of the two phone mockups side by side
- the logo small at the bottom

Keep the text inside the center 1080×1350. Export it as `cover.png`.

---

## 8. Instagram caption

```
عم تدفع عالإعلان وتبعت الناس عالصفحة الرئيسية؟ 💸

الـ Homepage معمولة لكل الناس: أقسام وقائمة وكبسات كتير.
بس إذا إعلانك على منتج واحد، الزائر لازم يوصل على صفحة وحدة بتحكي عن هيدا المنتج بس.

هيدي اسمها Landing Page.
إعلان واحد، صفحة وحدة، هدف واحد.

شو يعني؟ | الحلقات اللي قبل 👈 عالبروفايل

إعلاناتك لوين عم تبعت الناس؟ اكتبلنا 👇

#تسويق #تسويق_رقمي #إعلانات #مواقع #تصميم_مواقع #بزنس #لبنان #دبي #الإمارات #DigitalMarketing #LandingPage #WebDesign #SmallBusiness #ReigniteGroup
```

**For the comments:** if someone says "Homepage", reply with one concrete tip: make one page for that ad, with the same headline as the ad and one button. Don't pitch services in replies.

---

## 9. Done checklist for Claude Code

- [ ] No real website, brand or logo appears; the shoe store is fictional and drawn as vector UI
- [ ] Every count on screen matches what the mockups contain
- [ ] The chosen **landing-v2** Fadi take is in place, with timings mapped from the audio (Scribe)
- [ ] The composition is **1080×1920 at 30fps**
- [ ] No sentence appears twice on screen (subtitle hidden in scene 11; elsewhere only labels in the center)
- [ ] Only brand colors in graphics; Reignite logo untouched
- [ ] `npm run check` passes
- [ ] Rendered `landing-page-explained.mp4` (1080×1920, 30fps) + `cover.png`
- [ ] Committed to a new branch in hyperfr; ask Salem before opening a PR
