#!/usr/bin/python3
"""

Module Pascal

"""


def pascal_triangle(n):
    """
    Function that return the list of list
    Matrtrix
    """

    if n <= 0:
        return

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
