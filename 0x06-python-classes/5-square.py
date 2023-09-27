#!/usr/bin/python3


class Square:
    """
    class square with attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization function for our square class
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        gets the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        computes the area of the square
        """
        return self.__size ** 2
    def my_print(self):
        """
        prints square using '#' characters
        """
        i = 0
        for i in range(0, self.__size):
            j = 0
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        validates the size and checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
