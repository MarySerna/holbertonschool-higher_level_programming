#!/usr/bin/python3
"""
Import rectangle that inherits from Base
"""


from .base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of the Rectangle class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width setter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        X getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        X setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout of rectangle
        """
        for space in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        if args:
            for arg, element in zip(args, range(5)):
                if element is 0:
                    self.id = arg
                if element is 1:
                    self.width = arg
                if element is 2:
                    self.height = arg
                if element is 3:
                    self.x = arg
                if element is 4:
                    self.y = arg
                if element is None:
                    break
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
