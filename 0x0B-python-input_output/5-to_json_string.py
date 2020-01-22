#!/usr/bin/python3


import json


"""
module that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """
    Return string
    """
    return json.dumps(my_obj)
