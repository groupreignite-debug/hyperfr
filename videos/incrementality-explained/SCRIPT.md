# SCRIPT: Incrementality (client-recorded VO)

The voiceover is the client's own recording (`audio/vo-human/src/vo_human_raw.m4a`). The transcript below is
ElevenLabs Scribe's reading of it, laid out at the film's timings. The outtake at the end of the take
("نسيتها، هاه؟ لا، دوري نقول هذي؟") is cut.

| # | start (s) | line (as spoken) |
|---|-----------|------------------|
| 01 | 0.45 | صرفت 10 آلاف دولار على الإعلانات، وجبت 30 ألف دولار مبيعات، |
| 02 | 5.27 | بس هالـ إعلان فعلًا جاب كل هالمبيعات؟ |
| 03 | 7.96 | تخيل عندك 100 عميل، أربعين اشتروا، |
| 04 | 10.52 | بس 25 منهم كانوا راح يشتروا أصلًا حتى لو ما شافوا الإعلان. |
| 05 | 14.45 | يعني الإعلان فعليًا جايب لك 15 بيعة إضافية. |
| 06 | 17.80 | هون بيجي مفهوم اسمه Incrementality. |
| 07 | 20.27 | في فرق كبير بين Attribution و Incrementality. |
| 08 | 23.58 | Attribution بيسألك كم بيعة منقدر ننسبها للإعلان، |
| 09 | 26.92 | أما Incrementality بيسألك كم بيعة ما كانت راح تصير بدونه. |
| 10 | 30.96 | وأبسط طريقة تفهم فيها الفكرة إنك تقارن بين مجموعة شافت الإعلان ومجموعة ما شافته. |
| 11 | 36.55 | إذا الأولى جابت 50 بيعة والتانية 35، فالفرق 15 هو الزيادة الناتجة عن الإعلان. |
| 12 | 43.40 | يعني ممكن المنصة تقولك الـ ROAS ضرب خمس أضعاف، |
| 13 | 47.67 | بس لما تقيس التأثير الحقيقي للإعلان الـ Incremental ROAS بيكون أقل بكتير. |
| 14 | 53.28 | لذلك السؤال الحقيقي مش كم بيعة جاب الإعلان، |
| 15 | 56.50 | السؤال الحقيقي كم بيعة ما كانت حتصير بدونه. |
| 16 | 59.96 | حافظ على المصطلح Incrementality. |

Pipeline: `scripts/build_vo_human.py` (clean + cut + re-space + time map) → `scripts/apply_timemap.py`
(writes the map into `index.html`) → `scripts/build_audio.py` (score/SFX on the same map).
The earlier ElevenLabs TTS take is kept in `audio/vo/` for reference. It is no longer used in the film.
