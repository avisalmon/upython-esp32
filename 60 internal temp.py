import esp32
from time import sleep

while True:
    temp = esp32.raw_temperature()
    print(temp)
    sleep(1)
