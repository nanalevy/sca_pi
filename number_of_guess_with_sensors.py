#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random
# breadboard setup
GPIO. setmode (GPIO.BOARD)
GPIO. setwarnings (False)

# assign pin number for Passive Buzzer; pin 32 =GPIO 12
buzz_pin = 32
led_pin =11
# set Passive Buzzwe pin's mode as output
GPIO.setup (buzz_pin,GPIO.OUT)
GPIO. setup(led_pin, GPIO.OUT)
# create Buzz function and set unitial sound frequency to 1000 Hz
Buzz= GPIO. PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
n = random.randint(1,10)
# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start (50)
time.sleep(1)
GPIO. output (led_pin, True) 
time. sleep (2)
# stop Passive Buzzer using Buzz function
Buzz.stop()

# reset GPIO resources used by script
GPIO.cleanup()
