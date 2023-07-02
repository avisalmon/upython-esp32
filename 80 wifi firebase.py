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

station.connect("Avi1", "10203040")

while station.isconnected() == False:
    pass

print(station.isconnected())
print(station.ifconfig())

import ufirebase as firebase
print('Imported Firebase')
firebase.setURL("https://bookstoreproject-9ab6c-default-rtdb.firebaseio.com/")

firebase.setURL("https://bookstoreproject-9ab6c-default-rtdb.firebaseio.com/")
print('I am ready')
firebase.get('', 'DUMP', bg = False)
print(firebase.DUMP)
#ufirebase.put("testtag1", "1", id=0, bg = False)
#ufirebase.put("struct", {'1': "Hi there", '2': [1,2,3], '3': {'a': True, 'b': False}}, id=1, bg = False)
#ufirebase.get('', 'DUMP', bg = False)
#print(ufirebase.DUMP)
