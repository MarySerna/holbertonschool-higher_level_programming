#!/usr/bin/python3
"""Script that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Getter to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to set position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of a square
        Return:
            returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square"""
        if self.size == 0:
            print()
            return
        for n in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for s in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
