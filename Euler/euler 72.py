def phi_sieve(n):
    phi = list(range(n + 1))

    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    
    return phi


# calculate the number of unique reduced proper fractions with den <= D
def num_frations(D):
    return sum(phi_sieve(D)[2:])



print(num_frations(10**6))