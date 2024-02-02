#!/usr/bin/python3
"""

function that prints my name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """ Args:
        first_name
        last_name

    Check if the first_name and last_name are strings
                    Raise:
                        TypeError(first_name/last_name must be a string)
    Print the output
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
