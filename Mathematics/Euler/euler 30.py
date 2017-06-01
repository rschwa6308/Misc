

def is_form(n):
    return sum([int(digit)**5 for digit in str(n)]) == n



s = 0

for n in range(2,100000):
    if is_form(n):
        s += n


print s
