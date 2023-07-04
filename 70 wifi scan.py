import network
from time import sleep
#import urequests
#import _thread as th
#import ujson
#import ufirestore

station = network.WLAN(network.STA_IF)

print(station)
sleep(1)
station.active(True)
print(station.scan())

print(station.isconnected())

#station.connect("Avi1", "*****")

#while station.isconnected() == False:
#    pass

#print(station.isconnected())
#print(station.ifconfig())
