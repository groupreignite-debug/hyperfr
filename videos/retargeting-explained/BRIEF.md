---
workflow: faceless-explainer
flow: autonomous
storyboard: skip
angle: concept
length: 60.2s (56.6s VO + 0.6s tail + 3s end card)
destination: instagram-reels (@reignitegroup, Sat Nov 7 2026)
format: 1080x1920 @ 30fps
language: ar (Lebanese conversational) + English key terms
voice: client recording (audio/vo-human, Oct 13), first word trimmed to 0.12s (Oct 15 hook update)
vo_mode: verbatim (client script)
series: شو يعني؟ (after incrementality-explained, vanity-metrics)
brand: Reignite Group
---

> The client brief below is kept verbatim. Build notes: README.md. Script with real timings: SCRIPT.md.
> Scene plan: STORYBOARD.md. Instagram caption: CAPTION.md.

# Reel brief: Retargeting, why that ad keeps following you (شو يعني؟)

**Hand this whole file to Claude Code.** It is written so a fresh session can build the reel with no other context.

| | |
|---|---|
| Post date | Sat Nov 7, 2026, @reignitegroup |
| Series | **شو يعني؟** (What does it mean?). Same series as Incrementality, Vanity Metrics and SEO. |
| Length | ~55–60s of VO + 3s end card |
| Format | **1080×1920, 30fps**, MP4 H.264 (Instagram Reels) |
| Language | Lebanese Arabic, conversational. **Arabic subtitles** burned in; only key terms in English (Latin letters). |
| Tool | **hyperfr** repo (`groupreignite-debug/hyperfr`), **HyperFrames**. Start at `/hyperframes`, then use the `/faceless-explainer` workflow with the supplied VO, verbatim (do not rewrite or regenerate the script). Read the repo's `CLAUDE.md` first. |
| Reference build | The Incrementality reel: branch `ccr-65fff1ea-12hlnt`, folder `videos/incrementality-explained/`. **Copy its look, fonts, audio pipeline and logo handling.** Read its `BRIEF.md`, `SCRIPT.md` and `STORYBOARD.md` first. If `videos/seo-explained/` or `videos/vanity-metrics/` exist by then, match them too. |
| New folder | `videos/retargeting-explained/` on a new branch |

---

## 1. Goal

Teach one idea simply: **the people who already visited you are your closest customers, and retargeting is how you talk to them again, with the right message.** Everyone has had an ad "follow" them, so the hook is instantly familiar. The reel turns that creepy-feeling moment into something a business owner can use.

It should teach, not sell. The viewer should leave knowing three practical rules: show a different message by stage, don't repeat the same ad every day, and stop showing the ad once they buy.

**Honesty rules:**
- No statistics, conversion rates, "X times more likely" claims or promises.
- The jacket and the store are a generic example. No real brand, product photo or store name.
- `Instagram` and `YouTube` appear only as plain words in the brand font. **No platform logos, icons or brand colors.**
- Don't describe tracking in a scary or inaccurate way. The Pixel is described simply as "a small code on your site that remembers who visited and which page". Nothing more technical.

---

## 2. Voiceover

**Hook update (Oct 15): this reel is already built.** Salem recorded the script in his own voice and gave it to Claude Code when the video was made. **Keep that recording and the script exactly as they are.** Only the opening changes: scene 01, its sounds, and the first-second rules below. If you are the session that built it, edit the existing composition and render again. If you are a new session, find the existing `videos/retargeting-explained/` build on its branch in hyperfr and work from it.

- **Trim the start of Salem's recording** so his first word lands within the first ~0.15s. Cut any silence, breath or room noise before it. Don't change anything else in the audio, and keep all later timings synced to it.
- The Fadi takes in `/mnt/project-files/content/reel-10-vo/` are no longer used.

Scene and subtitle timings come from the existing word timings of Salem's recording. If you trim the start, shift every timing by the same amount.

**Pronunciation check:** `Retargeting`, `Pixel`, `Instagram` and `YouTube` should sound English. (Already checked in the existing build.)

### Script (spoken exactly like this)

