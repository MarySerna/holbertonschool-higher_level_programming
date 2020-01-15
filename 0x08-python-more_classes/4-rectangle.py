#!/usr/bin/python3
"""class Rectangle that defines
a rectangle """


class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Print() and str() should print the rectangle
    with the character # """
    def __str__(self):
        """If width or height is equal to 0, return an empty string"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for row in range(self.__height):
                for j in range(self.height - 1):
                    print("#" * self.__width)
                return "#" * self.width

    """return an empty string repr() should return a string representation
      of the rectangle to be able to recreate a new instance by using eval()"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    """Private instance attribute: width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """Private instance attribute: height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """Public instance method that returns the rectangle area"""
    def area(self):
        area = self.__width * self.__height
        return area

    """Public instance method that returns the perimeter area"""
    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return 0
        else:
            perimeter = (self.__width * 2) + (self.__height * 2)
            return perimeter
