#!/usr/bin/python3
"""

Module Input and Output

"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation
    of an object

    args:
        obj - to be serialized
    """

    return json.dumps(my_obj)
