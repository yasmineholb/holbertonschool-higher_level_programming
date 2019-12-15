#!/usr/bin/python3
def no_c(my_string):
    ss = ""
    for i in my_string:
        if i != "c" and i != "C":
            ss += i
    return (ss)
