# Reignite Group — "Landing Page vs Homepage" (شو يعني؟, 9:16 Arabic reel)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · script: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md` · cover: `cover.png` (from `cover/cover.html`).

Fully animated: the shoe store `SHOES` is fictional and drawn in HTML/CSS/SVG. No real site, brand,
statistic or AI image appears. Look, fonts, audio bed and logo handling follow `videos/incrementality-explained`.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`; gold `#FFB000` only on the three `١` stamps of scene 11.
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged, composited with
  `mix-blend-mode: lighten` so its black field sits on the charcoal.

## Timing pipeline (one cue sheet drives picture, subtitles and SFX)
1. `audio/vo/vo_full.mp3` = the chosen Fadi **landing-v2** take. `python3 scripts/build_vo.py` → `audio/vo/vo_track.wav`
   (light polish; sped up without pitch change only if it runs over 60 s).
2. Word timings: ElevenLabs Scribe on `vo_track.wav`, saved as `scripts/vo_words.json` (`[{text,start,end}]`).
3. `python3 scripts/cues.py --words scripts/vo_words.json` aligns Scribe's words to the script, derives every
   beat (`beats()`), writes `scripts/cues.json` and injects CUES into `index.html` (+ all clip durations).
4. `python3 scripts/build_audio.py` → `audio/music.wav` (bed, pre-ducked under each VO line) + `audio/sfx.wav`.

`python3 scripts/cues.py --placeholder` + `python3 scripts/build_vo.py --silent` give a timing preview on the
brief's target timings when no VO is in place.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npm run render -- --quality high --fps 30 --output renders/video.mp4
# Instagram loudness (-14 LUFS):
ffmpeg -i renders/video.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.0:LRA=11 -c:a aac -b:a 256k renders/landing-page-explained.mp4
node scripts/build_cover.mjs          # cover/cover.html → cover.png
```
