python prepare_align.py config/LJSpeech/preprocess.yaml
python preprocess.py config/LJSpeech/preprocess.yaml
CUDA_VISIBLE_DEVICES=1,2 python train.py -p config/LJSpeech/preprocess.yaml -m config/LJSpeech/model.yaml -t config/LJSpeech/train.yaml
python synthesize.py --text "his mother, however, was a little shy of the company for him, and besides she could not always spare him."  --speaker_id 1 --restore_step 20000 --mode single -p config/LibriTTS/preprocess.yaml -m config/LibriTTS/model.yaml -t config/LibriTTS/train.yaml --duration_control 1 --pitch_control 1 --energy_control 1
python synthesize.py --text "The main differences from the LibriSpeech corpus are listed below"  --speaker_id 5 --restore_step 200000 --mode single -p config/LibriTTS/preprocess.yaml -m config/LibriTTS/model.yaml -t config/LibriTTS/train.yaml --duration_control 1 --pitch_control 1 --energy_control 1
--restore_step 900000 --mode list -p config/LJSpeech/preprocess.yaml -m config/LJSpeech/model.yaml -t config/LJSpeech/train.yaml



--disable_textgrid_cleanup --optional_silence_phone sp --other_noise_phone onp
mfa train raw_data/AISHELL3/ lexicon/pinyin-lexicon-r.txt new_acoustic_model.zip preprocessed_data/AISHELL3 --clean --disable_textgrid_cleanup --optional_silence_phone sp --other_noise_phone onp
python preprocess.py config/AISHELL3/preprocess.yaml
env CUDA_VISIBLE_DEVICES=2 python train.py -p config/AISHELL3/preprocess.yaml -m config/AISHELL3/model.yaml -t config/AISHELL3/train.yaml

env CUDA_VISIBLE_DEVICES=2 python synthesize.py --text "您好，请问有什么可以帮到您" --speaker_id 17 --restore_step 90000 --mode single -p config/AISHELL3/preprocess.yaml -m config/AISHELL3/model.yaml -t config/AISHELL3/train.yaml
python prepare_align.py config/AISHELL3/preprocess.yaml



mfa align raw_data/hcsi_10speakers/Spk0.EN.LJSpeech/ lexicon/librispeech-lexicon.txt english preprocessed_data/hcsi_10speakers/Spk0.EN.LJSpeech/ --clean --disable_textgrid_cleanup --optional_silence_phone sp --other_noise_phone onp


env CUDA_VISIBLE_DEVICES=2 python train.py -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml
env CUDA_VISIBLE_DEVICES=2 python train.py -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml

python synthesize.py --restore_step 900000 --mode mul --lan zh --text "您好，请问有什么可以帮到您"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id 1
python synthesize.py --restore_step 900000 --mode mul --lan en --text "stay cool he added, with a smile"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id 4 --energy_control 1.0 --pitch_control 1.0

# child
python synthesize.py --restore_step 900000 --mode mul --lan en --text "the invention of movable metal letters in the middle of the fifteenth century may justly be considered as the invention of the art of printing."  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 2
python synthesize.py --restore_step 900000 --mode mul --lan zh --text "总台记者在现场看到，飞机撞击点附近淤积较深，作业比较困难。目前，撞击点附近区域正采用人机协同作业方式，多方救援力量合作将泥土运出去。"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 9
python synthesize.py --restore_step 900000 --mode mul --lan zh --text "老虎幼崽与宠物犬玩耍"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 9
五年来，从完成顶层设计到展开大规模实质性建设，这座未来之城从“一张白纸”着墨，稳扎稳打，目前已进入承接北京非首都功能和建设同步推进的重要阶段，一幅高质量发展的美好画卷

# noad
python synthesize.py --restore_step 50000 --mode mul --lan en --text "stay cool he added, with a smile"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id 4

# mixed
python synthesize.py --restore_step 900000 --mode mixed --text "声音的英文是"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 5
python synthesize.py --restore_step 900000 --mode mixed --text "语音合成技术(Text To Speech)，它涉及声学(acoustics)，信号处理技术(Signal processing technology)，多媒体技术(multimedia technology)等多个学科技术"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 2
python synthesize.py --restore_step 900000 --mode mixed --text "Python有五个标准的数据类型，包括Numbers数字，String字符串，List列表，Tuple元组，Dictionary字典"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 9
python synthesize.py --restore_step 900000 --mode mixed --text "Python有五个标准的数据类型，包括（数字），（字符串），（列表），（元组），（字典）"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 2
python synthesize.py --restore_step 900000 --mode mixed --text "“您好，请问有什么可以帮到您”的英文是Hello, may I help you"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 2
python synthesize.py --restore_step 900000 --mode mixed --text "“数字数据类型用于存储数值”的英文是The numeric data type is used to store numeric values"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 2
python synthesize.py --restore_step 900000 --mode mixed --text "“what can i help you”的中文是你好，有什么可以帮你"  -p config/12speakers/preprocess.yaml -m config/12speakers/model.yaml -t config/12speakers/train.yaml --speaker_id 2



python synthesize.py --restore_step 900000 --mode mixed --text "在Text或Speech，我们常用欧氏距离来计算最近的邻居之间的距离，有时也用曼哈顿距离，请对比下这两种距离的差别。"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id 5
python synthesize.py --restore_step 900000 --mode mixed --text "Numbers如何寻找最优特征？是有放回还是无放回的呢？"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id 5

