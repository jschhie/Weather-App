from flask import Blueprint, render_template, request
from . import db
from .models import City

views = Blueprint('views', __name__)

@views.route('/')
def index():
    
    cities = City.query.all() # query all cities in table

    # q={} query is city name 
    # units=imperial so we can see farenheit
    # appid given by open weather map
    # https://openweathermap.org/current#name 
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7397308c3b593fbf9e831fb14044c1a1'

    weather_data = [] # list to hold all weather data per city

    for city in cities:
        # send request to api where r = response
        r = requests.get(url.format(city)).json()

        # create dictionary with city details
        weather = {
            'city' : city, 
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)
