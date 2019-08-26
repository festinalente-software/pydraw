import tkinter as tk

from DrawingElements import TextElement
from PyDrawCanvas import PyDrawCanvas


def main():
    top = tk.Tk()

    canvas = PyDrawCanvas(master=top)
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.add_element(TextElement(position=canvas.drawing_area.center(), text='Hello PyDraw'))

    top.mainloop()


if __name__ == "__main__":
    main()
