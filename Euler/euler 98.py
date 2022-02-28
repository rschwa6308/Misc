from itertools import combinations


def is_anagram_pair(a, b):
    return sorted(a) == sorted(b)


assert(is_anagram_pair("CARE", "RACE"))
assert(is_anagram_pair("CAREE", "ERACE"))
assert(not is_anagram_pair("DOG", "DOOG"))



# def is_square(n):
#     return int(n ** 0.5) == n ** 0.5

# assert(is_square(999950884))
# assert(not is_square(999950884 + 1))



def pattern(string):
    pattern = []
    map = {}
    for char in string:
        if char not in map:
            map[char] = len(map)
        pattern.append(map[char])

    return pattern


print(pattern("POOR"))
print(pattern("1778"))




def make_square_anagram(squares, a, b):
    a_pattern = pattern(a)
    b_pattern = pattern(b)
    for s in squares:
        if pattern(s) == a_pattern:
            table = str.maketrans(a, s)
            b_trans = b.translate(table)
            if b_trans in squares:
                return (s, b_trans)




def get_all_anagram_pairs(strings):
    for a, b in combinations(strings, 2):
        assert(a != b)
        if is_anagram_pair(a, b):
            yield (a, b)
    




with open("p098_words.txt") as f:
    words = f.read().replace("\"", "").split(",")

# print(words[:100])



anagrams = list(get_all_anagram_pairs(words))

print(f"ANAGRAMS: {len(anagrams)}")
print(anagrams[:10])


max_len = max(max(len(a), len(b)) for a, b in anagrams)
print(max_len)


squares = []
n = 0
while len(str(n**2)) <= max_len:
    squares.append(str(n**2))
    n += 1

print(f"SQUARES: {len(squares)}")



candidate = -1
for a, b in anagrams:
    res = make_square_anagram(squares, a, b)
    if res is not None:
        print(a, b, res)
        candidate = max(candidate, max(map(int, res)))

print(candidate)
