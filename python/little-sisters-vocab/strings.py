def add_prefix_un(word):

    return "un" + word


def make_word_groups(vocab_words):

    without_pre = vocab_words[1:]
    for index, word in enumerate(without_pre):
        without_pre[index] = vocab_words[0] + word
    without_pre.insert(0, vocab_words[0])
    return " :: ".join(without_pre)


def remove_suffix_ness(word):

    new_word = word[:-4]
    if new_word[-1] == "i":
        return new_word[: len(new_word) - 1] + "y"
    return new_word


print(remove_suffix_ness("heaviness"))


def adjective_to_verb(sentence, index):

    split_sentence = sentence.split()
    word_to_change = split_sentence[index]
    word_to_change = word_to_change + "en"
    return word_to_change.replace(".", "")


# adjective_to_verb("It got dark as the sun set.", 2)
