#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
from sys import argv
import requests

if __name__ == "__main__":
    rqs = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if "json" not in rqs.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = rqs.json()
        print(res.get('id'))
