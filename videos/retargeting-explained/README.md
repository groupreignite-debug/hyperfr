# Reignite Group — "Retargeting" (شو يعني؟, 9:16 Arabic reel, 61.6s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script + timings: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/retargeting-explained.mp4` (H.264 1080×1920 30fps, AAC, −14 LUFS, true peak ≈ −1.1 dBFS)
and `cover.png`.

Arc: HOOK (visited, saw the jacket, left) → the jacket follows (Instagram · YouTube · everywhere) → FREEZE (صدفة؟ لأ.)
→ `Retargeting` (out and back) → the clothes shop (came in, tried, didn't buy; the salesperson remembers) → the Pixel
is the salesperson → warm vs stranger → don't repeat the same ad → the 3 rules → the line → comment PIXEL → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` once (the "bought" rule).
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`, copied from the Incrementality build.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the
  Incrementality copy). Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the charcoal.

## Audio pipeline
```bash
python3 scripts/build_vo.py      # take 4 → 1.05x, +9 dB, 0.3s lead → audio/vo/vo_track.wav; Scribe words → scripts/cues.json
python3 scripts/apply_cues.py    # scene windows + CUES (word times) into index.html
python3 scripts/build_audio.py   # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- `audio/vo/vo_full.mp3`: the chosen ElevenLabs take, as delivered. `scripts/vo_words.json`: its Scribe word timings.
  Line → word-index ranges are `LINES` in `build_vo.py`; every animation and subtitle time in `index.html` is `W(i)`,
  the start of Scribe word *i*. So a different take only needs a new Scribe pass, an index check, and the three scripts.
- SFX: tap on the jacket, three feed pops, a stop on "لأ", door bell, Pixel blips, card flicks, the gold-row
  positive click, Reignite chime. The music is kept low so a trending sound can be added in Instagram.
- Python deps: numpy, scipy, soundfile.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/retargeting-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS (re-measure with ebur128 if the mix changes):
ffmpeg -i renders/retargeting-raw.mp4 -c:v copy -af "volume=6.5dB,alimiter=limit=0.85:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/retargeting-explained.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```

`check` reports 17 `nested_structure_needs_subcomposition` warnings. This is the same single-file layout as the
Incrementality and Vanity Metrics builds; it does not affect the render.
