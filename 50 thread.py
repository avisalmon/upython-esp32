import _thread as th
from time import sleep
from machine import Pin

flag = 0

def prin_something(message, wait):
    global flag
    while flag == 0:
        sleep(wait)
        print(message)
        
th.start_new_thread(prin_something, ("I am thread 1", 1))
th.start_new_thread(prin_something, ("I am thread 2", 0.3))


sleep(15)
flag = 1