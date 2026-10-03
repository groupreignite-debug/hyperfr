# Reignite Group — "Why brands spend millions" (9:16 reel, 65s)

HyperFrames composition: `index.html` (1080×1920, 30fps).

Arc: SHOCK → ESCALATION ($1M → £1.7M/yr → $100M) → WHY? → REVEAL → PROOF (Coca-Cola, Google) → SYSTEM → PAYOFF → REIGNITE.

## 1. Brand assets

The brand logos in use are in `assets/brands/from-video/`. Each was cropped from a full-resolution frame of the
supplied reference video (*Billion Dollar Logos*, 720×1280). The pixels are unchanged: cropped only, with no recolouring,
redrawing, upscaling or background removal. They keep the black field they had in the source video, so they sit on dark
evidence cards. The two evolution plates (Coca-Cola, Google) sit on their original light backgrounds.

| File | Source frame |
| --- | --- |
| pepsi_old.png, pepsi_new.png | 2.5s |
| bbc_old.png, bbc_1997.png | 9.0s |
| accenture.png | 15.5s |
| andersen_consulting.png | 17.5s |
| coca_cola_evolution_plate.png | 40.5s |
| google_evolution_plate.png | 44.0s |

`npm run fetch-assets` still downloads the original vector files from the Brand Reference Pack into `assets/brands/`
when the network allows. Swap them into `index.html` for sharper logos.

The Reignite logo (`assets/reignite/reignite-group-logo.png`) is the supplied file, unchanged. It is only framed by a
container and composited with `mix-blend-mode: lighten` so its black field sits on the charcoal.

## 2. Preview / check / render

```bash
npm run check
npm run dev               # Studio preview
npm run render            # -> renders/reignite-branding-reel.mp4
# Instagram loudness (-14 LUFS):
ffmpeg -i renders/reignite-branding-reel.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.0:LRA=11 -c:a aac -b:a 256k renders/reignite-branding-reel-final.mp4
```

## Audio

- `audio/vo/` — voiceover lines (local Kokoro TTS, voice `bm_george`, 1.22×). Swap in a human VO with the same filenames; retime `data-start` in `index.html` if lengths change.
- `audio/music.wav`, `audio/sfx.wav` — procedural score + SFX from `scripts/build_audio.py`, driven by `scripts/cues.json` (VO starts are used to duck the music). Rebuild with `npm run audio`.
