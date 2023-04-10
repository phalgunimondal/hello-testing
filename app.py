from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/weather')
def conv_weather_apt():
    url="https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=767ab06d4aae399b47d43e6ef88df834"
    return url
