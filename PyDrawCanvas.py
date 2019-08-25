import tkinter as tk

from DrawingContext import DrawingContext
from DrawingElements import LineElement
from PointAndCo import Rectangle, Point


class PyDrawCanvas(tk.Canvas):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.elements = []
        self.initEvents()
        self.init_context()

    def initEvents(self):
        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.on_left_click)

    def init_context(self):
        self.drawing_area = Rectangle((0, 0, 1000, 1000))
        self.canvas_area = Rectangle((0, 0, self.winfo_width(), self.winfo_height()))
        self.drawing_context = DrawingContext(orig=self.drawing_area, target=self.canvas_area)

    def on_resize(self, event):
        self.canvas_area = Rectangle((0, 0, self.winfo_width(), self.winfo_height()))
        self.drawing_context.target_rect = self.canvas_area
        self.redraw()

    def on_left_click(self, event):
        x, y = event.x, event.y
        d_point = self.drawing_context.transposeBack(Point(x, y))
        if hasattr(self, '_last_click_position') and self._last_click_position:
            self.add_element(LineElement(start=self._last_click_position, end=d_point))
            self._last_click_position = None
        else:
            self._last_click_position = d_point
        self.redraw()

    def add_element(self, drawing_element):
        self.elements.append(drawing_element)
        self.redraw()

    def redraw(self):
        self.delete("all")

        for element in self.elements:
            element.draw_on_canvas(self, self.drawing_context)
