#!/usr/bin/python3
""" script that takes GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/users/{}".format(user)

    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(token),
            "X-GitHub-Api-Version": "2022-11-28"
               }

    r = requests.get(url, headers=headers)

    json_data = r.json()
    print(json_data.get('id'))
