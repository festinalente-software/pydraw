import tkinter as tk


class PyDrawCanvas(tk.Canvas):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.initEvents()

    def initEvents(self):
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.redraw()

    def redraw(self):
        self.delete("all")

        h, w = self.winfo_height(), self.winfo_width()
        text = "Hello PyDraw"
        self.create_text(w / 2, h / 2, text=text, anchor="center")
