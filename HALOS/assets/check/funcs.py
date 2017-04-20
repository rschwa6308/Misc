#classes and functions for checkers graphical
import pygame,os,sys
from pygame import *
from pygame.locals import *
from colors import *
from game_variables import *
from time import sleep


#center screen
os.environ["SDL_VIDEO_CENTERED"] = "1"

#set up screen stuff
s_width = 600
s_height = 600
bw = s_width/8
bh = s_height/8
screen = pygame.display.set_mode((s_width,s_height))

#define font
pygame.font.init()
my_font = pygame.font.SysFont("monospace",20)



#piece class
class Piece:
    def __init__(self,x,y,color):
        self.image = Surface(bw,bh)
        pygame.draw.ellipse(self.image,color,Rect(0,0,bw,bh),0)
        self.image.convert()
        self.x = x
        self.y = y
        if color == (0,0,0):
            self.play = 1
        elif color == (255,0,0):
            self.play = 2
        pieces.append(self)



#display function
def display(board):
    #draw background
    for y in range(8):
        if y%2 == 0:
            for x in range(8):
                if x%2 == 0:
                    pygame.draw.rect(screen,red,Rect(x*bw,y*bh,bw,bh),0)
                else:
                    pygame.draw.rect(screen,black,Rect(x*bw,y*bh,bw,bh),0)
        else:
            for x in range(8):
                if x%2 == 0:
                    pygame.draw.rect(screen,black,Rect(x*bw,y*bh,bw,bh),0)
                else:
                    pygame.draw.rect(screen,red,Rect(x*bw,y*bh,bw,bh),0)
    #draw board
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                pygame.draw.circle(screen,grey,(x*bw+bw/2,y*bh+bh/2),bh/2-4)
            elif board[y][x] == 2:
                pygame.draw.circle(screen,red,(x*bw+bw/2,y*bh+bh/2),bh/2-4)
    #update display
    pygame.display.update()



#define highligh function
def highlight(pos):
    display(board)
    pygame.draw.rect(screen,yellow,Rect(pos[0]*bw,pos[1]*bh,bw,bh),3)
    pygame.display.update()



#define is move function
def is_move(piece,tar,turn):
    #print piece
    #print tar
    px = piece[0]
    py = piece[1]
    tx = tar[0]
    ty = tar[1]
    
    #if tar is occupied
    if board[ty][tx] != 0:
        return False
    
    #player 1
    if turn == 1:
        #direct move
        if ty-py == 1 and abs(px-tx) == 1:
            return True
        #single jump
        if ty-py == 2 and tx-px != 0:
            #to left of piece
            if tx-px == -2:
                if 0!= board[py+1][px-1] != turn:
                    board[py+1][px-1] = 0
                    return True
            #to right of piece
            if tx-px == 2:
                if 0!= board[py+1][px+1] != turn:
                    board[py+1][px+1] = 0
                    return True
        #double jump
        if ty-py == 4:
            #if first jump is left
            if 0 != board[py+1][px-1] != turn and board[py+2][px-2] == 0:
                #if second jump is left
                try:
                    if 0 != board[ty-1][tx+1] == board[py+3][px-3] != turn and board[ty][tx] == 0 and px-tx == 4:
                        #animate first jump
                        board[py][px] = 0
                        board[py+2][px-2] = turn
                        board[py+1][px-1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py+2][px-2] = 0
                        board[py+3][px-3] = 0
                        return True
                except:
                    pass
                #if second jump is right
                try:
                    if 0 != board[ty-1][tx-1] == board[py+3][px-1] != turn and board[ty][tx] == 0 and px-tx == 0:
                        #animate first jump
                        board[py][px] = 0
                        board[py+2][px-2] = turn
                        board[py+1][px-1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py+2][px-2] = 0
                        board[ty-1][tx-1] = 0
                        return True
                except:
                    pass
            #if first jump is right
            elif 0 != board[py+1][px+1] != turn and board[py+2][px+2] == 0:
                #if second jump is left
                try:
                    if 0 != board[ty-1][tx+1] == board[py+3][px+1] != turn and board[ty][tx] == 0 and tx-px == 0:
                        #animate first jump
                        board[py][px] = 0
                        board[py+2][px+2] = turn
                        board[py+1][px+1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py+2][px+2] = 0
                        board[py+3][px+1] = 0
                        return True
                except:
                    pass
                #if second jump is right
                try:
                    if 0 != board[ty-1][tx-1] == board[py+3][px+3] != turn and board[ty][tx] == 0 and tx-px == 4:
                        #animate first jump
                        board[py][px] = 0
                        board[py+2][px+2] = turn
                        board[py+1][px+1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py+2][px+2] = 0
                        board[py+3][px+3] = 0
                        return True
                except:
                    pass
                
    #player 2
    if turn == 2:
        #direct move
        if py-ty == 1 and abs(px-tx) == 1:
            return True
        #single jump
        if py-ty == 2 and tx-px != 0:
            #to left of piece
            if tx-px == -2:
                if 0!= board[py-1][px-1] != turn:
                    board[py-1][px-1] = 0
                    return True
            #to right of piece
            if tx-px == 2:
                if 0!= board[py-1][px+1] != turn:
                    board[py-1][px+1] = 0
                    return True
        #double jump
        if py-ty == 4:
            #if first jump is left
            if 0 != board[py-1][px-1] != turn and board[py-2][px-2] == 0:
                #if second jump is left
                try:
                    if 0 != board[ty+1][tx+1] != turn and board[ty][tx] == 0 and px-tx == 4:
                        #animate first jump
                        board[py][px] = 0
                        board[py-2][px-2] = turn
                        board[py-1][px-1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py-2][px-2] = 0
                        board[py-3][px-3] = 0
                        return True
                except:
                    pass
                #if second jump is right
                try:
                    if 0 != board[ty+1][tx-1] != turn and board[ty][tx] == 0 and px-tx == 0:
                        #animate first jump
                        board[py][px] = 0
                        board[py-2][px-2] = turn
                        board[py-1][px-1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py-2][px-2] = 0
                        board[py-3][px-1] = 0
                        return True
                except:
                    pass
            #if first jump is right
            elif 0 != board[py-1][px+1] != turn and board[py-2][px+2] == 0:
                #if second jump is left
                try:
                    if 0 != board[ty+1][tx+1] != turn and board[ty][tx] == 0 and tx-px == 0:
                        #animate first jump
                        board[py][px] = 0
                        board[py-2][px+2] = turn
                        board[py-1][px+1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py-2][px+2] = 0
                        board[py-3][px+1] = 0
                        return True
                except:
                    pass
                #if second jump is right
                try:
                    if 0 != board[ty+1][tx-1] != turn and board[ty][tx] == 0 and tx-px == 4:
                        #animate first jump
                        board[py][px] = 0
                        board[py-2][px+2] = turn
                        board[py-1][px+1] = 0
                        display(board)
                        sleep(0.2)
                        #animate second jump
                        board[py-2][px+2] = 0
                        board[py-3][px+3] = 0
                        return True
                except:
                    pass

    return False




