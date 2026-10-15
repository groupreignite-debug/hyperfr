# Reignite Group — "Retargeting" (شو يعني؟, 9:16 Arabic reel, 62.2s = 2.0s intro + 60.2s film)

HyperFrames composition: `index.html` (1080×1920, 30fps). Brief: `BRIEF.md` · VO script + timings: `SCRIPT.md` ·
scene plan: `STORYBOARD.md` · Instagram caption: `CAPTION.md`.

Deliverables: `renders/retargeting-explained.mp4` (H.264 1080×1920 30fps, AAC, −14 LUFS, true peak ≈ −1.2 dBFS)
and `cover.png`.

Arc: INTRO (2.0s signature: `Retargeting` ignites, holds ~1s, burns away) → HOOK (teaser: the jacket in every feed, `لاحقك؟` → rewind → visited, saw the jacket, left) → the jacket follows (Instagram · YouTube · everywhere) → FREEZE (صدفة؟ لأ.)
→ `Retargeting` (out and back) → the clothes shop (came in, tried, didn't buy; the salesperson remembers) → the Pixel
is the salesperson → warm vs stranger → don't repeat the same ad → the 3 rules → the line → comment PIXEL → logo.

## Brand
- Palette: charcoal `#1A1A1A`, orange `#FF4D1A`, off-white `#F5F1EA`, gold `#FFB000` once (the "bought" rule).
- Type: Alexandria (Arabic + Latin, SIL OFL) in `assets/fonts/`, copied from the Incrementality build.
- Logo: `assets/reignite/reignite-group-logo.png` is the supplied file, unchanged (byte-identical to the
  Incrementality copy). Its clip uses `mix-blend-mode: lighten` so the PNG's black field sits on the charcoal.

## Signature intro (scene 00) and the film offset
The first 2.0s are a purely additive intro: `Retargeting` ignites left→right with an ember edge, a soft glow and a
light heat shimmer (SVG displacement, only while a front moves), holds crisp ~1s, then burns away with a few embers.
Everything after it is the film, unchanged:
- The film's GSAP timeline is authored in film time and nested into a master timeline at `INTRO` (1ms early so its
  time-0 states are applied on its first frame). `CUES` stays in film time.
- `scripts/apply_cues.py` offsets every scene clip, the subtitle track and the film's three audio tracks
  (VO, music, SFX) by `INTRO`; the root, ground and vignette span intro + film.
- The intro has its own sound (`scripts/build_intro_audio.py` → `audio/intro.wav`, `<audio id="a-intro">` at 0s);
  `audio/music.wav`, `audio/sfx.wav` and the VO are not touched by it.
- Verified on the render: every film frame (n+60) matches the pre-intro render (n), and the film audio is offset by
  exactly 0 samples, except the two bug fixes below.

Fixes found in the frame-by-frame check (they were in the pre-intro render too): the scene-08 ad stack now slides away
on "بيزهق" instead of being cut mid-slide at the scene end, and the scene-09 rows 1–2 now fade out with row 3 instead
of popping off.

## Audio pipeline
**Voiceover in use: the client's recording** (`audio/vo-human/`). See SCRIPT.md for the scan and wording notes.
```bash
python3 scripts/build_vo_human.py  # clean the recording, first word at 0.12s → audio/vo-human/vo_track.wav;
                                   # align its Scribe words to the 139 animation slots → scripts/cues.json
python3 scripts/apply_cues.py      # scene windows + CUES (word times) into index.html
python3 scripts/build_audio.py     # procedural music bed (pre-ducked under the VO) + SFX on the same cues
python3 scripts/build_intro_audio.py  # the 2.0s intro's ember sound → audio/intro.wav
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
# Instagram loudness: -14 LUFS, true peak < -1 dBFS. With the intro track the renderer's mix comes out ~0.6 dB hotter,
# so 2.19 dB (not 2.8) keeps the film's audio at exactly its previous level (re-measure with ebur128 if the mix changes):
ffmpeg -i renders/retargeting-raw.mp4 -c:v copy -af "volume=2.19dB,alimiter=limit=0.85:attack=3:release=60:level=false,aresample=48000" -c:a aac -b:a 256k renders/retargeting-explained.mp4
python3 scripts/build_cover.py        # cover/cover.html -> cover.png
```

`check` reports 17 `nested_structure_needs_subcomposition` warnings. This is the same single-file layout as the
Incrementality and Vanity Metrics builds; it does not affect the render.
