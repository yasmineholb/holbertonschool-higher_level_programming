#!/usr/bin/python3
def safe_print_division(a, b):
    s = 0
    try:
        s = a/b
    except :
        s = 0
    finally:
        print("inside result: {}".format(s))
