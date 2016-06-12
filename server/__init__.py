#! /usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, session, redirect
from flask_mongoengine import MongoEngine
import datetime
import re
from views import pages, api, calender
from server import filters
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

app = Flask(__name__)

BLUEPRINTS = [
    (pages, ""),
    (calender, "/calender"),
    (api, "/api/v1"),
]

for blueprint, url_prefix in BLUEPRINTS:
    app.register_blueprint(blueprint, url_prefix=url_prefix)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404

#jinja config
# app.jinja_env.globals.update(
#     format_time = models.Utils.format_time, 
#     format_time_full = models.Utils.format_time_full,
#     summarize = models.Utils.summarize,
#     is_mobile = models.Utils.is_mobile,
#     is_login = models.Utils.is_login,
#     is_person = models.Utils.is_person,
#     is_company = models.Utils.is_company,
#     is_rpo_status = models.Utils.is_rpo_status,
#     format_date = models.Utils.format_date,
#     print_age = models.Utils.print_age,
#     url_encrypt = models.Utils.url_encrypt
# )

app.jinja_env.filters["format_time"] = filters.format_time
app.jinja_env.filters["content_chopper"] = filters.content_chopper
# app.jinja_env.filters["in_recent_24_hours"] = models.Utils.in_recent_24_hours

# db.init_app(app)

# @app.errorhandler(InvalidId)
# def handle_invalid_id(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response