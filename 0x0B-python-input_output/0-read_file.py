#!/usr/bin/python3
"""
Module that reads a text file
"""


def read_file(filename=""):
    """
    Read the file and print
    """
    with open(filename, 'r', encoding='utf-8')as new:
        print(new.read(), end="")
