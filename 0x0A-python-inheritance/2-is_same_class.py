#!/usr/bin/python3
""" Module for is_same_class method """


def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly an instance of
        the specified class; otherwise False

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is and instance of a_class
        False if not
    """
    return type(obj) is a_class
