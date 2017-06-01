



def is_pan(n):
    digits = [1,2,3,4,5,6,7,8,9]
    for d in str(n):
        if int(d) in digits:
            digits.remove(int(d))
        else:
            return False
    if len(digits) == 0:
        return True
    else:
        return False







def get_mults(n):
    mults = []
    for d in range(1,n/2+1):
        if n % d == 0:
            mults.append((d,n/d))

    return mults






def is_form(n):
    for pair in get_mults(n):
        if is_pan(int(str(pair[0]) + str(pair[1]) + str(n))):
            return True
    return False







good = []

for n in range(20000):
    if is_form(n):
        good.append(n)


print good

print sum(good)

















