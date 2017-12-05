from copy import copy
from time import time
from random import randint

english_words = open('english_words.txt').read().split('\n')


def get_words_startwith(words_list, start):
    return [word for word in words_list if word.startswith(start.lower())]


def is_word(word):
    return word.lower() in english_words


def is_valid_position(position):
    return 0 <= position[0] <= 3 and 0 <= position[1] <= 3


def get_neighbors(position):
    adjacents = [(position[0] + x_offset, position[1] + y_offset) for x_offset in (-1, 0, 1) for y_offset in (-1, 0, 1)]
    adjacents.remove(position)
    return list(filter(is_valid_position, adjacents))


def find_words(board, position, visited, test_word='', candidates=english_words):
    words = []

    visited.append(position)
    x, y = position
    test_word += board[y][x]
    # print(test_word)

    if test_word.lower() in candidates:
        words.append(test_word)

    candidates = get_words_startwith(candidates, test_word)

    if len(candidates) <= 1:
        return words

    unused_neighbors = [pos for pos in get_neighbors(position) if pos not in visited]
    for next_position in unused_neighbors:
        # print(board[y][x] + " -> " + board[next_position[1]][next_position[0]])
        words += find_words(board, next_position, copy(visited), test_word, candidates)

    return words


def calculate_score(words):
    score = 0
    for word in words:
        if len(word) <= 7:
            score += (0, 0, 1, 1, 2, 3, 4)[len(word) - 1]
        else:
            score += 11
    return score


if __name__ == '__main__':
    start_time = time()
    # board = [['D', 'O', 'G', 'D'],
    #          ['E', 'F', 'G', 'H'],
    #          ['I', 'J', 'K', 'L'],
    #          ['M', 'N', 'O', 'P']
    #         ]
    board = [[chr(randint(65, 90)) for _ in range(4)] for _ in range(4)]
    print("\n".join([' '.join(row) for row in board]))

    words = []
    for x in range(4):
        for y in range(4):
            words += find_words(board, (x, y), [])

    words = list(set([w for w in words if len(w) > 2]))

    print(words)
    print("search time:", time() - start_time)

    print("score:", calculate_score(words))
