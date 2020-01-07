#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError):
        Ex = "Exception: Unknown format code 'd' for object of type 'str'\n"
        sys.stderr.write(Ex)
        return(False)
