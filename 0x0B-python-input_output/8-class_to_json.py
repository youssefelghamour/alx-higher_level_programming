#!/usr/bin/python3
""" Module that contains class_to_json function """


def class_to_json(obj):
    """ Function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

        Args:
            obj: object
    """
    return obj.__dict__
