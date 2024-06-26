#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the body of the response
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status = response.status_code()

    if status >= 400:
        print(f"Error code: {status}")
    else:
        print(response.text)
