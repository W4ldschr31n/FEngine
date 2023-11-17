import pygame as pg
from base_shapes.drawable import Drawable
from base_shapes.diamond import Diamond
from base_shapes.square import Square
from base_shapes.vertex import Vertex
from fengine.animation_player import ANIMATION_TYPE_MOVE, ANIMATION_TYPE_ROTATE
from fengine.fengine_core import FEngineCore

display = (640, 480)

class App:
    def __init__(self, elements):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_STENCIL_SIZE, 8)
        pg.display.set_mode(display, pg.OPENGL|pg.DOUBLEBUF|pg.GL_DEPTH_SIZE)
        self.clock = pg.time.Clock()
        self.fengine = FEngineCore(display, False, True)
        self.fengine.add_all_elements(elements)
        self.fengine.focus_next_element()
        self.main()

    def main(self):
        running = True
        self.fengine.start()

        while running:
            for event in pg.event.get():
                # Handle exit signal
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    # Scale elements
                    if event.key == pg.K_KP_PLUS:
                        for e in self.fengine.elements:
                            e.add_scale(0.1)
                    elif event.key == pg.K_KP_MINUS:
                        for e in self.fengine.elements:
                            e.add_scale(-0.1)
                    # Reset camera
                    if event.key == pg.K_KP_5:
                        self.fengine.reset_view()
                    # Reset elements
                    if event.key == pg.K_KP_0:
                        for e in self.fengine.elements:
                            e.reset_vertices()
                    if event.key == pg.K_r:
                        self.fengine.get_focused_element().reset_position()
                    if event.key == pg.K_f:
                        self.fengine.get_focused_element().reset_transformations()
                    # Animate element
                    if event.key == pg.K_KP_1:
                        self.fengine.play_animation(0, ANIMATION_TYPE_MOVE)
                    elif event.key == pg.K_KP_3:
                        self.fengine.play_animation(0, ANIMATION_TYPE_ROTATE)
                    # Add or delete element
                    if event.key == pg.K_1:
                        self.fengine.add_element(Square())
                    elif event.key == pg.K_2:
                        self.fengine.add_element(Diamond())
                    elif event.key == pg.K_3:
                        self.fengine.delete_focused_element()
                    # Changing focused element
                    if event.key == pg.K_LEFT:
                        self.fengine.focus_previous_element()
                    elif event.key == pg.K_RIGHT:
                        self.fengine.focus_next_element()
                    elif event.key == pg.K_UP:
                        self.fengine.set_focused_element(0)
                    elif event.key == pg.K_DOWN:
                        self.fengine.unfocus_element()
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
                self.fengine.rotate_view(rot_x, rot_y, rot_z)
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
                self.fengine.get_focused_element().add_rotation(rot_x, rot_y, rot_z)
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
                self.fengine.get_focused_element().add_translation(trans_x, trans_y, trans_z)
            

            self.fengine.draw_next()
            pg.display.flip()

            # Framerate
            self.clock.tick(60)
        
        self.quit()

    
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
        Square(color=Vertex(0,0,0)),
        Diamond(scale=0.4, origin=Vertex(0, 1, 0)),
        Square(scale=0.4, origin=Vertex(-1, 0, 0)),
        Square(scale=0.4, origin=Vertex(1, 0, 0)),
        Diamond(scale=0.4, origin=Vertex(0, -1, 0)),
    ]
    App(elements)