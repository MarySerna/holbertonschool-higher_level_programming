#!/usr/bin/python3
"""Script that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initializes Square class
        Args:
            size (int): size of a square
        """
        self.__size = size

    @property
    def size(self):
        """Getter to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set it"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of a square
        Return:
            returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
