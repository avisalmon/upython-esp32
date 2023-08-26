#########################################
# Learning Python in a fun way.
# on ESP32 controller (Micro-Python) 
# Created by: Avi Salmon. 
#
#   please visit www.matazim.co.il for more 
#   training and materials. 
#########################################


# In this example we will just blink a led. 

# this are the things we need to import and use for this example. 
from machine import Pin
from time import sleep

# Define a pin object on pin 12, define it as output:
led_12 = Pin(12, Pin.OUT)

count = 0

# lets blink the led ? times: 
while count < 4:
    led_12.value(1)
    sleep(1)
    led_12.value(0)
    sleep(1)
    count += 1  # this is like writing: count = count + 1
    print(f'blinking {count}')

# Now you do: 

# 1. Blinke it faster... slower...
# 2. Add another led and make them flash like a police car
# 3. Now take three leds, Red, Green and Yello and make them work like a traffic light. 
