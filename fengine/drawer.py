class Drawer:
    def __init__(self):
        self.elements = []
        self.focused_element = None

    def add_element(self, element):
        self.elements.append(element)
        self.unfocus_element()
        self.focus_previous_element()
    
    def add_all_elements(self, elements):
        self.elements.extend(elements)
    
    def set_focused_element(self, index):
        if 0 <= index < len(self.elements):
            self.focused_element = index
    
    def get_focused_element(self):
        if self.focused_element is not None:
            return self.elements[self.focused_element]

    def delete_focused_element(self):
        if self.focused_element is not None:
            del self.elements[self.focused_element]
            self.focus_previous_element()
    
    def get_non_focused_elements(self):
        if self.focused_element is not None:
            elements_copy = self.elements[:]
            elements_copy.pop(self.focused_element)
            return elements_copy
        return self.elements
    
    def focus_next_element(self):
        if self.elements:
            self.focused_element = 0 if self.focused_element is None else (self.focused_element + 1)%len(self.elements)
        else:
            self.focused_element = None
    
    def focus_previous_element(self):
        if self.elements:
            self.focused_element = (
                len(self.elements) - 1 
                if self.focused_element is None
                else (self.focused_element-1)%len(self.elements)
            )
        else:
            self.focused_element = None
    
    def unfocus_element(self):
        self.focused_element = None
