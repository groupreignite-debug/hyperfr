# Reignite Group — "Incrementality" (9:16 Arabic educational reel, 66.6s)

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
- **Voiceover (in use): `audio/vo-human/vo_track.wav`**, the client's recording. `python3 scripts/build_vo_human.py` cleans it
  (80 Hz HPF, −2.5 dB at 220 Hz, +2 dB presence at 3.2 kHz, air, de-ess, 3:1 compression, −1 dB limiter). It cuts the
  16 script lines at Scribe word boundaries, drops the end-of-take outtake, re-spaces the lines around the visual beats,
  and writes `scripts/timemap.json`. Then `python3 scripts/apply_timemap.py` updates `index.html`: the animation is still
  authored on the original cue sheet and plays through the map, so every reveal lands on its spoken word. Rerun
  `python3 scripts/build_audio.py` after either step.
- `audio/vo/` (reference only, not used): ElevenLabs `eleven_multilingual_v2`, voice "Fadi - Lebanese Conversational" (male, Levantine).
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
