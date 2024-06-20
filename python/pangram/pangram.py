# my definitely not optimized solution ha.

def is_pangram(sentence):

    if len(sentence) < 26:
        return False

    alphabet = {
        "a": False,
        "b": False,
        "c": False,
        "d": False,
        "e": False,
        "f": False,
        "g": False,
        "h": False,
        "i": False,
        "j": False,
        "k": False,
        "l": False,
        "m": False,
        "n": False,
        "o": False,
        "p": False,
        "q": False,
        "r": False,
        "s": False,
        "t": False,
        "u": False,
        "v": False,
        "w": False,
        "x": False,
        "y": False,
        "z": False,
    }

    new_sentence = sentence.replace(" ", "")

    for char in new_sentence:
        print("HI", char, char.isalpha())
        if char.isalpha() and alphabet[char.lower()] == False:
            alphabet[char.lower()] = True

    return not False in alphabet.values()


# https://exercism.org/tracks/python/exercises/pangram/dig_deeper

from string import ascii_lowercase


def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)
