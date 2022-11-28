#!usr/bin/python3
import models
from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """user class"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)        
a = User()
print(a.email)