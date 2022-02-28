from itertools import combinations, permutations, product




TREES = [
    "((axb)yc)zd",
    "(ax(byc))zd",
    "(axb)y(czd)",
    "ax((byc)zd)",
    "ax(by(czd))"
]


OPS = ["+", "-", "*", "/"]



def is_integer(n, eps=1e-6):
    return abs(n - int(n)) < eps




def all_targets(digits):
    strs = []
    for ds in permutations(digits):
        for ops in product(OPS, repeat=3):
            for tree in TREES:
                s = tree\
                    .replace("a", str(ds[0])) \
                    .replace("b", str(ds[1])) \
                    .replace("c", str(ds[2])) \
                    .replace("d", str(ds[3])) \
                    .replace("x", ops[0]) \
                    .replace("y", ops[1]) \
                    .replace("z", ops[2])
                strs.append(s)
                # print(s)

    ints = set()
    for s in strs:
        try:
            n = eval(s)
            if is_integer(n) and n > 0:
                ints.add(int(n))
        except ZeroDivisionError:
            pass
    return list(sorted(ints))



# print(all_targets([1, 2, 3, 4]))




def count_consecutives(ints):
    ints.sort()
    if ints[0] != 1:
        return 0
    
    i = 0
    while i < len(ints)-1 and ints[i] + 1 == ints[i+1]:
        i += 1
    return i + 1




candidate = None
most_consecutive_ints = -1

for digits in combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
    ints = all_targets(digits)

    cons = count_consecutives(ints)
    
    if cons > most_consecutive_ints:
        candidate = digits
        most_consecutive_ints = cons


print("".join(map(str,candidate)))
