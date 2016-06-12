from flask import Blueprint, request, render_template
from flask import current_app as app
import requests
from server.models import db
from server.utils import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

pages = Blueprint('pages', __name__)

@pages.route("/")
def index():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))
    comments = list(db.comments.find().skip(offset).limit(limit))
    return render_template("index.html", **locals())

@pages.route("/result")
def result():
    return render_template("result.html")

@pages.route("/Professor")
def Professor():
    return render_template("/Professor/index.html")
