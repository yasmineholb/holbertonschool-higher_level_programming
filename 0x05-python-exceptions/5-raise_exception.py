#!/usr/bin/python3
def raise_exception():
    try:
        raise AttributeError
    except AttributeError:
        print("Exception raised")
