#!/usr/bin/python3
def error_one(value):
    if not isinstance(value, tuple):
        raise TypeError("position must be a tuple of 2 positive integers")
    if len(value) != 2:
        raise TypeError("position must be a tuple of 2 positive integers")
    if not isinstance(value[0], int) or not isinstance(value[1], int):
        raise TypeError("position must be a tuple of 2 positive integers")
    if value[0] < 0 or value[1] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")


def error_two(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


class Square:
    def __init__(self, size=0, position=(0, 0)):
        error_two(size)
        error_one(position)
        self.__size = size
        self._position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        errorCheck(value)
        self.__size = value

    @property
    def position(self):
        return (self._position)

    def area(self):
        return (self.__size ** 2)

    @position.setter
    def position(self, value):
        errorCheckTuple(value)
        self._position = value

    def my_print(self):
        if not self.__size:
            print()
        for i in range(self._position[1]):
            print()
        for j in range(self.__size):
            for m in range(self._position[0]):
                print(" ", end="")
            for n in range(self.__size):
                print("#", end="")
            print()
