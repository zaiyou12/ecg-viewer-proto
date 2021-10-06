from flask import jsonify

from . import main
from .. import db
from .query import get_ecg_tests

@main.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@main.route('/ecg-tests')
def fetch_all_tests():
    cur = db.cursor()
    cur.execute(get_ecg_tests())
    data = [dict(row) for row in cur.fetchall()]
    return jsonify({'ecgTests': data})
