keys = [int(n) for n in """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716""".split()]


guess = []
for key in keys:
    




# def exists(a, b):
#     """checks if b exists in a as a subsequence"""
#     pos = 0
#     for ch in a:
#         if pos < len(b) and ch == b[pos]:
#             pos += 1
#     return pos == len(b)


# def possible(passcode):
#     return all(exists(str(passcode), str(key)) for key in keys)


# from itertools import product

# MAX_LENGTH = 7

# for length in range(1, MAX_LENGTH + 1):
#     for guess in product(map(str, range(10)), repeat=length):
#         # print(guess)
#         if possible(guess):
#             print(guess)