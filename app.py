#! /usr/bin/env python
#-*- coding: utf-8 -*-

from server import app

if __name__ == '__main__':
    app.run('0.0.0.0', 23300, debug=True)