| # | ~start | Arabic (spoken = subtitle text) | English meaning (reference only, not on screen) |
|---|---|---|---|
| 01 | 0.0 | فتت مرة على موقع، شفت جاكيت حلو… وفلّيت. | You visited a site once, saw a nice jacket… and left. |
| 02 | 3.5 | تاني يوم، صار الجاكيت لاحقك: عـ Instagram، عـ YouTube، بكل مكان. | Next day, the jacket is following you: on Instagram, on YouTube, everywhere. |
| 03 | 8.0 | صدفة؟ لأ. | Coincidence? No. |
| 04 | 9.5 | هيدا اسمو Retargeting. | This is called Retargeting. |
| 05 | 11.5 | يعني ترجع توصل للناس اللي شافوك قبل، بس ما اشتروا. | It means reaching again the people who saw you before but didn't buy. |
| 06 | 15.5 | تخيّل محل تياب. حدا فات، جرّب، وطلع بلا ما يشتري. | Imagine a clothes shop. Someone came in, tried something on, and left without buying. |
| 07 | 20.0 | البيّاع الشاطر ما بينساه. بس يرجع يمرق، بيقلّو: "بعدها القطعة ناطرتك." | A good salesperson doesn't forget them. When they pass by again, he says: "That piece is still waiting for you." |
| 08 | 25.5 | عالإنترنت، الـ Pixel هوي البيّاع. كود صغير بموقعك، بيتذكّر مين فات، وعلى أي صفحة. | Online, the Pixel is the salesperson. A small code on your site that remembers who visited and which page. |
| 09 | 32.0 | وليش هالشي مهم؟ لأن هيدا الشخص بيعرفك. ما عم تبلّش معو من الصفر. | Why does it matter? Because this person knows you. You're not starting from zero. |
| 10 | 37.0 | بس انتبه: ما تفرجيه نفس الإعلان كل يوم، هيك بيزهق. | But careful: don't show them the same ad every day. They'll get bored. |
| 11 | 41.0 | اللي شاف المنتج، فرجيه ياه مرة تانية. واللي حطّو بالسلة، ذكّرو إنو بعدو ناطرو. | Whoever viewed the product, show it again. Whoever put it in the cart, remind them it's still waiting. |
| 12 | 46.5 | وإذا اشترى؟ وقّف الإعلان عنو. | And if they bought? Stop showing them the ad. |
| 13 | 49.0 | مش كل إعلان لازم يحكي مع ناس جداد. أحياناً أقرب زبون… هوي اللي فات وفلّ. | Not every ad has to talk to new people. Sometimes your closest customer… is the one who came in and left. |
| 14 | 54.5 | موقعك فيه Pixel؟ اكتب PIXEL بالكومنتات، ومنقلّك كيف تتأكد. | Does your site have a Pixel? Comment PIXEL and we'll tell you how to check. |

---

## 3. Look

Same visual system as the earlier episodes, so the series looks consistent:

- **Palette:** charcoal `#1A1A1A` dominant background, orange `#FF4D1A` for meaning, off-white `#F5F1EA` for text, gold `#FFB000` at most twice (use it for the "bought" moment in scene 09). No other colors.
- **Type:** Alexandria (Arabic + Latin, weights 300–900), already in `assets/fonts/` of the reference build. Arabic shaped correctly in RTL; wrap English terms so word order doesn't flip. Never animate Arabic letter by letter (it breaks the joins); animate whole words or lines.
- **Background:** the same barely visible 72px grid with slow drift.
- **Motion:** soft masked rises, line draws, slides and gentle follows (`power3.out` / `expo.out`). No glitch, fire FX, flashy transitions, stock footage, real people, real screenshots or AI imagery.
- **One world:** the **jacket card** is the recurring object: a simple line-drawn jacket on an off-white rounded card. It is the item left behind in scene 01, it "follows" across screens in scene 02, hangs in the shop in scene 04, and is the product the Pixel remembers in scene 05. The **Pixel** is one small glowing orange dot, always the same size and style.
- **Subtitles: Arabic**, exactly the spoken line, RTL, bottom safe area, off-white on a subtle charcoal pill, one line at a time, synced to the VO. **Only these key terms are written in English (Latin letters) and highlighted in orange:** `Retargeting`, `Pixel`, `PIXEL`, `Instagram`, `YouTube`. Everything else stays Arabic. No English translation track. Keep subtitles clear of the Instagram UI (above the bottom ~300px and away from the right-edge icons).
- **One text layer rule (Salem, Oct 11): never show the same sentence twice.** The bottom subtitles carry every spoken sentence. The center graphics never repeat that sentence. They show visuals plus short labels only (the term, a stage name, 1–3 words). When a scene shows a full spoken line big in the center (the "LINE" beats), **hide the bottom subtitle for that line**, so the text appears only once.
- **Logo:** the official Reignite Group logo, used exactly as supplied: no redraw, recolor, crop or a different flame. Copy it from `videos/incrementality-explained/assets/reignite/reignite-group-logo.png` (branch `ccr-65fff1ea-12hlnt`). Only full-size on the end card. No watermark in the opening.

