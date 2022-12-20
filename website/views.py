import requests
from flask import Blueprint, render_template, request, \
    redirect, url_for, flash
from . import db
from .models import City

views = Blueprint('views', __name__)

# Function (not route) 
# Makes a request to api and get its response in json format
def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={ city }&units=imperial&appid=7397308c3b593fbf9e831fb14044c1a1'
    r = requests.get(url).json()
    return r # return response as json



@views.route('/') # GET by default
def home_get():
    cities = City.query.all() # query all cities in table
    weather_data = [] # list to hold all weather data per city

    for city in cities:
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
        }            
        weather_data.append(weather)
    return render_template('home.html', weather_data=weather_data)



@views.route('/', methods=['POST'])
def home_post():
    err_msg = ''
    if request.form['action'] == 'search':
        new_city = request.form['query']
        existing_city = City.query.filter_by(name=new_city).first()
        if not existing_city:
            new_city_data = get_weather_data(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)
                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = 'City does not exist in the world!'
        else:
            err_msg = 'City already exists in the database!'
    
    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('Successfully added new city!', 'success')
    return redirect(url_for('views.home_get'))



@views.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()
    flash('Successfully deleted {}'.format(city.name), 'success')
    return redirect(url_for('views.home_get'))