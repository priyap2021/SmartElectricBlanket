#init i2c bus, first import the needed libraries (I2C and SSD1306 Driver), then instantiate I2C + Driver
import board
import busio as io
import adafruit_ssd1306

class On_Display:
    def __init__(self): #define the class constructor (master will usually be an instance of tk.Tk())
        #create i2c instance
        self.i2c = io.I2C(board.SCL, board.SDA)
        #create an instance of the ssd1306 I2C driver
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c)
        self.init_labels() #make sure the labels are drawn
            
    def init_labels(self):
        self.oled.fill(0) #clear screen and then write the text, more labels can be added if needed (not much though)
        self.oled.text("Temp: ", 0, 0, 1) 
        self.oled.text("Status: ", 0, 20, 1) #changed from 'device' to status
        self.oled.show()
            
    def draw_labels(self, newTemp, statusMsg):
        self.oled.fill(0) #clear screen and then write the text, more labels can be added if needed (not much though)
        self.oled.text("Temp: ", 0, 0, 1)
        self.oled.text("Status: ", 0, 20, 1) #changed from 'device' to status
        
        if newTemp is not None: #make sure newTemp actually exists before trying to write it
            self.oled.text(str(newTemp), 32, 0, 1)
        else:
            self.oled.text("No Temp", 32, 0, 1)    
                    
        if statusMsg is not None: #make sure statusMsg actually exists before trying to write it
            self.oled.text(statusMsg, 45, 20, 1)
        else:
            self.oled.text("waiting...", 45, 20, 1)   
                    
        self.oled.show() #show the text that was just drawn, nuff said
    