# using regex
# import re

# RE = re.compile('^(x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$')


# def translate(phrase):
#     return ' '.join(map(translate_word, phrase.split()))


# def translate_word(word):
#     return RE.sub(lambda m: '{1}{0}ay'.format(*m.groups()), word)

# very cool

# def _rotate(word):
#     return word[1:] + word[0]
# def _pig_latin(word):
#     if word[:2] == 'xr':
#         return 'xrayay'  # for some reason
#     if word[0] == 'y' and word[1] in 'aeiou':
#         word = _rotate(word)
#     while word[0] not in 'aeiouy':
#         word = _rotate(word)
#     if word[-1] == 'q' and word[0] == 'u':
#         word = _rotate(word)
#     return word + 'ay'
# def translate(text):
#     return ' '.join([_pig_latin(word) for word in text.split()])

# neat

# def translate_word(word):
#     while not word[0] in 'aeiou':
#         if word[0] in 'xy' and not word[1] in 'aeiou':
#             break
#         word = word[1:] + word[0]
#         if word[-1] == 'q' and word[0] == 'u':
#             word = word[1:] + 'u'

#     return word + 'ay'

# def translate(sentence):
#     return ' '.join([translate_word(word) for word in sentence.split()])