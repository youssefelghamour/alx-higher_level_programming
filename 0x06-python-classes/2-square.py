#!/usr/bin/python3
"""Square class"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """
        constructor

        Args:
            size: size ofthe square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
