def chain(n):
    seen = set()
    curr = n
    while curr not in seen:
        seen.add(curr)
        curr = sum(int(d)**2 for d in str(curr))
    return curr


def chain_fast(n, cache):
    curr = n
    while True:
        if curr in cache:
            return True
        
        if curr == 89:
            return True
        elif curr == 1:
            return False
        curr = sum(int(d)**2 for d in str(curr))


# print(chain_fast(85))


count = 0
cache = set()
for n in range(1, 10_000_000):
    if n % 100_000 == 0:
        print(f"progress: {n}")
    if chain_fast(n, cache):
        count += 1
        cache.add(n)

print(count)
