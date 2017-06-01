


def tri(n):
    return n*(n+1)/2


def is_pent(x):
    n = ((24*x+1)**0.5+1)/6
    return n == int(n)


def is_hex(x):
    n = ((8*x+1)**0.5+1)/4
    return n == int(n)



n = 0
while True:
    n += 1
    x = tri(n)
    if is_pent(x):
        if is_hex(x):
            print x
            if x > 40755:
                break
