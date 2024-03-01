#!/usr/bin/python3
""" script that takes 2 arguments and lists 10 commits (from the most
    recent to oldest) of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    REPO = argv[1]
    OWNER = argv[2]
    url = "https://api.github.com/repos/" + OWNER + "/" + REPO + "/commits"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    r = requests.get(url, headers=headers)

    commits = r.json()

    for commit in commits[:10]:
        # to list only 10 commits
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")

        print("{}: {}".format(sha, name))
