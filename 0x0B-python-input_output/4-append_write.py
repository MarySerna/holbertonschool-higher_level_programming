#!/usr/bin/python3
"""
Module that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    and returns the number of characters added:
    """

    with open(filename, 'a', encoding='utf-8') as new:
        new.write(text)
    return len(text)
