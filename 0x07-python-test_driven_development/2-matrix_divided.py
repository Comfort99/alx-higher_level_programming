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

    if not isinstance(matrix, list) or not all(isinstance(row, list) 
            and all(isinstance(element, (int, float)) 
                for element in row) for row in matrix):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in  matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not type(div) in (int, float):
            raise TypeError("div must be number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
