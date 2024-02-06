#!/usr/bin/python3
"""

Module Input/Output

"""


import json


def load_from_json_file(filename):
    """
    File that creates an object from a "JSON file"
    arg:
        file: fo be serialized
    """

    with open(filename, 'r') as f:
        return json.load(f)
