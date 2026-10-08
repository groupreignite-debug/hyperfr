# Carousel 01: Incrementality vs ROAS (7 slides)

Instagram carousel for @reignitegroup (post date Wed Oct 14, 2026). It repurposes the Incrementality reel
(`videos/incrementality-explained/`) and uses the same hypothetical example numbers.

- `slides/slide-1.html` … `slide-7.html`: one page per slide, 1080×1350, Lebanese Arabic, RTL
- `styles.css` + `fonts.css`: shared design system (Alexandria, brand colors, 72px grid)
- `assets/`: Alexandria `.woff2` and the official logo, copied unchanged from the reel
- `out/01.png` … `07.png`: the export, ready to upload in order

## Render

```bash
node render.mjs   # needs playwright (Chromium); waits for the fonts and fails if Alexandria didn't load
```

## Caption

```
صرفت ١٠ آلاف وجبت ٣٠ ألف؟ 🤔
قبل ما تحتفل، اسأل السؤال الصح.

الـ ROAS بيقلك قديش بيعة منقدر ننسبها للإعلان.
الـ Incrementality بيقلك قديش بيعة ما كانت رح تصير بدونه.

٧ صفحات، احفظهن لحملتك الجاية 🔖
(الأرقام بالبوست مثال للتوضيح)

شو يعني؟ | الريل كامل عالبروفايل

#تسويق #تسويق_رقمي #إعلانات #إعلانات_ممولة #بزنس #ريادة_الأعمال #لبنان #دبي #الإمارات #DigitalMarketing #ROAS #Incrementality #PerformanceMarketing #ReigniteGroup
```

## Alt text

```
كاروسيل من ٧ صفحات بيشرح الفرق بين ROAS وIncrementality بمثال: ١٠٠ عميل، ٤٠ اشتروا، ٢٥ كانوا رح يشتروا أصلاً، و١٥ بس بسبب الإعلان.
```
