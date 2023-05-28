import machine
import time

from machine import Pin
from time import sleep

led_2 = Pin(32, Pin.OUT)

while True:
    led_2.value(1)
    sleep(1)
    led_2.value(0)
    sleep(1)
    print('ddD')