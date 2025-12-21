import requests
from flask import Blueprint, render_template, request, \
    redirect, url_for, flash
from . import db
from .models import City

from os import path, environ
from dotenv import load_dotenv

views = Blueprint('views', __name__)

# Function (not route) 
# Makes API request
def get_weather_data(city):
    # Get absolute path of current file (for server and local dev)
    current_dir = path.abspath(path.dirname(__file__))

    project_root = path.dirname(current_dir)
    env_path = path.join(project_root, '.env')

    load_dotenv(env_path)
    api_key = environ.get('WEATHER_API_KEY', 'api-key-error')
    print(api_key)

    if (api_key != 'api-key-error'):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'
        r = requests.get(url).json()
        return r # Return JSON response
    return {} # Return empty dict



@views.route('/') # GET by default
def home_get():
    cities = City.query.all() # query all cities in table
    weather_data = [] # list to hold all weather data per city

    for city in cities:
        try:
            # send request to api, where r = response
            r = get_weather_data(city.name)
            # create dictionary with city details
            weather = {
                'city' : city.name, 
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'temp_min': r['main']['temp_min'],
                'temp_max': r['main']['temp_max'],
                'country': r['sys']['country']
            }
            weather_data.append(weather)
        except:
            pass
            
    return render_template('home.html', weather_data=weather_data)



@views.route('/', methods=['POST'])
def home_post():
    err_msg = ''
    if request.form['action'] == 'search':
        new_city = request.form['query'].title()
        existing_city = City.query.filter_by(name=new_city).first()
        if not existing_city:
            new_city_data = get_weather_data(new_city)            
            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)
                db.session.add(new_city_obj)
                db.session.commit()
                flash('Added {}'.format(new_city_obj.name), 'success')
            else:
                err_msg = 'Whoops! Location does not exist in the world!'
        else:
            err_msg = 'Whoops! Location already saved!'
    
    if err_msg:
        flash(err_msg, 'error')

    return redirect(url_for('views.home_get'))



@views.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()
    flash('Removed {} from saved locations'.format(city.name), 'success')
    return redirect(url_for('views.home_get'))