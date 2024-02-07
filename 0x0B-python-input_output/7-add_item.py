#!/usr/bin/python3
"""Module 7 -add_item
Adds all arguments to a python list and then saves to file

"""


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

content = []

if o.path.exists(filename) and os.path.getsize(filename) > 0:
    content = load_from_json_file(filename)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        content.append(elem)

save_to_json_file(content, filename)
