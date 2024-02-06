#!/usr/bin/python3
"""

Module Input/Output

"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure

    arg:
        obj - to serialized
    """

    return obj.__dict__
