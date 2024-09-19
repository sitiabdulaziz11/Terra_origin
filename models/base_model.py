#!/usr/bin/python3
""" Base Module that defines a base class for all models in Terra origin.
"""

import uuid
from datatime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """ Base class
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        """
        
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())
            
            for key, value in kwargs.items():
                if key in ['updated_at', 'created_at', 'id', '__class__']:
                    continue
                setattr(self, key, value)
                