#!/usr/bin/python3
"""
Defines  a reactangle class

"""
from models.base import Base


class Rectangle(Base):
    """
    child class reactangle that inherits from Base
    with private instances attributes, each with its
    own getter and setter
    width, height, x, and y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor

        args:
            width
            height
            x
            y
            id - super call to use Base logic
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Reactangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the Reactangle

        Attribute
            Value(int): value to assign

        Raise:
            TypeError: value must be an integer
            ValueError: Value must be > 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get the height of the Reactangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Reactangle

        Attributes:
            value(int): value to assign

        Raise:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x

        Attribute:
            value(int): value to assign

        Raise:
            TypeError: value must be an integer
            VlueError: value must be > 0
        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y

        Attribute:
            value(int): value to assign

        Raise:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculate and return the area of the Reactangle.

        Return(int): height * width
        """
        return self.height * self.width

    def display(self):
        """
        function that displays the Rectangle
        using '#' character
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        override the __str__ method to return a custom
        string representation
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle based on the arguments.

        Args:
            *args: A variable based on positional arguments
            **kwargs: key-worded arguments representing attribute names
            and their values.
        """
        if args:
            num_args = len(args)
            if num_args == 1:
                self.id = args[0]
            if num_args == 2:
                self.id, self.width = args
            if num_args == 3:
                self.id, self.width, self.height = args
            if num_args == 4:
                self.id, self.width, self.height, self.x = args
            if num_args == 5:
                self.id, self.width, self.height, self.x, self.y = args
            else:
                pass

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation
        """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
