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

    def to_json(self):
        """ to json fn """
        return self.__dict__
