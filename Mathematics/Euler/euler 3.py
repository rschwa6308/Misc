import math


def is_prime(n):
    for d in range(2,int(math.sqrt(n))):
        if n % d == 0:
            return False
    return True


prime_divs = []
for i in range(2,int(math.sqrt(600851475143)+1)):
    if 600851475143 % i == 0:
        if is_prime(i):
            prime_divs.append(i)


print max(prime_divs)
