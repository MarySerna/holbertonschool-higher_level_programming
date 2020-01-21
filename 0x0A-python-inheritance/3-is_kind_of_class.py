#!/usr/bin/python3
"""
Return True or False
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of object return True
    You are not allowed to import any module
    """

    if isinstance(obj, a_class):
        return True
    return False
