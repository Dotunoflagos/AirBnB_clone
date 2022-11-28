#!usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    state class
    """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """Initialise state"""
        super().__init__(self, *args, **kwargs)