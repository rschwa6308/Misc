from math import factorial




def is_form(n):
    return sum([factorial(int(digit)) for digit in str(n)]) == n



s = 0

for n in range(3,100000):
    if is_form(n):
        s += n

print s
