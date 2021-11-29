from flask import Flask
from flask_cors import CORS

from config import config

db = None

def db_init(db_uri:str):
    import sqlite3
    global db
    print(db_uri)
    db = sqlite3.connect(db_uri, check_same_thread=False)
    db.row_factory = sqlite3.Row

def create_app(config_name:str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db_init(app.config['DATABASE_URL'])

    CORS(app)

    @app.route('/')
    def hello_world():
        return "<p>Hello, Cold Brew!</p>"

    from .ecgtest import ecgtest as ecgtest_blueprint
    from .group import group as group_blueprint
    app.register_blueprint(ecgtest_blueprint)
    app.register_blueprint(group_blueprint)

    return app
