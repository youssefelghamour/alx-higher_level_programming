#!/usr/bin/python3
""" Module for inherits_from method """


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        otherwise False

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is and instance of a_class
        False if not
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
