for i in {0..9}; do
  python synthesize.py --restore_step 900000 --mode mul --lan zh --text "总台记者在现场看到，飞机撞击点附近淤积较深，作业比较困难。目前，撞击点附近区域正采用人机协同作业方式，多方救援力量合作将泥土运出去。"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id $i
done