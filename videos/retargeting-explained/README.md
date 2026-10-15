# Reignite Group — "Retargeting" (شو يعني؟, 9:16 Arabic reel, 60.2s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script + timings: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/retargeting-explained.mp4` (H.264 1080×1920 30fps, AAC, −14 LUFS, true peak ≈ −1.2 dBFS)
and `cover.png`.

Arc: HOOK (teaser: the jacket in every feed, `لاحقك؟` → rewind → visited, saw the jacket, left) → the jacket follows (Instagram · YouTube · everywhere) → FREEZE (صدفة؟ لأ.)
→ `Retargeting` (out and back) → the clothes shop (came in, tried, didn't buy; the salesperson remembers) → the Pixel
is the salesperson → warm vs stranger → don't repeat the same ad → the 3 rules → the line → comment PIXEL → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` once (the "bought" rule).
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`, copied from the Incrementality build.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the
  Incrementality copy). Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the charcoal.

## Audio pipeline
**Voiceover in use: the client's recording** (`audio/vo-human/`). See SCRIPT.md for the scan and wording notes.
```bash
python3 scripts/build_vo_human.py  # clean the recording, first word at 0.12s → audio/vo-human/vo_track.wav;
                                   # align its Scribe words to the 139 animation slots → scripts/cues.json
python3 scripts/apply_cues.py      # scene windows + CUES (word times) into index.html
python3 scripts/build_audio.py     # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- Every animation and subtitle time in `index.html` is `W(i)`, the start of word slot *i* (the word-index space of the
  first TTS take's Scribe pass, `scripts/vo_words.json`). `build_vo_human.py` maps any new recording onto those
  slots with difflib, so a re-recorded VO only needs a new Scribe pass (`scripts/vo_human_words.json`) and the three
  scripts.
- Reference only (not used): the ElevenLabs "Fadi" TTS take 4 in `audio/vo/` and `scripts/build_vo.py`.
- Music starts at frame 0 with no fade-in.
- SFX: three notification pops from frame 0, whoosh-thud on `لاحقك؟`, tape-rewind zip on `⏪`, tap on the jacket, three feed pops, a stop on "لأ", door bell, Pixel blips, card flicks, the gold-row
  positive click, Reignite chime. The music is kept low so a trending sound can be added in Instagram.
- Python deps: numpy, scipy, soundfile.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/retargeting-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS (re-measure with ebur128 if the mix changes):
ffmpeg -i renders/retargeting-raw.mp4 -c:v copy -af "volume=2.8dB,alimiter=limit=0.85:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/retargeting-explained.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```

`check` reports 17 `nested_structure_needs_subcomposition` warnings. This is the same single-file layout as the
Incrementality and Vanity Metrics builds; it does not affect the render.
