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
    my_json_string = json.dumps({'Lat': latitude, 'Long': longitude,'Temp':temp, 'Pres':pressure,'Hum':humidity,'Wind':wind_speed})
    #print("Latitude:%s,Longitude:%s,Temp:%s,Pressure:%s,humidity:%s,Wind_speed:%s"%(latitude,longitude,temp,pressure,humidity,wind_speed))
    #print(my_json_string)
    return my_json_string

@app.route('/airpollution')
def air_pollution():
    x = requests.get('https://api.openweathermap.org/data/2.5/air_pollution?lat=23.682359&lon=87.613932&appid=767ab06d4aae399b47d43e6ef88df834')
    #print(x.status_code)
    data = x.json()
    #print(data)
    
    PM2_5 = str(round(data['list'][0]['components']['pm2_5'],2)) + 'ug/m3'
    PM10 = str(round(data['list'][0]['components']['pm10'],1)) + 'ug/m3'
    SO2 = str(round(data['list'][0]['components']['so2'],1)) + 'ug/m3'
    NO2 = str(round(data['list'][0]['components']['no2'],1)) + 'ug/m3'
    CO = str(round(data['list'][0]['components']['co'],1)) + 'ug/m3'
    O3 = str(round(data['list'][0]['components']['o3'],1)) + 'ug/m3'
    AQI = str(data['list'][0]['main']['aqi'])
    my_json_string = json.dumps({'PM2.5': PM2_5 , 'PM10': PM10,'SO2':SO2, 'NO2':NO2,'CO':CO,'O3':O3,'AQI':AQI})
    #print("Latitude:%s,Longitude:%s,Temp:%s,Pressure:%s,humidity:%s,Wind_speed:%s"%(latitude,longitude,temp,pressure,humidity,wind_speed))
   
    return my_json_string
