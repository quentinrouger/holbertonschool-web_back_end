#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """Hash password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a UUID
    """
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """Create session
        """
        user = self._db.find_user_by(email=email)
        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Get user from session ID
        """
        user = self._db.find_user_by(session_id=session_id)
        if user:
            return user
        return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy session
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Get reset password token
        """
        user = self._db.find_user_by(email=email)
        if user:
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password
        """
        user = self._db.find_user_by(reset_token=reset_token)
        if user:
            self._db.update_user(user.id, _hash_password(password),
                                 reset_token=None)
            return None
        raise ValueError
