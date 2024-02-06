#!/usr/python3
"""

Module Input/Output

"""


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args, filename):
    if (os.path.exists(filename)):
        content = load_from_json(filename)

    else:
        content = []

    content.extend(args)
    save_to_json(content, filename)


if __name__== "__main__":
    args = sys.args[1:]
    filename = "add_item.json"
    add_item(args,filename)
