



def is_palindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False




good = []


for a in range(100,1000):
    for b in range(100,1000):
        if is_palindrome(a*b):
            good.append(a*b)


print max(good)
