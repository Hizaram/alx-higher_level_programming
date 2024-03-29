#!/usr/bin/python3
"""Python Script that sends a POST request to the passed URL with email
as paramter, and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = [('email', email)]
        response = requests.post(url, data=form_data)
        print(response.text)
