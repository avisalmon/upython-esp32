from machine import Pin, TouchPad
from time import sleep

touch_obj = TouchPad(Pin(27))
led = Pin(23, Pin.OUT)

state = 'off'

while True:
    value = touch_obj.read()
    
    while state == 'off':
        sleep(0.3)
        led.value(0)
        value = touch_obj.read()
        print(f' off state: {value}')
        if value < 400:
            state = 'on'
            
    while state == 'on':
        led.value(1)
        sleep(0.3)
        value = touch_obj.read()
        print(f' on state: {value}')
        if value > 500:
            state = 'off'
    