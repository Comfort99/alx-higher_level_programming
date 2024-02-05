#!/usr/bin/python3
"""
Creates a square class


"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class to inherit from parent Class
    """

    def __init__(self, size):
        """
        method to take in arg size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return super().__str__()
