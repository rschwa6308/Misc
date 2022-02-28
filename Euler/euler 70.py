def phi_sieve(n):
    phi = list(range(n + 1))

    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    
    return phi


# returns True iff iterable a is a permutation of iterable b
def is_perm(a, b):
    return sorted(a) == sorted(b)


N = 10 ** 7
phi = phi_sieve(N)

candidates = [n for n in range(2, N + 1) if is_perm(str(n), str(phi[n]))]
# print(candidates)

print(min(candidates, key=lambda n: n / phi[n]))