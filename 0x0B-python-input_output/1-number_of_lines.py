#!/usr/bin/python3
"""
Module that return  number of line
"""


def number_of_lines(filename=""):
    """
    run the number of line
    """
    count = 0
    with open(filename, 'r') as new:

        for line in new:
            count += 1
    return count
