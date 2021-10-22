# -*- coding: utf-8 -*-
import Display.py
import tempScript.py

disp = On_Display()
cur_temp = read_temp()
cur_device = "none"

while(true): #create an infinite loop, the idea should be to have this run for the duration of the device uptime
    #fetch the current temp
    temp = read_temp()
    #TODO: insert a line here to get the current connected device name
    if temp != cur_temp: #TODO: include an OR here for if the connected device changes
        disp.draw_labels(temp, cur_device)
    
