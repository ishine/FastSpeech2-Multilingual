# FastSpeech 2 - Multilingual

运行方法

```shell
python synthesize.py --restore_step 900000 --mode mixed --text "Numbers如何寻找最优特征？是有放回还是无放回的呢？"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id 5 --duration_control 1 --pitch_control 1 --energy_control 1
```



说话人

speaker 0-9：

+ 0  Spk4.CN.03FR00

+ 1  Spk9.EN.F.DB2

+ 2  Spk8.EN.F.DB1

+ 3  Spk2.CN.Deng

+ 4  Spk1.CN.DataBaker

+ 5  Spk6.CN.Pachira

+ 6  Spk7.EN.M.DB1

+ 7  Spk3.EN.XuYue

+ 8  Spk5.CN.03MR00

+ 9  Spk0.EN.LJSpeech  





mfa提取

```shell
mfa align raw_data/hcsi_10speakers/Spk0.EN.LJSpeech/ lexicon/librispeech-lexicon.txt english preprocessed_data/hcsi_10speakers/Spk0.EN.LJSpeech/ --clean --disable_textgrid_cleanup --optional_silence_phone sp --other_noise_phone onp


# new_acoustic_model 放在 /ceph/home/huangqc18/Documents/MFA/pretrained_models/acoustic中
mfa adapt raw_data/hcsi_10speakers/Spk1.CN.DataBaker/ lexicon/pinyin-lexicon-r.txt new _acoustic_model preprocessed_data/hcsi_10speakers/Spk1.CN.DataBaker/ --clean --disable_textgrid_cleanup --optional_silence_phone sp --other_noise_phone onp
```



# References
- [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558), Y. Ren, *et al*.
- [ming024's FastSpeech implementation](https://github.com/ming024/FastSpeech2)



