


terms = []


for a in range(2,101):
    for b in range(2,101):
        n = a**b
        if n not in terms:
            terms.append(n)


print len(terms)
