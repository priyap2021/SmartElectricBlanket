# -*- coding: utf-8 -*-
import Display.py
import tempScript.py
import time

disp = Display.On_Display() #from the display script
cur_temp = tempScript.read_temp() #from the temp script
cur_device = "none"

while True: #create an infinite loop, the idea should be to have this run for the duration of the device uptime
    #fetch the current temp
    temp = tempScript.read_temp()
    time.sleep(.5)
    cur_temp = tempScript.read_temp()
    #TODO: insert a line here to get the current connected device name
    if temp != cur_temp: #TODO: include an OR here for if the connected device changes
        disp.draw_labels(temp, cur_device)
    
