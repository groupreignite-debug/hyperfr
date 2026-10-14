# Reignite Group — "A/B Testing" v2 (شو يعني؟, 9:16 Arabic reel, 50.9s)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script + timings: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/ab-testing-explained.mp4` (H.264 1080×1920 30fps, AAC, −14.3 LUFS, true peak −1.1 dBFS)
and `cover.png`.

Arc (v2 brief, Oct 14): HOOK (two ad cards, coins pouring out, `؟` at 1s: which one is wasting your money?) → your
gut (the dart misses) → `A/B Testing` (two versions, people decide) → the juice shop → flyer A vs flyer B → split the
crowd and count the flyers (B's pile is taller) → "the numbers are talking" → change ONE thing → don't judge on day
one → the winner is what the numbers say → comment what you'd test → logo. Frame 0 is already full, there's no logo
in the opening, and music + coin SFX start at frame 0.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` once (the winner, scene 10).
- A = off-white outline card, B = solid orange card, in every scene; A on the right, B on the left.
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`, copied from the earlier episodes.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the Incrementality
  copy). It appears only on the end card. Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the
  charcoal.

## Audio pipeline
```bash
python3 scripts/build_vo.py      # v2 take 1, no speed-up, +9.7 dB, from frame 0 → audio/vo/vo_track.wav; Scribe words → scripts/cues.json
python3 scripts/apply_cues.py    # scene windows + CUES (word times) into index.html
python3 scripts/build_audio.py   # procedural music bed (pre-ducked under the VO) + SFX on the same cues
```
- `audio/vo/vo_full.m4a`: the chosen ElevenLabs take (v2 take 1), byte-for-byte as delivered (it came as an audio-only
  `.mp4`, so it stays AAC rather than being re-encoded to the brief's `vo_full.mp3`). `scripts/vo_words.json`: its Scribe word timings.
  Line → word-index ranges are `LINES` in `build_vo.py`; every animation and subtitle time in `index.html` is `W(i)`,
  the start of Scribe word *i*. So a different take only needs a new Scribe pass, an index check, and the three scripts.
- SFX: coin clinks from frame 0 and a dry thud when `؟` lands, dart whoosh + knock on the miss, paper flutter for the
  flyers, shop-door bell and paper stacking ticks in the count, rubber-stamp thump for `1`, calendar page flips, a soft
  positive chime when B wins, the Reignite chime. Very low street ambience under the shop scenes. Stems: VO −23.3 LUFS,
  music −28.0, SFX −30.1, so the VO stays the loudest element and a trending sound can still be added in Instagram.
- Python deps: numpy, scipy, soundfile.

## Commands
```bash
npm run check                         # lint + runtime + layout + contrast
npx hyperframes preview --background  # Studio
npx hyperframes@0.8.127 render --quality high --fps 30 --output renders/ab-testing-raw.mp4
# Instagram loudness: -14 LUFS, true peak < -1 dBFS (measured -14.3 LUFS / -1.1 dBTP; re-measure with ebur128 if the mix changes):
ffmpeg -i renders/ab-testing-raw.mp4 -c:v copy -af "volume=6.2dB,alimiter=limit=0.8:attack=2:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/ab-testing-explained.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```

`check` reports 18 warnings (`nested_structure_needs_subcomposition` and file-size hints). This is the same
single-file layout as the earlier episodes; it does not affect the render. The CLI stays pinned to 0.8.127 like the
other شو يعني؟ episodes.
