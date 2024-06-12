def translate(text):

    vowels = ["a", "e", "i", "o", "u"]
    start_sound = ["xr", "yt", "ay"]

    split_text = text.split()

    i = 0
    for word in split_text:
        if word[:2] == "qu":
            split_text[i] = handle_qu(word) + "ay"
            i += 1
        elif word[0] in vowels or word[:2] in start_sound:
            split_text[i] = word + "ay"
            i += 1
        elif word[0] not in vowels:
            split_text[i] = handle_consonants(word) + "ay"
            i += 1
    return " ".join(split_text)


def handle_consonants(word):
    vowels = ["a", "e", "i", "o", "u"]

    new_word = []
    vowel_index = 0
    end_of_consonants = False
    for i in range(len(word)):
        char = word[i]
        print(char)
        if char not in vowels:
            if end_of_consonants == True:
                new_word.insert(vowel_index, char)
                vowel_index += 1
            else:
                if word[i] == "q":
                    return handle_qu(word[i:], append="".join(new_word))
                elif word[i] == "y":
                    return handle_y(word[i:], append="".join(new_word))
                else:
                    new_word.append(char)
        else:
            new_word.insert(vowel_index, char)
            vowel_index += 1
            end_of_consonants = True

    return "".join(new_word)


def handle_qu(word, append=""):
    if word[1] != "u":
        no_u_word = "" + word[1:] + "q"
        return no_u_word
    new_word = ""
    new_word = new_word + word[2:] + append + "qu"
    return new_word


def handle_y(word, append=""):
    if append == "":
        return word[1:] + "y"
    return word + append
