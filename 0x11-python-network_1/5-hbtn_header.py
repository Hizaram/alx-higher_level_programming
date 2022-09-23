#!/usr/bin/python3
"""Python script that returns the value of the `X-Request_id` variable
of the query of a URL
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]

        response = requests.get(url)
        print(response.headers['X-Request-Id'])
