#!/usr/bin/python3
"""

Module Input/Output

"""


import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    repesented by a JSON string

    arg:
        my-str - to be serialized
    """

    return json.loads(my_str)
