#!/usr/bin/python3

from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,  self.width))

    @property
    def size(self):
        """  """
        return super().width

    @size.setter
    def size(self, size):
        """   """
        super(Square, self.__class__).width.fset(self, size)

    def update(self, *args, **kwargs):
        if len(args) is 0:
            for i, j in kwargs.items():
                if i == "id":
                    self.id = kwargs.get(i)
                if i == "size":
                    self.__size = kwargs.get(i)
                if i == "x":
                    self.__x = kwargs.get(i)
                if i == "y":
                    self.__y = kwargs.get(i)
        else:
            k = []
            for s in args:
                k.append(s)
            if len(k) == 0:
                pass
            if len(k) > 0:
                self.id = k[0]
            if len(k) > 1:
                self.__width = k[1]
            if len(k) > 2:
                self.__height = k[2]
            if len(k) > 3:
                self.__x = k[3]
            if len(k) > 4:
                self.__y = k[4]

        

        

