from base_shapes.drawable import Drawable
from base_shapes.vertex import Vertex

class Square(Drawable):
    base_vertices = (
        Vertex(-0.5, -0.5, -0.5),
        Vertex(-0.5, 0.5, -0.5),
        Vertex(0.5, 0.5, -0.5),
        Vertex(0.5, -0.5, -0.5),

        Vertex(-0.5, -0.5, 0.5),
        Vertex(-0.5, 0.5, 0.5),
        Vertex(0.5, 0.5, 0.5),
        Vertex(0.5, -0.5, 0.5),
    )
    
    triangle_edges = (
        # South
        (0, 1, 2),
        (0, 2, 3),
        # Top
        (1, 5, 6),
        (1, 6, 2),
        # North
        (4, 5, 6),
        (4, 6, 7),
        # Bottom
        (0, 4, 7),
        (0, 7, 3),
        # West
        (1, 0, 4),
        (1, 4, 5),
        # East
        (2, 6, 7),
        (2, 7, 3)
    )




    