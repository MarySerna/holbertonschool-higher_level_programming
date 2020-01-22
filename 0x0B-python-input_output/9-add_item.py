#!/usr/bin/python3
"""Module to add all arguments to a list
"""


import json
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    new_file = load_from_json_file(filename)
except:
    new_file = []

for arg in argv[1:]:
    new_file.append(arg)

save_to_json_file(new_file, filename)
