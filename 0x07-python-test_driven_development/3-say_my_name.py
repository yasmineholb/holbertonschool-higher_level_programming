#!/usr/bin/python3
"""
this is a name function
it prints the name

"""


def say_my_name(first_name, last_name=""):
    """
this is the name function
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
