for i in {0..9}; do
  python synthesize.py --restore_step 900000 --mode mul --lan en --text "the invention of movable metal letters in the middle of the fifteenth century may justly be considered as the invention of the art of printing."  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id $i
done