import tkinter as tk


class PyDrawCanvas(tk.Canvas):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.points = []
        self.initEvents()

    def initEvents(self):
        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.on_left_click)

    def on_resize(self, event):
        self.redraw()

    def on_left_click(self, event):
        x, y = event.x, event.y
        self.add_point(x, y)
        self.redraw()

    def add_point(self, x, y):
        self.points.append((x, y))

    def redraw(self):
        self.delete("all")

        h, w = self.winfo_height(), self.winfo_width()
        text = "Hello PyDraw"
        self.create_text(w / 2, h / 2, text=text, anchor="center", activefill="red")

        if len(self.points) >= 2:
            flat_xy = [n for point in self.points for n in point]
            self.create_line(flat_xy, activefill="red")
