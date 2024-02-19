#!/usr/bin/env python3
""" Module to manage the API authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """ Class to manage the API authentication
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Extract base64 authorization header
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None

        base64_credentials = authorization_header.split(" ")[1]
        return base64_credentials

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Decode base64 authorization header
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Extract user credentials
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str or \
                ":" not in decoded_base64_authorization_header:
            return (None, None)

        user_credentials = decoded_base64_authorization_header.split(":")
        return (user_credentials[0], user_credentials[1])

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ Return the User instance based on email and password
        """
        if user_email is None or type(user_email) is not str or \
                user_pwd is None or type(user_pwd) is not str:
            return None

        user_list = []
        try:
            user_list = User.search({"email": user_email})
            if user_list == []:
                return None
        except Exception:
            return None

        user = user_list[0]
        if user.is_valid_password(user_pwd):
            return user

        return None

