#game variables


#init board
global board
board = [[0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [2,0,2,0,2,0,2,0],
         [0,2,0,2,0,2,0,2],
         [2,0,2,0,2,0,2,0]]

##board = [[0,1,0,1,0,1,0,1],
##         [1,0,0,0,1,0,1,0],
##         [0,1,0,1,0,1,0,1],
##         [0,0,2,0,0,0,2,0],
##         [0,0,0,0,0,1,0,0],
##         [0,0,2,0,2,0,2,0],
##         [0,0,0,0,0,0,0,0],
##         [0,0,0,0,0,0,0,0]]

#initiate turn variable
turn = 1

#initiate selected variable
selected = (-1,-1)

