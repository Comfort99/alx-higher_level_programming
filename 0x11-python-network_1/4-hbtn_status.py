#!/usr/bin/python3
"""
It abstracts the complexities of making requests behind a beautiful,
simple API so that you can focus on interacting with services
and consuming data in your application
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
