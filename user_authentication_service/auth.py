#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")
        return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login
        """
        user = self._db.find_user_by(email=email)
        if user and bcrypt.checkpw(password.encode(), user.hashed_password):
            return True
        return False
