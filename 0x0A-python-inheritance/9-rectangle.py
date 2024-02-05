#!/usr/bin/python3
"""

Module Geometry

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    child class to inherit from parent class(Geometry)
    """

    def __init__(self, width, height):
        """
        args:
            width
            height
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method tha return the string representation of class(Rectangle)
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
