from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/weather')
def conv_weather_apt():
    x = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Kolkata,in&APPID=767ab06d4aae399b47d43e6ef88df834')
    #print(x.status_code)
    data = x.json()
    #print(data)
    # of the first matching location
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    my_json_string = json.dumps({'Latitude': latitude, 'Longitude': longitude,'Temp':temp, 'Pressure':pressure,'humidity':humidity,'Wind_speed':wind_speed})
    #print("Latitude:%s,Longitude:%s,Temp:%s,Pressure:%s,humidity:%s,Wind_speed:%s"%(latitude,longitude,temp,pressure,humidity,wind_speed))
    #print(my_json_string)
    return my_json_string
