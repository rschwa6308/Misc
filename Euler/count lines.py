

lines = 0

problem = 0

while True:
    problem += 1
    try:
        if problem not in [23,24]:
            text = open("euler " + str(problem) + ".py").readlines()
            
    except:
        break
    print "problem #" + str(problem) + ": " + str(len(text))
    lines += len(text)


print ""
print "total lines:\n" + str(lines)
