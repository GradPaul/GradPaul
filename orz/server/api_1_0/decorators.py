from functools import wraps
from flask import g,jsonify
from ..utils import *


def permission_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user:
                return jsonify(Unconfirmed_code)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
