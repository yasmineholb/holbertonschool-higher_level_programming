#!/usr/bin/python3
"""


"""


def number_of_lines(filename=""):
    """ number of lines fn """
    with open(filename, mode="r", encoding="utf-8") as f:
        return len(f.readlines())
