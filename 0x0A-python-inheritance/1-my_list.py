#!/usr/bin/python3
""" Module for MyList class """


class MyList(list):
    """ Mylist class that inherits from list

    Args:
        list: list class
    """

    def print_sorted(self):
        """ Public instance method that prints the list sorted """
        print(sorted(self))
