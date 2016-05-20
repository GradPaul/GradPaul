#! /usr/bin/env python

from server import *

if __name__ == '__main__':
    app=create_app()
    app.run('0.0.0.0', 23300)
