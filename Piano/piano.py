#keyboard piano

import pygame,os,sys
from pygame import *
from pygame.locals import *
from random import *


#init pygame stuff
pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((800,600))

def flip(screen):
    screen.fill((randint(0,255),randint(0,255),randint(0,255)))
    pygame.display.update()



#load sounds
assets = os.path.split(os.path.abspath(__file__))[0]
assets = os.path.join(assets,"assets")
c4 = pygame.mixer.Sound(os.path.join(assets,"C4-261.wav"))
d4 = pygame.mixer.Sound(os.path.join(assets,"D4-293.wav"))
e4 = pygame.mixer.Sound(os.path.join(assets,"E4-329.wav"))
f4 = pygame.mixer.Sound(os.path.join(assets,"F4-349.wav"))
g4 = pygame.mixer.Sound(os.path.join(assets,"G4-392.wav"))
a4 = pygame.mixer.Sound(os.path.join(assets,"A4-440.wav"))
b4 = pygame.mixer.Sound(os.path.join(assets,"B4-493.wav"))
c5 = pygame.mixer.Sound(os.path.join(assets,"C5-523.wav"))
d5 = pygame.mixer.Sound(os.path.join(assets,"D5-587.wav"))
e5 = pygame.mixer.Sound(os.path.join(assets,"E5-659.wav"))
f5 = pygame.mixer.Sound(os.path.join(assets,"F5-698.wav"))
g5 = pygame.mixer.Sound(os.path.join(assets,"G5-784.wav"))
a5 = pygame.mixer.Sound(os.path.join(assets,"A5-880.wav"))
b5 = pygame.mixer.Sound(os.path.join(assets,"B5-988.wav"))


flip(screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                c4.play()
                flip(screen)
            if event.key == K_q:
                d4.play()
                flip(screen)
            if event.key == K_w:
                e4.play()
                flip(screen)
            if event.key == K_e:
                f4.play()
                flip(screen)
            if event.key == K_r:
                g4.play()
                flip(screen)
            if event.key == K_t:
                a4.play()
                flip(screen)
            if event.key == K_y:
                b4.play()
                flip(screen)
            if event.key == K_u:
                c5.play()
                flip(screen)
            if event.key == K_i:
                d5.play()
                flip(screen)
            if event.key == K_o:
                e5.play()
                flip(screen)
            if event.key == K_p:
                f5.play()
                flip(screen)
            if event.key == K_LEFTBRACKET:
                g5.play()
                flip(screen)
            if event.key == K_RIGHTBRACKET:
                a5.play()
                flip(screen)
            if event.key == K_BACKSLASH:
                b5.play()
                flip(screen)
        if event.type == KEYUP:
            if event.key == K_TAB:
                c4.stop()
            if event.key == K_q:
                d4.stop()
            if event.key == K_w:
                e4.stop()
            if event.key == K_e:
                f4.stop()
            if event.key == K_r:
                g4.stop()
            if event.key == K_t:
                a4.stop()
            if event.key == K_y:
                b4.stop()
            if event.key == K_u:
                c5.stop()
            if event.key == K_i:
                d5.stop()
            if event.key == K_o:
                e5.stop()
            if event.key == K_p:
                f5.stop()
            if event.key == K_LEFTBRACKET:
                g5.stop()
            if event.key == K_RIGHTBRACKET:
                a5.stop()
            if event.key == K_BACKSLASH:
                b5.stop()
