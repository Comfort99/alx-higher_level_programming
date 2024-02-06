#!/usr/bin/python3
"""

Module Input/Output

"""


class Student:
    """
    parent class of student insentives
    """

    def __init__(self, first_name, last_name, age):
        """
        method __init__
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves the dictionary representation of a student
        """

        return self.__dict__
