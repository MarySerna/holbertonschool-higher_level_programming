#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
from sys import argv
import requests

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    rqs = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(rqs.json().get('id'))
