
from collections import namedtuple
import math
from base_shapes.drawable import Drawable
from base_shapes.triangle import Triangle
from base_shapes.vertex import Vertex


RotationMatrix = namedtuple("RotationMatrix", "cos_x sin_x cos_y sin_y cos_z sin_z")

def update_element_if_needed(element: Drawable):
    if element.needs_update:
        update_element_vertices(element)
        update_element_triangles(element)
        element.needs_update = False


def update_element_vertices(element: Drawable):
    rotation_matrix = get_rotation_matrix_from_element(element)
    element.vertices = tuple(
        rotate_vertex(v, rotation_matrix) * element.scale + element.origin + element.translation
        for v in element.base_vertices
    )

def get_rotation_matrix_from_element(element: Drawable):
    rotation_z = math.radians(element.rotation.z)
    cos_z, sin_z = math.cos(rotation_z), math.sin(rotation_z)
    rotation_y = math.radians(element.rotation.y)
    cos_y, sin_y = math.cos(rotation_y), math.sin(rotation_y)
    rotation_x = math.radians(element.rotation.x)
    cos_x, sin_x = math.cos(rotation_x), math.sin(rotation_x)

    return RotationMatrix(cos_x, sin_x, cos_y, sin_y, cos_z, sin_z)

def rotate_vertex(vertex, rotation_matrix: RotationMatrix):
    # Z axis
    rotated_z = Vertex(
        vertex.x * rotation_matrix.cos_z + vertex.y * rotation_matrix.sin_z,
        -vertex.x * rotation_matrix.sin_z + vertex.y * rotation_matrix.cos_z,
        vertex.z,
    )
    # Y axis
    rotated_zy = Vertex(
        rotated_z.x * rotation_matrix.cos_y - vertex.z* rotation_matrix.sin_y,
        rotated_z.y,
        rotated_z.x * rotation_matrix.sin_y + rotated_z.z * rotation_matrix.cos_y,
    )
    # X axis
    rotated_zyx = Vertex(
        rotated_zy.x,
        rotated_zy.y * rotation_matrix.cos_x + rotated_zy.z * rotation_matrix.sin_x,
        -rotated_zy.y * rotation_matrix.sin_x + rotated_zy.z * rotation_matrix.cos_x,
    )

    return rotated_zyx


def update_element_triangles(element: Drawable):
    element.triangles = tuple(
        Triangle(element.vertices[x], element.vertices[y], element.vertices[z])
        for x, y, z in element.triangle_edges
    )