### Hook rules (first 2 seconds, Salem, Oct 14)

Instagram retention on our reels drops 50-65% in the first 3 seconds, then stays flat. So:
- **Frame 0 is already full.** The hook visual is on screen at the first frame, with movement inside the first 0.3s. Nothing builds up from empty, and there's no fade-in from black.
- **The twist is on screen inside 1.5 seconds, before the voice gets to it.** The spoken line 01 is only the setup ("you visited a site once… and left"); the twist (the jacket following you) comes in line 02 at ~3.5s. So the picture shows the twist first, as a short teaser, while the bottom subtitle carries line 01.
- **No logo in the opening.** The logo appears only on the end card. That keeps the first seconds from reading as an ad.

---

## 4. Storyboard

| # | Lines | Scene | On-screen text (exact) |
|---|---|---|---|
| 01 HOOK | 01 | **0–1.2s, a teaser of the twist (no build-up, no fade-in):** at frame 0 the jacket card is already big in the center, and in the first 0.3s it pops into three feed screens around it, one after another, each with a notification pop. At about 0.8s the jacket card lunges toward the camera and `لاحقك؟` stamps in big, orange, with a short shake. **1.2s, rewind:** a quick reverse-scrub (the screens fly back the way they came, with a small `⏪`) lands on a phone with an abstract shop page (no brand). As Salem says line 01, a cursor taps the jacket, the phone slides down, and the jacket card is left floating alone. No logo. | `لاحقك؟` · `⏪` · `👀 شفت` · `👋 فلّيت` |
| 02 FOLLOW | 02 | Three phone screens slide in one after another, each a simple feed layout labeled with a plain word. On each one the same jacket card pops into the feed. On the third, the card drifts slightly toward the camera, like it's following the viewer. | `Instagram` · `YouTube` · `بكل مكان` |
| 03 FREEZE | 03 | Everything dims and blurs. The question rises in the center, then `لأ` stamps in orange under it. | `صدفة؟` · `لأ.` (**bottom subtitle hidden** for this line) |
| 04 TERM | 04–05 | `Retargeting` lands huge. Under it, a simple loop arrow draws itself from a person icon back to the person icon (out and back). Then the definition line appears. | `Retargeting` · `👁 ← ✗ ← 🔁` (icons only, no sentence) |
| 05 SHOP | 06–07 | Line-drawn shop front with a door. A simple person icon walks in, stands by the jacket on a rail, then walks out. Later the person icon passes the door again; a speech bubble from the shop pops up with the line. | `فات ✓` · `جرّب ✓` · `اشترى ✗` · bubble: `👋` (the line itself stays in the subtitle) |
| 06 PIXEL | 08 | The shop dissolves into a website outline. The salesperson becomes the orange Pixel dot in the corner of the page. As a cursor visits two pages (the product page, then the cart), the dot pulses and draws a small line to a mini "memory" list. | `PIXEL = البيّاع` · list: `فات ✓` · `صفحة الجاكيت ✓` |
| 07 WARM | 09 | Two person icons side by side. The left one is grey, labeled as a stranger, with a long dotted path to the shop. The right one is orange, labeled as someone who knows you, with a short path. | `ما بيعرفك` · `بيعرفك` · `مش من الصفر` |
| 08 DON'T REPEAT | 10 | The same jacket ad stacks on itself 5 times, quickly, like a deck of cards, each slightly more faded. A tired emoji face appears and the stack slides away. | `×5 = 😴` |
| 09 THE RULES | 11–12 | The strongest beat. Three rows build down the screen, one per spoken rule, each with an icon on the right (RTL) and the message on the left: eye → "show it again", cart → "it's still waiting", check mark → ad switches off (row turns gold, the ad thumbnail fades out). | `👁 شاف ← 🔁` · `🛒 بالسلة ← 🔔` · `✓ اشترى ← ⛔` (short labels and icons) |
| 10 LINE | 13 | Calm type beat. First line appears, then a pause, then the second line with `فات وفلّ` in orange. Slow push-in. | `مش كل إعلان لازم يحكي مع ناس جداد.` · `أقرب زبون… هوي اللي فات وفلّ.` (**bottom subtitle hidden** for this line) |
| 11 CTA | 14 | A large comment bubble with the word, and the Pixel dot pulsing next to it. | `اكتب PIXEL 👇` · `ومنقلّك كيف تتأكد` |
| 12 END CARD | none | The logo fades in with a 0.97→1 scale on charcoal, with the Reignite chime. About 3s. No extra text. | (logo only) |

