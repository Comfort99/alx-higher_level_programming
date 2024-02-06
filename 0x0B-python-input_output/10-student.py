#!/usr/bin/python3
"""

Module Input/Output

"""


class Student:
    """
    Class to be serialized
    """

    def __init__(self, first_name, last_name, age):
        """
        method __init__
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation of student
        """

        my_dict = dict()
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            for elem in attrs:
                if elem in self.__dict__:
                    my_dict.update({elem: self.__dict__[elem]})

            return my_dict

        return self.__dict__.copy()
