#tic tac toe AI
from random import *




#HALOS takes a 3x3 2d array (a matrix) and what player # she is as input and return coords of HALOS's move as tuple(x,y)


def HALOS(board,me):
    #define enemies turn # for reference
    you = 3-me

    #check for immediate win
    #hor
    for y in range(3):
        if board[y].count(me) == 2 and board[y].count(0) == 1:
            return (board[y].index(0),y)
    #vert
    for x in range(3):
        if [board[0][x],board[1][x],board[2][x]].count(me) == 2 and [board[0][x],board[1][x],board[2][x]].count(0) == 1:
            return (x,[board[0][x],board[1][x],board[2][x]].index(0))
    #diag
    if [board[0][0],board[1][1],board[2][2]].count(me) == 2 and [board[0][0],board[1][1],board[2][2]].count(0) == 1:
        return ([board[0][0],board[1][1],board[2][2]].index(0),[board[0][0],board[1][1],board[2][2]].index(0))
    if [board[2][0],board[1][1],board[0][2]].count(me) == 2 and [board[2][0],board[1][1],board[0][2]].count(0) == 1:
        return ([board[2][0],board[1][1],board[0][2]].index(0),2-[board[2][0],board[1][1],board[0][2]].index(0))

    
    #check for immediate danger
    #hor
    for y in range(3):
        if board[y].count(you) == 2 and board[y].count(0) == 1:
            return (board[y].index(0),y)
    #vert
    for x in range(3):
        if [board[0][x],board[1][x],board[2][x]].count(you) == 2 and [board[0][x],board[1][x],board[2][x]].count(0) == 1:
            return (x,[board[0][x],board[1][x],board[2][x]].index(0))
    #diag
    if [board[0][0],board[1][1],board[2][2]].count(you) == 2 and [board[0][0],board[1][1],board[2][2]].count(0) == 1:
        return ([board[0][0],board[1][1],board[2][2]].index(0),[board[0][0],board[1][1],board[2][2]].index(0))
    if [board[2][0],board[1][1],board[0][2]].count(you) == 2 and [board[2][0],board[1][1],board[0][2]].count(0) == 1:
        return ([board[2][0],board[1][1],board[0][2]].index(0),2-[board[2][0],board[1][1],board[0][2]].index(0))


    #if no immediates and middle open take middle square (keep right after immediates)
    if board[1][1] == 0:
        return (1,1)


    #if HALOS has first move
    if sum([board[0].count(0),board[1].count(0),board[2].count(0)]) == 9:
        return (1,1)


    #if center is taken first move
    if board[1][1] == you and sum([board[0].count(me),board[1].count(me),board[2].count(me)]) == 0:
        return [(0,0),(2,0),(0,2),(2,2)][randint(0,3)]        
        
    #if nothing else
    empties = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == 0:
                empties.append((x,y))
    return empties[randint(0,len(empties)-1)]






###test code
##board = [[1,0,0],
##         [0,1,0],
##         [0,0,2]]
##
##print HALOS(board,2)
