#! /usr/bin/env python
#-*- coding: utf-8 -*-
import re, datetime
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def content_chopper(s, offset, limit):
    return re.sub(r'<.*?>|&.*?;', '', unicode(s))[offset:offset+limit]


def completeProtocal(url):
    if url[:4] == "http":
        return url
    else:
        return "http://" + url

def format_time(t):
    now = datetime.datetime.now()
    print now, t
    seconds = (now-t).seconds
    print seconds
    if seconds < 60:
        return "%i 秒之前" % seconds
    elif seconds < 3600:
        return "%i 分钟之前" % int(seconds/60)
    elif seconds < 86400:
        return "%i 小时之前" % int(seconds/3600)
    elif seconds < 259200:
        return "%i 天之前" % int(seconds/86400)
    else:
        return t.strftime("%Y-%m-%d")