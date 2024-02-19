#!/usr/bin/env python3
""" Module to manage the API authentication
"""
from api.v1.auth.auth import Auth


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
