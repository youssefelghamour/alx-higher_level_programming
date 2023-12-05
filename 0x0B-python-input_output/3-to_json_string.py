#!/usr/bin/python3
""" Module that contains to_json_string function that returns the
    JSON representation """
import json


def to_json_string(my_obj):
    """ Function that returns JSON representation of an object

    Args:
        my_obj: object
    """
    return json.dumps(my_obj)
