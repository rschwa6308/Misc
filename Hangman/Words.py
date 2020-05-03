# Words list from https://github.com/dwyl/english-words

import os
from string import ascii_lowercase as LETTERS
from random import choice

filename = os.path.join(os.path.dirname(__file__), 'words_alpha.txt')
with open(filename) as f:
    WORDS = set(f.read().split('\n'))


def letter_frequency(words):
    freq = {l: 0 for l in LETTERS}
    for word in words:
        for l in set(word):     # only care about at least one occurrence
            freq[l] += 1
    return freq


def random_word():
    return choice(list(WORDS))

# print(max(letter_frequency(WORDS).items(), key=lambda item: item[1]))
# print(len(WORDS))