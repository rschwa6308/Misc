from math import floor, ceil, gcd


# calculate the number of unique reduced proper fractions with den <= D that lie between 1/3 and 1/2
def num_frations(D):
    total = 0
    for d in range(4, D + 1):   
        n_range = (floor(d / 3) + 1, ceil(d / 2) - 1)
        # print(d, n_range)
        x = 0
        for n in range(n_range[0], n_range[1] + 1):
            if gcd(n, d) == 1:
                x += 1
        print(f'{d}   ->   {x} fractions')
        total += x
    return total


print(num_frations(12000))

