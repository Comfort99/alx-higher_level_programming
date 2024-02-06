#!/usr/bin/python3
"""

Module Json

"""


class Student:
    """
    Class serialized and deserialized
    """

    def __init__(self, first_name, last_name, age):
        """
        Method __init__
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves the dictionary representation of student
        arg:
            attrs - list of attributes
        """

        my_dict = dict()
        if attrs and all(isinstance(elem, str) for elem in attrs):
            for elem in attrs:
                if elem in self.__dict__:
                    my_dict.update({elem: self.__dict__[elem]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        to replaces all the attributes
        """
        for elem in json:
            self.__dict__.update({elem: json[elem]})
