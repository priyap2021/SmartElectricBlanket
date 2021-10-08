import tkinter as tk
from tkinter.constants import GROOVE, NONE

class GUI(tk.Frame):

    def __init__(self, master=None): #define the class constructor (master will usually be an instance of tk.Tk())
        super().__init__(master)
        self.master = master
        self.pack() 
        self.draw_ui()

    def draw_ui(self): #define window dimensions and properties
        self.master.geometry("300x500")
        self.master.title("Smart Blanket")
        self.master.resizable(False, False)
        self.button_frame = tk.Frame(self.master, borderwidth=4, relief=GROOVE, height=500, width=300) #define a container for buttons
        self.draw_buttons()
        self.button_frame.pack(side=tk.TOP) #make sure the frame is included at the top of the window
    
    def draw_buttons(self): #define the buttons that will populate the frame and window
        self.power_button = tk.Button(self.button_frame, text="Power", fg='red', height=2, width=20)
        self.wifi_button = tk.Button(self.button_frame, text="Wifi", fg='blue', height=2, width=20)
        self.temp_scale = tk.Scale(self.master, from_=68, to=140, tickinterval=1, length=450)
        self.power_button.pack(side=tk.RIGHT) #start packing the buttons in their containers
        self.wifi_button.pack(side=tk.LEFT)
        self.temp_scale.pack(side=tk.RIGHT)

root = tk.Tk()
interface = GUI(master=root)
interface.mainloop() #make sure mainloop is started so the GUI is displayed
