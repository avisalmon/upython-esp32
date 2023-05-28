from machine import Pin, ADC, PWM
import time


def map(x, in_min, in_max, out_min, out_max):
    """ return linear interpolation like map() fonction in Arduino"""
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


if __name__ == "__main__":

    # Create a PWM object linked to pin 23
    pwm_led = PWM(Pin(23,mode=Pin.OUT))
    pwm_led.freq(1_000)

    # Create an ADC object linked to pin 36
    adc = ADC(Pin(36, mode=Pin.IN))
    adc.atten(ADC.ATTN_11DB)


    while True:

        val = adc.read()
        pwm_value = map(x=val, in_min=0, in_max=4095, out_min=0,out_max=1023)
        pwm_led.duty(pwm_value)
        time.sleep_ms(10)

