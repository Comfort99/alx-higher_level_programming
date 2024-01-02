#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:  # if the character is lowercase
            result += chr(ord(c) - 32)  # convert to uppercase
        else:
            result += c  # leave the character as it is
    print("{}".format(result), end='')
    print()
