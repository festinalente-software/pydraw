import tkinter as tk

from DrawingContext import DrawingContext
from DrawingElements import LineElement
from MainMenu import MainMenu
from PointAndCo import Rectangle, Point


class PyDrawCanvas(tk.Canvas):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.elements = []
        self.init_events()
        self.init_menubar(master)
        self.init_context()

    def init_events(self):
        self.focus_set()
        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.on_left_click)
        self.master.protocol('WM_DELETE_WINDOW', self.on_closing)

    def init_menubar(self, master):
        self.menubar = MainMenu(master, self)

    def init_context(self):
        self.drawing_area = Rectangle((0, 0, 1000, 1000))
        self.canvas_area = Rectangle((0, 0, self.winfo_width(), self.winfo_height()))
        self.drawing_context = DrawingContext(orig=self.drawing_area, target=self.canvas_area, border=0.05)

    def on_resize(self, event):
        self.canvas_area = Rectangle((0, 0, self.winfo_width(), self.winfo_height()))
        self.drawing_context.target_rect = self.canvas_area
        self.redraw()

    def on_left_click(self, event):
        x, y = event.x, event.y
        d_point = self.drawing_context.transposeBack(Point(x, y))
        if not self.drawing_area.contains_point(d_point):
            # ignore outside border
            return

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
        self.draw_border()
        for element in self.elements:
            element.draw_on_canvas(self, self.drawing_context)

    def draw_border(self):
        ctx = self.drawing_context
        p1 = ctx.transpose(self.drawing_area.start)
        p3 = ctx.transpose(self.drawing_area.end)
        p2, p4 = Point(p1.x, p3.y), Point(p3.x, p1.y)
        points = [p1, p2, p3, p4, p1]
        flat_points = [item for p in points for item in p.xy]
        self.create_line(*flat_points)

    def new_drawing(self):
        self.elements = []
        self.redraw()

    def on_closing(self):
        self.master.destroy()
