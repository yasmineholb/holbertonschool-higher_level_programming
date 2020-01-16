#!/usr/bin/python3


class Rectangle:
    """
the rectangle class

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """   init fn      """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """     height fn   """
        self.__height

    @height.setter
    def height(self, value):
        """   height fn           """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """    width fn        """
        return self.__width

    @width.setter
    def width(self, value):
        """       width fn        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """   area fn             """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter fn        """
        if (self.__width == 0) or (self.__height == 0):
            self.perimeter = 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """       str fn     """
        if (self.__width == 0) or (self.__height == 0):
            return("")
        else:
            s = []
            for i in range(self.__height):
                for j in range(self.__width):
                    s.append(str(self.print_symbol))
                s.append("\n")
        del s[-1]
        return("".join(s))

    def __repr__(self):
        """  repr fn                """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ del fn        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """  bigger/equal fn        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return(rect_2)
        else:
            return(rect_1)

    @classmethod
    def square(cls, size=0):
        """  square fn       """
        return cls(size, size)
