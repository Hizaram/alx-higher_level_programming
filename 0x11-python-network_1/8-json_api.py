#!/usr/bin/python3
"""Sends a search parameter to a URL."""
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
        query = q
    else:
        q = ""
        query = q

    form_data = [('q', query)]
    response = requests.post(url, data=form_data)
    try:
        json_content = response.json()
        if json_content:
            print('[{}] {}'.format(json_content['id'], json_content['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
