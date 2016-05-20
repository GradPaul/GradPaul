from flask import Flask, render_template, request, jsonify, session, redirect
import datetime
import re
from views import pages
from api_1_0 import api



def create_app():
    app = Flask(__name__)
    app.debug = app.config["DEBUG"]
    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix='/api/v1.0')
    return app
