import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from base_shapes.drawable import Drawable
from base_shapes.diamond import Diamond
from base_shapes.square import Square
from base_shapes.triangle import Triangle
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
                # Handle scale and translate
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_KP_PLUS:
                        scale = 0.1
                    elif event.key == pg.K_KP_MINUS:
                        scale = -0.1
                    if event.key == pg.K_KP_5:
                        self.reset_view()
            # Handle rotations
            keys = pg.key.get_pressed()
            rot_x, rot_y, rot_z = 0, 0, 0
            if keys[pg.K_KP_4]:
                rot_y = -5
            elif keys[pg.K_KP_6]:
                rot_y = 5
            if keys[pg.K_KP_8]:
                rot_x = -5
            elif keys[pg.K_KP_2]:
                rot_x = 5
            if keys[pg.K_KP_7]:
                rot_z = 5
            elif keys[pg.K_KP_9]:
                rot_z = -5
            if any ([rot_x, rot_y, rot_z]):
                glRotatef(1, rot_x, rot_y, rot_z)

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
        custom_el,
        Square(scale=0.4, origin=Vertex(-1, 0, 0)),
        Square(scale=0.4, origin=Vertex(1, 0, 0)),
        Diamond(scale=0.4, origin=Vertex(0, 1, 0)),
        Diamond(scale=0.4, origin=Vertex(0, -1, 0)),
    ]
    App(elements)