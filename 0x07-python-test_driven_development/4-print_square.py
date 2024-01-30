#!/usr/bin/python3
"""

Function that prints a sqaure of the character #

"""

def print_square(size):
    """
    Arg:
        size: size of the square
    
    check size if is an integer:
                raise TypeError(size must be an integer)
    
    if size is less than 0:
                raise ValueError(size must be greater or equal to 0)
    
    Print the output

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
