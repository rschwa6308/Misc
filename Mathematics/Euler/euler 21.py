

def get_divs(n):
    divs = []
    for d in range(1,n/2+1):
        if n % d == 0:
            divs.append(d)
    return divs



def is_amicable(n):
    m = sum(get_divs(n))
    return sum(get_divs(m)) == n and m != n


s = 0
for n in range(1,10000):
    if is_amicable(n):
        print n
        s += n

print s
