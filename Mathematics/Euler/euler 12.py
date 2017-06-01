
def triangle(n):
    return n*(n+1)/2


def count_divisors(n):
    s = 1
    for d in range(1,n/2+1):
        if n % d == 0:
            s += 1
    return s



def tau(n):
    sqroot,t = int(n**0.5),0
    for factor in range(1,sqroot+1):
            if n % factor == 0:
                    t += 2 # both factor and N/factor
    if sqroot*sqroot == n: t = t - 1 # if sqroot is a factor then we counted it twice, so subtract 1
    return t


for n in range(1000000):
    tri  = triangle(n)
    div = tau(tri)
    if div > 500:
        print tri
        print div
        break
