from random import random


def in_circle((x,y)):
    return ((x-0.5)**2+(y-0.5)**2)**0.5 < 0.5



if __name__ == "__main__":

    trials = 1000000

    circle_count = 0


    for i in range(trials):
        x, y = random(), random()
        #print x, y

        if in_circle((x, y)):
            circle_count += 1


    pi = (float(circle_count)/trials)*4
    print pi
