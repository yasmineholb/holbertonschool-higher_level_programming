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

    @classmethod
    def save_to_file(cls, list_objs):
        """ this is save fn """
        if list_objs is None or list_objs == []:
            js = "[]"
        else:
            js = cls.to_json_string([o.to_dictionary() for o in list_objs])
        fil = cls.__name__ + ".json"
        with open(fil, 'w') as f:
                f.write(js)

    def from_json_string(json_string):
        """ from json fn """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create fn """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """this is the load fn """
        try:
            with open(cls.__name__ + ".json", "r") as fl:
                ld = cls.from_json_string(fl.read())
            return [cls.create(**j) for j in ld]
        except:
            return []
