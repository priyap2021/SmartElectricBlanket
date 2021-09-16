import tkinter as tk
from tkinter.constants import GROOVE, NONE

class GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() 
        self.draw_ui()

    def draw_ui(self):
        self.master.geometry("300x500")
        self.master.title("Smart Blanket")
        self.master.resizable(False, False)
        self.button_frame = tk.Frame(self.master, borderwidth=4, relief=GROOVE, height=500, width=300)
        self.draw_buttons()
        self.button_frame.pack(side=tk.TOP)
    
    def draw_buttons(self):
        self.power_button = tk.Button(self.button_frame, text="Power", fg='red', height=2, width=20)
        self.wifi_button = tk.Button(self.button_frame, text="Wifi", fg='blue', height=2, width=20)
        self.temp_scale = tk.Scale(self.master, from_=0, to=140, tickinterval=1, length=450)
        self.power_button.pack(side=tk.RIGHT)
        self.wifi_button.pack(side=tk.LEFT)
        self.temp_scale.pack(side=tk.RIGHT)

root = tk.Tk()
interface = GUI(master=root)
interface.mainloop()
