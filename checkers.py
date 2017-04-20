from random import randint
from time import sleep

print "Set Window Size To 36x36 For Best Experience. A restart may be required to apply settings."
print "This game is still in Alpha so there is no double jumping capability. Update coming soon..."
sleep(2)

#set up board
board = [['X',' ','X',' ','X',' ','X',' '],
         [' ','X',' ','X',' ','X',' ','X'],
         ['X',' ','X',' ','X',' ','X',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ','O',' ','O',' ','O',' ','O'],
         ['O',' ','O',' ','O',' ','O',' '],
         [' ','O',' ','O',' ','O',' ','O']]


#display function
def display(board):
    print "  ---------------------------------"
    for i in range(0,8):
        print str(7-i) + " | " + " | ".join(board[i]) + " |"
        if i != 7:
            print "  | -   -   -   -   -   -   -   - |"
        else:
            print "  ---------------------------------"
    print "    0   1   2   3   4   5   6   7"

def checkForWin(board):
    Xs = 0
    Os = 0
    for x in range(0,7):
        for y in range(0,7):
            if board[x][y] == "X":
                Xs += 1
            elif board[x][y] == "O":
                Os += 1
    if Xs == 0:
        print "\(^o^)/"
        print "Player 2 Wins!"
        sleep(1000000)
    elif Os == 0:
        print "\(^o^)/"
        print "Player 1 Wins!"
        sleep(1000000)


#game function
def game():
    #turn loop
    for i in range(1,1000):
        display(board)
        print ""
        if i%2 == 1:
            player = 1
            movable = "X"
            print "PLAYER 1 (" + movable + ")"
        else:
            player = 2
            movable = "O"
            print "PLAYER 2 (" + movable + ")"
        print ""

        #piece selection
        while True:
            piece = raw_input("Select Piece (x,y)\n")
            piece = piece.split(",", 1)
            #right player's piece
            if board[7-int(piece[1])][int(piece[0])] == movable:
                #piece has diag moves
                if player == 1:
                    #if on left edge
                    if int(piece[0]) == 0:
                        #has open space
                        if board[7-int(piece[1])+1][int(piece[0])+1] == " ":
                            break
                        #has capture
                        elif board[7-int(piece[1])+1][int(piece[0])+1] == "O" and board[7-int(piece[1])+2][int(piece[0])+2] == " ":
                            break
                    #if on right edge
                    elif int(piece[0]) == 7:
                        #has open space
                        if board[7-int(piece[1])+1][int(piece[0])-1] == " ":
                            break
                        #has capture
                        elif board[7-int(piece[1])+1][int(piece[0])-1] == "O" and board[7-int(piece[1])+2][int(piece[0])-2] == " ":
                            break
                    #if not on edge
                    else:
                        #has open space
                        if board[7-int(piece[1])+1][int(piece[0])-1] == " " or board[7-int(piece[1])+1][int(piece[0])+1] == " ":
                            break
                        #has capture
                        else:
                            if int(piece[0]) >= 2:
                                if board[7-int(piece[1])+1][int(piece[0])-1] == "O" and board[7-int(piece[1])+2][int(piece[0])-2] == " ":
                                    break
                            if int(piece[0]) <= 5:
                                if board[7-int(piece[1])+1][int(piece[0])+1] == "O" and board[7-int(piece[1])+2][int(piece[0])+2] == " ":
                                    break
                                
                elif player == 2:
                    #if on left edge
                    if int(piece[0]) == 0:
                        #has open space
                        if board[7-int(piece[1])-1][int(piece[0])+1] == " ":
                            break
                        #has capture
                        elif board[7-int(piece[1])-1][int(piece[0])+1] == "X" and board[7-int(piece[1])-2][int(piece[0])+2] == " ":
                            break 
                    #if on right edge
                    elif int(piece[0]) == 7:
                        #has open space
                        if board[7-int(piece[1])-1][int(piece[0])-1] == " ":
                            break
                        #has capture
                        elif board[7-int(piece[1])-1][int(piece[0])-1] == "X" and board[7-int(piece[1])-2][int(piece[0])-2] == " ":
                            break
                    #if not on edge
                    else:
                        #has open space
                        if board[7-int(piece[1])-1][int(piece[0])-1] == " " or board[7-int(piece[1])-1][int(piece[0])+1] == " ":
                            break
                        #has capture
                        else:
                            if int(piece[0]) >= 2:
                                if board[7-int(piece[1])-1][int(piece[0])-1] == "X" and board[7-int(piece[1])-2][int(piece[0])-2] == " ":
                                    break
                            elif int(piece[0]) <= 5:
                                if board[7-int(piece[1])-1][int(piece[0])+1] == "X" and board[7-int(piece[1])-2][int(piece[0])+2] == " ":
                                    break
            print "Not A Valid Selection!"
        print "piece: " + ",".join(piece)
        print ""

        #target selection
        while True:
            target = raw_input("Select Target (x,y)\n")
            target = target.split(",", 1)
            if player == 1:
                if abs(int(target[0])-int(piece[0])) == 1 and int(piece[1])-int(target[1]) == 1 and board[7-int(target[1])][int(target[0])] == " ":
                    break
                elif board[((7-int(piece[1]))+(7-int(target[1])))/2][(int(piece[0])+int(target[0]))/2] == "O":
                    if abs(int(target[0])-int(piece[0])) == 2 and int(piece[1])-int(target[1]) == 2 and board[7-int(target[1])][int(target[0])] == " ":
                        break
            elif player == 2:
                if abs(int(target[0])-int(piece[0])) == 1 and int(target[1])-int(piece[1]) == 1 and board[7-int(target[1])][int(target[0])] == " ":
                    break
                elif board[((7-int(piece[1]))+(7-int(target[1])))/2][(int(piece[0])+int(target[0]))/2] == "X":
                    if abs(int(target[0])-int(piece[0])) == 2 and int(target[1])-int(piece[1]) == 2 and board[7-int(target[1])][int(target[0])] == " ":
                        break
                
            print "Not A Valid Selection!"
        print "target: " + ",".join(target)
        
        #move piece to target
        board[7-int(piece[1])][int(piece[0])] = " "
        board[7-int(target[1])][int(target[0])] = movable
        #delete captured piece
        if board[((7-int(piece[1]))+(7-int(target[1])))/2][(int(piece[0])+int(target[0]))/2] != " " and abs(int(target[1])-int(piece[1])) == 2:
            board[((7-int(piece[1]))+(7-int(target[1])))/2][(int(piece[0])+int(target[0]))/2] = " "
        
        sleep(.5)
        for x in range(1,15):
            print ""

        checkForWin(board)


game()




