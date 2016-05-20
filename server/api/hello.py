from flask import Blueprint, request, render_template
from flask import current_app
import requests
from server.utils import *
from flask.ext import restful


from flask import Flask

from flask.views import MethodView
# from server import apiw

# app = Flask(__name__)
# apis = Blueprint(__name__, __name__)

# app = current_app._get_current_object()
# api = restful.Api(app)
# print api

# class HelloWorld(restful.Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# # @apis.route("/hello")
# api.add_resource(HelloWorld, '/HelloWorld')


#
# class UserAPI(MethodView):
#
#     def get(self):
#         users = "teacher"
#
#
#     def post(self):
#         user ="teacher"
#
#
# app.add_url_rule('/Professor/', view_func=UserAPI.as_view('users'))
#
# @apis.route("/Professor/<id>")
# def help():
#     return "help"

# @api.route("/hello")
# def hello():
#     return "hello"
