import tkinter as tk
from datetime import datetime
from tkinter import messagebox, PhotoImage

from DragAndDropOperation import Drp_DrawLine, Drp_MoveObject
from DrawingContext import DrawingContext
from DrawingElements import LineElement
from MainMenu import MainMenu
from PointAndCo import Rectangle, Point
from StatusBar import StatusBar


def ctrlKeyPressed(event):
    return event.state & 0b100


def shftKeyPressed(event):
    return event.state & 0b001


class PyDrawCanvas(tk.Canvas):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.elements = []
        self.init_events()
        self.init_menubar()
        self.init_context()
        self.set_appicon()
        self.set_title()
        self.statusbar = None
        self.drp_Operation = None
        self.selectedObject = None

    # region Inits

    def set_appicon(self):
        self.master.tk.call('wm', 'iconphoto', self.master._w, PhotoImage(file='appicon.png'))

    def set_title(self):
        self.master.title("PyDraw by Festina Lente Software ")

    def init_events(self):
        self.focus_set()
        self.bind("<Key>", self.on_keypress)
        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.on_left_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_drop)
        self.master.protocol('WM_DELETE_WINDOW', self.on_closing)

    def init_menubar(self):
        self.menubar = MainMenu(self.master, self)

    def init_after_pack(self):
        self.create_statusbar()

    # endregion

    # region DrawingContext

    def init_context(self):
        self.drawing_area = Rectangle((0, 0, 1000, 1000))
        self.canvas_area = Rectangle((0, 0, self.winfo_width(), self.winfo_height()))
        self.drawing_context = DrawingContext(orig=self.drawing_area, target=self.canvas_area, border=0.05)

    def transposeBack(self, pos):
        return self.drawing_context.transposeBack(pos)

    def transpose(self, pos):
        return self.drawing_context.transpose(pos)

    # endregion

    # region Events

    def on_keypress(self, event):
        ec = event.char
        ek = event.keysym

        if ek == 'Escape':
            self.selectedObject = None


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

        if self.selectedObject:
            self.drp_Operation = Drp_MoveObject(self, Point(x, y), self.selectedObject)
        else:
            newLine = LineElement(start=d_point, end=d_point + (1, 1))
            self.add_element(newLine)
            self.redraw()
            self.drp_Operation = Drp_DrawLine(self, Point(x, y), newLine)
            self.selectedObject = newLine

    def on_object_click(self, object, event):
        self.selectedObject = object
        # print(f"on_object_click: event={event},object={object}")

    def on_closing(self):
        if not messagebox.askokcancel(
                'Exit Tool',
                'Do you really want to exit this tool?'):
            return
        self.master.destroy()

    def on_drag(self, event):
        if self.drp_Operation:
            self.drp_Operation.on_drag((event.x, event.y))

    def on_drop(self, event):
        if self.drp_Operation:
            self.drp_Operation.on_drop((event.x, event.y))
            self.drp_Operation = None

    # endregion

    # region Elements

    def add_element(self, drawing_element):
        self.elements.append(drawing_element)
        self.redraw()

    def new_drawing(self):
        self.setStatusMessage(text='Creating new drawing')
        self.elements = []
        self.redraw()
        self.setStatusMessage(text='Created new drawing', resetInSecs=5)

    # endregion

    # region Drawing

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

    # endregion

    # region Statusbar

    def create_statusbar(self):
        self.statusbar = StatusBar(master=self.master)
        self.statusbar.pack(fill=tk.X)

    def setStatusMessage(self, **kwargs):
        if self.statusbar:
            self.statusbar.setMessage(**kwargs)
        else:
            txt = kwargs.get("text", "")
            print(f'{datetime.now()} Status:  {txt}')

    def setProgress(self, **kwargs):
        if self.statusbar:
            self.statusbar.setProgress(**kwargs)
        else:
            ptext = kwargs.get('text', '')
            value = kwargs.get('value', 0)
            range = kwargs.get('maximum', 0)
            progr = "" if not value \
                else f'[{value}]' if not range \
                else f'[{value}/{range}]'

            print(f'{datetime.now()} Progress: {progr} - {ptext}')

    # endregion
