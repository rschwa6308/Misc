from random import randint
from time import sleep

#initialize board
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

#display funtion
def display(board):
    for x in range(0,3):
        print " | ".join(board[x])
        if x != 2:
            print "---------"

#check for a win
def checkForWin(board):
    #horizontal
    for x in range(0,2):
        if " " != board[x][0] and board[x][0] == board[x][1] and board[x][0] == board[x][2]:
            return board[x][0]
    #vertical
    for x in range(0,2):
        if board[0][x] != " " and board[0][x] == board[1][x] and board[0][x] == board[2][x]:
            return board[0][x]
    #diagonal up
    if board[2][0] != " " and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        return board[2][0]
    #diagonal down
    if board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0,0]

#ai function
def ai(board):
    if board[1][1] == "X":
        return [0,2]
    #check for danger horizontally
    for x in range(0,2):
        if board[x][0] == "X" and board[x][1] == "X":
            return [x,2]
        elif board[x][1] == "X" and board[x][2] == "X":
            return [x,0]
        elif board[x][0] == "X" and board[x][2] == "X":
            return [x,1]
    #check for danger vertically
    for x in range(0,2):
        if board[0][x] == "X" and board[1][x] == "X":
            return [2,x]
        elif board[1][x] == "X" and board[2][x] == "X":
            return [0,x]
        elif board[0][x] == "X" and board [2][x] == "X":
            return [1,x]
    #check for danger diagonally down
        if board[0][0] == "X" and board[1][1] == "X":
            return [2,2]
        elif board[1][1] == "X" and board[2][2] == "X":
            return [0,0]
        elif board[0][0] == "X" and board[2][2] == "X":
            return [1,1]
    #check for danger diagonally up
        if board[2][0] == "X" and board[1][1] == "X":
            return [0,2]
        elif board[1][1] == "X" and board[0][2] == "X":
            return [2,0]
        elif board[2][0] == "X" and board[0][2] == "X":
            return [1,1]
        elif board[1][1] == " ":
            return [1,1]
    




#game

print "Set window size to 32x15."

display(board)

while True:
    while True:
        slot = raw_input("Enter Location Coordinates (x,y)" + "\n")
        slot = slot.split(",", 1)
        slot[0] = int(slot[0])
        slot[1] = int(slot[1])
        if board[2-slot[0]][slot[1]] == ' ':
            break
        print "Not Valid"

    board[2-slot[1]][slot[0]] = "X"

    sleep(.5)

    display(board)

    sleep(1)

    z = ai(board)
    board[z[0]][z[1]] = "O"

    for x in range(1,15):
        print ""

    display(board)

    z = checkForWin(board)
    if z == "X":
        print "YOU WIN!!!"
    elif z == "O":
        print "GLADOS WINS!!!"
        print "Better luck next time!"
        
        





