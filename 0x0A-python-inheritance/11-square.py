#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


"""A class Square that inherits from Rectangle"""


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
