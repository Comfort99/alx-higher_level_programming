#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    data = {'q': argv[1]} if len(argv) >= 2 else {'q': ''}

    response = requests.post(url, data)
    header = response.headers['Content-type']

    if header == 'application/json':
        result = response.json()
        _id = result.get('id')
        name = result.get('name')
        if _id and name:
            print(f"[{_id}] {name}")
        else:
            print('No result')
    else:
        print('Not a valid JSON')
