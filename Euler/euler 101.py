from scipy.interpolate import lagrange


def eval_poly(poly, n):
    return sum(
        c * n**i
        for i, c in enumerate(poly)
    )


# print(eval_poly([6, -11, 6], 4))


POLY = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
# POLY = [0, 0, 0, 1]

POLY_VALS = [eval_poly(POLY, n) for n in range(20)]

print(POLY_VALS)




def OP(k):
    X = list(range(1, k+1))
    Y = [POLY_VALS[n] for n in X]
    # print(X, Y)
    coeffs = lagrange(X, Y).c[::-1]
    assert(len(coeffs) == k)
    # assert(all(
    #     eval_poly(coeffs, n) == POLY_VALS[n]
    #     for n in range(1, k+1)
    # ))
    return coeffs


# print(OP(3))



# def FIT(poly):
#     n = 1
#     while (val := eval_poly(poly, n)) == POLY_VALS[n]:
#         n += 1
    
#     # print(poly)
#     # assert(n > len(poly))
    
#     return val

epsilon = 0.5


s = 0
for k in range(1, len(POLY)):
    optimal_poly = OP(k)
    print(f"\nOP({k}, n) = {optimal_poly}")

    n = 1
    while abs((val := eval_poly(optimal_poly, n)) - POLY_VALS[n]) < epsilon:
        n += 1
    
    print(f"FIT is n = {n} ({val})")
    
    s += val

print(int(s))

# => 37076114526
