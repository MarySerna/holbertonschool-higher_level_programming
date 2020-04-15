#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response
"""
if __name__ == '__main__':

    import urllib.parse as parse
    import urllib.request as request
    from sys import argv

    values = {'email': argv[2]}
    dt = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], dt)
    with request.urlopen(req) as rqs:
        print(rqs.read().decode('utf-8'))
