import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from base_shapes.drawable import Drawable
from base_shapes.diamond import Diamond
from base_shapes.square import Square
from base_shapes.vertex import Vertex

display = (640, 480)

class App:
    def __init__(self, elements):
        pg.init()
        pg.display.set_mode(display, pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.2, 0.2, 0.3, 1)
        self.elements = elements
        self.main()

    def main(self):
        running = True
        self.reset_view()

        while running:
            scale = 0.0
            for event in pg.event.get():
                # Handle exit signal
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    # Scale elements
                    if event.key == pg.K_KP_PLUS:
                        scale = 0.1
                    elif event.key == pg.K_KP_MINUS:
                        scale = -0.1
                    # Reset camera
                    if event.key == pg.K_KP_5:
                        self.reset_view()
                    # Reset elements
                    if event.key == pg.K_KP_0:
                        for e in self.elements:
                            e.reset_vertices()
                    if event.key == pg.K_r:
                        self.elements[0].reset_position()
                    if event.key == pg.K_f:
                        self.elements[0].reset_transformations()
            keys = pg.key.get_pressed()
            # Camera rotation
            rot_x, rot_y, rot_z = 0, 0, 0
            if keys[pg.K_KP_4]:
                rot_y = 5
            elif keys[pg.K_KP_6]:
                rot_y = -5
            if keys[pg.K_KP_8]:
                rot_x = 5
            elif keys[pg.K_KP_2]:
                rot_x = -5
            if keys[pg.K_KP_7]:
                rot_z = -5
            elif keys[pg.K_KP_9]:
                rot_z = 5
            if any ([rot_x, rot_y, rot_z]):
                glRotatef(1, rot_x, rot_y, rot_z)
            # Rotate element
            rot_x, rot_y, rot_z = 0, 0, 0
            if keys[pg.K_q]:
                rot_y = 1
            elif keys[pg.K_d]:
                rot_y = -1
            if keys[pg.K_z]:
                rot_x = 1
            elif keys[pg.K_s]:
                rot_x = -1
            if keys[pg.K_a]:
                rot_z = -1
            if keys[pg.K_e]:
                rot_z = 1
            if any([rot_x, rot_y, rot_z]):
                self.elements[0].add_rotation(rot_x, rot_y, rot_z)
            # Move element
            trans_x, trans_y, trans_z = 0, 0, 0
            if keys[pg.K_j]:
                trans_x = -0.1
            elif keys[pg.K_l]:
                trans_x = 0.1
            if keys[pg.K_i]:
                trans_y = 0.1
            elif keys[pg.K_k]:
                trans_y = -0.1
            if keys[pg.K_u]:
                trans_z = 0.1
            if keys[pg.K_o]:
                trans_z = -0.1
            if any([trans_x, trans_y, trans_z]):
                self.elements[0].add_translation(trans_x, trans_y, trans_z)

            # Refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            for el in self.elements:
                el.set_scale(el.scale + scale)
                el.update_vertices()
                el.update_triangles()
                el.draw()
            pg.display.flip()

            # Framerate
            self.clock.tick(60)
        
        self.quit()

    def reset_view(self):
        glLoadIdentity()
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(20, 1, 0, 0)
    
    def quit(self):
        pg.quit()


if __name__=="__main__":
    custom_el = Drawable(
        (
            Vertex(0, 0, 0),
            Vertex(-0.5, 0, 1),
            Vertex(0.5, 0, 1),
            Vertex(0, 0.5, 0.8),
        ),
        (
            (0, 1, 2),
            (0, 3, 2),
            (1, 3, 0),
            (2, 3, 1),
        )
    )
    elements = [
        Square(scale=0.4, origin=Vertex(-1, 0, 0)),
        Square(scale=0.4, origin=Vertex(1, 0, 0)),
        custom_el,
        Diamond(scale=0.4, origin=Vertex(0, 1, 0)),
        Diamond(scale=0.4, origin=Vertex(0, -1, 0)),
    ]
    App(elements)