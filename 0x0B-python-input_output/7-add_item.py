#!/usr/bin/python3
"""Module 7 -add_item
Adds all arguments to a python list and then saves to file
"""


import sys
import json
import os.path

if __main__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        content = load_from_json_file("add_item.json")
    except FilenotFoundError:
        content = []
    content.extend(sys.arg[1:])
    save_to_json_file(content, "add_items.json")
