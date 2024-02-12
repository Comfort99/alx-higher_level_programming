#!/usr/bin/python3
"""

Model spuare

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Grandchild class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """

        super().__init__(id=id, x=x, y=y, width=size, height=size)
        self.size = size

    def __str__(self):
        """
        The overloading __str__ method should
        return custom string representation
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.size}"

    @property
    def size(self):
        """get the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    def update(self, *args, **kwargs):
        """
        assign arguments to attributes
        """
        if args:
            num_arg = len(args)
            if num_arg == 1:
                self.id = args[0]
            elif num_arg == 2:
                self.id, self.size = args
            elif num_arg == 3:
                self.id, self.size, self.x = args
            elif num_arg == 4:
                self.id, self.size, self.x, self.y = args
            else:
                pass

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of square
        """

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
