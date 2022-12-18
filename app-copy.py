# pipenv install flask
# pipenv install flask_sqlalchemy
# pipenv install requests
# pipenv shell
# export FLASK_APP=app.py (allows us to use 'flask run')

import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)



@app.route('/')
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


if __name__ == "__main__":
    db.create_all() # create DB if DNE
    app.run(debug=True)