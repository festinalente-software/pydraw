import tkinter as tk

from DrawingElements import LineElement


class PyDrawCanvas(tk.Canvas):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.elements = []
        self.initEvents()

    def initEvents(self):
        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.on_left_click)

    def on_resize(self, event):
        self.redraw()

    def on_left_click(self, event):
        x, y = event.x, event.y
        if hasattr(self, '_last_click_position') and self._last_click_position:
            self.add_element(LineElement(start=self._last_click_position, end=(x, y)))
            self._last_click_position = None
        else:
            self._last_click_position = (x, y)
        self.redraw()

    def add_element(self, drawing_element):
        self.elements.append(drawing_element)
        self.redraw()

    def redraw(self):
        self.delete("all")

        for element in self.elements:
            element.draw_on_canvas(self)
