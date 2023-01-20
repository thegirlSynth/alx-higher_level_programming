#!/usr/bin/python3
"""This module contains a class ``Base``"""
import json


class Base:
    """This class is the base class for the module"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        """
        with open("{}.json".format(cls.__name__), "w") as newfile:
            if list_objs:
                newdict = [obj.to_dictionary() for obj in list_objs]
                newfile.write(Base.to_json_string(newdict))
            else:
                newfile.write("[]")
