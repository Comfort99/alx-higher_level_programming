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

    typeErr = "matrix must be a matrix (list of lists) of integers/floats"
    sizeErr = "Each row of the matrix must have the same size"
    for row in matrix:
        if len(element) != len(matrix[0]):
            raise TypeError(sizeErr)
        for element in row:
            if not isinstance(y, (int, float)):
                raise TypeError(typeErr)
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
