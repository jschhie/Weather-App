# pipenv install flask
# pipenv install flask_sqlalchemy
# pipenv install requests
# pipenv shell
# export FLASK_APP=app.py (allows us to use 'flask run')

# requirements.txt will have the pipfile packages needed

# git init
# git remote add origin https://github.com/jschhie/weather-app.git
# git add .
# git commit -m 'init base code'
# git push origin master [pushes to git repo online]

import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/') # index
def index():
    # q={} query is city name 
    # units=imperial so we can see farenheit
    # appid given by open weather map
    # https://openweathermap.org/current#name 
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7397308c3b593fbf9e831fb14044c1a1'
    city = 'Las Vegas'

    # send request to api where r = response
    # get weather from api
    r = requests.get(url.format(city)).json()

    # create dictionary with needed details
    weather = {
        'city' : city, 
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    print(weather)
    
    """
    {'city': 'Las Vegas', 
    'temperature': 39.31, 
    'description': 'scattered clouds', 
    'icon': '03n'}
    """

    return render_template('weather.html', weather=weather)
