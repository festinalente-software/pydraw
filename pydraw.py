import tkinter as tk

from PyDrawCanvas import PyDrawCanvas


def main():
    top = tk.Tk()
    top.title("PyDraw by Festina Lente Software ")

    canvas = PyDrawCanvas(master=top)
    canvas.pack(fill=tk.BOTH, expand=True)

    top.mainloop()


if __name__ == "__main__":
    main()
