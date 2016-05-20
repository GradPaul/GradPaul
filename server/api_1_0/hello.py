from flask import Blueprint, request, render_template

import requests
from flask import jsonify, request, g, abort, url_for, current_app
from flask.ext import restful
from flask_restful import Api, Resource, url_for
from . import api as api_bp
from flask import Flask

from flask.views import MethodView

api = Api(api_bp)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
