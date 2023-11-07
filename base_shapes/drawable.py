from base_shapes.triangle import Triangle
from base_shapes.vertex import Vertex

class Drawable:
    base_vertices = tuple()
    triangle_edges = tuple()
    scale = 1
    origin = Vertex(0, 0, 0)
    vertices = tuple()
    triangles = tuple()

    def __init__(self, base_vertices=tuple(), triangle_edges=tuple(), scale=1, origin=Vertex(0, 0, 0)):
        # Resize then translate
        self.base_vertices = base_vertices or self.base_vertices
        self.triangle_edges = triangle_edges or self.triangle_edges
        self.set_scale(scale)
        self.set_origin(origin)
        self.update_vertices()
        self.update_triangles()

    def set_scale(self, number):
        self.scale = number
    
    def set_origin(self, origin):
        self.origin = origin
    
    def update_vertices(self):
        self.vertices = tuple(
            v * self.scale + self.origin for v in self.base_vertices
        )

    def reset_vertices(self):
        self.vertices = self.base_vertices

    def update_triangles(self):
        self.triangles = tuple(
            Triangle(self.vertices[x], self.vertices[y], self.vertices[z])
            for x, y, z in self.triangle_edges
        )

    def draw(self):
        for t in self.triangles:
            t.draw()