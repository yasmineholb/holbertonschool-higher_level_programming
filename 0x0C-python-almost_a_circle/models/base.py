#!/usr/bin/python3
"""
"""


class Base:
    """ this is the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        m = "[]"
        if list_dictionaries is None:
            return m
