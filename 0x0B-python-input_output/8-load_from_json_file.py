#!/usr/bin/python3
"""


"""
import json


def load_from_json_file(filename):
    """ save to json fn """
    with open(filename, encoding="utf-8") as f:
        return (json.loads(f.read()))
