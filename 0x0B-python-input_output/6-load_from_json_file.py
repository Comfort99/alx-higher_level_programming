#!/usr/bin/python3
"""

Module Input/Output

"""


def load_from_json_file(filename):
    """
    Fike that creates an object from a "JSON file"
    arg:
        file: fo be serialized
    """

    with open(filename, 'r', encodind="utf-8") as f:
        return json.load(f)
