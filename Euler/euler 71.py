
best, candidate = 999, None

N = 10 ** 6
for d in range(2, N + 1):
    n = (d * 3)//7 + 1
    while n/d >= 3/7:
        n -= 1 
    # print(f'{n}/{d} = {n/d}')
    score = 3/7 - n/d
    if score < best:
        # print(f'New Best: {n}/{d} = {n/d}')
        best = 3/7 - n/d
        candidate = (n, d)

print(candidate)