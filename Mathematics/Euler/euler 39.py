

def is_pythag(a,b,c):
    return a**2 + b**2 == c**2


def get_solutions(p):
    solutions = []
    for a in range(1,p/2):
        for b in range(1,a):
            c = p - a - b
            if is_pythag(a,b,c):
                solutions.append((a,b,c))
    return solutions


most_solutions = 0
best_p = 0

for p in range(1,1001):
    print p
    s = len(get_solutions(p))
    if s > most_solutions:
        best_p = p
        most_solutions = s

print best_p

