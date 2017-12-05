# This is a bad idea lol
# The attempt was to create a master list of all valid walks which would be loaded into memory and looped through
# But its way too cpu intensive to generate, and the file would take too long to load into memory

from itertools import permutations


def are_adjacent(pos_a, pos_b):
    if pos_a == pos_b:
        return False

    return abs(pos_b[0] - pos_a[0]) <= 1 and abs(pos_b[1] - pos_a[1]) <= 1


def is_valid_walk(walk):
    for i in range(len(walk) - 1):
        if not are_adjacent(walk[i], walk[i + 1]):
            return False

    return True


if __name__ == '__main__':
    position_set = [(x, y) for x in range(4) for y in range(4)]

    valid_walks = []
    for walk_length in range(1, 7):
        print(walk_length)
        perms = permutations(position_set, walk_length)
        for walk in perms:
            if is_valid_walk(walk):
                # print(list(walk))
                valid_walks.append(list(walk))

    print(len(valid_walks))