import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# verticies = (
#     (1, -1, -1),
#     (1, 1, -1),
#     (-1, 1, -1),
#     (-1, -1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, -1, 1),
#     (-1, 1, 1)
# )

# edges = (
#     (0,1),
#     (0,3),
#     (0,4),
#     (2,1),
#     (2,3),
#     (2,7),
#     (6,3),
#     (6,4),
#     (6,7),
#     (5,1),
#     (5,4),
#     (5,7)
# )

# surfaces = (
#     (0,1,2,3),
#     (3,2,7,6),
#     (6,7,5,4),
#     (4,5,1,0),
#     (1,5,7,2),
#     (4,0,3,6)
# )


vertices = [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)
]


edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (0, 3),
    (1, 3),
    (2, 3)
]


surfaces = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
]


colors = (
    (1, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 0, 0)
)



def Simplex():
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    # draw surfaces
    glBegin(GL_TRIANGLES)
    for surface, color in zip(surfaces, colors):
        glColor3fv(color)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    # draw lines
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1, 1, 1))   # white
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Simplex()
        pygame.display.flip()
        pygame.time.wait(10)


main()