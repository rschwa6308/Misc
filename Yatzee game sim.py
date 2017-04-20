from random import randint



secondRolls = 0


wins = 0

for trial in range(1000000):
    dice = []

    for x in range(5):
        dice.append(randint(1,6))

    #print "first roll: " + str(dice)


    count = []

    for x in range(1,7):
        count.append(dice.count(x))



    z = 0

    for x in range(0,6):
        if count[x] > z:
            z = count[x]
            n = x


    if z > 1:
        secondRolls += 1
        #print str(z) + " of a kind (" + str(n+1) + ")"
        dice = [n+1 for x in range(z)]
        for x in range(5-z):
            dice.append(randint(1,6))
        #print "second roll: " + str(dice)
        if dice.count(z) == 5:
            #print "YATZEE"
            wins += 1
    #else:
        #print "no incentive"




print "wins: " + str(wins)
print "second rolls: " + str(secondRolls)
print float(wins)/float(secondRolls)
