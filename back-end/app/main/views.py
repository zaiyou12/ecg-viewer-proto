from . import main

@main.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
