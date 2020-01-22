#!/usr/bin/python3
"""


"""


def write_file(filename="", text=""):
    """ number of lines fn """
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
