#!/usr/bin/python3
""" Module for is_kind_of_class method """


def is_kind_of_class(obj, a_class):
    """ Function that returns Trueif the object is an instance of,
        or if the object is an instance of a class that inherited from
        the specified class ; otherwise False

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is and instance of a_class
        False if not
    """
    return isinstance(obj, a_class)
