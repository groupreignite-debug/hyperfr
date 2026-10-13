# Storyboard — as built

Every beat time is derived from the VO's word timings in `scripts/cues.py → beats()` (e.g. the
menu opens on the word «قائمة», each highlight box lands on its noun). Scene numbers follow BRIEF.md §5.

| # | Lines | Built | Centre text |
|---|---|---|---|
| 01 HOOK | 01–02 | Ad card (fictional `SHOES` sneaker ad), tap on «اطلب هلّق», arrow to a line-drawn house labelled Homepage; camera pushes in; a lost visitor, three `؟`, a coin drops, bounces and rolls out. Logo watermark at top. | `Homepage` · `؟ ؟ ؟` |
| 02 EXAMPLE | 03 | Phone slides up with Mockup A at the top; `SHOES` wordmark settles. | `مثال` |
| 03 HOMEPAGE | 04 | Menu opens (6 items), page dims, orange box + badge `٦`. Page then scrolls section by section: each of the 8 sections flashes, each of the 12 buttons gets an orange dot; counters tick. | `قائمة ٦` · `أقسام ٨` · `كبسات ١٢` |
| 04 FOR EVERYONE | 05 | Phone shrinks right; three visitors on the left draw lines to the رجالي tile, the نسائي tile and the العروض strip. | `رجالي` · `نسائي` · `العروض` |
| 05 THE AD | 06 | Ad card pops in, its shoe pulses; a dashed arrow hesitates toward the homepage; `؟`. | `؟` |
| 06 TERM | 07 | Phone recentres; orange wipe swaps to Mockup B. | `Landing Page` |
| 07 ONE OF EACH | 08 | Empty dashed box with ✗ where the menu was → shoe box → headline box `١` → button box `١`; everything else at 40%; tap ripple on «اطلب هلّق». | `قائمة ✗` · `صورة` · `عنوان ١` · `كبسة ١` |
| 08 SIDE BY SIDE | 09 | Landing page left with one box (the CTA); homepage right with its boxes, dots and badges `٦ ٨ ١٢`, jittering; the ad connects only to the left phone. | `Homepage = للكل` · `Landing Page = لهدف واحد` |
| 09 DINNER | 10 | 12 identical line-drawn houses; a guest wanders the streets with `؟`. | — |
| 10 DOOR OPEN | 11 | One house lights orange, camera pushes in, door swings open, a table appears, guest walks in. Door → table icon row. | (icons) |
| 11 THE RULE | 12 | Full line big in the centre, subtitle hidden; three gold `١` stamps (the only gold in the film). | `القاعدة بسيطة: إعلان واحد، صفحة وحدة، هدف واحد.` |
| 12 CTA | 13 | Comment bubble with two chips and a bouncing down arrow. | `Homepage` · `Landing Page` |
| 13 END CARD | — | Supplied logo fades in 0.97→1 with the chime; 3 s. | (logo) |

## Mockup counts (what the counters show)
- Homepage menu: رجالي · نسائي · أطفال · العروض · من نحن · تواصل معنا = **6**
- Homepage sections: hero, categories, offers, product grid (6 shoes), best sellers, blog, newsletter, footer = **8**
- Homepage buttons (`.btn`): تسوّق الآن, اكتشف, شوف الكل ×2, أضف ×6, اقرأ المزيد, اشترك = **12**
  (`HOME_BUTTONS` in `scripts/cues.py` must match; the page warns in the console if not)
- Landing page: no menu, one shoe image, one headline, one action (`اطلب هلّق`, repeated once below the fold)

Emoji from the brief (💸 🏘️ 🚪 🍽️ 👇) are drawn as brand-colour vectors (coin, houses, door, table, arrow) so the
palette stays orange / off-white / charcoal and nothing depends on an emoji font.
