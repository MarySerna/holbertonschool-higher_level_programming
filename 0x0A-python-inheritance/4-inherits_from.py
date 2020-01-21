#!/usr/bin/python3
"""
Function that returns an instance
of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Return True or False
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
