# Reignite Group — "Why brands spend millions" (9:16 reel, 65s)

HyperFrames composition: `index.html` (1080×1920, 30fps).

Arc: SHOCK → ESCALATION ($1M → £1.7M/yr → $100M) → WHY? → REVEAL → PROOF (Coca-Cola, Google) → SYSTEM → PAYOFF → REIGNITE.

## 1. Add the real brand assets (required before the final render)

```bash
npm install
npm run fetch-assets      # downloads the exact files from the Brand Reference Pack into assets/brands/
```

The Coca-Cola evolution link in the pack is a Pinterest page, not an image: save that image by hand as
`assets/brands/04_Coca_Cola/Coca_Cola_evolution_reference.jpg`.

Until a file exists, its card shows a labelled "supplied asset pending" slot. No logo is ever redrawn or substituted.
Assets are shown with `object-fit: contain` on warm off-white evidence cards — original colours and proportions.

The Reignite logo (`assets/reignite/reignite-group-logo.png`) is the supplied file, unchanged; it is only framed
(cropped by a container) and composited with `mix-blend-mode: lighten` so its black field sits on the charcoal.

## 2. Preview / check / render

```bash
npm run check
npm run dev               # Studio preview
npm run render            # -> renders/reignite-branding-reel.mp4
```

## Audio

- `audio/vo/` — voiceover lines (local Kokoro TTS, voice `bm_george`, 1.22×). Swap in a human VO with the same filenames; retime `data-start` in `index.html` if lengths change.
- `audio/music.wav`, `audio/sfx.wav` — procedural score + SFX from `scripts/build_audio.py`, driven by `scripts/cues.json` (VO starts are used to duck the music). Rebuild with `npm run audio`.
