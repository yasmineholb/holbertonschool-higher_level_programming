#!/usr/bin/python3


class Rectangle:
    """
the rectangle class

    """
    def __init__(self, width=0, height=0):
        """  init function     """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """   height fn   """
        self.__height

    @height.setter
    def height(self, value):
        """     height setter  """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """    width property      """
        return self.__width

    @width.setter
    def width(self, value):
        """        width setter fn """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """      fn area          """
        return self.__width * self.__height

    def perimeter(self):
        """        fn perimeter      """
        if (self.__width == 0) or (self.__height == 0):
            self.perimeter = 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """     str function        """
        if (self.__width == 0) or (self.__height == 0):
            return("")
        else:
            s = []
            for i in range(self.__height):
                for j in range(self.__width):
                    s.append("#")
                s.append("\n")
        del s[-1]
        return("".join(s))

    def __repr__(self):
        """      repr fn    """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
