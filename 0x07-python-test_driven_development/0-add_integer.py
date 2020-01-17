#!/usr/bin/python3
"""
adds two integers
>>> add_integer(1,3)
4
"""


def add_integer(a, b=98):
    """
    Write a function that adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    else:
        return int(a) + int(b)
