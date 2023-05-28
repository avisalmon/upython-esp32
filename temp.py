from machine import Pin
from time import sleep
import dht


dht_obj = dht.DHT11(Pin(2))

while True:
    
    try:
        dht_obj.measure()
        temp = dht_obj.temperature()
        hum = dht_obj.humidity()
        print(f'Humidity: {hum} ; temp: {temp}')
        sleep(1)
    except OSError as e:
        print(f'Failed: {e}')
        
        