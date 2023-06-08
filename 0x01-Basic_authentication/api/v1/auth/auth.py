#!/usr/bin/env python3

"""a template fot the user class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth template"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if a user is authenticated"""

        if path is None or excluded_paths is None:
            return True

        for i in excluded_paths:
            if path.startswith(i[:-1]) and i.endswith('*'):
                return False

            elif i in {path, path + '/'}:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization hearder function"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""

        return None
