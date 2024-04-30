#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8)
manages urllib.error.HTTPError exceptions and prints status
"""

from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.agv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
 
    except error.HTTPError as err:
        print(f"Error code: {err.status}")
