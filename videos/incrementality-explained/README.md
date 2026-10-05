# Reignite Group — "Incrementality" (9:16 Arabic educational reel, 75.4s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script: `SCRIPT.md` · scene plan: `STORYBOARD.md`.

Arc: HOOK (10,000$ → 30,000$ → ROAS 3X) → FREEZE (the question) → 100 customers → 40 bought → 25 would have anyway
→ 15 incremental → INCREMENTALITY → ATTRIBUTION vs INCREMENTALITY → control group 50 − 35 = 15
→ ROAS 5.0X vs INCREMENTAL ROAS 2.1X → the real question → memory word → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` (used only on the sparkline and the `=` sign).
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged. Its clip is composited with
  `mix-blend-mode: lighten`, so the PNG's black field sits on the charcoal. The pixels are never edited.

## Audio
- `audio/vo/`: ElevenLabs `eleven_multilingual_v2`, voice "Fadi - Lebanese Conversational" (male, Levantine).
  Raw takes are in `audio/vo/src/`. `python3 scripts/build_vo.py` trims silence, applies 1.07× tempo, lays the lines
  out, and writes `scripts/cues.json` (line starts + word anchors measured with ElevenLabs Scribe).
- `audio/music.wav`, `audio/sfx.wav`: procedural bed + SFX from `python3 scripts/build_audio.py` (needs numpy, scipy, soundfile).
  The music is pre-ducked under every VO line.
- If you swap in a human VO, keep the filenames, rerun `build_vo.py`, then update the `<audio data-start>` values and the
  GSAP times in `index.html` (they mirror `cues.json`).

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npm run render -- --quality high --output renders/video.mp4
# Instagram loudness (-14 LUFS):
ffmpeg -i renders/video.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.0:LRA=11 -c:a aac -b:a 256k renders/video-ig.mp4
```
