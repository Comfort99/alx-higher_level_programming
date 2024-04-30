#!/usr/bin/python3
"""

"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.agv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content)
    
    except HTTPError as error:
        print(Error code: error.status)
