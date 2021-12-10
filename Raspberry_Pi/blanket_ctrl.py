# This script will be used to send signals from specified GPIO pins to the electric blanket 
import RPi.GPIO as GPIO
import time
import Display
from w1thermsensor import W1ThermSensor

sig = 5
dc=100

GPIO.setmode(GPIO.BCM)
GPIO.setup(sig, GPIO.OUT) # '.OUT' indicates that the signal is outgoing
pwm = GPIO.PWM(sig, 1)

sensor = W1ThermSensor()
disp = Display.On_Display()

temp = sensor.get_temperature()

def active_sig():
    #GPIO.output(sig, GPIO.HIGH)# send the signal
    pwm.start(dc)

def kill_sig():
    #GPIO.output(sig, GPIO.LOW)# stop sending the signal
    pwm.stop()
    GPIO.cleanup(sig) # revert the GPIO pin to its state before the signal was sent
    
def change_temp(req_temp):
    temp = sensor.get_temperature()
    if req_temp > sensor.get_temperature():
        active_sig() # turn on the signal to change the temperature
        while temp < req_temp: # loop until the correct temperature has been reached
            temp = sensor.get_temperature() # update temp by getting a measure from the probe
            time.sleep(0.05)
            cur_temp = sensor.get_temperature()
            if temp != cur_temp: #TODO: include an OR here for if the connected device changes
                disp.draw_labels(temp, "Heating...")
        kill_sig() # kill the signal once the correct temperature has been reached.
    else:
        disp.draw_labels(temp, "At Temperature!!")
        time.sleep(1)
        disp.draw_labels(temp, "Ready to Heat")