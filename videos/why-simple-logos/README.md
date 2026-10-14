# Reignite Group — "ليش أشهر الشعارات بسيطة؟" (9:16 reel, 106.5s)

HyperFrames composition: `index.html` (1080×1920, 30fps) + 12 scenes in `compositions/frames/`.
Plan: `BRIEF.md`, `STORYBOARD.md`, `SCRIPT.md`, design tokens in `frame.md`.

## Assets
- `assets/reignite/reignite-group-logo.png` — the supplied logo file, byte-identical. It is only
  framed, faded and scaled 98→100%. Its black field is composited onto the charcoal with
  `mix-blend-mode: lighten`; the logo pixels themselves are untouched.
- `assets/logos/{nike,apple,mcdonalds}.svg` — the marks from the Simple Icons package (v16.34),
  used unaltered for educational reference (Nike/Apple in off-white, arches in gold).
- Fonts: Noto Kufi Arabic (display), IBM Plex Sans Arabic (support), Inter (Latin labels) — local woff2.

## Audio
- `audio/vo/vo_01…vo_11.mp3` — ElevenLabs, voice "Fadi – Lebanese Conversational", `eleven_multilingual_v2`,
  one take per script section. `audio/vo/words.json` holds the word timings used to sync every reveal.
- `audio/music.wav`, `audio/sfx.wav` — procedural bed + sound design from `scripts/build_audio.py`
  (`python3 scripts/build_audio.py`). VO starts in that script mirror `index.html`.

## Commands
```bash
npm run check
npx hyperframes preview --background
npx hyperframes render --quality high --fps 30 -o renders/reignite-why-simple-logos.mp4
# Instagram loudness (-14 LUFS):
ffmpeg -i renders/reignite-why-simple-logos.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.0:LRA=11 -c:a aac -b:a 256k renders/reignite-why-simple-logos-final.mp4
```
