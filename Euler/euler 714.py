def is_duodigital(n):
    return len(set(str(n))) <= 2


def d(n):
    curr = n
    while not is_duodigital(curr):
        curr += n
    
    return curr

# for n in range(1, 1000):
#     print(n, d(n))


def D_naive(k):
    s = 0
    for n in range(1, k + 1):
        s += d(n)
    return s






def get_duodigitals(k):
    for n in range(1, k+1):
        if is_duodigital(n):
            yield n


def get_divisors(n):
    for d in range(1, n+1):
        if n % d == 0:
            yield d



from proper_divs import proper_divs

def D(k):
    infty = 10**15
    A = [infty] * (k + 1)
    for duo in get_duodigitals(k * 20_000):
        # if duo % 10_000 == 0: print(duo / (k * 20_000))
        for div in list(proper_divs(duo)) + [duo]:
            if div > k: continue
            A[div] = min(A[div], duo)
    
    # print(A)
    
    s = 0
    for n in range(1, k + 1):
        val = A[n]
        if val == infty:
            print(f"d({n}) not found!")
            s += d(n)
        else:
            s += val
    
    return s
    





# print(D(110), 11_047)
# print(D(150), 53_312)
# print(D(500), 29_570_988)

print(D(50_000))
