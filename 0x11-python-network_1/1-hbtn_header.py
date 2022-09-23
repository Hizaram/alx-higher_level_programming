#!/usr/bin/python3
"""Python script that takes a URRL as argument, sends a request and
displays the value of X-Request-Id variable found in its header
"""
from urllib import request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.headers['X-Request-Id'])
