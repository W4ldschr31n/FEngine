from base_shapes.drawable import Drawable
from base_shapes.vertex import Vertex


class Diamond(Drawable):
    base_vertices = (
        Vertex(-0.5, 0, 0),
        Vertex(-0.5, 0, 1),
        Vertex(0.5, 0, 1),
        Vertex(0.5, 0, 0),
        Vertex(0, 1, 0.5),
        Vertex(0, -1, 0.5),
    )
    
    triangle_edges = (
        # Top South
        (0, 4, 3),
        # Top West
        (1, 4, 0),
        # Top North
        (2, 4, 1),
        # Top East
        (3, 4, 2),
        # Bottom South
        (0, 3, 5),
        # Bottom West
        (1, 0, 5),
        # Bottom North
        (2, 1, 5),
        # Bottom East
        (3, 2, 5),
    )




    