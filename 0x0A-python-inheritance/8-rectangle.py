#!/usr/bin/python3
"""

module Geometry

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        method called you when create a new class
        args:
            width
            height
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
