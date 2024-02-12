#!/usr/bin/python3
"""

Module Base of my project

"""

import json


class Base:
    """
    Class that serves a base for my project

    The goal is to manage the 'id' attribute
    in future classes and avoid duplicating code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        If 'id' is provided assign it to the
        public instance attributes 'id'.

        Otherewise increment '__nd_obejects' and
        assign the new value to 'id'.
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Json is a standard format for sharing data representation

        returns:
            str: Json string representation of the list
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the Json string of instances that inherit from Base

        args:
            list_objs(list): list of instance that inherits from Base
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json.dump([], json_file)
            else:
                new_dict = [item.to_dictionary() for item in list_objs]
                json_string = cls.to_json_string(new_dict)
                json.dump(new_dict, json_file)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by the Json string.

        Arg:
            json_string: A string representating a list of dictionaries in
            JSON format.
        Return:
            list: list of dictionaries
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set based on the
        provided dictionary

        Args:
            **dictionary: A dictionary containing attribute-value pair.

        Return:
            Base: an instance with attributes set according to the dictionary
        """

        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a Json file.

        Returns:
            lists: list of instances(type depends on cls).
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as json_file:
                json_string = json_file.read()
                instance_list = cls.from_json_string(json_string)
                return [cls.create(**item) for item in instance_list]
        except FileNotFoundError:
            return []
