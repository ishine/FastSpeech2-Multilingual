import os

import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm

from text import _clean_text


def prepare_audio():
    in_dir = '/ceph/datasets/hcsi_10speakers/MultiSets/Spk7.EN.M.DB1'
    out_dir = 'raw_data/hcsi_10speakers/Spk7.EN.M.DB1'
    sampling_rate = 22050
    max_wav_value = 32767.0
    cleaners = ["english_cleaners"]
    count = 0
    with open(os.path.join(in_dir, "metadata.csv.txt"), encoding="utf-8") as f:
        for line in tqdm(f):
            # print(line)
            parts = line.strip().split("|")
            base_name = parts[0][-6:]
            print(base_name)
            text = parts[1]
            text = _clean_text(text, cleaners)

            wav_path = os.path.join(in_dir, "Wave.48k", "{}.wav".format(base_name))
            print(wav_path)
            # print(os.path.exists(wav_path))
            if os.path.exists(wav_path):  
                # os.makedirs(os.path.join(out_dir, speaker), exist_ok=True)
                # print(base_name)
                wav, _ = librosa.load(wav_path, sampling_rate)
                wav = wav / max(abs(wav)) * max_wav_value
                wavfile.write(
                    os.path.join(out_dir,  "{}.wav".format(base_name)),
                    sampling_rate,
                    wav.astype(np.int16),
                )
                with open(
                    os.path.join(out_dir,  "{}.lab".format(base_name)),
                    "w",
                ) as f1:
                    f1.write(text)
                




if __name__ == '__main__':
    prepare_audio()

