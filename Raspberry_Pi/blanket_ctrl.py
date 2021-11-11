# -*- coding: utf-8 -*-

# This script will be used to send signals from specified GPIO pins to the electric blanket 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#specify what pin(s) to use
GPIO.setup(17, GPIO.OUT) # '.OUT' indicates that the signal is outgoing

def active_sig():
    GPIO.output(17, True)# send the signal

def kill_sig():
    GPIO.output(17, False)# stop sending the signal