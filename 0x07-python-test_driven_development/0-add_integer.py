#!/usr/bin/python3
"""

function that adds two integers of floats

"""

def add_integer(a, b=98):
    """

    Args:
        a: first number
        b: second number

    Raise:
       TypeError: If a or b aren't integers
    
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """

    cast a and b into integers if they floats

    Return:
        The addition of two integers
    
    """

    return (int(a) + int(b))
