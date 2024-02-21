#!/usr/bin/env python3
""" Session authentication view for handling login requests.
"""
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """ Handles session authentication login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({'email': email})

    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    session_name = os.getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)

    return response
