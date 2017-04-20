from random import randint

cards = range(1,53)
player = []
caller = []

def resetCards():
    cards = range(1,53)
    #print cards


def resetGame():
    cards = range(1,53)

    for x in range(1,14):
        z = randint(0,len(cards)-1)
        z = cards[z]
        player.append(z)
        cards.remove(z)

    cards = range(1,53)


    for x in range(52):
        if len(cards) == 0:
            break
        z = randint(0,len(cards)-1)
        z = cards[z]
        caller.append(z)
        cards.remove(z)

endPoints = []
resetGame()
#print player
#print caller


y = 0
trials = 100000
probs = []
for x in range(0,53):
    probs.append(float(0))


for x in range(trials+1):
    if x % 10000 == 0:
        print "Trial: " + str(x)
    while True:
        if len(player) == 0:
            probs[52-y] += float(1)/float(trials)
            break
        y = len(caller) - 1
        for z in range(0,len(player)):
            if player[z] == caller[y]:
                player.remove(player[z])
                break
        caller.remove(caller[y])
    resetGame()




print ""

for x in range(len(probs)):
    print str(x) + ": " + str(probs[x])
