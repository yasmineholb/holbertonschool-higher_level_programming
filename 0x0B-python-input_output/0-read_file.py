#!/usr/bin/python3
"""


"""


def read_file(filename=""):
    """ read file fn """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
