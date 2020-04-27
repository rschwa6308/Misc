from OpenGL.GL import *
from OpenGL.GLU import *

class Polyhedron:
    def __init__(self, vertices, edges, faces, face_colors, mesh_type=GL_TRIANGLES):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces  # must be given in counterclockwise wrapping order

        if len(faces) != len(face_colors):
            raise ValueError(f'Number of face colors given ({len(face_colors)}) does not match number of faces ({len(faces)}).')

        self.face_colors = face_colors
        self.mesh_type = mesh_type
    
    def draw_wireframe(self):
        glBegin(GL_LINES)
        glColor3fv((0, 0, 0))   # black
        for e in self.edges:
            for v in e:
                glVertex3fv(self.vertices[v])
        glEnd()
    
    def draw(self):
        glBegin(self.mesh_type)
        for f, color in zip(self.faces, self.face_colors):
            glColor3fv(color)
            for v in f:
                glVertex3fv(self.vertices[v])
        glEnd()

        self.draw_wireframe()


if __name__ == '__main__':
    import pygame
    from pygame.locals import *

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

    gluPerspective(45, (display_dims[0] / display_dims[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -3.0)

    red = (1, 0, 0)
    green = (0, 1, 0)
    blue = (0, 0, 1)
    yellow = (1, 1, 0)
    simplex = Polyhedron(
        [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)],
        [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)],
        [(0, 2, 1), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
        [blue, green, blue, yellow]
    )

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        simplex.draw()
        pygame.display.flip()
