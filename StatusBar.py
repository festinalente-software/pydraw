import tkinter as tk
from tkinter import ttk

class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(bd = 2, relief=tk.SUNKEN)

        self.label = tk.Label(self, bd=2, anchor=tk.W)
        self.label.pack(fill=tk.X)
        self.label.grid(row=0, column=0, sticky="WS")

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("my.Horizontal.TProgressbar", troughcolor='#1e3b65', background='#c41811')
        self.progress = ttk.Progressbar(self, style="my.Horizontal.TProgressbar", orient="horizontal", mode="determinate")
        self.progress.grid(sticky=tk.NSEW, row=0, column=1)
        self.progress.grid_remove()
        tk.Grid.columnconfigure(self, 1, weight=1)

    def setMessage(self, text=None, **kwargs):
        if text is None:
            text = ''
        self.label.config(text=text)
        self.master.update_idletasks()

        resetInSecs = kwargs.get('resetInSecs', 0)
        if resetInSecs:
            self.master.after(resetInSecs * 1000, self.reset)

    def reset(self):
        self.label.config(text='Ready')
        self.master.update_idletasks()

    def setProgress(self, text=None, value=None, range=None):
        if text == "" and value == 0 and range == 0:
            self.progress.grid_remove()
        else:
            self.progress.grid()
        self.master.update_idletasks()

