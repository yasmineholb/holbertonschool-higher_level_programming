#!/usr/bin/python3
"""


"""


def read_lines(filename="", nb_lines=0):
    """ read file fn """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            for i in f:
                print(i, end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
