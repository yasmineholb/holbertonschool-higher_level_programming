#!/usr/bin/python3
"""
the class

"""


class BaseGeometry:
    """ base geo """

    def area(self):
        """ area fn """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validater fn """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
