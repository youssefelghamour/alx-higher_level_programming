#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
