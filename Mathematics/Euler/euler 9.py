


def is_pythag(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


    
for a in range(1,999):
    print a
    for b in range(1,999):
        for c in range(1,999):
            if is_pythag(a,b,c):
                if a + b + c == 1000:
                    print a*b*c
