from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME ="weather.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fb66099b595b09d56b7082aab997b1ee' # to enable sessions and flashed messages
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # register blueprints into app
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # create or retrieve existing DB
    from .models import City

    #create_database(app)
    with app.app_context():
        db.create_all()

    return app
