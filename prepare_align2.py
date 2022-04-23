import os

import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm

from text import _clean_text


def prepare_audio():
    in_dir = '/ceph/datasets/hcsi_10speakers/MultiSets/Spk2.CN.Deng'
    out_dir = 'raw_data/hcsi_10speakers/Spk2.CN.Deng'
    sampling_rate = 22050
    max_wav_value = 32767.0
    count = 0
    with open(os.path.join(in_dir, "prompts.csv.txt"), encoding="utf-8") as f:
        for line in tqdm(f):
            # print(line)
            parts = line.strip().split("|")
            base_name = parts[0][-6:]
            text = parts[2]

            wav_path = os.path.join(in_dir, "wave.48k", "{}.wav".format(base_name))
            if os.path.exists(wav_path):  
                # os.makedirs(os.path.join(out_dir, speaker), exist_ok=True)
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

