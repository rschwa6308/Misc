#requires pygame module to run
import math
from random import *
from funcs import *


#initiate pygame
pygame.init()


#initialize caption
pygame.display.set_caption("player " + str(turn) + "'s turn")

#display board
display(board)


#game loop
global done
done = False
while not done:
    
    #user input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #select piece
            if event.button == 1:
                z = pygame.mouse.get_pos()
                z = [z[0]/bw,z[1]/bh]
                #if clicked is turn's piece
                if board[z[1]][z[0]] == turn:
                    highlight(z)
                    selected = z
                #if clicked is target square
                if selected != z and selected != (-1,-1) and z[0]%2 != z[1]%2:
                    #print "clicking target"
                    if is_move(selected,z,turn):
                        #move piece
                        #print "moving piece"
                        board[selected[1]][selected[0]] = 0
                        board[z[1]][z[0]] = turn
                        #check for win
                        if sum(row.count(3-turn) for row in board) == 0:
                            print "Player " + str(turn) + " wins!"
                            display(board)
                            sleep(2)
                            pygame.display.quit()
                            pygame.quit()
                            quit()
                        #change turn
                        if turn == 1:
                            turn = 2
                        elif turn == 2:
                            turn = 1
                        pygame.display.set_caption("player " + str(turn) + "'s turn")
                        display(board)
                        
    



















