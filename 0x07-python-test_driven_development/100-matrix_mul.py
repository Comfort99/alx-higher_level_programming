#!/usr/bin/python3

"""
Module that multiples

"""


def matrix_mul(m_a, m_b):
    """
    args:
        m_a;
        m_b;

    m_a and m_b must be a matrix
    raise TypeError:
            m_a must be a list or m_b must be a list

    m_a and m_b is empty
    raise  ValueError:
            m_a can't be empty or m_b can't be empty

    element of a list not a integer of float
     raise TypeError:
         m_a or m_b should contain only integers or floats

    rows must be the same size
     raise TypeError:
            each row of m_a must be of the same size

    raise ValueError:
            m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [
        [
            sum(x*y for x, y in zip(m_a_row, m_b_col))
            for m_b_col in zip(*m_b)
        ]
        for m_a_row in m_a
    ]

    return result
