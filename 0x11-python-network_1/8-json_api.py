#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    rqs = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        re_dict = rqs.json()
        id = re_dict.get('id')
        name = re_dict.get('name')
        if len(re_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(re_dict.get('id'), re_dict.get('name')))
    except:
        print("Not a valid JSON")
