import msvcrt
from graphics import *

x = 100
y = 100

win = GraphWin()


while True:
    Point(x,y).draw(win)
    
    char = msvcrt.getch()
    if char == 37:
        x -= 5
    elif char == 39:
        x += 5
    elif char == 38:
        y -= 5
    elif char == 40:
        y += 5
