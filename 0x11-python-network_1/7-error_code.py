#!/usr/bin/python3
"""Python script that requests a URL and returns the body of the response
or the error code
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
