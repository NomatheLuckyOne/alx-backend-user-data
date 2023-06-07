#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

"""
A template for all authentification you will implement
"""


class Auth:
    """
    Auth template
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Lists str
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Authorization hearder function
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None
