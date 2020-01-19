#!/usr/bin/python3


class Rectangle:
    """
this is Rectangle function

    """
    def __init__(self, width=0, height=0):
        """ init function             """
        self.height = height
        self.width = width

    @property
    def height(self):
        """   height function     """
        self.__height

    @height.setter
    def height(self, value):
        """ height setter             """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ width property             """
        return self.__width

    @width.setter
    def width(self, value):
        """      width setter fn   """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """   area function             """
        return self.__width * self.__height

    def perimeter(self):
        """     perimeter fn   """
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (self.__width * 2) + (self.__height * 2)
