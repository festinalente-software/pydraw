import logging
from tkinter import Menu

logger = logging.getLogger(__name__)


class MainMenu(Menu):

    def __init__(self, master, owner, **kwargs):
        super().__init__(master, **kwargs)
        self.owner = owner
        self.initMenuItems()
        master.config(menu=self)

    def initMenuItems(self):
        self.menu_file = Menu(self, tearoff=0)
        self.menu_file.add_command(label="New", command=self.action_newDrawing)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Exit", command=self.action_exit)
        self.add_cascade(label="File", menu=self.menu_file)

    def action_newDrawing(self):
        self.owner.new_drawing()

    def action_exit(self):
        self.owner.on_closing()
