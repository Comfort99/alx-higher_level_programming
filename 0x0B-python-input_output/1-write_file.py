#!/usr/bin/python3
"""

Module Input and Output

"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)
    and returns a number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        characters_written = f.write(text)
    return characters_written
