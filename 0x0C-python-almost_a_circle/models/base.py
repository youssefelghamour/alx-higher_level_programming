#!/usr/bin/python3
""" Module for Base class """
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        lst = []
        if list_objs is not None:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates a new instance """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)  # Rectangle(1,1)
        elif cls.__name__ == "Square":
            new = cls(1)  # Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new
