#!/usr/python3
"""

Module Input/Output

"""


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

Filename = "add_items.json"

List = []

if os.path.exists(Filename) and os.path.getsize(my_file) > 0:
    List = load_from_json_file(Filename)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        Filename.append(element)

save_to_json_file(List, Filename)
