#!/usr/bin/env python3

"""Creating a template for the user class which is mapped to the
   user table by the declarative base using SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """Template for the user table"""

    ___tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(256), nullable=False)
    hashed_password = Column(String(256), nullable=False)
    session_id = Column(String(256))
    reset_token = Column(String(256))
