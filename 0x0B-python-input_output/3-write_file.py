#!/usr/bin/python3
"""
Modulo that writes a string
"""


def write_file(filename="", text=""):
    """
     create the file if does not exist
    """
    with open(filename, 'w', encoding='utf-8') as new:
        new.write(text)
    return len(text)
