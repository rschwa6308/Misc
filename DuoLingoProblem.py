with open("Hangman/words_alpha.txt") as f:
    WORDS = f.read().split()


SUBWORDS_MAP = {}

for word in WORDS:
    for i in range(len(word)):
        subword = word[:i] + word[i+1:]
        if subword not in SUBWORDS_MAP:
            SUBWORDS_MAP[subword] = []
        SUBWORDS_MAP[subword].append((word, i))


def validate_word(word):
    """given a word, return T iff word is at most a single error away from a valid word"""
    for i in range(len(word)):
        subword = word[:i] + word[i+1:]
        if subword not in SUBWORDS_MAP:
            continue

        parents = SUBWORDS_MAP[subword]
        if any(p[1] == i for p in parents):
            return True
    
    return False


def validate(text):
    """given text containing n space-seperated words, return a vector in [T, F]^n"""
    return [validate_word(word) for word in text.split()]


if __name__ == "__main__":
    test_text = "hello world dfhjdsfh thix sentence is full od singlt letuer typos"
    print(validate(test_text))