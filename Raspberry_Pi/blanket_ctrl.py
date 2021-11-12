# This script will be used to send signals from specified GPIO pins to the electric blanket 
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

GPIO.setmode(GPIO.BCM)
sensor = W1ThermSensor()

#specify what pin(s) to use
GPIO.setup(32, GPIO.OUT) # '.OUT' indicates that the signal is outgoing

temp = sensor.get_temperature()

def active_sig():
    GPIO.output(32, GPIO.HIGH)# send the signal

def kill_sig():
    GPIO.output(32, GPIO.LOW)# stop sending the signal
    GPIO.cleanup(32) # revert the GPIO pin to its state before the signal was sent
    
def change_temp(req_temp):
    temp = sensor.get_temperature()
    if req_temp > sensor.get_temperature():
        active_sig() # turn on the signal to change the temperature
        while temp != req_temp: # loop until the correct temperature has been reached
            temp = sensor.get_temperature() # update temp by getting a measure from the probe
        kill_sig() # kill the signal once the correct temperature has been reached.