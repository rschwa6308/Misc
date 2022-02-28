from itertools import combinations



SQUARES = [str(n**2).zfill(2) for n in range(1, 10)]
assert(all(int(s) < 100 for s in SQUARES))


def is_valid(a, b):
    if 6 in a: a.add(9)
    if 9 in a: a.add(6)

    if 6 in b: b.add(9)
    if 9 in b: b.add(6)

    for s in SQUARES:
        d1, d2 = map(int, s)
        if (d1 in a and d2 in b) or (d1 in b and d2 in a):
            pass
        else:
            return False
    return True


# print(is_valid(
#     {0, 5, 6, 7, 8, 9},
#     {1, 2, 3, 4, 6, 7}
# ))



DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
for a in combinations(DIGITS, 6):
    for b in combinations(DIGITS, 6):
        # skip duplicates by enforcing lexicographic ordering on the pair
        if str(a) > str(b):
            continue
        if is_valid(set(a), set(b)):
            print(a, b)
            count += 1


print(count)