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
        """W9rites the JSON string representation of list_objs to a file
        """
        with open("{}.json".format(cls.__name__), "w") as newfile:
            if list_objs:
                newdict = [obj.to_dictionary() for obj in list_objs]
                newfile.write(Base.to_json_string(newdict))
            else:
                newfile.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `json_string`
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__), "r") as readfile:
                read_data = readfile.read()
                dictnlist = cls.from_json_string(read_data)
                return [cls.create(**dictn) for dictn in dictnlist]
        except IOError:
            return []
