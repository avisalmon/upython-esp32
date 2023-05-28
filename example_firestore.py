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

station.connect("Avi1", "")

while station.isconnected() == False:
    pass

print(station.isconnected())
print(station.ifconfig())


#ufirestore.set_project_id("esp32-e1916")
#ufirestore.set_access_token("AIzaSyAYYbh7Yo1-E4LLT70zDuayTgwomBrDtTM")
#raw_doc = ufirestore.get("DOCUMENT_PATH")
#doc = FirebaseJson.from_raw(raw_doc)
