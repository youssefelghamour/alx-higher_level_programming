#!/usr/bin/python3
""" Module that contains from_json_string function that
    deserializes a JSON string """
import json


def from_json_string(my_str):
    """ Function that returns deserializes a JSON string

    Args:
        my_obj: object

    Returns:
        an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
