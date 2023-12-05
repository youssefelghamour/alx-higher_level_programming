#!/usr/bin/python3
""" Module that contains load_from_json_file function that creates
    an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”

    Args:
        my_obj: object
        filename: name of the file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return json.load(file)
