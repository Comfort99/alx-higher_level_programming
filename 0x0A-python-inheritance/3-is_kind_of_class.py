#!/usr/bin/python3
"""

Module of a Booler function

"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if a object is an instance,
    or if the object is an instance of a class that inherits
    from or False

    Args:
        obj - to be compared
        a_class - to be compared with

    Return:
        True or False
    """
    return isinstance(obj, a_class)
