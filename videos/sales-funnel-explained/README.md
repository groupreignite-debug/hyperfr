# Reignite Group — "Sales Funnel" (شو يعني؟, 9:16 Arabic reel, 55.7s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script + timings: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/sales-funnel-explained.mp4` (H.264 1080×1920 30fps, AAC, −13.9 LUFS, true peak −1.3 dBFS)
and `cover.png`.

Arc: HOOK (an ad, a shrug, a scroll) → the stranger (the ad bounces off) → `Sales Funnel` (the path from first sight to
the cart) → the café → Awareness → Consideration → Decision → Loyalty (the funnel fills band by band) → THE MISTAKE (the
"buy now" ad hits the top band and breaks) → one message per stage → drop-off + "where?" → comment your stage → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` for the Loyalty stage only.
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`, copied from the Incrementality build.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the
  Incrementality copy). Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the charcoal.
- The funnel (`#fnBox`: 4 polygons, 600×640) and its colours are built to be reused in the Retargeting episode.

## Audio pipeline
```bash
python3 scripts/build_vo_human.py  # client VO: clean + level, tighten 3 silences → audio/vo-human/vo_track.wav; Scribe words → scripts/cues.json
python3 scripts/apply_cues.py    # scene windows + CUES (word times) into index.html
python3 scripts/build_audio.py   # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- Voice: the client recording `audio/vo-human/src/vo_human_raw.m4a` (AUD-20261013-WA0100), as delivered;
  `scripts/vo_human_words.json`: its Scribe word timings. The earlier TTS take stays in `audio/vo/` as a fallback
  (`build_vo.py`, see `SCRIPT.md`).
  Line → word-index ranges are `LINES` in `build_vo_human.py`; every animation and subtitle time in `index.html` is `W(i)`,
  the start of Scribe word *i*. So a different take only needs a new Scribe pass, an index check, and the three scripts.
- SFX: swipe as the ad is scrolled past, pen-draw as the funnel outlines, very low street ambience under the café
  scenes, shop-door bell + cup set on Decision, a rising fill tick per band, a dull thud when the ad hits the funnel,
  three soft pops for the message tags, Reignite chime. The music is kept low so a trending sound can be added in
  Instagram.
- Python deps: numpy, scipy, soundfile.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/sales-funnel-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS (measured -13.9 LUFS / -1.3 dBTP; re-measure with ebur128 if the mix changes):
ffmpeg -i renders/sales-funnel-raw.mp4 -c:v copy -af "volume=6.0dB,alimiter=limit=0.85:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/sales-funnel-explained.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```

`check` reports 20 `nested_structure_needs_subcomposition` warnings. This is the same single-file layout as the
earlier episodes; it does not affect the render.
