from flask import Blueprint, request, render_template
from flask import current_app as app
import requests
from server.utils import *

calendar = Blueprint(__name__, __name__)

@calendar.route("/")
def index():
    return render_template("index.html")

@calendar.route("/result")
def result():
    return render_template("result.html")
