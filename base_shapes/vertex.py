from OpenGL.GL import *

from numbers import Number

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def draw(self):
        glVertex3d(self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, Number):
            return Vertex(self.x+other, self.y+other, self.z+other)
        elif isinstance(other, Vertex):
            return Vertex(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z,
            )
        else:
            raise NotImplementedError
    
    def __mul__(self, other):
        if isinstance(other, Number):
            return Vertex(self.x*other, self.y*other, self.z*other)
        elif isinstance(other, Vertex):
            return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __neg__(self):
        return Vertex(-self.x, -self.y, -self.z)