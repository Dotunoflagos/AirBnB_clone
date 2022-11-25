#!/usr/bin/python3
import uuid
from datetime import datetime
"""
This is the base moedl for all classes
"""


class BaseModel:
    """
    This is the base moedl for all classes
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                self.__dict__[key] = value
        else:
            self.my_number = None
            self.name = None
            dateString = datetime.now()
            self.created_at = dateString
            self.id = str(uuid.uuid4())
            self.updated_at = dateString

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        keyValue = self.__dict__
        keyValue['__class__'] = self.__class__.__name__
        keyValue['created_at'] = keyValue['created_at']\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        keyValue['updated_at'] = keyValue['updated_at']\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        return keyValue

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
