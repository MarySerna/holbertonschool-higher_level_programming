#!/usr/bin/python3
"""
Module that read n lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Read the entire file
    """

    count = 0
    with open(filename, 'r', encoding='utf-8')as new:
        for line in new:
            if count < nb_lines or nb_lines <= 0:
                print(line, end="")
                count += 1
