from random import randint
from time import sleep

codeNames = []
randCodeNames = []

for x in range(1,11):
    codeNames.append(raw_input("code name #" + str(x) + ": "))

print ""
print codeNames


for x in range(0,10):
    z = randint(0,len(codeNames)-1)
    randCodeNames.append(codeNames[z])
    codeNames.remove(codeNames[z])

print ""
print "displaying target mapping in"
print "3..."
sleep(1)
print "2..."
sleep(1)
print "1..."
sleep(1)

for x in range(0,10):
    print randCodeNames[x] + " ---> " + randCodeNames[(x+1)%10]

