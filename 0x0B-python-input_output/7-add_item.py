#!/usr/python3
"""

Module Input/Output

"""


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_items.json"

my_list = []

if os.path.exists(Filename) and os.path.getsize(filename) > 0:
    my_list = load_from_json_file(filename)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        Filename.append(element)

save_to_json_file(my_list, filename)
