#!/usr/bin/python3


class Square:
    """
    class square with attributes, size
    other attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        checks for input errors for size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        computes the area of the square
        """
        return self.__size ** 2


