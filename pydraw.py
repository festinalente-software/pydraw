import tkinter as tk

from DrawingElements import TextElement
from PyDrawCanvas import PyDrawCanvas
from PointAndCo import Point


def main():
    top = tk.Tk()

    TextElement.Set_Default_Fontname('Courier')
    TextElement.Set_Default_Fontsize(40)

    canvas = PyDrawCanvas(master=top)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.init_after_pack()

    cv_center = canvas.drawing_area.center()
    txt1 = TextElement(position=cv_center, text='Hello PyDraw', font_size=80)
    canvas.add_element(txt1)
    txt2 = TextElement(position=(cv_center + Point(0, cv_center.y / 2)), text='by Festina Lente Software',
                       font_name='Helvetica')
    txt2.font_size = 30
    canvas.add_element(txt2)

    top.mainloop()


if __name__ == "__main__":
    main()
