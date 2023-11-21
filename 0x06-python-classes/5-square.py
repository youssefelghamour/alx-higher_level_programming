#!/usr/bin/python3
"""Square class"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: size ofthe square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Calculates the are of the square

        Returns:
            the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if not self.__size:
            print()
        else:
            for i in range(self__.size):
                for j in range(self.__size):
                    print("#", end='')
                print()
