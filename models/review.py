#!usr/bin/python3
"""
Place module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Place class
    """
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """Initialise Place"""
        super().__init__(self, *args, **kwargs)