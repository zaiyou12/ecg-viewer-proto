import os

from flask import Flask

basedir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)
db = None

def get_db():
    import sqlite3
    global db
    db = sqlite3.connect('./sqlite.db')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.shell_context_processor
def make_shell_context():
    get_db()
    return dict(db=db)
