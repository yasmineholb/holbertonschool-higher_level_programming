#!/usr/bin/python3


"""Take URL"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))
