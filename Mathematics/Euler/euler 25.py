from time import sleep






a = 1
b = 1

term = 0

while True:
    term += 1
    if len(str(a)) == 1000:
        print a
        print "term: " + str(term)
        break
    #print a
    n = a + b
    a = b
    b = n
