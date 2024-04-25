#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
# and displays the size of the body of the respon
curl -s -w "%{SIZE_DOWNLOAD}" -o /dev/null $1
