#!/usr/bin/python3
''' Defines Square class '''


class Square:

    ''' class that contains private attribute '''

    def __init__(self, size):

        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
