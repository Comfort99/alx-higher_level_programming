#!/usr/bin/python3
"""
Module class that return a list

"""


def lookup(obj):
    """Function that returns the list of the available
    attributes and methods of an object

    Args:
        obj - list of of attributes and methods

    Return:
        list of an object(dir() returns the list of an object)
    """

    return dir(obj)
