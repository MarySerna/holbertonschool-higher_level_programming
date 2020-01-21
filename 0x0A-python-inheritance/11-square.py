#!/usr/bin/python3


""""class BaseGeometry"""


class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method: def integer_validator(self, name, value):
     that validates value"""

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    """ should print, and str() should return, the following
    rectangle description"""

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
