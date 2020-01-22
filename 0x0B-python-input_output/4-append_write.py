#!/usr/bin/python3
"""


"""


def append_write(filename="", text=""):
    """ number of lines fn """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
