#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response

if [ $# -lt 1 ]
then
	echo "no argument passed";
else
	url=$1
	curl -s "$url" | wc -c
fi
