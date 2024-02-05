#!/usr/bin/python3
"""

Module Geometry

"""


class BaseGeometry:
    """
    Parent Class
    """

    def area(self):
        """
        instance raise Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        instance that validates value
        """
        if type(value) is not (int):
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
