#!/usr/bin/python3
""" script that takes GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    token = argv[2]

    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, token))

    json_data = r.json()
    print(json_data.get('id'))
