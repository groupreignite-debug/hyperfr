# SCRIPT: Retargeting (client-recorded VO)

**The voiceover in use is the client's own recording** (`audio/vo-human/src/vo_human_raw.m4a`, WhatsApp AAC 64 kb/s
mono, 59.2s, received Oct 13). `scripts/build_vo_human.py` cleans it (80 Hz HPF, −2.5 dB at 220 Hz, +2 dB presence at
3.2 kHz, air, de-ess, 3:1 compression, limiter), trims everything before the first word so it lands at 0.12s (Oct 15 hook update: first word within ~0.15s), and plays it as one
continuous take at its own pace: no cuts, no tempo change. ElevenLabs Scribe word timings (`scripts/vo_human_words.json`)
are aligned onto the animation's 139 word slots, so every scene, subtitle and SFX cue follows the recording.
Times below are film seconds. The subtitle text is the brief's line, except where the recording clearly differs (11, 14).
**One text layer rule:** the bottom subtitle is hidden for line 03 (FREEZE), line 13 (LINE beat) and the second half of
line 14 (CTA), because the centre shows those words big.

| # | start | end | line (= subtitle text) |
|---|-------|-----|------------------------|
| 01 | 0.12 | 2.92 | فتت مرة على موقع، شفت جاكيت حلو… وفلّيت. |
| 02 | 3.32 | 6.60 | تاني يوم، صار الجاكيت لاحقك: عـ Instagram، عـ YouTube، بكل مكان. |
| 03 | 7.04 | 8.14 | صدفة؟ لأ. |
| 04 | 8.84 | 10.02 | هيدا اسمو Retargeting. |
| 05 | 10.56 | 13.66 | يعني ترجع توصل للناس اللي شافوك قبل، بس ما اشتروا. |
| 06 | 14.14 | 17.56 | تخيّل محل تياب. حدا فات، جرّب، وطلع بلا ما يشتري. |
| 07 | 18.08 | 22.62 | البيّاع الشاطر ما بينساه. بس يرجع يمرق، بيقلّو: "بعدها القطعة ناطرتك." |
| 08 | 23.20 | 28.94 | عالإنترنت، الـ Pixel هوي البيّاع. كود صغير بموقعك، بيتذكّر مين فات، وعلى أي صفحة. |
| 09 | 29.56 | 33.58 | وليش هالشي مهم؟ لأن هيدا الشخص بيعرفك. ما عم تبلّش معو من الصفر. |
| 10 | 34.64 | 37.94 | بس انتبه: ما تفرجيه نفس الإعلان كل يوم، هيك بيزهق. |
| 11 | 38.64 | 43.84 | اللي شاف المنتج، فرجيه مرة تانية. واللي حطّو بالسلة، ذكّرو إنو بعدو ناطرو. *(no "ياه" in the recording)* |
| 12 | 44.48 | 46.24 | وإذا اشترى؟ وقّف الإعلان عنو. |
| 13 | 46.88 | 51.70 | مش كل إعلان لازم يحكي مع ناس جداد. أحياناً أقرب زبون… هوي اللي فات وفلّ. |
| 14 | 52.42 | 56.64 | موقعك فيه Pixel؟ اكتب PIXEL بالكومنت، ومنقلّك كيف تتأكد. *(recording says "بالـ comment")* |

End card: 57.24–60.24s.

## What the scan found (recording vs. brief script)
- **Audio quality:** clean. Noise floor ≈ −85 dB (phone noise suppression), no clipping, raw level −29 LUFS
  (−18.8 LUFS after cleanup). Pace is a little brisker than the TTS take (56.5s of speech → 60.2s film).
- **All 14 lines are present and in order.** English terms (`Instagram`, `YouTube`, `Retargeting`, `pixel`) come back
  from Scribe in Latin script.
- **Wording differences** (subtitles follow the brief unless noted):
  - Line 11: "فرجيه **ياه** مرة تانية" → "فرجيه مرة تانية" (no "ياه"). **Subtitle follows the recording.** The on-screen
    rule card in scene 09 keeps the brief's exact text.
  - Line 14: "بالكومنتات" → "بالـ comment". **Subtitle uses "بالكومنت"** so that only the brief's listed terms are in Latin.
  - Line 07: Scribe hears "بينسى" / "بيمر" / "بعده على القطعة" for "بينساه" / "يمرق" / "بعدها القطعة". Most likely
    accent or transcription. Subtitles keep the brief's text.
  - Line 02: Scribe writes "لايحك" for "لاحقك" (transcription). Line 13 has no extra "لنا" (unlike the TTS take).

The earlier ElevenLabs TTS take (Fadi, take 4) is kept for reference in `audio/vo/` with `scripts/build_vo.py`.
It is no longer used in the film.
