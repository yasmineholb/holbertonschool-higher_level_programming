#!/usr/bin/python3
"""


"""


class Base:
    """ this is the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            self.id = Base.__nb_objects
            Base.__nb_objects += 1

    def to_json_string(list_dictionaries):
        m = "[]"
        if list_dictionaries is None:
            return m
