import urequests as requests
import ujson as json

city = 'Haifa'
lat = '32.794044'
lon = '34.989571'
api_key = 'd4313f080224daba7c392fc9bbfed282'

map_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + api_key

temp = requests.get(map_url).json().get('main').get('temp')

print(temp-273)