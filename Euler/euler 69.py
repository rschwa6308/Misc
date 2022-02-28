def phi_sieve(n):
    phi = list(range(n + 1))

    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    
    return phi


# print(phi_sieve(10 ** 6)[:10])

N = 10 ** 6
phi = phi_sieve(N)
print(max(range(1, N + 1), key=lambda n: n / phi[n]))