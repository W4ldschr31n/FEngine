from OpenGL.GL import *

from base_shapes.vertex import Vertex

class Triangle:
    def __init__(self, v1, v2, v3):
        self.vertices = [v1, v2, v3]
        self.vertex_count = 3
    
    def draw(self, color=Vertex(255, 255, 255)):
        glColor3f(color.x, color.y, color.z)
        # Empty triangles
        glBegin(GL_LINES)
        self.vertices[0].draw()
        self.vertices[1].draw()
        self.vertices[1].draw()
        self.vertices[2].draw()
        self.vertices[2].draw()
        self.vertices[0].draw()
        glEnd()
        # Filled triangles
        # glBegin(GL_TRIANGLES)
        # self.vertices[0].draw()
        # self.vertices[1].draw()
        # self.vertices[2].draw()
        # glEnd()
