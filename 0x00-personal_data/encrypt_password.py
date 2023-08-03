#!/usr/bin/env python3
"""
Defines a hash_password function
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str -> bytes:
    """Returns a hashed password
    Args:
        password (str): password to be hashed"""
    b = password.encode()
    hashed = hashpw(b, bcrrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str)-> bool:
    """
    Check if a password is valid
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string
    Return:
        bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
