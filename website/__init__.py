from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import path, environ
from dotenv import load_dotenv

db = SQLAlchemy()
DB_NAME ="weather.db"



def create_app():
    app = Flask(__name__)

    # Get absolute path of current file (for server and local dev)
    current_dir = path.abspath(path.dirname(__file__))

    project_root = path.dirname(current_dir)
    env_path = path.join(project_root, '.env')

    load_dotenv(env_path)

    # Fetch secret key from .env var (Default: placeholder string if DNE)
    # (To enable sessions and flashed messages)
    app.config['SECRET_KEY'] = environ.get('FLASK_SECRET_KEY', 'local-dev-only-secret-key')
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
