import time
from machine import Pin, ADC, PWM
from time import sleep

adc_pin = Pin(32, Pin.IN)
adc = ADC(adc_pin)
adc.atten(ADC.ATTN_11DB)

pwm_led = PWM(Pin(12, mode=Pin.OUT))
pwm_led.freq(1000)

while True:
    val = int(adc.read() / 4)
    pwm_led.duty(val)
    
    sleep(0.1)
    
    
# Now you: make it swipe. 

