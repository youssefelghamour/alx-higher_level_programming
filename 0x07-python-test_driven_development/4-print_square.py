#!/usr/bin/python3
"""Module containing a function that prints a square with the character #"""


def print_square(size):
    """Function that prints a square with the character #

    Args:
        size: size of the square

    Raises:
        TypeError: If size is not an integer number
        ValueError: If size is negative
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
