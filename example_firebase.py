import network
from time import sleep
#import urequests
#import _thread as th
#import ujson


station = network.WLAN(network.STA_IF)

print(station)
sleep(1)
station.active(True)
print(station.scan())

print(station.isconnected())

#station.connect("Avi1", "")

#while station.isconnected() == False:
    #pass

#print(station.isconnected())
#print(station.ifconfig())

import ufirebase
ufirebase.setURL("https://esp32-e1916-default-rtdb.firebaseio.com/")
print('I am ready')
ufirebase.get('', 'DUMP', bg = False)
print(ufirebase.DUMP)
ufirebase.put("testtag1", "1", id=0, bg = False)
ufirebase.put("struct", {'1': "Hi there", '2': [1,2,3], '3': {'a': True, 'b': False}}, id=1, bg = False)
ufirebase.get('', 'DUMP', bg = False)
print(ufirebase.DUMP)