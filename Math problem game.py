from random import randint
from time import sleep
from math import floor

score = 0
streak = 0
highStreak = 0
numRight = 0

print "Math Facts Game"
sleep(1)
 
numProblems = raw_input("How many problems? ")

for i in range(0,int(numProblems)):
    a = randint(1,10)
    b = randint(1,10)
    z = randint(1,4)
    op = ""
    if z == 1:
        ans = a+b
        op = "+"
    elif z == 2:
        ans = a-b
        op = "-"
    elif z == 3:
        ans = a*b
        op = "x"
    elif z == 4:
        while a%b != 0:
            a = randint(1,10)
            b = randint(1,10)
        ans = a/b
        op = "/"
    userAns = raw_input(str(a) + op + str(b) + "\n")
    if int(userAns) == ans:
        print "correct!"
        score += 1
        streak += 1
        numRight += 1
        if streak > highStreak:
            highStreak = streak
    else:
        print "wrong!"
        score -= 1
        streak = 0
    sleep(.5)

print "Game Over!"
print "You scored " + str(score) + " points!"
print "You got " + str(int(floor(float(numRight)/float(numProblems)*100))) + "% correct."
print "Your highest streak was " + str(highStreak) + " correct answers in a row!"


