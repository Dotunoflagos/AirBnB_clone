#!usr/bin/python3
"""User class"""
import models
from models.base_model import BaseModel


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