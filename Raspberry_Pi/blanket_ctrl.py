# -*- coding: utf-8 -*-

# This script will be used to send signals from specified GPIO pins to the electric blanket 
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
GPIO.setmode(GPIO.BCM)
sensor = W1ThermSensor()

#specify what pin(s) to use
GPIO.setup(32, GPIO.OUT) # '.OUT' indicates that the signal is outgoing

temp = sensor.get_temperature()

def active_sig():
    GPIO.output(32, True)# send the signal

def kill_sig():
    GPIO.output(32, False)# stop sending the signal
    
def change_temp(req_temp):
    temp = sensor.get_temperature()
    if req_temp > sensor.get_temperature():
        active_sig() # turn on the signal to change the temperature
        while temp != req_temp: # loop until the correct temperature has been reached
            temp = sensor.get_temperature() # update temp by getting a measure from the probe
        kill_sig() # kill the signal once the correct temperature has been reached.
            
    #if req_temp < sensor.get_temperature():
        