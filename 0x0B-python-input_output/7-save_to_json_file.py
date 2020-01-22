#!/usr/bin/python3


import json


"""
function that returns an object
"""


def save_to_json_file(my_obj, filename):
    """
    return a object
    """
    with open(filename, 'w', encoding='utf-8') as new:
        new.write(json.dumps(my_obj))
