#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius):
        """add the magic class"""
        """verify the type"""
        """return the error"""
        """                """
        """                """
        """                """
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

        """         """
    def area(self):
        return self._MagicClass__radius ** 2 * math.pi

        """      """
    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
