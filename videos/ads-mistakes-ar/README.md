# Reignite Group — "3 أخطاء بتقتل إعلاناتك" (9:16 reel, 41.5s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Arabic, Lebanese conversational.

Arc: HOOK (ad dashboard: spend climbs, results flat) → 3 أخطاء → 01 weak Hook (ad skipped in 2s)
→ 02 product talk vs. the customer's problem (attention meter 6% → 94%) → 03 weak CTA (ad ends, viewer
has nothing to do, 0 clicks) → ENDING (same dashboard, results now move) → "بيخليهم يتحركوا." + logo.

One phone persists across all three mistakes, and the same dashboard opens and closes the film.
A chapter tracker (01 Hook / 02 مشكلة العميل / 03 CTA) stays on screen and ticks off at the end.

## Type and colour
- Display: Alexandria (800/900). UI: IBM Plex Sans Arabic. Local woff2 in `assets/fonts/` (from @fontsource).
- Brand tokens: `#FF4D1A` orange, `#1A1A1A` charcoal, `#F5F1EA` off-white text, `#FFB000` used only for accents.
- `dir="rtl"` must NOT be set on `<html>` (HyperFrames renders a black video). RTL is scoped to text containers.

## Audio
- `audio/vo/vo_01..11.wav`: ElevenLabs voiceover (voice "Laloosh – Engaging & Confident E-Comm", female,
  Levantine; model `eleven_v3`), one file per line of `audio/vo/script.tsv`, trimmed and peak-normalised.
  The line starts live in `index.html` and `scripts/cues.json`, and the music is ducked under them, so after
  replacing a line run `python3 scripts/build_audio.py`.
- `audio/music.wav`, `audio/sfx.wav` are a procedural 100 BPM electronic bed and UI SFX from
  `scripts/build_audio.py`, driven by `scripts/cues.json`. The music is pre-ducked under each VO line. Rebuild with `python3 scripts/build_audio.py`.

## Check / render
```bash
npx hyperframes check
npx hyperframes render --quality high --fps 30 -o renders/reignite-3-ad-mistakes.mp4
ffmpeg -i renders/reignite-3-ad-mistakes.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.0:LRA=11 -c:a aac -b:a 256k renders/reignite-3-ad-mistakes-final.mp4
```
