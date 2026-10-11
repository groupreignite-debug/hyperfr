# Reignite Group — "A/B Testing" (شو يعني؟, 9:16 Arabic reel, 65.1s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script + timings: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/ab-testing-explained.mp4` (H.264 1080×1920 30fps, AAC, −14.2 LUFS, true peak −1.1 dBFS)
and `cover.png`.

Arc: HOOK (an ad fails, another does a bit better, why?) → guessing (the dart misses) → `A/B Testing` (two versions,
people decide) → the juice shop → flyer A vs flyer B → split the crowd → count the flyers (B's pile is taller) →
"the numbers are talking" → change ONE thing → don't judge on day one → same idea in ads → the winner is what the
numbers say → comment what you'd test → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` once (the winner, scene 12).
- A = off-white outline card, B = solid orange card, in every scene; A on the right, B on the left.
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`, copied from the earlier episodes.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the Incrementality
  copy). Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the charcoal.

## Audio pipeline
```bash
python3 scripts/build_vo.py      # take 2 → 1.07x, +7 dB, 0.3s lead → audio/vo/vo_track.wav; Scribe words → scripts/cues.json
python3 scripts/apply_cues.py    # scene windows + CUES (word times) into index.html
python3 scripts/build_audio.py   # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- `audio/vo/vo_full.mp3`: the chosen ElevenLabs take, as delivered. `scripts/vo_words.json`: its Scribe word timings.
  Line → word-index ranges are `LINES` in `build_vo.py`; every animation and subtitle time in `index.html` is `W(i)`,
  the start of Scribe word *i*. So a different take only needs a new Scribe pass, an index check, and the three scripts.
- SFX: dull buzz on the ✗, dart whoosh + knock on the miss, paper flutter for the flyers, shop-door bell and paper
  stacking ticks in the count, rubber-stamp thump for `1`, calendar page flips, a soft positive chime when B wins,
  the Reignite chime. Very low street ambience under the shop scenes. Stems: VO −23.3 LUFS, music −29.2, SFX −30.6,
  so the VO stays the loudest element and a trending sound can still be added in Instagram.
- Python deps: numpy, scipy, soundfile.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/ab-testing-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS (measured -14.2 LUFS / -1.1 dBTP; re-measure with ebur128 if the mix changes):
ffmpeg -i renders/ab-testing-raw.mp4 -c:v copy -af "volume=6.3dB,alimiter=limit=0.85:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/ab-testing-explained.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```

`check` reports 21 warnings (`nested_structure_needs_subcomposition` and file-size hints). This is the same
single-file layout as the earlier episodes; it does not affect the render. The CLI stays pinned to 0.8.127 like the
other شو يعني؟ episodes.
