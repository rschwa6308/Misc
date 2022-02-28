
from math import factorial


def chain_length(n):
    chain = set()
    curr = n
    while curr not in chain:
        chain.add(curr)
        curr = sum(factorial(int(d)) for d in str(curr))

    return len(chain)        


# print(chain_length(540))




total = 0
for n in range(1, 10**6):
    if n % 10**4 == 0: print(n)
    if chain_length(n) == 60:
        total +=1

print(total)
