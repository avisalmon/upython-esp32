import machine
import time

from machine import Pin, ADC
from time import sleep

adc_pin = Pin(36, mode=Pin.IN)
adc = ADC(adc_pin)
adc.atten(ADC.ATTN_11DB)

while True:
    print(f'The value is: {adc.read()}')
    sleep(0.2)
