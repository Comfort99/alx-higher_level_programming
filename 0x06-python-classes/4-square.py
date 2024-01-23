#!/usr/bin/python3
''' Defines Square class '''


class Square:

    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):

        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            """
        self.__size = size

    @property
    def size(self):

        ''' get size '''
        return self.__size

    @size.setter
    def size(self, value):

        ''' set size '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        ''' calculate area of square '''
        return self.__size * self.__size
