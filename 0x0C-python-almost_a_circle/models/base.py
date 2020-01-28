#!/usr/bin/python3
"""
this is the module base
"""
import json


class Base:
    """ this is the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ this is to_json fn """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return(json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """ this is save fn """
        ob = []
        if list_objs is None or len(list_objs) is 0:
            ob = []
        else:
            for m in list_objs:
                ob.append(m.to_dictionary())
        js = Base.to_json_string(ob)
        with open("{}.json".format(cls.__name__), mode='w', encoding='utf-8')\
                as file:
            file.write(js)

    def from_json_string(json_string):
        """ from json fn """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return(json.loads(json_string))

    def create(cls, **dictionary):
        """ create fn """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
