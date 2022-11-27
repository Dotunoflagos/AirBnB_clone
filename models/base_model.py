#!/usr/bin/python3
import uuid
from datetime import datetime
import models
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
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            dateString = datetime.now()
            self.created_at = dateString
            self.updated_at = dateString
            models.storage.new(self)

    """def __setattr__(self, key, value):
        self.__dict__[key] = value
        models.storage.new(self)"""

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    """def delete(self):
        models.storage.delete(self)"""

    def to_dict(self):
        keyValue = self.__dict__.copy()
        keyValue['__class__'] = self.__class__.__name__
        keyValue['created_at'] = keyValue['created_at']\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        keyValue['updated_at'] = keyValue['updated_at']\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        return keyValue

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
