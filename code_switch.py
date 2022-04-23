import numpy as np
import re
from g2p_en import G2p
from pypinyin import pinyin, Style
from text import text_to_sequence, sequence_to_text
from string import punctuation
import yaml


def read_lexicon(lex_path):
    lexicon = {}
    with open(lex_path) as f:
        for line in f:
            temp = re.split(r"\s+", line.strip("\n"))
            word = temp[0]
            phones = temp[1:]
            if word.lower() not in lexicon:
                lexicon[word.lower()] = phones
    return lexicon


def preprocess_english(text, lexicon):
    if text == "":
        sequence = []
        return "", sequence
    # text = text.rstrip(punctuation)

    g2p = G2p()
    phones = []
    words = re.split(r"([,;.\-\?\!\s+])", text)
    for w in words:
        if w.lower() in lexicon:
            phones += lexicon[w.lower()]
        else:
            phones += list(filter(lambda p: p != " ", g2p(w)))
    phones = "{" + "}{".join(phones) + "}"
    phones = re.sub(r"\{[^\w\s]?\}", "{sp}", phones)
    phones = phones.replace("}{", " ")
    sequence = text_to_sequence(phones, ["english_cleaners"])
    return phones, sequence


def preprocess_mandarin(text, lexicon=None):
    if text == "":
        sequence = []
        return "", sequence

    phones = []
    pinyins = [
        p[0]
        for p in pinyin(
            text, style=Style.TONE3, strict=False, neutral_tone_with_five=True
        )
    ]
    for p in pinyins:
        if p in lexicon:
            phones += lexicon[p]
        else:
            phones.append("sp")

    phones = "{" + " ".join(phones) + "}"
    sequence = text_to_sequence(phones, [])
    return phones, sequence


def append(phones, sequence, raw_text, p, s, r):
    # print(phones, sequence, p, s)
    phones += p
    sequence += s
    if r != "":
        raw_text.append(r)

    return phones, sequence, raw_text


def preprocess_text(text):
    zh_re = re.compile(r"(.*?)([\u4e00-\u9fa5，：！？、（）]+)(.*)")
    sequence = []
    phones = ""
    en_lexicon = read_lexicon("lexicon/librispeech-lexicon.txt")
    zh_lexicon = lexicon = read_lexicon("lexicon/pinyin-lexicon-r.txt")

    raw_text = []
    while len(text):
        m = zh_re.match(text)
        if not m:
            p, s = preprocess_english(text, en_lexicon)
            phones, sequence, raw_text = append(phones, sequence, raw_text, p, s, text)
            break

        p, s = preprocess_english(m.group(1), en_lexicon)
        phones, sequence, raw_text = append(phones, sequence, raw_text, p, s, m.group(1))

        p, s = preprocess_mandarin(m.group(2), zh_lexicon)
        phones, sequence, raw_text = append(phones, sequence, raw_text, p, s, m.group(2))

        text = m.group(3)

    print("Raw Text Sequence: {}".format("{" + "}{".join(raw_text)) + "}")
    print("Phoneme Sequence: {}".format(phones))

    return raw_text, phones, sequence


if __name__ == '__main__':
    text = "stay cool, he added他们说sound是声音的意思"
    raw_text, phones, sequence = preprocess_text(text)
    print(sequence_to_text(sequence))
