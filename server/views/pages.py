#! /usr/bin/env python
#-*- coding: utf-8 -*-

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
    # offset = int(request.args.get("offset", 0))
    # limit = int(request.args.get("limit", 10))
    # comments = list(db.comments.find().skip(offset).limit(limit))
    comments=[{
        "name": "钟典",
        "text": "谢谢大家支持，转载随意：）——————————————————————————————看完首映，离开电影院，在路边发了一会呆。这是一场告别，其实我们都知道。影片结束时，没有掌声，所有人都默默的在等字幕结束，希望有彩蛋，希望还有。直到电影放…",
        "course": {
            "name": "智能数据挖掘大数据推荐引擎构建",
            "department": "统计学院",
        },
        "teacher": {
            "name": "陈心远",
            "department": "信息学院",
        },
        "createdTime": datetime.datetime.now() - datetime.timedelta(minutes=5)
    },{
        "name": "钟典典",
        "text": "谢谢大家支持，转载随意：）——————————————————————————————看完首映，离开电影院，在路边发了一会呆。这是一场告别，其实我们都知道。影片结束时，没有掌声，所有人都默默的在等字幕结束，希望有彩蛋，希望还有。直到电影放…",
        "course": {
            "name": "智能数据挖掘大数据推荐引擎构建",
            "department": "统计学院",
        },
        "teacher": {
            "name": "陈心远",
            "department": "信息学院",
        },
        "createdTime": datetime.datetime.now() - datetime.timedelta(minutes=5)
    },{
        "name": "钟典典典",
        "text": "谢谢大家支持，转载随意：）——————————————————————————————看完首映，离开电影院，在路边发了一会呆。这是一场告别，其实我们都知道。影片结束时，没有掌声，所有人都默默的在等字幕结束，希望有彩蛋，希望还有。直到电影放…",
        "course": {
            "name": "智能数据挖掘大数据推荐引擎构建",
            "department": "统计学院",
        },
        "teacher": {
            "name": "陈心远",
            "department": "信息学院",
        },
        "createdTime": datetime.datetime.now() - datetime.timedelta(minutes=5)
    }]
    return render_template("index.html", **locals())
@pages.route("/login")
def login():
    return render_template("login.html")

@pages.route("/register")
def register():
    return render_template("register.html")
