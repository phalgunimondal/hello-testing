from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/weather')
def conv_weather_apt():
    url="http://api.openweathermap.org/data/2.5/air_pollution/history?lat=508&lon=50&start=1606223802&end=1606482999&appid=84511fdebb693f2a434a8e4094e3dc5e"
    return url
