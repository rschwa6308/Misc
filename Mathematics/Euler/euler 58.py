


def is_prime(n):
    for d in range(2, min(int(n**0.5), 50)):
        if n%d == 0:
            return False
    return 2 in [n, 2**n%n]






def corners(length):
    s = length**2
    gap = length-1
    return [s, s-gap, s-gap*2, s-gap*3]




count = 0
total = 0

for length in [x*2+1 for x in range(1,100000)]:
    print length
    for corner in corners(length):
        total += 1
        if is_prime(corner):
            count += 1
    percent = float(count)/total
    print percent
    if percent < 0.1:
        print length
        break


 





##print corners(5000)
##
##for c in corners(5000):
##    print is_prime(c)
