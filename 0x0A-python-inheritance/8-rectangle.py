#!/usr/bin/python3
"""
Public instance method that validates value
"""


class BaseGeometry:
    """
    BaseGeometry Class
    """
    def area(self):
        """
        Raise an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates Value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        call the fucntion validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
