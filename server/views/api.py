#! /usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Blueprint, request, render_template, jsonify, Response
from flask import current_app as app
import requests
from server.models import db
from server.utils import *
import sys
import json
from bson import ObjectId

api = Blueprint('api', __name__)

@api.route("/signup", methods=["POST"])
@format_output
def signup():
    obj_id = ObjectId()
    user = {
        "_id": obj_id,
        "username": request.json.get("username"),
        "password": encrypt_password(request.json.get("password"), obj_id),
    }
    print user
    old = db.users.find_one({"username": user.get("username")})
    print old
    if old:
        return "用户名已被占用"
    else:
        return db.users.find_one({"_id": ObjectId(db.users.insert(user))})

@api.route("/login", methods=["POST"])
@format_output
def login():
    user = db.users.find_one({"username": request.json.get("username")})
    if not user:
        return "用户不存在"
    if user.get('password') == encrypt_password(request.json.get("password"), user.get("_id")):
        sessioin['me'] = user
        return user
    else:
        return "用户名和密码不匹配"

@api.route("/<string:resource>", methods=["GET", "POST"])
@format_output
def handle_resource(resource):
    if request.method == "GET":
        offset = int(request.args.get("offset", 0))
        limit = int(request.args.get("limit", 10))
        return bson_to_json(list(db[resource].find().skip(offset).limit(limit)))
    else:
        return db[resource].find_one({"_id": ObjectId(db[resource].insert(request.json))})

@api.route("/<string:resource>/<string:document_id>", methods=["GET", "PATCH", "DELETE"])
@format_output
def handle_document(resource, document_id):
    if request.method == "GET":
        return db[resource].find_one({"_id": ObjectId(document_id)})
    elif request.method == "PATCH":
        return db[resource].update({"_id": ObjectId(document_id)}, request.json)
    else:
        return db[resource].remove({"_id": ObjectId(document_id)})
