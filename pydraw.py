import tkinter as tk

from DrawingElements import TextElement
from PyDrawCanvas import PyDrawCanvas


def main():
    top = tk.Tk()
    top.title("PyDraw by Festina Lente Software ")

    canvas = PyDrawCanvas(master=top)
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.add_element(TextElement(position=(100, 100), text='Hello PyDraw'))

    top.mainloop()


if __name__ == "__main__":
    main()
