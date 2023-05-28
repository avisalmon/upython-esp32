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

station.connect("MakerSpace", "makers1234")

while station.isconnected() == False:
    pass

print(station.isconnected())
print(station.ifconfig())

import ufirebase as firebase
firebase.setURL("https://bookstoreproject-9ab6c-default-rtdb.firebaseio.com/")

# ufirestore.set_project_id("bookstoreproject-9ab6c")
#ufirestore.set_access_token("-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDN41raai8bzbOj\nsXokSTwVg+1QugFKt7PcMexAwP8RvUXFc5wB6kQbRE6yluvs72BUu08nckF29UXx\nQt55s8BlYmz0ObHmbcNaJS+PnmnxdW39wiCEWWHOUs1JlC87xjheJEOLwVR/qrc+\nS5c9ofTFMvDzIaBWQXPw8KagZGiNaRaaw3NZ6XAick5wNYVQjFekCZpG3IUNsJKv\nVZjAIdLvzKSVoNO2dmaK+U0Xm617cYwg5ztt0iUbqfVELDNLT7rF/J1gC625ezJs\nbcB4Gv/jeKjwdkEFYhaZM4Oe4qDhKY4FHikQ9kFxKKKVvdgISB3Y00ejS/DiangE\nlb8hGfEfAgMBAAECggEAIKTWp+DEHV1tCRw/qHcwHp0vSGhlggpEazpDIjU3fAGN\niXP+HVOeftBCxhAl0ghWNrkIINH9zTWwZENc8ODuNWT4r3RiX42xtp5Evzm3xIAA\n84YPD8z4M/Vu9SaYopqYH10SlJsPobpYmXj0vuHp5EZia7o+KM7x6hbN5IpnBVyF\n97d+J7zHCDYiRidmPRQp6JGK4bTQuGKgFnazM9Hh3bHqFM1fyBLr5IttbhyvfNlF\n+AH1t51jv0E06uWbOajJMhImKIlVsyYHPVHpMnGUmW5P1/3yUS93+qczwMB6snne\n9T02Z5r+PPaT56u0/wz4j83HznhA/GrfLCoQiU4e0QKBgQD+fen/dmb8pA7tuXYX\n+E6LojxQbvynMVkAbOZQ8DqQHW4ZbbE3pzxz4s3YUJaDk8JxEsE57UbdpqyPpR+Y\niDxt65qhnvtYdDOykVn5WSQwEBNavgeHHSf4jcqQEyC1UmqkwnInYV7wQ8zZwQ24\nK4dzJ0MF+DjJXgxekrRZ7IQIyQKBgQDPG7RtR8hZ5X0cdo10R8x+Nf74NznaoNxN\nX4Lf+vEMrkHfOTHxHnWLfdYERd8ou+LF+lFS79mdbFfuvyNRCt3RR2RE2+fZYqcn\nea9FnyeEfIdlWRe59AI2bpF3/nXUuHESuKcjJaPvWI0cROrww02+//L19Bi2Bhuj\nwSGB5eeGpwKBgQCrgyCY0qtFyStme39jWC1XXddYPfR4mYFqD/qIwd42Eh+Jc6vj\n3gmX8FraVjWaJ5L7sbAX4hnId/QEOzy4B9jyG77y/bpXOrk8t0j0C2egHLVuinN4\nU+YEVUsXHk0E5q6Iq6NTdwQM2STN/JXKcUuwB93bwBZFX+TmN+jkUcoKQQKBgDyd\ngjAdu0C8TuK+u+XVgb9KtGYXW8JmJDQtCRPe0SAB/FuF1N0aKhL6cGHtxUOZweRp\nv9WDR3CwngfNP1vfz04KFAmnRvMz0XJXRfode6ZmAAakjbIp/V/K+p5hBkGM/eMZ\n0ikSQimyBBLLBOwUbTPCm2xq1bSokvxZcSIglKOvAoGBAOvxhNX5dcO/8soeFyZy\n2uk8bsx5Hsj06RjZ2RX+T9X23YWFLLSf092oWimkt+N9BuFdYZh1xnxXZm1X1GSQ\nl+sLK4zK5s5Xlr4oOaujyLnois5gohqsS2FVxVssGXRX4cT/V19jl1sOM/IfCH4t\nxBrySQTaUXcN3DhEf3ZrOu46\n-----END PRIVATE KEY-----\n"")
# raw_doc = ufirestore.get("/")
# doc = FirebaseJson.from_raw(raw_doc)
# print(doc)
