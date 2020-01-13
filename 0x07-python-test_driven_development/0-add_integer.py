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
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")

    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")

    else:
        return int(a) + int(b)
