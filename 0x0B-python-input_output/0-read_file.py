#!/usr/bin/python3
"""

Module Input and Output


"""


def read_file(filename=""):
    """
    function that reads a file (UTF8)
    and prints it standard stdout
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
