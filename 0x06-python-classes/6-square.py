#!/usr/bin/python3
''' Defines Square class '''


class Square:

    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):

        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):

        ''' calculate area of square '''
        return self.__size * self.__size

    def my_print(self):

        """Prints the square with the # character on stdout."""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
