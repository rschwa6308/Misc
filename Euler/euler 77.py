def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True


primes = [2]
for n in range(3, 1000):
    if is_prime(n, primes):
        primes.append(n)



# TODO: use dynamic programming
# count(0) = 1, count(1) = 0
# count(n) = \sum_{p <= n} count(n - p)
counts = [1, 0]
for n in range(2, 100):
    c = 0
    i = 0
    while (p := primes[i]) <= n:
        if n == 5: print(p)
        c += counts[n - p]
        i += 1
    counts.append(c)

for n, c in enumerate(counts):
    print(n, c)