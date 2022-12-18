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
    return render_template('weather.html')
