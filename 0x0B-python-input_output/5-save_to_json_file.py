#!/usr/bin/python3
"""

Module Input/Output

"""


import json


def save_to_json_file(my_object, filename):
    """
    Function that writes an Object to a text file
    using a JSON representation

    arg:
        obj - to be serialized
        filename - write object
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
