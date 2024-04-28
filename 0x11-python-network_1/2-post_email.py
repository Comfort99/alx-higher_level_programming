#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    #encode email from bites to string
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    #create a post request
    post = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(post) as response:
        response_body = response.read().decode('utf-8')
    
    print(response_body)
