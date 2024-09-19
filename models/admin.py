#!/usr/bin/python3
""" Admin Module for Terra origin
"""

from sqlalchemy import Column, String


class Admin:
    """ Admin class
    """
    __tablename__ = 'admin'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    ph_no = Column(String(45), nulable=False)