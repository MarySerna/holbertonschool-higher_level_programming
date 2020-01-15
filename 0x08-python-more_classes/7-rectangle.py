#!/usr/bin/python3
"""
   Rectangle class
"""


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    """Private instance attribute: width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Private instance attribute: height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        rect = ""
        for altura in range(self.height):
            i = 0
            for base in range(self.width):
                rect += "#"
                i = i + 1
                if i == self.width and altura is not self.height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two rectangles
            Args:
                rect_1: first rectangle
                rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
