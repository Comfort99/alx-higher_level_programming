#!/usr/bin/python3
"""

Module Input and Output

"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of the file (UTF8)
    and returns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        characters_appended = f.write(text)

    return characters_appended
