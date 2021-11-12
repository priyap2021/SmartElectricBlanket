# -*- coding: utf-8 -*-
import Display
#import tempScript
import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
disp = Display.On_Display() #from the display script

cur_temp = sensor.get_temperature() #from the temp script
cur_device = "none"

while True: #create an infinite loop, the idea should be to have this run for the duration of the device uptime
    #fetch the current temp
    temp = sensor.get_temperature()
    time.sleep(0.05)
    cur_temp = sensor.get_temperature()
    #TODO: insert a line here to get the current connected device name
    if temp != cur_temp: #TODO: include an OR here for if the connected device changes
        disp.draw_labels(temp, cur_device)
    
