#!/usr/bin/env python
# this script turns the Passive Buzzer on and then off using two sound frequencies

import RPi.GPIO as GPIO
import time 

# breadboard setup
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)

# assign pin number for Passive Buzzer; pin 32 =GPIO 12
buzz_pin = 32

# set Passive Buzzer pin's mode as output
GPIO . setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM (buzz_pin,1000)

def buzz (freq) :
	Buzz.ChangeFrequency (freq)
	Buzz.start (50)
	time.sleep (1)
	Buzz.stop()
buzz (440)
buzz (880)

GPIO.cleanup()
