#!/usr/bin/python3
"""
module of booler

"""


def is_same_class(obj, a_class):
    """
    function that Return True if an
    object is exactly an instance otherwise False

    args:
        obj - to be compared
        a_class - to be compared with

    Return:
        True or False
    """
    return True if type(obj) is a_class else False
