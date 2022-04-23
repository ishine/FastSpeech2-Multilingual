from sklearn.manifold import TSNE
import yaml
from utils.model import get_model
import torch
import argparse
import numpy as np
import matplotlib.pyplot as plt
from text import text_to_sequence

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

preprocess_config = yaml.load(
    open("config/12speakers/preprocess.yaml", "r"), Loader=yaml.FullLoader
)
model_config = yaml.load(open("config/12speakers/model.yaml", "r"), Loader=yaml.FullLoader)
train_config = yaml.load(open("config/12speakers/train.yaml", "r"), Loader=yaml.FullLoader)

configs = (preprocess_config, model_config, train_config)

# weight = model.speaker_emb.weight.data.cpu().numpy()
# labels = np.array(['r', 'b', 'g', 'b', 'r', 'r', 'r', 'b', 'b', 'g', 'r', 'b'])


#phoneme en 64~147  zh 149~357

# 97 ER0 234 ian3

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--restore_step", type=int, default=900000)
    args = parser.parse_args()
    # Get model
    model = get_model(args, configs, device, train=False)
    weight = model.encoder.src_word_emb.weight.data.cpu().numpy()
    text_to_sequence("aaaa",[])

    # en_weight, zh_weight = weight[64:148], weight[149:358]
    # en_labels, zh_labels = np.full(en_weight.shape[0], "b"), np.full(zh_weight.shape[0], "r")
    # weight = np.concatenate((en_weight, zh_weight))
    # labels = np.concatenate((en_labels, zh_labels))
    weight = model.speaker_emb.weight.data.cpu().numpy()
    labels = np.array(['r', 'b', 'g', 'b', 'r', 'r', 'r', 'b', 'b', 'g', 'r', 'b'])
    X_tsne = TSNE(n_components=2, random_state=2333).fit_transform(weight)


    plt.cla()
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels)
    txt = ["Spk4.CN.03FR00", "Spk9.EN.F.DB2", "child", "Spk8.EN.F.DB1", "Spk2.CN.Deng", "Spk1.CN.DataBaker", "Spk6.CN.Pachira", "Spk7.EN.M.DB1", "Spk3.EN.XuYue", "tts-DB-EN-M-01", "Spk5.CN.03MR00", "Spk0.EN.LJSpeech"]

    for i in range(X_tsne.shape[0]):
        plt.annotate(txt[i], xy=(X_tsne[i, 0], X_tsne[i, 1]))

    plt.savefig(f"speaker embedding.png")