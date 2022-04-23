import textgrid
import os
import json
from tqdm import tqdm

def get_len(tg_path):
    info = {}
    total_info = {"count": 0, "total_time" : 0.0, "total_phone" : 0, "avg_time" : 0.0, "avg_phone" : 0, "max_time":0.0, "min_time":1e9, "max_phone":0, "min_phone":1e9}

    for speaker in tqdm(os.listdir(tg_path)):
        speaker_path = os.path.join(tg_path, speaker)
        speaker_info = {"count": 0, "total_time" : 0.0, "total_phone" : 0, "avg_time" : 0.0, "avg_phone" : 0}
        for tg_name in os.listdir(speaker_path):
            tg = textgrid.TextGrid()
            tg.read(os.path.join(speaker_path, tg_name))
            speaker_info["count"] += 1
            total_info["count"] += 1

            speaker_info["total_time"] += tg.maxTime
            total_info["total_time"] += tg.maxTime

            speaker_info["total_phone"] += len(tg.tiers[1].intervals)
            total_info["total_phone"] += len(tg.tiers[1].intervals)

            if tg.maxTime > total_info["max_time"]:
                total_info["max_time"] = tg.maxTime

            if tg.maxTime < total_info["min_time"]:
                total_info["min_time"] = tg.maxTime

            if len(tg.tiers[1].intervals) > total_info["max_phone"]:
                total_info["max_phone"] = len(tg.tiers[1].intervals)

            if len(tg.tiers[1].intervals) < total_info["min_phone"]:
                total_info["min_phone"] = len(tg.tiers[1].intervals)

        speaker_info["avg_time"] = speaker_info["total_time"] / speaker_info["count"]
        speaker_info["avg_phone"] = speaker_info["total_phone"] / speaker_info["count"]
        speaker_info["total_time"] = speaker_info["total_time"] / 3600

        info[speaker] = speaker_info

    total_info["avg_time"] = total_info["total_time"] / total_info["count"]
    total_info["avg_phone"] = total_info["total_phone"] / total_info["count"]
    total_info["total_time"] = total_info["total_time"] / 3600

    info["total"] = total_info

    with open("statistics10.json", "w") as f:
        f.write(json.dumps(info))

if __name__ == '__main__':
    get_len("preprocessed_data/hcsi_10speakers/TextGrid")
