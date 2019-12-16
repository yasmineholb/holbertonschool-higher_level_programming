#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if i == key:
            del a_dictionary[i]
            for j in a_dictionary:
                print("{}: {}".format(j, a_dictionary[j]))

