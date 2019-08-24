from abc import ABCMeta, abstractmethod


class DrawingElement:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def draw_on_canvas(self, canvas): raise NotImplementedError

    @property
    def focus_color(self):
        return "red"


class TextElement(DrawingElement):
    def __init__(self, position, text):
        super().__init__()
        self.position = position
        self.text = text

    def draw_on_canvas(self, canvas):
        canvas.create_text(*self.position, text=self.text, activefill=self.focus_color)


class LineElement(DrawingElement):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end

    def draw_on_canvas(self, canvas):
        flat_xy = list(self.start)
        flat_xy.extend(self.end)
        canvas.create_line(flat_xy, activefill=self.focus_color)
