"""Arabic voiceover via offline Piper VITS (sherpa-onnx).

Usage: python3 scripts/build_vo.py <model_dir> [speed]
model_dir: an extracted sherpa-onnx piper model, e.g. vits-piper-ar_JO-kareem-medium
(https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models).
Reads audio/vo/lines.tsv (diacritized text for the TTS) and writes audio/vo/vo_NN.wav (48 kHz mono)
plus audio/vo/durations.json. Swap in a human VO with the same filenames for the final cut.
"""
import glob, json, sys
from pathlib import Path

import numpy as np
import sherpa_onnx
import soundfile as sf
from scipy.signal import resample_poly

ROOT = Path(__file__).resolve().parent.parent
model_dir = Path(sys.argv[1])
speed = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
onnx = glob.glob(str(model_dir / "*.onnx"))[0]
tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
    vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=onnx, tokens=str(model_dir / "tokens.txt"),
                                               data_dir=str(model_dir / "espeak-ng-data")),
    num_threads=4)))

durs = {}
for line in (ROOT / "audio/vo/lines.tsv").read_text().strip().splitlines():
    key, text, *rest = line.split("\t")
    a = tts.generate(text, sid=0, speed=float(rest[0]) if rest else speed)
    x = np.asarray(a.samples, dtype=np.float64)
    x = resample_poly(x, 160, 147) if a.sample_rate == 44100 else resample_poly(x, 320, 147)  # 22.05k -> 48k
    # trim leading/trailing silence, short fades, normalise to -3 dBFS peak
    nz = np.where(np.abs(x) > 0.01)[0]
    x = x[max(0, nz[0] - 960): nz[-1] + 5760]
    f = 480
    x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
    x *= 0.708 / np.max(np.abs(x))
    sf.write(ROOT / f"audio/vo/vo_{key}.wav", x.astype(np.float32), 48000)
    durs[key] = round(len(x) / 48000, 3)
    print(key, durs[key])
(ROOT / "audio/vo/durations.json").write_text(json.dumps(durs, indent=1))
