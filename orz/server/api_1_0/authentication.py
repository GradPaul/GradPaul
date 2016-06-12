from flask import g, jsonify
from flask.ext.httpauth import HTTPBasicAuth
from ..models import User
from . import api
from ..utils import *

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token,password):
    if not token :
        return None
    g.current_user = User.verify_auth_token(token)
    return g.current_user is not None

# @api.before_request
# @auth.login_required
# def before_request():
#     if not g.current_user:
#         return jsonify(Unconfirmed_code)
