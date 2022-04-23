import os

import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm

from text import _clean_text


def prepare_audio():
    in_dir = '/ceph/datasets/hcsi_10speakers/MultiSets/Spk3.EN.XuYue'
    out_dir = 'raw_data/hcsi_10speakers/Spk3.EN.XuYue'
    sampling_rate = 22050
    max_wav_value = 32767.0
    cleaners = ["english_cleaners"]
    for file_name in tqdm(os.listdir(os.path.join(in_dir, 'wave'))):
        wav_path = os.path.join(in_dir, 'wave', file_name)
        if os.path.exists(wav_path):
            wav, _ = librosa.load(wav_path, sampling_rate)
            wav = wav / max(abs(wav)) * max_wav_value
            wavfile.write(
                os.path.join(out_dir, file_name),
                sampling_rate,
                wav.astype(np.int16),
            )

def prepare_text():
    in_dir = '/ceph/datasets/hcsi_10speakers/MultiSets/Spk3.EN.XuYue/text'
    text_dir = ["700001-701132.sen", "800001-810000.sen"]
    out_dir = 'raw_data/hcsi_10speakers/Spk3.EN.XuYue'
    sampling_rate = 22050
    max_wav_value = 32767.0
    cleaners = ["english_cleaners"]
    for t_dir in text_dir:
        with open(os.path.join(in_dir, t_dir), encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                name = line[:6]
                text = line[7:]
                text = _clean_text(text, cleaners)
                with open(os.path.join(out_dir, f"{name}.lab"), "w") as f1:
                    f1.write(text)


if __name__ == '__main__':
    prepare_audio()
    # prepare_text()

