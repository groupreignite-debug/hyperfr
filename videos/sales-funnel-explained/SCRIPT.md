# SCRIPT: Sales Funnel (client voiceover)

**Voice used in the reel:** the client recording `AUD-20261013-WA0100.m4a` (Oct 13), kept as
`audio/vo-human/src/vo_human_raw.m4a` (WhatsApp AAC 65 kb/s mono, 55.0s). `scripts/build_vo_human.py` cleans it
(EQ for the phone mic, de-ess, light compression, levelled to −23 LUFS like the TTS track the mix was balanced on)
and tightens three silences only: the 1.06s lead-in → 0.40s, the 1.5s breath between lines 10 and 11 → 0.75s, and a
0.9s mid-sentence hesitation in line 12 → 0.4s. No time-stretch, no words cut. Word timings: ElevenLabs Scribe
(`scripts/vo_human_words.json`, Scribe flow `M7KMp6NVxT8H2QSBmbHQ`). Times below are film seconds.

| # | start | end | line (as written in the brief = subtitle text) |
|---|-------|-----|------------------------------------------------|
| 01 | 0.39 | 2.69 | ليش ما حدا بيشتري منك من أول مرة بيشوفك؟ *(shown big in scene 01; subtitle hidden)* |
| 02 | 3.06 | 4.91 | لأن الناس ما بيشتروا من حدا ما بيعرفوه. |
| 03 | 5.49 | 6.84 | هيدا اسمو Sales Funnel. |
| 04 | 7.21 | 10.80 | يعني الطريق اللي بيمشيه الزبون، من أول مرة بيسمع فيك، لحد ما يشتري. |
| 05 | 11.32 | 12.87 | تخيّل في قهوة جديدة بحيّك. |
| 06 | 13.24 | 16.70 | أول مرة بتمرق قدّامها، بس بتلاحظها. هيدي الـ Awareness. |
| 07 | 17.18 | 22.57 | بعدين بتشمّ الريحة، بتشوف الناس قاعدين، بتقرا الريفيوز. هيدا الـ Consideration. |
| 08 | 23.16 | 26.20 | وبيوم، بتفوت وبتطلب أول فنجان. هيدا الـ Decision. |
| 09 | 26.91 | 30.73 | وإذا عجبتك؟ بترجع كل يوم، وبتخبّر رفقاتك. هيدي الـ Loyalty. |
| 10 | 31.34 | 35.05 | الغلطة؟ إنك تطلب من حدا يشتري، وهوي بعدو أول مرة عم يشوفك. |
| 11 | 35.78 | 42.96 | كل مرحلة إلها رسالة. للي ما بيعرفك، علّمو شي. للي عم يفكّر، فرجيه ليش إنت. وللي جاهز، سهّلّو يشتري. |
| 12 | 43.66 | 46.52 | ومش كل الناس بيكمّلوا الطريق، وهيدا طبيعي. |
| 13 | 47.06 | 48.65 | المهم تعرف وين عم تخسرهن. |
| 14 | 49.06 | 52.06 | بأي مرحلة عم تخسر زباينك؟ اكتبلنا بالكومنتات. |

End card: 52.66–55.66s.

## Check of the recording against the script (Scribe pass)
- **Complete and in order:** all 14 lines, 131 words, no repeats, no outtakes, no missing phrases.
- **English terms:** Scribe returned `Sales Funnel`, `Awareness`, `Consideration`, `Decision` and `Loyalty` in Latin
  script (capitalised), a good sign they were said as English. A quick listen still confirms it.
- **No stumble:** the stray "أم" that the TTS take had in line 11 is not in this recording.
- **Small wording differences Scribe heard** (subtitles keep the brief's text in every case):
  - line 04 `اللي بيمشي الزبون` (script: `بيمشيه`)
  - line 11 `علموه شي` (script: `علّمو شي`), `اللي ما بيعرفك` / `اللي عم يفكر` (script: `للي`)
  - line 12 `وهيدا الطبيعي` (script: `وهيدا طبيعي`)
  - line 14 `اكتبنا` (script: `اكتبلنا`); `إذا بينك` is Scribe mishearing `زباينك`
  These are natural spoken variants or transcription spellings, not errors worth a re-record. Salem may want to
  listen to line 12 (`الطبيعي`) once.
- **Audio quality:** clean (noise floor ≈ −80 dB, no clipping, steady level ±1.5 dB), but phone-band: the top end
  above 5 kHz is 10–17 dB below the TTS take, so the clean-up adds presence and a high shelf. It sounds like a good
  phone recording, not a studio mic.

## Fallback: TTS take
The earlier ElevenLabs "Fadi" take 3 (flow `b2xrMxWciA7lUhILktXK`) is still in `audio/vo/` with `scripts/build_vo.py`
and `scripts/vo_words.json`. To switch back: run `build_vo.py`, point `#a-vo` in `index.html` at
`audio/vo/vo_track.wav`, then `apply_cues.py` and `build_audio.py`.
