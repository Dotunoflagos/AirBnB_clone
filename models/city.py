#!usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    state class
    """
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """Initialise state"""
        super().__init__(self, *args, **kwargs)