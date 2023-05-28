import machine
import time

from machine import Pin
from time import sleep

led_32 = Pin(32, Pin.OUT)
count = 0

while True:
    led_32.value(1)
    sleep(1)
    led_32.value(0)
    sleep(1)
    count += 1
    print(f'blinking {count}')
