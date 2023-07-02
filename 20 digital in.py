# digital in

import machine
import time

from machine import Pin
from time import sleep

led_12 = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    print(led_12.value())
    sleep(1)
    
# Now you: write a code that inputs from a button and set a led accordingly. 
