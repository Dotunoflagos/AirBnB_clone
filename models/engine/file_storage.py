#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""Fils storage module"""

classes = {"BaseModel":BaseModel}
class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        if self.__objects is not None and len(self.__objects) != 0:
            newdic = {}
            for key, value in self.__objects.items():
                newdic[key] = value
            return newdic
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    """def delete(self, obj):
        if obj is not None:
            dkey = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(dkey)
            json_objects = {}
            for key in self.__objects:
                json_objects[key] = self.__objects[key].to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(json_objects, f)
            print (f"Object {obj.id} gets destroyed")
            del obj"""

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                str = json.load(f)
            for key in str:
                self.__objects[key] = classes[str[key]["__class__"]](**str[key])
        except:
            pass