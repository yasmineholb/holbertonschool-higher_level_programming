#!/usr/bin/python3
"""
this is an square module
it prints squares

"""


def print_square(size):
    """
this is the square function
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
            print("#" * size)
