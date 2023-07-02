import time
from machine import Pin, ADC
from time import sleep

adc_pin = Pin(32, Pin.IN)
adc = ADC(adc_pin)
adc.atten(ADC.ATTN_11DB)

while True:
    print(f'The value is {adc.read()}')
    sleep(1)
    
    
# Now you: Make it be a VoltMeter. 