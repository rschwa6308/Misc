from random import randint
while True: print ["you lose", "you win!"][(input("0 = rock, 1 = paper, 2 = scizzors\n") - randint(0,2)) % 3 is 1]
