#!/usr/bin/python3
"""
Public instance method,
that raises an Exception
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
