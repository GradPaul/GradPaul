from flask import Blueprint, request, render_template
from flask import current_app as app
import requests
from server.utils import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

calender = Blueprint('calender', __name__)

@calender.route("/")
def index():
    return render_template("calender/index.html")

@calender.route("/result")
def result():
    return render_template("calender/result.html")
