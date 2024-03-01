#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    payload = {'q': ""}

    try:
        payload = {'q': argv[1]}
    except:
        pass

    url = "http://0.0.0.0:5000/search_user"

    r = requests.post(url, data=payload)

    try:
        body_json = r.json()
        if body_json:
            print("[{}] {}".format(body_json.get('id'), body_json.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
