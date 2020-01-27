#!/usr/bin/python3
"""
import the json and os
"""


import json
import os


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
            Args:
                cls: belonging class
                list_objs: list of instances who inherits of Base
        """
        filename = '{}.json'.format(cls.__name__)
        dic = []

        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))

        with open(filename, 'w', encoding='utf-8') as new_file:
            new_file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
            Args:
                cls: belonging class
                **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(36916, 36916)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(36916)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
            Args:
                cls: belonging class
        """
        filename = '{}.json'.format(cls.__name__)
        list_ins = []

        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as new_file:
                content = cls.from_json_string(new_file.read())
            for i in content:
                list_ins.append(cls.create(**i))
            return list_ins
        else:
            return []
