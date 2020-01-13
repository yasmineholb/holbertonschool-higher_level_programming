#!/usr/bin/python3
"""
this is an add module
it add integers

"""
def add_integer(a, b=98):
    """
this is the add function
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return(a+b)
