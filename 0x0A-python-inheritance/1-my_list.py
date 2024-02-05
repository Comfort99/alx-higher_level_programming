#!/usr/bin/python3
"""

module that sort the list

"""


class MyList(list):
    """
    Class Mylist
    """

    def print_sorted(self):
        """
        class that inherits from list
        arg:
            self

        create a copy of a list

        """
        sorted_list = self.copy()
        sorted_list.sort()

        print(sorted_list)
