#!/usr/bin/python3
"""

module Square

"""


BaseGeometry = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    to inherit from Rectangle

    """
    def __init__(self, size):
        """
        arg:
            size - sqaure
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))
