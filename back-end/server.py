import os

from flask import Flask

from app import create_app, db_init, db

app = Flask(__name__)
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    db_init('./sqlite.db')
    return dict(db=db)