If an emoji doesn't render in the brand font, replace it with a simple line icon in the same style (don't use a fallback emoji font that looks different from scene to scene).

---

## 5. Audio

- **VO:** Salem's recording, the loudest element. Normalize the full mix to about −14 LUFS integrated.
- **Music:** the same dark minimal electronic bed as the earlier episodes, ducked well under the VO. It starts at frame 0, with no fade-in.
- **SFX (subtle):** three quick notification pops from frame 0, a whoosh-thud when `لاحقك؟` stamps, a short tape-rewind zip on `⏪`, then a soft tap when the cursor clicks the jacket (scene 01), three light "pop" notification sounds as the jacket appears in each feed (scene 02), a short stop/silence beat on `لأ` (scene 03), a shop door bell when the person enters (scene 05), a tiny digital blip each time the Pixel pulses (scene 06), quick card-flick sounds for the stacked ads (scene 08), a soft positive click when the row turns gold (scene 09), and the Reignite chime on the end card.
- Salem may add a trending sound inside Instagram, so keep the music low enough that this still works.

---

## 6. Cover (thumbnail frame)

Same template every episode: charcoal background, small `شو يعني؟` at the top in orange, `Retargeting` huge in off-white, `ليش الإعلان لاحقك؟` beneath it, the jacket card small beside it, and the logo small at the bottom. Keep all text inside the center 1080×1350 so it survives the grid crop. Export as `cover.png`.

---

## 7. Instagram caption

```
فتت على موقع… وتاني يوم صار الإعلان لاحقك بكل مكان؟ 👀

هيدا اسمو Retargeting: إنك ترجع توصل للناس اللي شافوك وما اشتروا.

٣ قواعد:
١. اللي شاف المنتج، فرجيه ياه مرة تانية
٢. اللي حطّو بالسلة، ذكّرو إنو بعدو ناطرو
٣. اللي اشترى، وقّف الإعلان عنو

شو يعني؟ | الحلقات اللي قبل 👈 عالبروفايل

موقعك فيه Pixel؟ اكتب PIXEL بالكومنتات ومنقلّك كيف تتأكد 👇

#تسويق #تسويق_رقمي #إعلانات #إعلانات_ممولة #بزنس #ريادة_الأعمال #لبنان #دبي #الإمارات #DigitalMarketing #Retargeting #MetaAds #SmallBusiness #ReigniteGroup
```

**For the comments:** when someone writes PIXEL, reply and ask in DM what platform their site is on. Then explain the honest check: for Meta, the free Meta Pixel Helper browser extension, or Events Manager → the pixel's "last received" activity. Don't promise results.

---

## 8. Done checklist for Claude Code

- [ ] Salem's own recording kept; script unchanged; first word within ~0.15s of the start; all timings still synced
- [ ] Hook: frame 0 already shows the jacket card (no empty or black first frame); `لاحقك؟` on screen by about 1s; no logo before the end card
- [ ] Composition is **1080×1920 at 30fps**
- [ ] Every on-screen string matches section 4 exactly, with Arabic shaped correctly in RTL
- [ ] Arabic subtitles synced, only the listed key terms in English and orange, inside the safe area
- [ ] No sentence appears twice on screen (subtitle hidden on the LINE beat; center shows labels only)
- [ ] Only brand colors; no platform logos or colors; no real brands, people or screenshots; logo untouched
- [ ] `npm run check` passes in the composition folder
- [ ] Rendered `retargeting-explained.mp4` (1080×1920, 30fps) + `cover.png`
- [ ] Committed to a new branch in hyperfr; ask Salem before opening a PR
