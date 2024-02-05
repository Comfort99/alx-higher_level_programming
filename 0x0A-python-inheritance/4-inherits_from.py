#!/usr/bin/python3
"""

module of Booler function

"""


def inherits_from(obj, a_class):
    """
    function that Returns True if the object is an instance
    of a class that inherited(directly or indirectly)

    arg:
        obj
        a_class

    Return:
        True or False
    """

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False
