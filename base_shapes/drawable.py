import math

from base_shapes.triangle import Triangle
from base_shapes.vertex import Vertex

class Drawable:
    base_vertices = tuple()
    triangle_edges = tuple()
    scale = 1
    origin = Vertex(0, 0, 0)
    rotation = Vertex(0, 0, 0)
    vertices = tuple()
    triangles = tuple()

    def __init__(self, base_vertices=tuple(), triangle_edges=tuple(), scale=1, origin=Vertex(0, 0, 0), rotation=Vertex(0, 0, 0)):
        self.base_vertices = base_vertices or self.base_vertices
        self.triangle_edges = triangle_edges or self.triangle_edges
        self.set_scale(scale)
        self.set_origin(origin)
        self.set_rotation(rotation)
        self.update_vertices()
        self.update_triangles()

    def set_scale(self, number):
        self.scale = number
    
    def set_origin(self, origin):
        self.origin = origin

    def set_rotation(self, rotation):
        self.rotation = rotation
    
    def add_rotation(self, x, y, z):
        self.rotation += Vertex(x, y, z)
    
    def update_vertices(self):
        # Resize, translate and rotate
        self.vertices = tuple(
            self.rotate_vertex(v) * self.scale + self.origin for v in self.base_vertices
        )
    
    def rotate_vertex(self, vertex):
        # Z axis
        rotation_z = math.radians(self.rotation.z)
        cos_z, sin_z = math.cos(rotation_z), math.sin(rotation_z)
        rotated_z = Vertex(
            vertex.x * cos_z + vertex.y * sin_z,
            -vertex.x * sin_z + vertex.y * cos_z,
            vertex.z,
        )
        # Y axis
        rotation_y = math.radians(self.rotation.y)
        cos_y, sin_y = math.cos(rotation_y), math.sin(rotation_y)
        rotated_zy = Vertex(
            rotated_z.x * cos_y - vertex.z* sin_y,
            rotated_z.y,
            rotated_z.x * sin_y + rotated_z.z * cos_y,
        )
        # X axis
        rotation_x = math.radians(self.rotation.x)
        cos_x, sin_x = math.cos(rotation_x), math.sin(rotation_x)
        rotated_zyx = Vertex(
            rotated_zy.x,
            rotated_zy.y * cos_x + rotated_zy.z * sin_x,
            -rotated_zy.y * sin_x + rotated_zy.z * cos_x,
        )

        return rotated_zyx


    def reset_vertices(self):
        self.vertices = self.base_vertices
        self.scale = 1
        self.origin = Vertex(0, 0, 0)
        self.rotation = Vertex(0, 0, 0)
    
    def reset_position(self):
        self.origin = Vertex(0, 0, 0)
    
    def reset_transformations(self):
        self.scale = 1
        self.rotation = Vertex(0, 0, 0)

    def update_triangles(self):
        self.triangles = tuple(
            Triangle(self.vertices[x], self.vertices[y], self.vertices[z])
            for x, y, z in self.triangle_edges
        )

    def draw(self):
        for t in self.triangles:
            t.draw()