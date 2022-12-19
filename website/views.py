import requests
from flask import Blueprint, render_template, request, \
    redirect, url_for, flash
from . import db
from .models import City

views = Blueprint('views', __name__)

@views.route('/') # GET method by default
def home_get():
    cities = City.query.all() # query all cities in table
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7397308c3b593fbf9e831fb14044c1a1'
    weather_data = [] # list to hold all weather data per city

    for city in cities:
        # send request to api where r = response
        r = requests.get(url.format(city.name)).json()
        if r['cod'] == 200:
            # create dictionary with city details
            weather = {
                'city' : city.name, 
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'temp_min': r['main']['temp_min'],
                'temp_max': r['main']['temp_max'],
            }            
            weather_data.append(weather)
            flash('{} added!'.format(weather['city']), 'success')
        else:
            # 404 or other status error
            flash('{} does not exist. \
                Please try a different city.'.format(city.name), 'error')

    return render_template('weather.html', weather_data=weather_data)



@views.route('/', methods=['POST'])
def home_post():
    cities = City.query.all() # query all cities in table
    # get city name from search bar
    if request.form['action'] == 'search':
        new_city = request.form['query']

        for city_obj in cities:
            if city_obj.name == new_city:
                flash('Error: Duplicate city name!', 'error')
                return redirect(url_for('views.home_get'))

        # add unique city to database
        new_city_obj = City(name=new_city)
        db.session.add(new_city_obj)
        db.session.commit()

    return redirect(url_for('views.home_get'))
