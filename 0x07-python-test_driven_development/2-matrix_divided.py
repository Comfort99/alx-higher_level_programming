#!/usr/bin/python3
"""

Function that divides all the elements of a matrix

"""


def matrix_divided(matrix, div):
    """ Args:
        matrix: list of lists of integers and floats
        div: number used to divide the matrix

    Check if the matrix is a list of lists integers of floats

    Check if the rows in the matrix have the same size of elements

    Check if div is a number (integer or float)

    Check if div is equal to 0
    ZeroDivisionError: If div is zero

    Divide all elements of the matrix by div and round to 2 decimal places



    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

     nm = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (nm)

    
