import tkinter as tk
from tkinter.constants import GROOVE, NONE

class GUI(tk.Frame):

    def __init__(self, master=None): #define the class constructor (master will usually be an instance of tk.Tk())
        super().__init__(master)
        self.master = master
        self.pack() 
        self.requestedTemp = tk.DoubleVar() #declare a variable that will be set by the slider
        self.displayTemp = tk.StringVar() #declare a variable to hold the current temperature as a string
        self.draw_ui()

    def draw_ui(self): #define window dimensions and properties
        self.master.geometry("300x500")
        self.master.title("Smart Blanket")
        self.master.resizable(False, False)
        self.button_frame = tk.Frame(self.master, borderwidth=4, relief=GROOVE, height=500, width=300) #define a container for buttons
        self.draw_buttons()
        self.draw_TempFrame()
        self.button_frame.pack(side=tk.TOP) #make sure the frame is included at the top of the window
    
    def draw_buttons(self): #define the buttons that will populate the frame and window
        self.power_button = tk.Button(self.button_frame, text="Power", fg='red', height=2, width=20)
        self.wifi_button = tk.Button(self.button_frame, text="Wifi", fg='blue', height=2, width=20)
        self.temp_scale = tk.Scale(self.master, from_=68, to=140, tickinterval=1, length=450, variable=self.requestedTemp)
        self.power_button.pack(side=tk.RIGHT) #start packing the buttons in their containers
        self.wifi_button.pack(side=tk.LEFT)
        self.temp_scale.pack(side=tk.RIGHT)

    def draw_TempFrame(self): #draw the label that will display the current temperature
        self.TempFrame = tk.Label(self.master, height=5, width=20, textvariable=self.displayTemp, borderwidth=4, relief=GROOVE)
        self.TempFrame.pack(side=tk.BOTTOM)
    
    def set_displayTemp(self, s): #set the temperature being displayed in the text field
       self.displayTemp.set(s) #change the value of curTemp to s
       #this function could allow us to fetch a temp reading from the sensors and display it.
       #For a good example of how the text field can be manipulated, try changing the variable used
       #in TempFrame from 'displayTemp' to 'requestedTemp' and observe.
        
    def get_requestedTemp(self):
        return self.requestedTemp

root = tk.Tk()
interface = GUI(master=root)
interface.mainloop() #make sure mainloop is started so the GUI is displayed
