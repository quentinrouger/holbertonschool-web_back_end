#!/usr/bin/env python3
""" Module to manage the API authentication
"""
from flask import jsonify, request, make_response
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

    user = User.search({'email': email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)

    session_name = os.getenv('SESSION_NAME', '_my_session_id')
    response = make_response(jsonify(user[0].to_json()))
    response.set_cookie(session_name, session_id)

    return response
