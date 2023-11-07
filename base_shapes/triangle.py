from OpenGL.GL import *

class Triangle:
    def __init__(self, v1, v2, v3):
        self.vertices = [v1, v2, v3]
        self.vertex_count = 3
    
    def draw(self):
        glBegin(GL_LINES)
        self.vertices[0].draw()
        self.vertices[1].draw()
        self.vertices[1].draw()
        self.vertices[2].draw()
        self.vertices[2].draw()
        self.vertices[0].draw()
        glEnd()