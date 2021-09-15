import tkinter as tk
from tkinter.constants import GROOVE, NONE

class GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() 
        self.draw_ui()

    def draw_ui(self):
        self.master.geometry("600x300")
        self.master.title("Smart Blanket")
        self.master.resizable(False, False)
         

root = tk.Tk()
interface = GUI(master=root)
interface.mainloop()
