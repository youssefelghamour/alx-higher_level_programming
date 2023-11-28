#!/usr/bin/python3
""" Module containing LockedClass class"""


class LockedClass:
    """ LockedClass class with no class or object attribute,
        it prevents the user from dynamically creating new instance attributes,
        except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']
