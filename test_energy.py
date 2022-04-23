import soundfile as sf
from scipy.io import wavfile

if __name__ == '__main__':
    sig, sample_rate = sf.read('demo/sen0005.wav')
    sf.write(
        "demo/sen00052.wav",
        sig * 0.2,
        sample_rate,
        subtype='PCM_16'
    )