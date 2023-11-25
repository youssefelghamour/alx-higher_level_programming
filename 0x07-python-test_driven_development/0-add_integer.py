#!/usr/bin/python3
"""add module containing the add() function that add 2 numbers"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The sum of two numbers

    Raises:
        TypeError: If a or b aren't ints or floats
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
