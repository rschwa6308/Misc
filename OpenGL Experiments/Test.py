from Polyhedron import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from random import random

pygame.init()
display_dims = (1000, 800)
pygame.display.set_mode(display_dims, DOUBLEBUF|OPENGL)

glDepthMask(GL_TRUE)
glDepthFunc(GL_LESS)
glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)
glFrontFace(GL_CCW)     # use counterclockwise wrapping as front face
glShadeModel(GL_SMOOTH)
glLineWidth(2)

glClearColor(0.9, 0.9, 0.9, 1)

gluPerspective(45, (display_dims[0] / display_dims[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5.0)

red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
yellow = (1, 1, 0)
rand_color = lambda: (random(), random(), random())
cube = Polyhedron(
    [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)],
    [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)],
    [(3, 2, 1, 0), (4, 5, 6, 7), (1, 5, 4, 0), (3, 7, 6, 2), (4, 7, 3, 0), (2, 6, 5, 1)],
    [rand_color() for _ in range(6)],
    mesh_type=GL_QUADS
)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 1, 2, 2)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    cube.draw()
    pygame.display.flip()
