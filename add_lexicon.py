
if __name__ == '__main__':
    lexicon = []
    with open("lexicon/pinyin-lexicon-r.txt", "r") as f:
        for line in f:
            lexicon.append(line)

    len = len(lexicon)
    new_lexicon = []
    for i in range(len):
        new_lexicon.append(lexicon[i])
        if i % 5 == 4:
            new_line = lexicon[i].replace("5", "6")
            new_lexicon.append(new_line)

    with open("lexicon/pinyin-lexicon-r-new.txt", "w") as f:
        for line in new_lexicon:
            f.write(line)
    print(1)