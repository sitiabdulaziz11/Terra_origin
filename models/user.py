#!/usr/bin/python3
""" users Module
"""

from sqlalchemy import Column, String, ForeignKey

from models.base_model import BaseModel, Base


class Users(BaseModel, Base):
    """ Users class
    """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    ph_no = Column(String(45), nulable=False)
    
    admin_id = Column(String(60), ForeignKey('admin.id'), nullable=False)
    