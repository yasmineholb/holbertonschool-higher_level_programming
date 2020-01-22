#!/usr/bin/python3
"""
student class

"""


class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        """ init fn """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json fn """
        if type(attrs) is list:
            lib = {}
            for i in attrs:
                if i in self.__dict__:
                    lib[i] = self.__dict__[i]
            return lib
        return self.__dict__

    def reload_from_json(self, json):
        """ reload fn """
        for i, j in json.items():
            self.__dict__[i] = j
