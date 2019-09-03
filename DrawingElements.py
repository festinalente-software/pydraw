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

    @property
    def widget(self):
        return None if not hasattr(self, '_widget') else self._widget

    @widget.setter
    def widget(self, obj):
        self._widget = obj

    def bindEventsFor(self, elem, canvas):
        def onObjClick(event) :
            canvas.on_object_click(self, event)
        canvas.tag_bind(elem, '<ButtonPress-1>', onObjClick)

    def moveBy(self, delta):
        raise NotImplemented()

class TextElement(DrawingElement):
    position: Point
    text: str

    def __init__(self, position, text, font_size=None, font_name=None):
        super().__init__()
        self.position = Point(position)
        self.text = str(text)
        self.font_size = font_size if font_size is not None else self.__class__.Get_Default_Fontsize()
        self.font_name = font_name if font_name is not None else self.__class__.Get_Default_Fontname()

    def draw_on_canvas(self, canvas, context: DrawingContext):
        pos = context.transpose(self.position)
        fsize = int(context.scaled(self.font_size))
        self.widget = canvas.create_text(*pos.xy, text=self.text, font=(self.font_name, fsize),
                                         activefill=self.focus_color)
        self.bindEventsFor(self.widget, canvas)

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, newvalue):
        self._font_size = newvalue

    @classmethod
    def Get_Default_Fontsize(cls):
        return  50 if not hasattr(cls,'_Default_Font_Size') else cls._Default_Font_Size

    @classmethod
    def Set_Default_Fontsize(cls, newvalue):
        cls._Default_Font_Size = newvalue

    @classmethod
    def Get_Default_Fontname(cls):
        return  "TkDefaultFont" if not hasattr(cls,'_Default_Font_Name') else cls._Default_Font_Name

    @classmethod
    def Set_Default_Fontname(cls, newvalue):
        cls._Default_Font_Name = newvalue

    def moveBy(self, delta):
        self.position += delta

class LineElement(DrawingElement):
    def __init__(self, start, end):
        super().__init__()
        self.start = Point(start)
        self.end = Point(end)

    def draw_on_canvas(self, canvas, context: DrawingContext):
        flat_xy = list(context.transpose(self.start).xy)
        flat_xy.extend(context.transpose(self.end).xy)
        self.widget = canvas.create_line(flat_xy, activefill=self.focus_color)
        self.bindEventsFor(self.widget, canvas)

    def moveBy(self, delta):
        self.start += delta
        self.end += delta
