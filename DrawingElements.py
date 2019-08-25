from abc import ABCMeta, abstractmethod

from DrawingContext import DrawingContext
from PointAndCo import Point


# from PyDrawCanvas import PyDrawCanvas


class DrawingElement:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def draw_on_canvas(self, canvas, context: DrawingContext): raise NotImplementedError

    @property
    def focus_color(self):
        return "red"


class TextElement(DrawingElement):
    position: Point
    text: str

    def __init__(self, position, text):
        super().__init__()
        self.position = Point(position)
        self.text = str(text)

    def draw_on_canvas(self, canvas, context: DrawingContext):
        pos = context.transpose(self.position)
        canvas.create_text(*pos.xy, text=self.text, activefill=self.focus_color)


class LineElement(DrawingElement):
    def __init__(self, start, end):
        super().__init__()
        self.start = Point(start)
        self.end = Point(end)

    def draw_on_canvas(self, canvas, context: DrawingContext):
        flat_xy = list(context.transpose(self.start).xy)
        flat_xy.extend(context.transpose(self.end).xy)
        canvas.create_line(flat_xy, activefill=self.focus_color)
