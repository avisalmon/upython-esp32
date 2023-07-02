import machine
import time

from machine import Pin
from time import sleep

led_12 = Pin(12, Pin.OUT)
count = 0

while True:
    led_12.value(1)
    sleep(1)
    led_12.value(0)
    sleep(1)
    count += 1
    print(f'blinking {count}')
