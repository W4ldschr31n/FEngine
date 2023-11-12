from OpenGL.GL import *
from OpenGL.GLU import *

from base_shapes.drawable import Drawable
from base_shapes.triangle import Triangle
from base_shapes.vertex import Vertex
from fengine import fengine_utility
from fengine.animation_player import Animation, AnimationPlayer

class FEngineCore:
    def __init__(self, display, color_chaos_mode=False, fill_triangles_mode=False):
        self.display = display
        self.color_chaos_mode = color_chaos_mode
        self.fill_triangles_mode = fill_triangles_mode
        self.elements = []
        self.animation_player = AnimationPlayer()
        self.focused_element = None
    
    def start(self):
        glClearColor(0.2, 0.2, 0.3, 1)
        glClearDepth(1.0)
        glDepthMask(GL_TRUE)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glDepthRange(0.0, 1.0)
        glEnable(GL_STENCIL_TEST)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST); 
        self.reset_view()
    
    def reset_view(self):
        glLoadIdentity()
        gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(20, 1, 0, 0)

    def rotate_view(self, rot_x, rot_y, rot_z):
        glRotatef(1, rot_x, rot_y, rot_z)

    def draw_next(self):
        # Refresh screen
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT)
        # Animate
        self.animation_player.play_step()
        # Update elements that changed since last draw
        for element in self.elements:
            fengine_utility.update_element_if_needed(element)
        if self.focused_element is not None:
            fengine_utility.update_element_if_needed(self.focused_element)
        # Draw all elements
        if self.focused_element is not None:
            self.draw_element_with_outline(self.focused_element)
        for element in self.elements:
            self.draw_element(element)
    
    def draw_element(self, element: Drawable):
        for t in element.triangles:
            self.draw_triangle(t, element.color)
    
    def draw_triangle(self, triangle: Triangle, color=Vertex(255, 255, 255)):
        glColor3f(color.x, color.y, color.z)
        if self.fill_triangles_mode:
            glBegin(GL_TRIANGLES)
            self.draw_vertex(triangle.vertices[0])
            self.draw_vertex(triangle.vertices[1])
            self.draw_vertex(triangle.vertices[2])
            glEnd()
        else:
            glBegin(GL_LINES)
            self.draw_vertex(triangle.vertices[0])
            self.draw_vertex(triangle.vertices[1])
            self.draw_vertex(triangle.vertices[1])
            self.draw_vertex(triangle.vertices[2])
            self.draw_vertex(triangle.vertices[2])
            self.draw_vertex(triangle.vertices[0])
            glEnd()

    def draw_vertex(self, vertex: Vertex):
        if self.color_chaos_mode:
            glColor3f((vertex.x+1)/2, (vertex.y+1)/2, (vertex.z+1)/2)
        glVertex3d(vertex.x, vertex.y, vertex.z)

    def play_animation(self, i, ani_type):
        self.animation_player.start_animation(Animation(ani_type, self.elements[i]))
    
    def add_element(self, element):
        self.elements.append(element)

    def remove_focused_element(self):
        self.focused_element = None

    def focus_element(self, index):
        if 0 <= index < len(self.elements):
            if self.focused_element is not None:
                self.elements.append(self.focused_element)
            self.focused_element = self.elements.pop(index)
    
    def focus_next_element(self):
        self.focus_element(0)

    def focus_previous_element(self):
        self.focus_element(len(self.elements)-1)
    
    def unfocus_element(self):
        if self.focused_element is not None:
            self.elements.append(self.focused_element)
            self.focused_element = None

    def draw_element_with_outline(self, element):
        highlighted_copy = element.get_copy()
        highlighted_copy.add_scale(0.1)
        highlighted_copy.color = Vertex(1,1,1)
        fengine_utility.update_element_if_needed(highlighted_copy)

        glStencilFunc(GL_ALWAYS, 1, 0xFF)
        glStencilMask(0xFF)
        self.draw_element(element)

        glStencilFunc(GL_NOTEQUAL, 1, 0xFF)
        glStencilMask(0x00)
        glDisable(GL_DEPTH_TEST)
        self.draw_element(highlighted_copy)

        glStencilFunc(GL_ALWAYS, 0, 0xFF)
        glStencilMask(0xFF)
        glEnable(GL_DEPTH_TEST)
