# Reignite Group — "Vanity Metrics" v2 (شو يعني؟ #2, 9:16 Arabic reel, 45.9s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/vanity-metrics.mp4` (−14 LUFS, AAC) and `cover.png`.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`. Alexandria (SIL OFL) in `assets/fonts/`.
- Logo: `assets/reignite/reignite-group-logo.png`, the supplied file unchanged, on the end card only
  (`mix-blend-mode: lighten` so its black field sits on the charcoal).

## Audio pipeline
```bash
python3 scripts/build_vo.py      # vo_full.m4a -> vo_full.wav (+10 dB), phrase map + word anchors -> scripts/cues.json
python3 scripts/apply_cues.py    # VO tag, scene windows, cues -> index.html
python3 scripts/build_audio.py   # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- `audio/vo/vo_full.m4a`: ElevenLabs Fadi, v2 take 1, untouched. `build_vo.py` maps the speaker's pauses to
  the script (`PHRASES`) and stops if a different take splits differently; word onsets are `ANCHORS`.
- To use another take: replace `vo_full.m4a`, run the three scripts, and adjust `PHRASES`/`ANCHORS` if the build
  reports a different phrase count.
- Python deps: numpy, scipy, soundfile.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/vanity-metrics-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS (gain + transparent limiter; re-measure with ebur128):
ffmpeg -i renders/vanity-metrics-raw.mp4 -c:v copy -af "volume=4.7dB,alimiter=limit=0.75:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/vanity-metrics.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```
