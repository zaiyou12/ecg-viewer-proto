import os
from flask import Flask

from config import config

db = None

def db_init(db_uri:str):
    import sqlite3
    global db
    db = sqlite3.connect(db_uri)

def create_app(config_name:str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db_init(app.config['DATABASE_URI'])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
