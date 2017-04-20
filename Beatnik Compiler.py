SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
          "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for letter in word:
        total += SCORES[letter]
    return total




class Stack():
    def __init__(self):
        data = []

    def push(self, n):
        self.data.insert(0, n)

    def pop():
        top = self.data[0]
        self.data.pop([0])
        return top
