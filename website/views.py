import requests
from flask import Blueprint, render_template, request
from . import db
from .models import City

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        # get city name
        new_city = request.form.get('city')
        
        if new_city:
            # add to database   
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all() # query all cities in table

    # q={} query is city name 
    # units=imperial so we can see farenheit
    # appid given by open weather map
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7397308c3b593fbf9e831fb14044c1a1'
    weather_data = [] # list to hold all weather data per city

    for city in cities:

        print(city.name)

        # send request to api where r = response
        r = requests.get(url.format(city.name)).json()
    
        # create dictionary 'weather' with city details
        weather = {
            'city' : city.name, 
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)
