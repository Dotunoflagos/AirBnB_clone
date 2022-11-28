#!usr/bin/python3
"""
Amenities module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    state class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialise Amenity"""
        super().__init__(self, *args, **kwargs)
