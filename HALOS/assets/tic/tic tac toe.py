#requires pygame module to run

import pygame,sys,os
from pygame import *
from math import *
from random import *
from time import *
from colors import *
from HALOS import HALOS




#define display function
def display(board):
    screen.fill(white)
    #vert
    pygame.draw.line(screen,black,(s_width/3,0),(s_width/3,s_height),line_width)
    pygame.draw.line(screen,black,(2*s_width/3,0),(2*s_width/3,s_height),line_width)
    #hor
    pygame.draw.line(screen,black,(0,s_height/3),(s_width,s_height/3),line_width)
    pygame.draw.line(screen,black,(0,2*s_height/3),(s_width,2*s_height/3),line_width)

    for y in range(3):
        for x in range(3):
            if board[y][x] == 0:
                pass
            elif board[y][x] == 1:
                z = s_width/15
                #neg slope
                pygame.draw.line(screen,black,(float(x)/3.0*s_width+z,float(y+1)/3.0*s_height-z),(float(x+1)/3.0*s_width-z,float(y)/3.0*s_height+z),8)
                #pos slope
                pygame.draw.line(screen,black,(float(x)/3.0*s_width+z,float(y)/3.0*s_height+z),(float(x+1)/3.0*s_width-z,float(y+1)/3.0*s_height-z),8)    
            elif board[y][x] == 2:
                pygame.draw.circle(screen,black,(int(float(x)/3.0*s_width+s_width/6),int(float(y)/3.0*s_height+s_height/6)),s_width/8,6)
    
    pygame.display.update()



#define check for win function
def check_win(board):
    #hor
    for y in range(3):
        if 0 != board[y][0] == board[y][1] == board[y][2]:
            return True
    #vert
    for x in range(3):
        if 0 != board[0][x] == board[1][x] == board[2][x]:
            return True
    #diag
    if 0 != board[0][0] == board[1][1] == board[2][2]:
        return True
    if 0 != board[0][2] == board[1][1] == board[2][0]:
        return True
    return False
    

#define check for tie funciton
def check_tie(board):
    if sum([board[0].count(0),board[1].count(0),board[2].count(0)]) == 0:
        return True


#main function
def main():
    #initiate pygame module
    pygame.init()

    #initate clock
    clock = pygame.time.Clock()

    #set up sceen
    global s_width
    s_width = 300
    global s_height
    s_height = 300
    global screen
    screen = pygame.display.set_mode((s_width,s_height))

    #define line width
    global line_width
    line_width = 2

    #initiate board
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    display(board)

    #initiate turn variable
    turn = 1
    
    #turn loop
    global done
    done = False
    while not done:
        clock.tick(60)
        #update window header
        symbol = "X" if turn == 1 else "O"
        pygame.display.set_caption("Player " + str(turn) + "'s turn (" + symbol + ")")
        #user input
        for event in pygame.event.get():            
            if event.type == QUIT:
                pygame.quit()
                quit()
                sys.exit(0)
                
            if event.type == KEYDOWN:
                if event.key == K_h:
                    #apply ai
                    pos = HALOS(board,turn)
                    #pos = (float(pos[0])/3.0*s_width+s_width/6,float(pos[1])/3.0*s_height+s_height/6)
                    #pygame.event.post(pygame.event.Event(MOUSEBUTTONDOWN,button=1,pos=pos))
                    board[pos[1]][pos[0]] = turn
                    display(board)
                    if check_win(board):
                        pygame.display.set_caption("player " + str(turn) + " wins!!!")
                        done = True
                        sleep(2)
                        pygame.quit()
                        quit()
                        sys.exit(0)
                    if check_tie(board):
                        pygame.display.set_caption("Tie!!!")
                        done = True
                    #change turn
                    turn = 3-turn
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = int(floor(3*float(pygame.mouse.get_pos()[0])/float(s_width)))
                    y = int(floor(3*float(pygame.mouse.get_pos()[1])/float(s_height)))
                    #print "(" + str(x) + "," + str(y) + ")"
                    if board[y][x] == 0:
                        board[y][x] = turn
                        display(board)
                        if check_win(board):
                            pygame.display.set_caption("player " + str(turn) + " wins!!!")
                            done = True
                        if check_tie(board):
                            pygame.display.set_caption("Tie!!!")
                            done = True
                            sleep(2)
                            pygame.quit()
                            quit()
                            sys.exit(0)
                        #change turn
                        turn = 3-turn
                        
    sleep(2)
    pygame.quit()
    quit()
    sys.exit(0)




main()














