#!/usr/bin/python3
"""Python script that sends a request to a URL and displays the response
or error code"""
from urllib import request, error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as err:
            print('Error code: {}'.format(err.code))
