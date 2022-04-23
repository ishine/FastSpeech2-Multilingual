for i in 0.8 1 1.2; do
  python synthesize.py --restore_step 900000 --mode mul --lan en --text "produced the block books, which were the immediate predecessors of the true printed book"  -p config/hcsi_10speakers/preprocess.yaml -m config/hcsi_10speakers/model.yaml -t config/hcsi_10speakers/train.yaml --speaker_id $i
done