#!/usr/bin/python3

"""Take a letter"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        re = argv[1]
    else:
        re = ""
    resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': re})
    try:
        dicc = resp.json()
        if not dicc:
            print('No result')
        else:
            print('[{}] {}'.format(dicc.get('id'), dicc.get('name')))
    except:
        print('Not a valid JSON')
