#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -s -w "%{SIZE_DOWNLOAD}" -o /dev/null $1
