import math
import random
from base_shapes.triangle import Triangle
from base_shapes.vertex import Vertex

def needs_update_wrapper(func):
    def wrapper(element, *args, **kwargs):
        result = func(element, *args, **kwargs)
        element.needs_update = True
        return result
    return wrapper

class Drawable:
    base_vertices = tuple()
    triangle_edges = tuple()
    translation = Vertex(0, 0, 0)
    scale = 1
    origin = Vertex(0, 0, 0)
    rotation = Vertex(0, 0, 0)
    vertices = tuple()
    triangles = tuple()
    needs_update = True

    def __init__(
            self,
            base_vertices=tuple(),
            triangle_edges=tuple(),
            translation=Vertex(0, 0, 0),
            scale=1,
            origin=Vertex(0, 0, 0),
            rotation=Vertex(0, 0, 0),
        ):
        self.base_vertices = base_vertices or self.base_vertices
        self.triangle_edges = triangle_edges or self.triangle_edges
        self.set_translation(translation)
        self.set_scale(scale)
        self.set_origin(origin)
        self.set_rotation(rotation)
        self.needs_update = True
        self.color = Vertex(random.random(), random.random(), random.random())

    @needs_update_wrapper
    def set_translation(self, translation):
        self.translation = translation

    @needs_update_wrapper
    def add_translation(self, x, y, z):
        self.translation += Vertex(x, y, z)

    @needs_update_wrapper
    def set_scale(self, number):
        self.scale = number
    
    @needs_update_wrapper
    def add_scale(self, number):
        self.scale += number
    
    @needs_update_wrapper
    def set_origin(self, origin):
        self.origin = origin

    @needs_update_wrapper
    def set_rotation(self, rotation):
        self.rotation = rotation
    
    @needs_update_wrapper
    def add_rotation(self, x, y, z):
        self.rotation += Vertex(x, y, z)

    @needs_update_wrapper
    def reset_vertices(self):
        self.vertices = self.base_vertices
        self.translation = Vertex(0, 0, 0)
        self.scale = 1
        self.origin = Vertex(0, 0, 0)
        self.rotation = Vertex(0, 0, 0)
    
    @needs_update_wrapper
    def reset_position(self):
        self.translation = Vertex(0, 0, 0)
    
    @needs_update_wrapper
    def reset_transformations(self):
        self.scale = 1
        self.rotation = Vertex(0, 0, 0)
