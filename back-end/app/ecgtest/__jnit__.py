from flask import Blueprint

ecgtest = Blueprint('ecgtest', __name__)

from . import views