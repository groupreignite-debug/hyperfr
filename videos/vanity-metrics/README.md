# Reignite Group — "Vanity Metrics" (شو يعني؟ #2, 9:16 Arabic reel, 56.1s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/vanity-metrics.mp4` (−14 LUFS, AAC) and `cover.png`.

Arc: HOOK (10,000 ❤ · 0 زبون) → FREEZE (شو صار؟) → VANITY METRICS → balloons (likes/views/followers) popped
→ shop: 1,000 passed → 10 entered → 2 bought, REACH vs BUSINESS → VANITY vs ACTIONABLE → the real question → ask
the viewer → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`. Gold is not used in this episode.
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/` (copied from the Incrementality build).
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the
  Incrementality copy). Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the charcoal.

## Audio pipeline
```bash
python3 scripts/build_vo.py      # trim + 1.07x tempo, lay lines out, detect pauses -> scripts/cues.json
python3 scripts/apply_cues.py    # write VO tags, scene windows, subtitle/animation cues into index.html
python3 scripts/build_audio.py   # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- `audio/vo/`: ElevenLabs `eleven_multilingual_v2`, voice "Fadi - Lebanese Conversational", one take per line in
  `audio/vo/src/`. Spacing between lines is `GAPS` in `build_vo.py`.
- SFX: counter ticks, balloon pops, a whoosh as the 10 dots enter the shop, a scratch on the strike-through,
  the Reignite chime on the end card.
- Python deps: numpy, scipy, soundfile.

## Swapping in a human VO (Salem)
Replace `audio/vo/src/vo_NN.bin` with one cut file per line (same numbering), then run the three scripts above.
Every animation, subtitle and SFX time is read from `cues.json`, so nothing in `index.html` needs hand edits.
Word anchors inside lines without a pause (the scene-06 items, the balloon words) are offsets in `index.html`
(`views`, `follows`, `items`, `tAct`) and may need a nudge.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/vanity-metrics-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS. Speech peaks sit ~18 dB over its average, so use
# gain + a transparent limiter rather than loudnorm alone (re-measure with ebur128 if the mix changes):
ffmpeg -i renders/vanity-metrics-raw.mp4 -c:v copy -af "volume=7.8dB,alimiter=limit=0.75:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/vanity-metrics.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```
