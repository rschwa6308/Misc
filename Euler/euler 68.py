# Numbering scheme:
#   outer ring (starting at top left and going clockwise)   (0, 1, 2, 3, 4)
#   inner ring (starting at top and going clockwise)        (5, 6, 7, 8, 9)


GROUPS = [
    (0, 5, 6),
    (1, 6, 7),
    (2, 7, 8),
    (3, 8, 9),
    (4, 9, 5)
]


def ev(group, N):
    return sum(N[i] for i in group)


def is_magic(N):
    s = ev(GROUPS[0], N)
    return all([s == ev(group, N) for group in GROUPS])


def get_concat(N):
    curr = min(enumerate(N[:5]), key=lambda p: p[1])[0]
    # print(start)
    out = []
    for _ in range(5):
        group = GROUPS[curr]
        out.extend(N[i] for i in group)
        curr = (curr + 1) % 5
    return int(''.join(str(n) for n in out))


# print(get_concat([9, 8, 7, 6, 5, 2, 0, 3, 1, 4]))


from itertools import permutations


candidates = []
for N in permutations(range(1, 11)):
    if is_magic(N):
        candidates.append(N)
        print(N)
    
concats = [get_concat(N) for N in candidates]
print(max(c for c in concats if len(str(c)) == 16))
