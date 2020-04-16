#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL & displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    rqs = requests.get(argv[1])
    if rqs.status_code >= 400:
        print("Error code: {}".format(rqs.status_code))
    else:
        print(rqs.text)
