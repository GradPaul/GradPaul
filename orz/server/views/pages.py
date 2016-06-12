<<<<<<< HEAD
from flask import Blueprint, request, render_template
from flask import current_app as app
# import requests
from server.utils import *

pages = Blueprint(__name__, __name__)

@pages.route("/")
def index():
    return render_template("index.html")

@pages.route("/result")
def result():
    return render_template("result.html")

@pages.route("/Professor")
def Professor():
    return render_template("/Professor/index.html")
=======
from flask import Blueprint, request, render_template
from flask import current_app as app
# import requests
from server.utils import *

pages = Blueprint(__name__, __name__)

@pages.route("/")
def index():
    return render_template("index.html")

@pages.route("/login")
def login():
    return render_template("login.html")

@pages.route("/register")
def register():
    return render_template("register.html")

@pages.route("/result")
def result():
    return render_template("result.html")

@pages.route("/Professor")
def Professor():
    return render_template("/Professor/index.html")

@pages.route("/Professor/comment")
def comment():
    return render_template("/Professor/comment.html")
>>>>>>> 790c97ba486e2e063df55c5169d585793ccefb21
