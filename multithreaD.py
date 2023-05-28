import _thread as th
from time import sleep
from machine import Pin

led1 = Pin(23, Pin.OUT)
led2 = Pin(22, Pin.OUT)
flag = 0

def blink_led(message, led, start, wait):
    sleep(start)
    print(message)
    global flag
    while flag == 0:
        led.on()
        sleep(wait)
        led.off()
        sleep(wait)
        
try:
    print("try")
    th.start_new_thread(blink_led, ("Hi", led1, 2, 1))
    th.start_new_thread(blink_led, ("Hello", led2, 5, 0.3))
except th.error as e:
    print("error")

sleep(15)
flag = 1