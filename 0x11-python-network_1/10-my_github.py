#!/usr/bin/python3
""" Uses the GitHub """
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    webb = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=webb)
    print(req.json().get("id"))
