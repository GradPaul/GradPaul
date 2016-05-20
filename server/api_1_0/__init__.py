

from flask import current_app
from flask import Blueprint

api = Blueprint('api', __name__)
from . import hello

# print type(current_app)
