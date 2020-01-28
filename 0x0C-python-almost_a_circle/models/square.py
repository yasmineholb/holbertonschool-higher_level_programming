#!/usr/bin/python3
""" this is the square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ this is the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ this is the str fn """
        return("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y,  self.width))

    @property
    def size(self):
        """ this is the size  """
        return super().width

    @size.setter
    def size(self, size):
        """ this is the size setter """
        super(Square, self.__class__).width.fset(self, size)

    def update(self, *args, **kwargs):
        """ the update fn """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, value in kwargs.items():
                if k == "id":
                    self.id = value
                if k == "size":
                    self.size = value
                if k == "x":
                    self.x = value
                if k == "y":
                    self.y = value

    def to_dictionary(self):
        """ the dict fn """
        di = {}
        di['id'] = self.id
        di['size'] = self.size
        di['x'] = self.x
        di['y'] = self.y
        return di
