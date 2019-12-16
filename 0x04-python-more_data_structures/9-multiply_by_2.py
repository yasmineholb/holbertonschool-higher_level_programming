#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ch = dict()
    for i, j in a_dictionary.items():
        ch[i] = j * 2
    return(ch)
